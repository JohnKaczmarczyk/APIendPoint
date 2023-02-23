import json



def get():
    
    f = open('/media/pi/KINGSTON/project1/test/crawling/other/p.json')
    

    data = json.load(f)
    u = data['credentials'][0]["user"]
    p = data['credentials'][0]["password"]
    db = data['credentials'][0]["database"]

    return u,p,db

