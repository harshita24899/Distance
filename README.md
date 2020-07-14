# Distance
Distance between current location (or any source) and destination address using Google Map APIs

```
Input: Current location (or any location) and destination location 
Output: Distance in KMs
```
Google Cloud Platform (GCP) was the chosen cloud service and python as the programming language.

#### Google Cloud Platform provides a variety of Map APIs from which the following were used:
##### 1.	Geocoding Map API
*	Convert between addresses and geographic coordinates.
*	Convert addresses into geographic coordinates (geocoding). 
*	This API also allows converting geographic coordinates into an address (reverse geocoding).
*	To use the Geocoding API, it must be enabled and obtain the proper authentication credentials. 

##### 2.	Distance matrix map API
*	With this API, one can access travel distance and time for a matrix of origins and destinations.
*	The information returned is based on the recommended route between start and endpoints and consists of rows containing duration and distance values for each pair.
*	Just like the Geocoding Map API, this must enable this API, and produce an API key as well before using else will be thrown an ERROR message.


#### Below listed are the Python Modules used: 

##### 1. Googlemaps: 
*Imported to access the Distance Matrix API which finds the distance between two locations that is given by user
##### 2. Geocoder: 
*Imported to access the Geocoding API which will help convert the address into latitude and longitude 
##### 3. Geopy: 
*This contains Nominatim which is imported to help with reverse coding (i.e. to convert latitude and longitude to an address)
##### 4. Subprocess: 
*One can start a process in Python using the Popen function call, which is very handy when you want to run a system. Here, it is used to access the GPS location of the user's device to obtain the current location
##### 5. Tkinter: 
*This module is used to create the GUI of the application.
##### 6. PIL: 
*Used to put the background image in the GUI   
