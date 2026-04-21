from parser import * 
from concurrent.futures import ThreadPoolExecutor
from db import *
from model import *
state_api = 'https://www.kia.com/api/kia2_in/findAdealer.getStateCity.do'
city_api = 'https://www.kia.com/api/kia2_in/findAdealer.getDealerList.do'

all_states = all_state_data(state_api)
all_kia_data = []
create_db()
count = 0
def process(data):
    global count
    params = {}
    state_name = data.get('state_name')
    state_code = data.get('state_code') 
    params['state'] = state_code
    store_data = {
        'state_name':state_name,
        'state_code':state_code,
        'all_stores':[]
    }

    for c in data.get('cities'):
        city_code = c.get('city_code')
        params['city'] = city_code

        responce = json.loads(request(city_api,params))

        stores_json = responce.get('data')

        stores = []
        for s in stores_json:
            address = [s.get('address1'),s.get('address2'),s.get('address3')]
            stores.append({
                'id':s.get('id'),
                'store_name':s.get('dealerName'),
                'url':s.get('website') or None,
                'full_address': "".join(i for i in address if i),
                'phone1':s.get('phone1') or None,
                'phone2':s.get('phone2') or None,
                'dealer_type':s.get('dealerType') or None
            })

            count += 1
            

        store_data['all_stores'].append({
            'city': c.get('city_name'),
            'stores': stores
        })

    print(store_data.get('state_name'))
    validate = State(**store_data)
    return validate.model_dump()


with ThreadPoolExecutor(max_workers=8) as executor:
    all_kia_data = list(executor.map(process, all_states))

    conn,cur = connection()
    store_count = 0
    for a in all_kia_data:
        for s in a.get('all_stores'):
            store_count +=1
            for store in s.get('stores'):

                cur.execute("""
                    INSERT INTO kia(state_name,store_id,store_name,url,full_address,phone1,phone2,dealer_type) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                """,(
                    a.get('state_name'),
                    store.get('id'),
                    store.get('store_name'),
                    store.get('url'),
                    store.get('full_address'),
                    store.get('phone1'),
                    store.get('phone2'),
                    store.get('dealer_type')
                ))

                conn.commit()
            print(f'{store_count} city was add!!')

conn.close()
print(count)
with open('kia.json','w',encoding='utf-8') as f:
    json.dump(all_kia_data,f,indent=4,default=str)