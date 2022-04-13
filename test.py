import requests

BASE = 'http://127.0.0.1:5000/'  # base url

data=[
    {'likes':100,'views':50,'name':'title1'},
    {'likes':1000,'views':5000,'name':'title2'},
    {'likes':20,'views':50,'name':'title3'},
]

# for i in range(len(data)):
#     response= requests.put(BASE+'video/'+str(i), data[i])
#     print(response.json())

# response = requests.get(BASE+'helloworld/bill')
# print(response.json())

# response = requests.post(BASE+'world') # accessing the endpoint
# print(response.json())

# response = requests.put(BASE+'video/1',{'name':'name','likes':10,'views':100}) #entering the data
# print(response.json())

# input()
# response = requests.put(BASE+'video/1',{'name':'name','likes':10,'views':100}) #entering the data
# print(response.json())

# input()

# response = requests.get(BASE+'video/10') # getting the data at id=10 (abort function because no data at 10)
# print(response.json())

# response = requests.delete(BASE+'video/1') # delete method
# print(response)
# input()

# response = requests.get(BASE+'video/1') # getting the data at id=1
# print(response.json())