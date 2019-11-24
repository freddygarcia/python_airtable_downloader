import copy
import datetime
import uuid
import pandas
import tempfile

def files_to_json(session: dict, files: list):
    
    if not session.get('files'):
        session['files'] = {}

    session['files'].update(files)
    new_files = { f:files[f]['name'] for f in files}

    return new_files
        

def check_old_files(session):
    # 20 minutes
    MAX_FILE_LIFETIME_SECONDS = 1200
    
    if not session.get('files'):
        session['files'] = {}

    files = session['files'].copy()
    for _file in files:
        time_diff = datetime.datetime.now() - session['files'][_file]['created_at']
        
        if time_diff.total_seconds() > MAX_FILE_LIFETIME_SECONDS:
            del session['files'][_file]


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
    res['Question Type'] = 'MA' if len(fields['correct_answer']) > 1 else 'SA'
    res['Question Text'] = fields.get('question_text')
    res['Explanation'] = fields.get('feedback', '')

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


def export_excel(output_name: str, questions: list) -> None:
    '''
        :params
        - output_name: output file name
        - questions: formated list of questions to export 
    '''

    # convert array into pandas dataframe for simplicity
    questions = list(map(format_question, questions))
    df = pandas.DataFrame(questions)
    f = tempfile.NamedTemporaryFile(delete=False)
    # prepare export
    df.to_excel(f,
                sheet_name='QUESTIONS',
                index=False,
                columns=[
                    'Question Type', 'Question Text', 'Explanation',
                    *['Choice' + str(c + 1) for c in range(10)]
                ])
    return f.name


def group_questions(questions: list) -> list:

    grouped_questions = {}

    for question in questions:
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


def export_questions(questions: list) -> bool:

    files = {}

    def random_id():
        return str(uuid.uuid4())

    questions = questions['content']
    question_by_chapter = group_questions(questions)
    for chapter in question_by_chapter:
        file_name = chapter + '.xlsx'
        question_list = question_by_chapter[chapter]
        f_exported = export_excel(file_name, question_list)
        files[random_id()] = {'file': f_exported, 'name': chapter,
                              'created_at': datetime.datetime.now()}

    f_exported = export_excel('AllChapters.xlsx', questions)
    files[random_id()] = {'file': f_exported, 'name': 'All Chapters',
                          'created_at': datetime.datetime.now()}

    return files
