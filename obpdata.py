import requests
import json
from constants import LOGIN_URL,BALANCE_URL,login_header,DL_TOKEN

balance_data = [{"bank_id":"Latlux","account_id":"5430670","balance":3640,"expenses":[{"name":"Transportation","amount":1000,"categoryId":1},{"name":"Food","amount":1224.35,"categoryId":2},{"name":"Utilities","amount":520,"categoryId":3},{"name":"Medical & Healthcare","amount":2321,"categoryId":4}]},{"bank_id":"Pannier","account_id":"51-8010051","balance":8627,"expenses":[{"name":"Transportation","amount":1200,"categoryId":1},{"name":"Food","amount":2245.35,"categoryId":2},{"name":"Utilities","amount":1235.29,"categoryId":3},{"name":"Medical & Healthcare","amount":1623,"categoryId":4}]},{"bank_id":"Tampflex","account_id":"20-5375546","balance":-2432,"expenses":[{"name":"Transportation","amount":675.68,"categoryId":1},{"name":"Food","amount":980.35,"categoryId":2},{"name":"Utilities","amount":823.29,"categoryId":3},{"name":"Medical & Healthcare","amount":1327.98,"categoryId":4}]},{"bank_id":"Tres-Zap","account_id":"04-3114529","balance":1723.82,"expenses":[{"name":"Transportation","amount":700.68,"categoryId":1},{"name":"Food","amount":1207.35,"categoryId":2},{"name":"Utilities","amount":874.29,"categoryId":3},{"name":"Medical & Healthcare","amount":1225.98,"categoryId":4}]},{"bank_id":"Greenlam","account_id":"58-6993977","balance":-3000.82,"expenses":[{"name":"Transportation","amount":1008.68,"categoryId":1},{"name":"Food","amount":1637.35,"categoryId":2},{"name":"Utilities","amount":432.29,"categoryId":3},{"name":"Medical & Healthcare","amount":1325.98,"categoryId":4}]},{"bank_id":"It","account_id":"09-6877184","balance":3521.82,"expenses":[{"name":"Transportation","amount":3421.68,"categoryId":1},{"name":"Food","amount":1637.35,"categoryId":2},{"name":"Utilities","amount":531.29,"categoryId":3},{"name":"Medical & Healthcare","amount":1275.98,"categoryId":4}]},{"bank_id":"Latlux","account_id":"37-1906857","balance":-2388.82,"expenses":[{"name":"Transportation","amount":1436.68,"categoryId":1},{"name":"Food","amount":2005.35,"categoryId":2},{"name":"Utilities","amount":538.29,"categoryId":3},{"name":"Medical & Healthcare","amount":722.98,"categoryId":4}]},{"bank_id":"Home Ing","account_id":"59-7476513","balance":2788.82,"expenses":[{"name":"Transportation","amount":1384.68,"categoryId":1},{"name":"Food","amount":1328.35,"categoryId":2},{"name":"Utilities","amount":528.29,"categoryId":3},{"name":"Medical & Healthcare","amount":841.98,"categoryId":4}]},{"bank_id":"Job","account_id":"97-0957797","balance":-1563.82,"expenses":[{"name":"Transportation","amount":1263.68,"categoryId":1},{"name":"Food","amount":2005.35,"categoryId":2},{"name":"Utilities","amount":673.29,"categoryId":3},{"name":"Medical & Healthcare","amount":1478.98,"categoryId":4}]}]

def call_obp_login_service():
    r = requests.post(LOGIN_URL, headers=login_header)
    print(r.status_code)
    print(r.text)
    t = r.json()['token']
    print("Received token: {0}".format(t))
    return t

# def get_obp_balances(bank_id, account_id):
#     print(DL_TOKEN)
#     r = requests.get(BALANCE_URL, headers=DL_TOKEN)
#     statuscode = r.status_code
#     print(statuscode)
#     print(DL_TOKEN.get('Authorization'))
#     print(type(DL_TOKEN))
#     print('token' in DL_TOKEN)
#     if statuscode == 400 or 'token' in DL_TOKEN:
#       token =  call_obp_login_service()
#       print('token = ' + token)
#       DL_TOKEN.replace('token', token)
#       r = requests.get(BALANCE_URL, headers=DL_TOKEN)
#     print(r.status_code)
#     print(r.text)

def get_obp_balances(bank_id, account_id):
    balances = []
    print(type(balance_data))
    for balance in balance_data:
        print(balance)
        if balance["account_id"] == account_id and balance["bank_id"] == bank_id:
            #balances.append("{}: {}".format(balances["loan_name"], balances["ammount"]))
            balances.append(balance)

    if len(balances) == 0:
        return "bank or account was not found"
    return_string = " "
    for b in balances:
        print(type(b))
        return b
    return "data not found"
