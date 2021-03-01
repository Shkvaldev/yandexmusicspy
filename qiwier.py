import requests
import json
import config
import random
import time

class QiwiKassa:

	def __init__(self):
		pass

	def expiration(self):
			now_time = time.strftime("%Y-%m-%dT%H:%M:%S")
			exp_time = now_time + "+00:03"
			print(exp_time)
			return exp_time

	def billid(self):
		billid = 'BotProvider-'+str(random.randint(111111, 999999))+"-"+str(random.randint(111111, 999999))
		return billid

	def Bill(self, value, comment = "by Shkval"):
		headers={'Authorization': 'Bearer {}'.format(config.QIWI_TOKEN),
		         'Accept': 'application/json',
		         'Content-Type': 'application/json',
		         }

		params={'amount': {'value': value, 
		                   'currency': 'RUB',
		                   },
		        'comment': comment, 
		        'expirationDateTime': self.expiration(), 
		        'customer': {}, 
		        'customFields': {},        
		        }
		params = json.dumps(params)

		g = requests.put('https://api.qiwi.com/partner/bill/v1/bills/{}'.format(self.billid()),
		                  headers=headers,
		                  data=params,
		                  )
		ans = g.json()
		return ans

	def check(self, billid):
		headers={'Authorization': 'Bearer {}'.format(config.QIWI_TOKEN),
		         'Accept': 'application/json',
		         'Content-Type': 'application/json',
		         }
		g = requests.get('https://api.qiwi.com/partner/bill/v1/bills/{}'.format(billid), headers = headers)
		ans = g.json()
		return ans['status']['value']


	def reject(self, billid):
		headers={'Authorization': 'Bearer {}'.format(config.QIWI_TOKEN),
		         'Accept': 'application/json',
		         'Content-Type': 'application/json',
		         }
		g = requests.post('https://api.qiwi.com/partner/bill/v1/bills/{}/reject'.format(billid), headers = headers)