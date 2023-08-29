from tkinter import *
from tkinter import ttk
import requests

def get():  # function create to get the city name from combobox
    city=city_name.get()# give any 
    data=requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=67aa8f36cf971ee65d227c3de98e95d5').json()
    w_label1.config(text=data['weather'][0]['main']) # key, o index, key
    wb_label1.config(text=data['weather'][0]['description'])
    temp_label1.config(text=int(data['main']['temp']-273.15)) # kelvin ko degree mai convert karne kai liye minus kiya
    pres_label1.config(text=data['main']['pressure'])

win= Tk()
win.title('weather app')
win.config(bg= 'blue')
win.geometry('500x570')
win.resizable(0,0)

mylabel=Label(text='current weather update',font=('Time New Roman',27,'bold'),bg='light blue')
mylabel.place(x=25,y=50,height=50,width=450)  # x and y is for padding 

list_name= ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh"
            ,"Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram",
            "Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand",
            "West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep",
            "National Capital Territory of Delhi","Puducherry"]

city_name=StringVar()  # cityname datatype is string

com =ttk.Combobox(win,text='current weather update',values= list_name,font=('Time New Roman',20,'bold'),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)  # values= list_name means state name, 


w_label=Label(win,text='Wheather Climate',font=('Time New Roman',18,'bold'),bg='light blue')
w_label.place(x=25,y=260,height=50,width=210)

w_label1=Label(win,text='',font=('Time New Roman',18,'bold'),bg='light blue',relief='groove')
w_label1.place(x=250,y=260,height=50,width=210)

wb_label=Label(win,text='Weather Description',font=('Time New Roman',15,'bold'),bg='light blue')
wb_label.place(x=25,y=330,height=50,width=210)

wb_label1=Label(win,text='',font=('Time New Roman',18,'bold'),bg='light blue',relief='groove')
wb_label1.place(x=250,y=330,height=50,width=210)

temp_label=Label(win,text='Temperature',font=('Time New Roman',18,'bold'),bg='light blue')
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1=Label(win,text='',font=('Time New Roman',18,'bold'),bg='light blue',relief='groove')
temp_label1.place(x=250,y=400,height=50,width=210)

pres_label=Label(win,text='Pressure',font=('Time New Roman',18,'bold'),bg='light blue')
pres_label.place(x=25,y=470,height=50,width=210)

pres_label1=Label(win,text='',font=('Time New Roman',18,'bold'),bg='light blue',relief='groove')
pres_label1.place(x=250,y=470,height=50,width=210)

done_button=Button(text='Done',font=('Time New Roman',20,'bold'),bg='light blue',relief="groove",command=get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()
