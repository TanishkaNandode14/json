# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 18:19:03 2022

@author: Dell
"""

from tkinter import *
import requests
import json

root=Tk()
root.title("Find the Capital City's Info In No Time")
root.geometry("550x500")
root.configure(background="powder blue")

#Setting labels
city_name_label=Label(root, text="Capital City Name",font=("Helvetica", 18,'bold'),bg="powder blue")
city_name_label.place(relx=0.12,rely=0.15,anchor=W)

city_entry=Entry(root)
city_entry.place(relx=0.12,rely=0.25,anchor=W)

country_label = Label(root,text="Country: ", bg="powder blue", font=("bold", 10))
country_label.place(relx=0.12,rely=0.5,anchor=W) 

region_label = Label(root,text="Region: ", bg="powder blue", font=("bold",10)) 
region_label.place(relx=0.12,rely=0.6,anchor=W) 

language_label = Label(root,text="Language: ", bg="powder blue", font=("bold",10)) 
language_label.place(relx=0.12,rely=0.7,anchor=W)

population_label = Label(root,text="Population: ", bg="powder blue", font=("bold",10)) 
population_label.place(relx=0.12,rely=0.8,anchor=W)

area_label = Label(root,text="Area: ", bg="powder blue", font=("bold",10)) 
area_label.place(relx=0.12,rely=0.9,anchor=W)
    
def city_name():
    api_request = requests.get("https://restcountries.com/v2/capital/" + city_entry.get())
    api_output_json = json.loads(api_request.content)
    
    country_info = api_output_json[0]['name']
    print(country_info)
    
    region_info = api_output_json[0]['region']
    print(region_info)
    
    language_info = api_output_json[0]['languages'][0]["nativeName"]
    print(language_info)
    
    population_info = api_output_json[0]['population']
    print(population_info)
    
    area_info = api_output_json[0]['area']
    print(str(area_info) + " km2")
    
    
    country_label["text"] = "Country: " + str(country_info)
    region_label["text"] = "Region: " + str(region_info)
    language_label["text"] = "Language: " + str(language_info)
    population_label["text"] = "Population: " + str(population_info)
    area_label["text"] = "Area: " + str(area_info)
    
    #city_name_label["text"] = city_entry.get()
    #city_entry.destroy()
    #search_btn.destroy()


btn = Button(root,text="Search",command=city_name,relief=FLAT)
btn.place(relx=0.12,rely=0.35,anchor=W)

root.mainloop()
