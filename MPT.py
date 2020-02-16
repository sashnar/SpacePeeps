import requests
import json

customerId = '5e4866a7322fa016762f38fe'
apiKey = 'cb65471378a01fc922eeb8ed364c6ec4'
accountId = '5e4866a8322fa016762f3900'

urlAccounts = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
urlBills = 'http://api.reimaginebanking.com/accounts/{}/bills?key={}'.format(accountId,apiKey)


payload = {"payment_amount" : 121, "status": "pending",
  "payee": "5e4866a8322fa016762f3900",
  "nickname": "Delmer\'s Account",
  "payment_date": "2020-02-16",
  "recurring_date": 1
}

response1 = requests.get(urlAccounts)
response2 = requests.get(urlBills)

print(response1)
print(response1.content)

print(response2)
print(response2.content)

response = requests.post(urlBills,data= json.dumps(payload), headers={'content-type':'application/json'})
print(response)
print(response.content)

response2 = requests.get(urlBills)
print(response2)
print(response2.content)

    def check_percentages(self)
        if (math.sum(percent_dict.values()) != 1.0)
            for x in range(0, len(percent_dict.values()))
                percent_dict

