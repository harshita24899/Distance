#!/usr/bin/env python
# coding: utf-8

# In[2]:


import googlemaps
import geocoder


# In[3]:


# API key for Distance matrix map API
API_key = 'AIzaSyCUERxhqvGGrAmO7225MRSLT8D6tK1gGFo'
gmaps = googlemaps.Client(key=API_key)


# In[31]:


# API key for geocoding map API
gmaps_key =googlemaps.Client(key= 'AIzaSyCIWxn8xOIdSiEGXmRfmmzOkzHfcllWVWA' ) 

#-----------------------------------------#
#    Finding current location of user     #
#-----------------------------------------#

myloc = geocoder.ip('me')
lat1=(myloc.latlng[0])
long1=(myloc.latlng[1])

origins = (lat1,long1)
#origins = (LatOrigin,LongOrigin)

#-----------------------------------------#
#         Destination location            #
#-----------------------------------------#

geocode_result=gmaps_key.geocode('Marathahalli Bangalore')
lat2 = geocode_result[0]['geometry']['location']['lat']
lng2 = geocode_result[0]['geometry']['location']['lng']

destination = (lat2,lng2)

#-----------------------------------------#
# Find Distance bn source and destination #
#-----------------------------------------#

result = gmaps.distance_matrix(origins, destination)["rows"][0]["elements"][0]["distance"]["text"]
src = gmaps.distance_matrix(origins, destination)["origin_addresses"][0]
desti = gmaps.distance_matrix(origins, destination)["destination_addresses"][0]

print('------------------')
print('Src:',src)
print('------------------')
print('Destination:',desti)
print('------------------')
print('Distance: ',result)
print('------------------')


# In[33]:


myloc = geocoder.ip('me')
lat1=(myloc.latlng[0])
long1=(myloc.latlng[1])

origins = (lat1,long1)
print(origins)


# In[ ]:




