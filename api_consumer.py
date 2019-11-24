
import requests
import json
import pandas


def get_questions(base_id: str, key: str, offset=None) -> list:
    '''
        :params
        - base_id: Airtable Base ID
        - key : Airtable API KEY
        - offset: offset id from request to paginate resulsts
    '''

    # decide if have to offset
    offset = '&offset=' + offset if offset else ''
    # status filter and offset
    extra = '?filterByFormula=({status}="Approved")' + offset
    # build url
    url = f'https://api.airtable.com/v0/{base_id}/Questions' + extra
    # required headers to correctly authenticate
    headers = {'Authorization': 'Bearer ' + key}
    # everythinh together
    r = requests.get(url, headers=headers)

    # check if the request of successful
    if not r.ok:
        return None

    # convert the result into a dict
    questions = json.loads(r.text)
    # extract the possible offset from response
    offset = questions.get('offset')
    # get only the record list from response
    questions = questions.get('records', list())

    # if there is more data, append to it. same process
    if offset:
        questions += get_questions(base_id, key, offset)

    # return the question dict list
    return questions


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
    res['Question Text'] = fields['question_text']
    res['Explanation'] = fields['feedback']

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
    df = pandas.DataFrame(questions)

    # to add some features in the near future
    writer = pandas.ExcelWriter(output_name, engine='xlsxwriter')

    # prepare export
    df.to_excel(writer,
                sheet_name='QUESTIONS',
                index=False,
                columns=[
                    'Question Type', 'Question Text', 'Explanation',
                    *['Choice' + str(c + 1) for c in range(10)]
                ])

    # save excel
    writer.save()


def main():

    KEY = 'key5k8M0BZMn7RNf6'
    BASE_ID = 'appEfbsDGIsNiYX6R'
    output_name = './AllChapters.xls'

    questions = get_questions(BASE_ID, KEY)
    questions = list(map(format_question, questions))
    export_excel(output_name, questions)


if __name__ == "__main__":
    main()

