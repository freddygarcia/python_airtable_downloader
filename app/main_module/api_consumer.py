import requests
import json


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
    # everything together
    r = requests.get(url, headers=headers)

    # check if the request of successful
    if not r.ok:
        return {
            'success' : False,
            'code' : r.status_code,
            'content' : r.reason
        }

    # convert the result into a dict
    json_response = json.loads(r.text)
    # extract the possible offset from response
    offset = json_response.get('offset')
    # get only the record list from response
    questions = json_response.get('records', list())

    # if there is more data, append to it. same process
    if offset:
        questions += get_questions(base_id, key, offset)['content']

    # return the question dict list
    return {
        'success' : True,
        'code' : r.status_code,
        'content': questions
    }


def main():

    KEY = 'key5k8M0BZMn7RNf6_'
    BASE_ID = 'appEfbsDGIsNiYX6R'
    output_name = './AllChapters.xlsx'

    questions = get_questions(BASE_ID, KEY)
    questions = list(map(format_question, questions))
    export_excel(output_name, questions)


if __name__ == "__main__":
    main()

