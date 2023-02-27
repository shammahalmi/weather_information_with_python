#firestore'a eklemeden sadece ekrana hava durumunun bilgilerini yazdıran kod
import requests, json
apiKey="6853996b05196595ef2117e21a701482"
baseUrl="https://api.openweathermap.org/data/2.5/weather?q="
cityName=input("enter your city: ")
completeUrl= baseUrl+ cityName+ "&appid="+apiKey
response =requests.get(completeUrl)
data =response.json()
print("Current temperature: ",data["main"]["temp"],'k')
print("all information: ",data)
