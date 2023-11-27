from flask import Flask
from datetime import datetime, timedelta
import pandas as pd
from ota.agoda import search_agoda
from ota.booking import search_booking
import pytz

 
app = Flask(__name__)

@app.route("/agoda")
def FindHotelAgoda():
  today = datetime.now().strftime("%Y-%m-%d")
  file_path = 'agoda_id.csv'
  df = pd.read_csv(file_path)
  hotels = []
  for idHotel in df['ObjectId']:
    list = []
    nameHotel = ""
    for i in range(3):
      original_date = datetime.strptime(f"{today}T17:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")
      new_date = original_date + timedelta(days=i)
      start_date = new_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
      new_end_date = original_date + timedelta(days=i+1)
      end_date = new_end_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
      res = search_agoda(idHotel, start_date, end_date)["data"]["citySearch"]["properties"]
      theHotel = [hotel for hotel in res if hotel["propertyId"] == idHotel]
      start_date_local = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.UTC)
      jakarta_timezone = pytz.timezone('Asia/Jakarta')
      start_date_jakarta = start_date_local.astimezone(jakarta_timezone)
      start_date_locale = start_date_jakarta.strftime("%Y-%m-%d")
      if(len(theHotel) > 0):
          nameHotel = theHotel[0]["content"]["informationSummary"]["displayName"]
          price = None
          if(len(theHotel[0]["pricing"]["offers"]) > 0):
            price = theHotel[0].get("pricing", {}).get("offers", [])[0].get("roomOffers", [])[0].get("room", {}).get("mseRoomSummaries", [])[0].get("pricingSummaries", [])[0].get("price", {}).get("perRoomPerNight",{}).get("exclusive",{}).get("display",{})
          list.append({
              "date": start_date_locale,
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
  file_path = 'agoda_id.csv'
  df = pd.read_csv(file_path)
  hotels = []
  for nameHotel in df['Name']:
    list = []
    for i in range(3):
      original_date = datetime.strptime(f"{today}T17:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")
      new_date = original_date + timedelta(days=i)
      start_date = new_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
      new_end_date = original_date + timedelta(days=i+1)
      end_date = new_end_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")

      start_date_local = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.UTC)
      jakarta_timezone = pytz.timezone('Asia/Jakarta')
      start_date_jakarta = start_date_local.astimezone(jakarta_timezone)
      start_date_locale = start_date_jakarta.strftime("%Y-%m-%d")
      res = search_booking(nameHotel, start_date, end_date)
      hotelFind = [hotel for hotel in res if all(word in hotel["displayName"]["text"].lower().split() for word in nameHotel.lower().split())]
      amount = None
      if hotelFind and len(hotelFind) > 0:
        if "blocks" in hotelFind[0]:
            blocks = hotelFind[0]["blocks"]
            if blocks and len(blocks) > 0:
                if "finalPrice" in blocks[0]:
                    amount = blocks[0]["finalPrice"]["amount"]
      list.append({
        "date": start_date_locale,
        "price": amount
      })
    hotels.append({
      'name': nameHotel,
      "results": list
    })

    dataSet = {
    'ota': "Booking.com",
    "hotels": hotels
    }
  return dataSet
