import requests


url = 'http://localhost:9696/predict'

customer = {
    "gender":"Female",
    "age":21.0,
    "height":1.62,
    "weight":64.0,
    "family_history_with_overweight":"yes",
    "favc":"no",
    "fcvc":2.0,
    "ncp":3.0,
    "caec":"Sometimes",
    "smoke":"no",
    "ch2o":2.0,
    "scc":"no",
    "faf":0.0,
    "tue":1.0,
    "calc":"no",
    "mtrans":"Public_Transportation"
    }

response = requests.post(url, json=customer).json() # .json() converts the response to JSON
print(response)

if response['level'] == 0:
    print('Your weight status is UNDERWEIGHT')
elif response['level'] == 1:
    print('Your weight status is NORMAL')
elif response['level'] == 2:
    print('Your weight status is OBESITY TYPE 1')
elif response['level'] == 3:
    print('Your weight status is OBESITY TYPE 2')
elif response['level'] == 4:
    print('Your weight status is OBESITY TYPE 3')
elif response['level'] == 5:
    print('Your weight status is OVERWEIGHT LEVEL 1')
elif response['level'] == 6:
    print('Your weight status is OVERWEIGHT LEVEL 2')