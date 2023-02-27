#firestore'a hava durumunun bilgilerini ekleyerek ekrana yazdıran kod
#şimdiki tarihi ve zamanı yazdırırken çalışan sistemin tarihi ve saati almaktadır , diğer bölgelerdeki saati hesaplamamaktadır, onun için ayrı bir import işlemi yapılması gerek.


import firebase_admin
import datetime
from firebase_admin import credentials
from firebase_admin import firestore
import requests

# Initialize Firebase credentials
cred = credentials.Certificate('python\weather\serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore database
db = firestore.client()

# OpenWeatherMap API key
api_key = '6853996b05196595ef2117e21a701482'

baseUrl="https://api.openweathermap.org/data/2.5/weather?q="
cityName=input("enter your city: ")
completeUrl= baseUrl+ cityName+ "&appid="+api_key
response =requests.get(completeUrl)
data =response.json()

# istedeiğimiz hava durumu bilgilerini çıkardık
temp = data['main']['temp']
description = data['weather'][0]['description']


# tarih ve saati almak 
now = datetime.datetime.now()
date_string = now.strftime("%Y-%m-%d")
time_string = now.strftime("%H:%M:%S")



#  Firestore'da data'ları saklamak
doc_ref = db.collection('weather').document(cityName)
doc_ref.set({
    'temperature': temp,
    'description': description,
    'current_time':time_string,
    'current_date':date_string
})

#firestore'da saklanacak tüm bilgileri ekrana yazdırmak
#print("all data: ",data)
print("Current date is:", date_string)
print("Current time is:", time_string)
print(f'Current temperature: {temp} K')
print(f'Weather description: {description}')
