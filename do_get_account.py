import json
import requests

api_token = 'qCmMDn7csHYkLMWneHewKtii/09VZKPJ'
api_scode = 'A28'
api_url_base = 'https://18.235.218.228'

headers = {'Content-Type': 'application/json','Autorization': 'shortCode %s' % api_scode, 'Auth': 'token %s ' % api_token}
#params={'shortCode':'A28','token':'qCmMDn7csHYkLMWneHewKtii/09VZKPJ'}
#beta  
# feito por naldo, testando git
# gi status 2
#Mudado
#inserção
def get_account_info():

    api_url = '{0}/api/ContasPagar/PlanoFinanceiro/'.format(api_url_base)
    print(format(api_url))
    print(format(headers))
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


account_info = get_account_info()

if account_info is not None:
    print("Here's your info: ")
    for k, v in account_info['PlanoFinanceiro'].items():
        print('{0}:{1}'.format(k, v))

else:
    print('[!] Request Failed')
