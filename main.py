import redis
import random
import  tkinter
# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)
# Send a ping request and check the response
response = r.ping()
print("Response:", response)
#generate random code
random_Code=random.randint(1 , 10)
mobile_number=""
#catch mobile number from user
mobile_number=input(f'please enter your mobile number:{mobile_number}')
#print (mobile_number)