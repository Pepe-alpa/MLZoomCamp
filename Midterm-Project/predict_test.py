import requests


url = 'http://localhost:9696/predict'

customer = {"status":1,
            "drug":"Placebo","age":44.0,"sex":"F","ascites":"N","hepatomegaly":"N","spiders":"N","edema":"N","bilirubin":0.9,"cholesterol":400.0,"albumin":3.6,"copper":31.0,"alk_phos":1689.0,"sgot":164.3,"tryglicerides":166.0,"platelets":327.0,"prothrombin":10.4,"stage":3.0}
							
response = requests.post(url, json=customer).json() # .json() converts the response to JSON
print(response)

if response['status_cirrhosis'] == 0:
    print('High risk of death for cirrhosis')
elif response['status_cirrhosis'] == 1:
    print('Low risk of death for cirrhosis')
