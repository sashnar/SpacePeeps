import requests
import json

customerId = '5e4866a7322fa016762f38fe'
apiKey = 'cb65471378a01fc922eeb8ed364c6ec4'
accountId = '5e4866a8322fa016762f3900'

urlAccounts = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
urlBills = 'http://api.reimaginebanking.com/accounts/{}/bills?key={}'.format(accountId,apiKey)

response1 = requests.get(urlAccounts)
response2 = requests.get(urlBills)

payload = {
  "status": "pending",
  "payee": "5e4866a8322fa016762f3900",
  "nickname": "Delmer\'s Account",
  "payment_date": "2020-02-16",
  "recurring_date": 1
}


print(response1)
print(response1.content)

print(response2)
print(response2.content)

response = requests.post(urlBills, data = json.dumps(payload), header = {"Accept: application/json" })
print(response)
