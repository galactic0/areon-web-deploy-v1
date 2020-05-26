from __future__ import absolute_import, unicode_literals
from celery import shared_task
from time import sleep
# from urllib import request, response, parse
import json
from datetime import datetime
from ampapp.models import trackingapi
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from AMTPL.celery import *
import requests


#https://github.com/celery/celery/issues/4178


logger = get_task_logger(__name__)

# def get_km():
#     try:
#         print("------")
#         x = requests.get('https://www15.trakntell.com/tnt/servlet/tntAPI?orgid=083fdecea16a486519650060568865f2&vehicle_id=*&method=GET').json()
#         print(x['status'])
#     except:
#         print("exception came")

      


# def save_distance(data):
#     data=float(data)
    



@periodic_task(
    run_every=(crontab(minute='*/5')),
    name="driver func for km",
    ignore_result=False
    
)
# @shared_task(name='driver func for km')
def driver_km():
    print("------")
    x = requests.get('https://www15.trakntell.com/tnt/servlet/tntAPI?orgid=083fdecea16a486519650060568865f2&vehicle_id=*&method=GET').json()
    dict1=x['response']
    km_sum=sum([float(x.get('odometer')) for x in dict1])
    trackingapi.objects.create(distance=km_sum)
    print("the value is stored {}".format(km_sum))

# @shared_task() 
# def see_you():
#     print("See you in ten seconds!")
# app.conf.beat_schedule = {
#     "see-you-in-ten-seconds-task": {
#         "task": "periodic.see_you",
#         "schedule": 10.0
#     }
# }

    

