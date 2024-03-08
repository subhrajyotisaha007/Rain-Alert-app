import requests
import smtplib

my_email = 'test001saha@gmail.com'
passw = 'ghqligvctzfftjop'
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "ad9c268435b4ee3d5ac2bbb3bfba1ab4"
MY_LAT = '51.507351'#'36.852924'
MY_LNG = '-0.127758'#'-75.977982'
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

# for each in range(0,len(wether_data_4times)):
#     print(wether_data_4times[each]['weather'][0]['id'])
#     if wether_data_4times[each]['weather'][0]['id'] < 700:
#         print('Bring Umbrella')
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
        connection.sendmail(from_addr=my_email,to_addrs='test001saha@yahoo.com',msg='Subject: Rain alert\n\nBring Umbrella please ')