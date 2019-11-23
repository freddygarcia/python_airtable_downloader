from dotenv import load_dotenv
import xlsxwriter
import json
import requests
import os
import sys

def getJson():
    """
    This is that get json from airtable using api
    """
    load_dotenv()
    base_id = os.getenv('BASE_ID')
    api_key = os.getenv('API_KEY')
    authentication_api = os.getenv('AUTHENTICATION_API')
    authentication_api = authentication_api.format(base_id, api_key)

    #call api in Airtable
    response = requests.get(authentication_api)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        #get value whose status is 'Approved'
        parseJson(json_data)
        
    return response.status_code

def parseJson(json_data):
    """
    This is that get value whose status is 'Approved'
    """
    records_list = json_data['records']
    for record_item in records_list:
        fields_dict = record_item['fields']
        if fields_dict['status'] == 'Approved':            
            saveRecord(record_item)
        else:
            continue

def saveRecord(item):
    pass

def createXlsx():
    return getJson()