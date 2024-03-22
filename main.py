import requests
import smtplib

my_email = 'shshshshs@gmail.com'
passw = '123456'
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "12234444"
MY_LAT = '89.222'
MY_LNG = '78.939'
parameters = {
    'appid' : api_key,
    'lat' : MY_LAT,
    'lon' : MY_LNG,
    'cnt' : 4
}

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast",params=parameters)
#print(response.status_code)
response.raise_for_status()
data = response.json()
print(data)
#print(data['list'][0]['weather'][0]['id'])
wether_data_4times = data['list']
#print(len(wether_data_4times))


will_rain = False

for each_hour in wether_data_4times:
    condition_code = each_hour['weather'][0]['id']
    if condition_code < 700:
        will_rain = True

if will_rain:
    print('Bring Umbrella')
    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=passw)
        connection.sendmail(from_addr=my_email,to_addrs='sksksksks@yahoo.com',msg='Subject: Rain alert\n\nBring Umbrella please ')
