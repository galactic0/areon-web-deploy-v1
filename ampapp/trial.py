import requests
import json



# def get_km():
x = requests.get('https://www15.trakntell.com/tnt/servlet/tntAPI?orgid=083fdecea16a486519650060568865f2&vehicle_id=*&method=GET').json()
j=json.loads(x)
print(j['status'])



# get_km()

