from pprint import pprint
import requests
# project=['dp-slackbot','dp-sandbox','americanpod']
# service=['dp-slackbotser','dp-service','americanservice']
# pods=[['dp-slackbot1'],['dp-sandbox1'],['americanpod1']]

# [p.update({i:s.update({j:pods})}) for j in service for i in project ]
# pprint(p)

projecturl="https://dpslackbotlistnr-dev.aexp.com/api/v1/tickroperations/projects?carid=200003973"
serviceurl="https://dpslackbotlistnr-dev.aexp.com/api/v1/tickroperations/services?projects={}"
podsurl="https://dpslackbotlistnr-dev.aexp.com/api/v1/tickroperations/pods?projects={}&services={}"
project=requests.get(url=projecturl).json()
p={}
s={}
for i in project:
    service=requests.get(serviceurl.format(i)).json()
    s={}
    #service will be fetched for each project
    for j in service:
        pods = requests.get(podsurl.format(i,j)).json()
        s.update({j:pods})
        # print(s)
    print(s)
    p.update({i:s})
print(p)

pprint(p)