from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from .forms import Subscribe
from AMTPL.settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives
from .models import trackingapi
from celery.decorators import task



# Create your views here.
def index(request):

    
    return render(request,'index.html',{'dist':trackingapi.objects.values()[len(trackingapi.objects.values())-1]['distance']+251110.0})
# save into database
def submit(request):
    data = request.POST
   
    a = Contact()
    a.name = data['name']

    a.email = data['email']

    a.message = data['message']
    a.save()

    
    

# send emails to users
    
    if request.method == 'POST':
        name, email, message = data['name'],data['email'],data['message']

        subject = 'Welcome to Areon Mobility Technologies Private Ltd'
       
        message = "Hi {} \n\nThank you for your interest in Areon Mobility Technologies. We are thrilled to hear from you.\n\nWe’d like to connect with you over a call to know your requirements and understand how we can be a good fit for your project needs. \nRequesting you to revert back with a detailed requirement and suitable time for a call.\n\nFeel free to simply reply if you have any queries, we’d be happy to assist.\n\nRegards,\n\nAreon Mobility".format(name) 
        recepient = str(data['email'])
        send_mail(subject,message,EMAIL_HOST_USER , [recepient],  fail_silently = False)
        

        contact = {'name':name, 'recepient':recepient, 'message':message,}

#send emails to info@areon.in

    if request.method == 'POST':
        name, email, message = data['name'],data['email'],data['message']

        subject = '{} requested for a call'.format(name)
    
        message = "Hi Aman Pal, \n\n{0} would like to contact with you.\n\n Below are the {0}'s contact form submitted : \n\n Name\t : {0} \nEmail\t : {1} \nMessage\t : {2}".format(name,email,message) 

        send_mail(subject,message,EMAIL_HOST_USER , ['info@areon.in'], fail_silently = False)
    
    
        return redirect('index')
        
    return redirect('index',context=contact )
    

# Hi [Name],

# Thank you for your interest in Areon Mobility Technologies. We are thrilled to hear from you.

# We’d like to connect with you over a call to know your requirements and understand how we can be a good fit for your project needs. Requesting you to revert back with a detailed requirement and suitable time for a call.

# Feel free to simply reply if you have any queries, we’d be happy to assist.

# Regards,
 #Areon Mobility

def subscribe(request):
    return render(request,'subscribe.html')


    
# get_km()


# def update_km():
#     try:
#         x = request.urlopen('https://www15.trakntell.com/tnt/servlet/tntAPI?orgid=083fdecea16a486519650060568865f2&vehicle_id=*&method=GET').read()
#         j=json.loads(x)
#         dict1=j['response']
#         distance=sum([float(x.get('odometer')) for x in dict1])+250000
#         data = {'distance': distance}
#         trackingapi.objects.update(**data)
#     except:
#         pass

       
# Run this function if database is empty
# if not trackingapi.objects.all():      
#     get_km()


