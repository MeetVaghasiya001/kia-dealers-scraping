from parser import * 
from concurrent.futures import ThreadPoolExecutor
from db import *
from model import *
import time

st = time.time()
state_api = 'https://www.kia.com/api/kia2_in/findAdealer.getStateCity.do' # state api retrun all codes and state and city name
city_api = 'https://www.kia.com/api/kia2_in/findAdealer.getDealerList.do'# it retrun all city store data in json form

all_states = all_state_data(state_api) # it return store.json
all_kia_data = [] # all data was store in this list
create_db() # it create kia table
count = 0


# this function was extract store data and all in all_kia_data 
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

        # it is request delers api for get store data
        responce = json.loads(request(city_api,params))

        stores_json = responce.get('data')

        # all stores for 1 city was itrate hear
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
            
        # store was add in store_data dict
        store_data['all_stores'].append({
            'city': c.get('city_name'),
            'stores': stores
        })

    print(store_data.get('state_name'))
    # it validate store_data and then return it
    validate = State(**store_data)
    return validate.model_dump()

# it create 8 threads for make work fast and all_kia_data list for itrate 
with ThreadPoolExecutor(max_workers=8) as executor:
    all_kia_data = list(executor.map(process, all_states))

    row = []
    store_count = 0
    # it is itrate all stores and add it in db 
    for a in all_kia_data:
        # it skip none data 
        if not a:
            continue

        for s in a.get('all_stores'):
            store_count +=1
            for store in s.get('stores'):

                row.append((
                    a.get('state_name'),
                    store.get('id'),
                    store.get('store_name'),
                    store.get('url'),
                    store.get('full_address'),
                    store.get('phone1'),
                    store.get('phone2'),
                    store.get('dealer_type')
                ))

                # this is add 100 data when length of row is 100
                if len(row) == 100:
                    insert_data(row)
                    row.clear()

# if there is any data in row then this is add in db 
if row:
    insert_data(row)

print(count)
# it dumps all_kia_data json 
with open('kia.json','w',encoding='utf-8') as f:
    json.dump(all_kia_data,f,indent=4,default=str,ensure_ascii=False)

# it calculate run time of program
et = time.time()
print(f'total time :{(et-st)/60:.2f}')