import json
f=open("c://pycharm//ds1//random.txt","r")
s=f.read()
content= json.loads(s)
print(content)
print(content['aman'])
print(content['aman']['age'])

d={"india":{"captain":"rohit sharma", "wicket-keeper":"rishabh pant",
            "coach":"ravi shahstri"}, "australia":{"captain": "pat cummins",
            "wicket-keeper": "brad haddin", "coach": "garry kirsten"}}

print(json.dumps(d['india']['captain']))
print(json.dumps(d))
print(json.dumps(d['australia']))
