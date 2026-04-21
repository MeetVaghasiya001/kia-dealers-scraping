from request_data import request 
import requests as re
import json

state_api = 'https://www.kia.com/api/kia2_in/findAdealer.getStateCity.do'


def all_state_data(state_api):
    state_data = json.loads(request(state_api))

    all_codes = [{
        'state_code':code.get('val1').get('key'),
        'state_name':code.get('val1').get('value'),
        'cities':[{'city_code':s.get('key'),'city_name':s.get('value')} for s in code.get('val2')]
    } for code in state_data.get('data').get('stateAndCity')]

    # with open('clean1.json','w',encoding='utf-8') as f:
    #     json.dump(all_codes,f,indent=4,default=str)
    
    return all_codes

with open('stores.json','w',encoding='utf-8') as f:
    json.dump(all_state_data(state_api),f,indent=4,default=str)


    
    








