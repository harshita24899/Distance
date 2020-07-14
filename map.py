import tkinter as tk
import googlemaps
import geocoder
from tkinter import *
from subprocess import check_output
from PIL import ImageTk,Image
import re
import time

root= tk.Tk()
root.title("HIK Maps")

canvas1 = tk.Canvas(root, width = 400, height = 300)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\Harshita\\Downloads\\map2.png"))
canvas1.create_image(0,0,anchor=NW,image=image)
canvas1.pack()

entry2 = tk.Entry (root,bg='white')
entry2.insert(0, "Source")
entry2.configure(state=DISABLED)
canvas1.create_window(200, 100, window=entry2,width=250)

entry1 = tk.Entry (root,bg='white')
entry1.insert(0, "Destination")
entry1.configure(state=DISABLED)
canvas1.create_window(200, 140, window=entry1,width=250)

def on_click1(event):
    entry1.configure(state=NORMAL)
    entry1.delete(0, END)
    entry1.unbind('<Button-1>', on_click_id1)

def on_click2(event):
    entry2.configure(state=NORMAL)
    entry2.delete(0, END)
    entry2.unbind('<Button-2>', on_click_id2)

on_click_id1 = entry1.bind('<Button-1>', on_click1)
on_click_id2 = entry2.bind('<Button-1>', on_click2)

def getDistance ():
    src=entry2.get()
    dest=entry1.get()

    # API key for Distance matrix map API
    API_key = 'ENTER_API_KEY_HERE'
    gmaps = googlemaps.Client(key=API_key)

    # API key for geocoding map API
    gmaps_key =googlemaps.Client(key= 'ENTER_API_KEY_HERE' )

    #-----------------------------------------#
    #            Source location              #
    #-----------------------------------------#

    geocode_result=gmaps_key.geocode(src)
    print(geocode_result)
    print('****************************************************************************')
    lat1 = geocode_result[0]['geometry']['location']['lat']
    lng1 = geocode_result[0]['geometry']['location']['lng']

    origins = (lat1,lng1)

    #-----------------------------------------#
    #         Destination location            #
    #-----------------------------------------#

    geocode_result=gmaps_key.geocode(dest)
    print(geocode_result)
    print('****************************************************************************')
    lat2 = geocode_result[0]['geometry']['location']['lat']
    lng2 = geocode_result[0]['geometry']['location']['lng']

    destination = (lat2,lng2)

    #-----------------------------------------#
    # Find Distance bn source and destination #
    #-----------------------------------------#

    result = gmaps.distance_matrix(origins, destination)["rows"][0]["elements"][0]["distance"]["text"]
    print(gmaps.distance_matrix(origins, destination))
    src = gmaps.distance_matrix(origins, destination)["origin_addresses"][0]
    desti = gmaps.distance_matrix(origins, destination)["destination_addresses"][0]

    label1 = tk.Label(root, text=result,fg="black",font=("Arial Bold", 26))
    canvas1.create_window(200, 230, window=label1)

    #-----------------------------------------#
    #     Find current location of user       #
    #-----------------------------------------#
def getCurrent():

    # API key for Distance matrix map API
    API_key = 'ENTER_API_KEY_HERE'
    gmaps = googlemaps.Client(key=API_key)

    accuracy = 3 #Starting desired accuracy is fine and builds at x1.5 per loop
    lat1=0
    lng1=0


    while True:
        out = check_output(["powershell.exe", "C:\\Users\\Harshita\\Documents\\College\\sem6\\Cloud\\a.ps1"])
        out=out.decode('ascii')
        out = re.split('\r\n', out)
        print(out)
        lat = float(out[0])
        long = float(out[1])
        lat1=str(lat)
        lng1=str(long)
        break
    origins=(lat1,lng1)

    import geopy
    from geopy.geocoders import Nominatim
    from geopy.extra.rate_limiter import RateLimiter
    locator = Nominatim(user_agent='myGeocoder')
    coordinates = str(lat1+','+lng1)
    location = locator.reverse(coordinates)
    location.raw
    src=location.address

    entry2.insert(0,src)




button1 = tk.Button(text='Calculate distance', command=getDistance,bg='white')
canvas1.create_window(200, 180, window=button1)

button1 = tk.Button(text='Get Current location', command=getCurrent,bg='white')
canvas1.create_window(200, 60, window=button1)

root.mainloop()
