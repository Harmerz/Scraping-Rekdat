from flask import Flask
from datetime import datetime, timedelta
import pandas as pd
from ota.agoda import search_agoda
from ota.booking import search_booking

 
app = Flask(__name__)

@app.route("/agoda")
def FindHotelAgoda():
  today = datetime.now().strftime("%Y-%m-%d")
  list = []

  file_path = 'agoda_id.csv'
  df = pd.read_csv(file_path)
  hotels = []
  for idHotel in df['ObjectId']:
    nameHotel = ""
    for i in range(14):
      original_date = datetime.strptime(f"{today}T17:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")
      new_date = original_date + timedelta(days=i)
      start_date = new_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
      new_end_date = original_date + timedelta(days=i+1)
      end_date = new_end_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
      res = search_agoda(idHotel, start_date, end_date)["data"]["citySearch"]["properties"]
      theHotel = [hotel for hotel in res if hotel["propertyId"] == idHotel]
      if(len(theHotel) > 0):
          nameHotel = theHotel[0]["content"]["informationSummary"]["displayName"]
          price = None
          if(len(theHotel[0]["pricing"]["offers"]) > 0):
            price = theHotel[0].get("pricing", {}).get("offers", [])[0].get("roomOffers", [])[0].get("room", {}).get("mseRoomSummaries", [])[0].get("pricingSummaries", [])[0].get("price", {}).get("perRoomPerNight",{}).get("exclusive",{}).get("display",{})
          list.append({
              "date": start_date,
              "price": price,
          })
    hotels.append({
      'name': nameHotel,
      "id": idHotel,
      "results": list
    })

  dataSet = {
    'ota': "Agoda",
    "hotels": hotels
  }
  
  return dataSet

@app.route('/booking')
def FindHotelBooking():
  today = datetime.now().strftime("%Y-%m-%d")

  nameHotel = "Hotel New Saphir Yogyakarta"
  original_date = datetime.strptime(f"{today}T17:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")
  new_date = original_date + timedelta(days=0)
  start_date = new_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
  new_end_date = original_date + timedelta(days=1)
  end_date = new_end_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")

  res = search_booking(nameHotel, start_date, end_date)
  hotelFind = [hotel for hotel in res if hotel["displayName"]["text"] == nameHotel]
  amount = hotelFind[0]["blocks"][0]["finalPrice"]
  print(amount)
  return amount
