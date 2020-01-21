import requests, os, os.path, time
from datetime import datetime
from os import system, name, path
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

# ดึง API ผ่าน openweathermap
api_url = "http://api.openweathermap.org/data/2.5/weather"

def current_weather():
    clear()
    while True:
      try:
        city = input("จังหวัดที่อยู่: ")

        params = {
            'q': city,
            'appid': '11c0d3dc6093f7442898ee49d2430d20', # Token ความปลอดภัยของ API
            'units': 'metric'
            }

        res = requests.get(api_url, params=params)

        # แปลงข้อมูลที่ได้มาเป็น json format
        data = res.json()
        main_temp = 'อุณหภูมิในจังหวัด {} คือ     {} องศาเซลเซียส'
        feels_like = 'รู้สึกเหมือน               {} องศาเซลเซียส'
        min_temp = 'อุณหภูมิต่ำสุด              {} องศาเซลเซียส'
        max_temp = 'อุณหภูมิสูงสูด              {} องศาเซลเซียส'
        humanity = 'ความชื่น                 {} เปอร์เซ็น'
        wind = 'ความเร็วลม              {} กม./ชม.'

        sunrise = 'พระอาทิตย์ขึ้นเมื่อ          ' + datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S')
        sunset = 'พระอาทิตย์ตกเมื่อ          ' + datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S')

        # หน่วงเวลาเพื่อโหลดข้อมูล API หากอินเทอร์เน็ตช้า
        print('กำลังติดต่อกับเซิฟเวอร์....')
        time.sleep(1)
        
        clear()
        print('-----------[ สภาพอากาศจังหวัด '+ city +' ]-----------')
        print('')
        print(main_temp.format(city, data["main"]["temp"]))
        print(feels_like.format(data["main"]["feels_like"]))
        print(min_temp.format(data["main"]["temp_min"]))
        print(max_temp.format(data["main"]["temp_max"]))
        print(wind.format(data["wind"]["speed"]))
        print(humanity.format(data["main"]["humidity"]))
        print('')
        print(sunrise)
        print(sunset)
        print('')

        x = input('คุณต้องการดูจังหวัดอื่นๆหรือไม่? [Y / N]\n')
        if 'Y' in x or 'y' in x:
            clear()
            continue
        elif 'N' in x or 'n' in x:
            index_()
            break
        else:
            break
      except:
        print('ERR: invild city please try again')
        continue

def index_():
    try:
        while True:
            clear()
            print('--------- [ โปรแกรมตรวจสอบสภาพอากาศ ] ---------')
            print('|')
            print('|    [1] ตรวจสอบข้อมูลอุณหภูมิ')
            print('|    [2] ตรวจค่าฝุ่น PM 2.5')
            print('|    [3] ตรวจค่าฝุ่น PM 10')
            print('|')
            print('|    [0] ออกจากโปรแกรม')
            print('------------------------------------------------')

            x = int(input('ป้อนตัวเลข: '))
            if x == 1:
                current_weather()
                break
            elif x == 2:
                break
            elif x == 3:
                break
            else:
                continue
    except:
        print('ERR: โปรแกรมไม่สามารถทำงานได้เนื่องจากเหตุผลบางอย่าง')

if __name__ == "__main__":
    index_()