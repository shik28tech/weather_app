import tkinter as tk
import requests
from PIL import Image,ImageTk
root = tk.Tk()
#==========Image================
img = Image.open('E:\PYTHON\Weather_Info/sky.jpg')
img = img.resize((600,500),Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)

bg_lbl = tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)
#===========HEADER=============
root.title("Weather App")
root.geometry("600x500")
#Key - b9725aef27425ec40577db5c28140e82
#API - api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

#==========FUNCTIONS===========
def display(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        disp = 'City:%s\nCondition:%s\nTemperature:%s'%(city,condition,temp)
    except:
        disp = 'There is a problem while fetching the API.'
    return disp

def get_info(city):
    key = 'b9725aef27425ec40577db5c28140e82'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':key, 'q':city, 'units':'imperial'}
    response = requests.get(url,params)
    # print(response.json())
    weather = response.json()
    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])
    txt_out['text'] = display(weather)
    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(F2.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('E:\PYTHON\Weather_Info/img/'+icon+'.png').resize((size,size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor='nw',image=img)
    weather_icon.image = img
title = tk.Label(bg_lbl,text="Welcome to our weather portal. Hope you get right information.",fg="crimson",bg="sky blue",font=("times new roman",13,"bold"))
title.place(x=80,y=20)
#==========FRAME-1==============
F1 = tk.Frame(bg_lbl,bg="light blue",bd=5)
F1.place(x=80,y=60,width=450,height=50)

#=========Text-Field-1===========
txt_box = tk.Entry(F1,font=("times new roman",25),width=17)
txt_box.grid(row=0,column=0,sticky='w')

#========Button=================
btn = tk.Button(F1,text="Get Weather",fg="black",bg="grey",font=("times new roman",15,"bold"),command=lambda: get_info(txt_box.get()))
btn.grid(row=0,column=1,padx=10)

#==========FRAME-2==============
F2 = tk.Frame(bg_lbl,bg="light blue",bd=5)
F2.place(x=80,y=130,width=450,height=350)

txt_out = tk.Label(F2,font=40,bg="white",justify='left',anchor='nw')
txt_out.place(relwidth=1,relheight=1)

weather_icon = tk.Canvas(txt_out,bg='white',bd=0,highlightthickness=0)
weather_icon.place(relx=.75,rely=0,relwidth=1,relheight=0.5)
root.mainloop()