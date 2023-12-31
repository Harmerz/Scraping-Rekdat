from flask import Flask
from datetime import datetime, timedelta
import pandas as pd
from ota.agoda import search_agoda
from ota.booking import search_booking
import pytz



app = Flask(__name__)
def find_hotel_by_id(id, data):
    return [hotel["Name"] for hotel in data if hotel["ObjectId"] == id][0]

def find_local_id(name, data):
   return [hotel["id"] for hotel in data if hotel["name"] == name][0]

@app.route("/agoda")
def FindHotelAgoda():
  today = datetime.now().strftime("%Y-%m-%d")
  file_path = 'hotel.csv'
  df = pd.read_csv(file_path)
  hotels = []

  idLocalData = [{"id": i, "name": name} for i, name in enumerate(df['Name'], 1)]

  idAgoda = df.to_dict(orient='records')
  for idHotel in df['ObjectId']:
    list = []
    for i in range(30):
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
          price = None
          if(len(theHotel[0]["pricing"]["offers"]) > 0):
            price = theHotel[0].get("pricing", {}).get("offers", [])[0].get("roomOffers", [])[0].get("room", {}).get("mseRoomSummaries", [])[0].get("pricingSummaries", [])[0].get("price", {}).get("perRoomPerNight",{}).get("exclusive",{}).get("display",{})
          list.append({
              "date": start_date_locale,
              "price": price,
          })
    hotels.append({
      'name': find_hotel_by_id(idHotel, idAgoda),
      "id": idHotel,
      "results": list,
      "local_id": find_local_id(find_hotel_by_id(idHotel, idAgoda), idLocalData)
    })

  dataSet = {
    'ota': "Agoda",
    "hotels": hotels
  }
  
  return dataSet

@app.route('/booking')
def FindHotelBooking():
  today = datetime.now().strftime("%Y-%m-%d")
  file_path = 'hotel.csv'
  df = pd.read_csv(file_path)
  hotels = []
  idLocalData = [{"id": i, "name": name} for i, name in enumerate(df['Name'], 1)]

  for nameHotel in df["Name"]:
    list = []
    for i in range(30):
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
      id = None
      if hotelFind and len(hotelFind) > 0:
        id = hotelFind[0]["basicPropertyData"]["id"]
        if "blocks" in hotelFind[0]:
            blocks = hotelFind[0]["blocks"]
            if blocks and len(blocks) > 0:
                if "finalPrice" in blocks[0]:
                    amount = blocks[0]["finalPrice"]["amount"]
      if(amount == None):
         for _ in range(3):
            res = search_booking(nameHotel, start_date, end_date)
            hotelFind = [hotel for hotel in res if all(word in hotel["displayName"]["text"].lower().split() for word in nameHotel.lower().split())]
            amount = None
            if hotelFind and len(hotelFind) > 0:
              if "blocks" in hotelFind[0]:
                  blocks = hotelFind[0]["blocks"]
                  if blocks and len(blocks) > 0:
                      if "finalPrice" in blocks[0]:
                          amount = blocks[0]["finalPrice"]["amount"]
            if(amount != None):
               break
      list.append({
        "date": start_date_locale,
        "price": amount
      })
    hotels.append({
      'name': nameHotel,
      "results": list,
      "id": id,
      "local_id": find_local_id(nameHotel, idLocalData)
    })

    dataSet = {
    'ota': "Booking.com",
    "hotels": hotels
    }
  return dataSet
