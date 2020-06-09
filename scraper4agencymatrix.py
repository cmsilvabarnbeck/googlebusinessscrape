import json
import requests
import urllib
import pandas as pd
import pprint
from bs4 import BeautifulSoup
import re
from IPython.core.display import HTML


api_key = "AIzaSyCYcWpLDKf5yUAOqotd4QIBT3WULvcqMYU"
business = input("What type of businesses are you searching? ")
type(business)

url = urllib.request.urlopen("https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + business + '&key=' + api_key)

data = url.read().decode('utf-8')

dataInJson = json.loads(data)

dataResults = dataInJson["results"]
nameCount = json.dumps(dataResults).count('name')

df = pd.DataFrame(
        {
            "Name":[],
            "First Name":[],
            "Last Name":[],
            "Business Name":[],
            "Address":[],
            "City":[],
            "State":[],
            "Zip":[],
            "Language":[],
            "Phone1":[],
            "Phone2":[],
            "Phone3":[],
            "Phone4":[],
            "Driver's License Number":[],
            "DOB":[],
            "SSN":[],
            "Gender":[],
            "Marital Status":[],
            "Driver License State":[],
            "Date Licensed":[],
            "Email address 1":[],
            "Email address 2":[]
            
            
        })

for k in range (0, nameCount):
    busName = dataInJson["results"][k]["name"]
    busAdd = dataInJson["results"][k]["formatted_address"]
    busId = dataInJson["results"][k]["place_id"]
    url2 = urllib.request.urlopen("https://maps.googleapis.com/maps/api/place/details/json?placeid=" + busId + '&key=' + api_key)
    data2 = url2.read().decode('utf-8')

    dataInJson2 = json.loads(data2)
    phoneNumber = dataInJson2["result"]
    phoneNumber = phoneNumber.get("formatted_phone_number")
    street = dataInJson2["result"]
    street = street.get('adr_address')
    street = BeautifulSoup(street).text
    
    commaCount = street.count(",")
    testAddress = re.search("^[0-9]\d", street)
    
    if testAddress and phoneNumber is not None and commaCount == 3:
        street = street.split(", ")
        streetName = street[0]
        City = street[1]
        State = street[2].split(" ")
        StateName = State[0]
        Zip = State[1]
        Zip = str(Zip)[:5]
        
        if StateName == "NC":
            new_row = {"Name": busName, "Business Name": busName, "Address": streetName, "City": City, "State": StateName, "Zip": Zip,  "Phone1": phoneNumber}
            df = df.append(new_row, ignore_index=True)
    
   
pageOneToken = dataInJson.get('next_page_token')

if pageOneToken is not None:
   
    pageOne = urllib.request.urlopen("https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken=" + pageOneToken + '&key=' + api_key)
    p1Data = pageOne.read().decode('utf-8')
    p1Json = json.loads(p1Data)
    
    p1DataResults = p1Json["results"]
    p1NameCount = json.dumps(p1DataResults).count('name')

    for l in range (0, p1NameCount):
        p1BusName = p1Json["results"][l]["name"]
        p1BusAdd = p1Json["results"][l]["formatted_address"]
        p1BusId = p1Json["results"][l]["place_id"]
        p1url = urllib.request.urlopen("https://maps.googleapis.com/maps/api/place/details/json?placeid=" + p1BusId + '&key=' + api_key)
        p1Data = p1url.read().decode('utf-8')

        p1Json2 = json.loads(p1Data)
        p1PhoneNumber = p1Json2['result']
        p1PhoneNumber = p1PhoneNumber.get('formatted_phone_number')
        p1Street = p1Json2['result']
        p1Street = p1Street.get('adr_address')
        p1Street = BeautifulSoup(p1Street).text
        p1CommaCount = p1Street.count(",")
        #test and make sure we are working with a full address
        p1TestAddress = re.search("^[0-9]\d", p1Street)
           
        if p1TestAddress and p1PhoneNumber is not None and p1CommaCount == 3:
            
            p1Street = p1Street.split(", ")
            p1StreetName = p1Street[0]
            p1City = p1Street[1]
            p1State = p1Street[2].split(" ")
            p1StateName = p1State[0]
            p1Zip = p1State[1]
            p1Zip = str(p1Zip)[:5]
            
            if p1StateName == "NC":
                new_row1 = {"Name": p1BusName, "Business Name": p1BusName, "Address": p1StreetName, "City": p1City, "State": p1StateName, "Zip": p1Zip, "Phone1": p1PhoneNumber}
                df = df.append(new_row1, ignore_index=True)            
 
pageTwoToken = p1Json.get('next_page_token')

if pageTwoToken is not None:
   
    pageTwo = urllib.request.urlopen("https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken=" + pageTwoToken + '&key=' + api_key)
    p2Data = pageTwo.read().decode('utf-8')
    p2Json = json.loads(p2Data)
    
    p2DataResults = p2Json["results"]
    p2NameCount = json.dumps(p2DataResults).count('name')


    for m in range (0, p2NameCount):
        p2BusName = p2Json["results"][m]["name"]
        p2BusAdd = p2Json["results"][m]["formatted_address"]
        p2BusId = p2Json["results"][m]["place_id"]
        p2url = urllib.request.urlopen("https://maps.googleapis.com/maps/api/place/details/json?placeid=" + p2BusId + '&key=' + api_key)
        p2Data = p2url.read().decode('utf-8')

        p2Json2 = json.loads(p2Data)
        p2PhoneNumber = p2Json2['result']
        p2PhoneNumber = p2PhoneNumber.get('formatted_phone_number')
        p2Street = p2Json2['result']
        p2Street = p2Street.get('adr_address')
        p2Street = BeautifulSoup(p2Street).text
        p2CommaCount = p2Street.count(",")
        
        p2TestAddress = re.search("^[0-9]\d", p2Street)
           
        if p2TestAddress and p2PhoneNumber is not None and p2CommaCount == 3:
            
            p2Street = p2Street.split(", ")
            p2StreetName = p2Street[0]
            p2City = p2Street[1]
            p2State = p2Street[2].split(" ")
            p2StateName = p2State[0]
            p2Zip = p2State[1]
            p2Zip = str(p2Zip)[:5]
            
            if p2StateName == "NC":
                new_row2 = {"Name": p2BusName, "Business Name": p2BusName, "Address": p2StreetName, "City": p2City, "State": p2StateName, "Zip": p2Zip, "Phone1": p2PhoneNumber}
                df = df.append(new_row2, ignore_index=True)
    
    df.drop_duplicates(subset='Business Name', keep='first', inplace=True)
    display(df)
    df.to_csv('newClients.csv', index=False)
    
else:
    
    df.drop_duplicates(subset='Business Name', keep='first', inplace=True)
    display(df)
    df.to_csv('newClients.csv', index=False)
    
