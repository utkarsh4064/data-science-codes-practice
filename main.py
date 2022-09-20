import json
f=open("c://pycharm//ds1//random.txt","r")
s=f.read()
content= json.loads(s)
print(content)
print(content['aman'])
print(content['aman']['age'])