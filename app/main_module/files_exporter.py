import copy
import datetime
import uuid
import pandas
import tempfile
import abc


class FileExporter(metaclass=abc.ABCMeta):

    def __init__(self, questions: list):
        self.questions = questions['content']

    def group_questions(self) -> list:

        grouped_questions = {}

        for question in self.questions:
            chapter = question['fields']['chapter']

            if type(chapter) == list and len(chapter) > 0:
                chapter = chapter[0]

            if type(chapter) == list and len(chapter) == 0:
                continue

            if chapter in grouped_questions:
                grouped_questions[chapter].append(question)
            else:
                grouped_questions[chapter] = [question]

        return grouped_questions

    def export_questions(self) -> list:

        files = {}

        def random_id():
            return str(uuid.uuid4())

        question_by_chapter = self.group_questions()

        for chapter in question_by_chapter:
            file_name = chapter + '.xlsx'
            question_list = question_by_chapter[chapter]
            f_exported = self.export_excel(file_name, question_list)
            files[random_id()] = {'file': f_exported, 'name': chapter,
                                  'created_at': datetime.datetime.now()}

        f_exported = self.export_excel('AllChapters.xlsx', self.questions)
        files[random_id()] = {'file': f_exported, 'name': 'All Chapters',
                              'created_at': datetime.datetime.now()}

        return files

    def export_excel(self, output_name: str, questions: list) -> str:
        '''
            :params
            - output_name: output file name
            - questions: formated list of questions to export 
        '''

        # convert array into pandas dataframe for simplicity
        questions = list(map(self.format_question, questions))
        df = pandas.DataFrame(questions)
        f = tempfile.NamedTemporaryFile(delete=False)
        # prepare export
        df.to_excel(f,
                    sheet_name='QUESTIONS',
                    index=False,
                    columns=self.EXCEL_COLUMNS)
        return f.name

    @abc.abstractstaticmethod
    def format_question(question: dict):
        # needs to be implemented for specfici file output format
        pass


class ThinkificExporter(FileExporter):

    EXCEL_COLUMNS = (
        'QuestionType', 'QuestionText', 'Explanation',
        'Choice1', 'Choice2', 'Choice3', 'Choice4', 'Choice5',
        'Choice6', 'Choice7', 'Choice8', 'Choice9', 'Choice10',
    )

    @staticmethod
    def format_question(question: dict) -> dict:
        '''
            :params
            - question: question object to format
        '''
        res = {}
        fields = question['fields']

        # to improve readability and save some keystroke
        for i in range(10):
            res['Choice' + str(i + 1)] = ''

        answer = ('', 'a', 'b', 'c', 'd')
        res['QuestionType'] = 'MA' if len(
            fields['correct_answer']) > 1 else 'SA'
        res['QuestionText'] = '<p>' + fields.get('question_text') + '</p>'
        res['Explanation'] = '<p>' + fields.get('feedback', '') + '</p>'

        # Complete choice fields
        for k in fields.keys():
            if 'option_' in k:
                letter = k[-1]
                res['Choice' + str(answer.index(letter))
                    ] = fields['option_' + letter]

        # add '*' prefix to answers
        for letter in fields['correct_answer']:
            letter = letter.lower()
            option_content = fields.get('option_' + letter, '')

            res['Choice' + str(answer.index(letter))] = '*' + option_content

        return res


class iSpringExporter(FileExporter):

    EXCEL_COLUMNS = (
        'QuestionType', 'QuestionText', 'Image', 'Video', 'Audio',
        'Answer1', 'Answer2', 'Answer3', 'Answer4', 'Answer5',
        'Answer6', 'Answer7', 'Answer8', 'Answer9', 'Answer10',
        'CorrectFeedBack', 'IncorrectFeedBack', 'Points'
    )

    @staticmethod
    def format_question(question: dict) -> dict:
        '''
            :params
            - question: question object to format
        '''
        res = {}
        fields = question['fields']

        # to improve readability and save some keystroke
        for i in range(10):
            res['Answer' + str(i + 1)] = ''

        answer = ('', 'a', 'b', 'c', 'd')
        res['QuestionType'] = 'MR' if len(fields['correct_answer']) > 1 else 'MC'
        res['QuestionText'] = fields.get('question_text')
        res['CorrectFeedBack'] = 'That\'s correct - ' + fields.get('feedback', '')
        res['IncorrectFeedBack'] = 'Sorry, that\'s incorrect - ' + fields.get('feedback', '')
        res['Points'] = 1

        # Complete choice fields
        for k in fields.keys():
            if 'option_' in k:
                letter = k[-1]
                res['Answer' + str(answer.index(letter))
                    ] = fields['option_' + letter]

        # add prefix/suffix to answers
        for letter in fields['correct_answer']:
            letter = letter.lower()
            option_content = fields.get('option_' + letter, '')

            res['Answer' + str(answer.index(letter))] = '*' + option_content

        return res


class GeneralExporter():

    @staticmethod
    def export_questions(questions: list):
        ispringexporter = iSpringExporter(questions)
        thinkificexporter = ThinkificExporter(questions)

        ispringexporter_files = ispringexporter.export_questions()
        thinkificexporter_files = thinkificexporter.export_questions()

        return {
            'Thinkific': thinkificexporter_files,
            'ISpring': ispringexporter_files
        }
