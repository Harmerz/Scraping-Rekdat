from datetime import datetime
import pytz
from .request_data import send_request
from bs4 import BeautifulSoup
import json

idAgoda = [
    {
        "id": 1678127,
        "name": "Satoria Hotel Yogyakarta - CHSE Certified"
    },
    {
        "id": 9158876,
        "name": "Malyabhara Hotel"
    },
    {
        "id": 891281,
        "name": "Gallery Prawirotaman Hotel"
    },
    {
        "id": 1550653,
        "name": "Allstay Ecotel Yogyakarta"
    },
    {
        "id": 4308974,
        "name": "Aveta Hotel Malioboro - CHSE Certified"
    },
    {
        "id": 1439830,
        "name": "Tjokro Style Yogyakarta"
    },
    {
        "id": 1618997,
        "name": "Grand Kangen Hotel Urip Sumoharjo"
    },
    {
        "id": 1388440,
        "name": "Hotel Neo Malioboro by ASTON"
    },
    {
        "id": 4826351,
        "name": "RedDoorz near Malioboro Mall 2"
    },
    {
        "id": 8894935,
        "name": "House Of Cokro near Malioboro Area RedPartner"
    },
    {
        "id": 5989457,
        "name": "PORTA by Ambarrukmo"
    },
    {
        "id": 2242692,
        "name": "YATS Colony"
    },
    {
        "id": 2869066,
        "name": "ARTOTEL Yogyakarta"
    },
    {
        "id": 337055,
        "name": "ARTOTEL Suites Bianti Yogyakarta, CHSE Certified"
    },
    {
        "id": 4353040,
        "name": "Arte Hotel Yogyakarta"
    },
    {
        "id": 2433734,
        "name": "GRAMM HOTEL by Ambarrukmo - Formerly Grand Ambarrukmo Yogyakarta"
    },
    {
        "id": 6771182,
        "name": "The Manohara Hotel Yogyakarta"
    },
    {
        "id": 402860,
        "name": "The Rich Jogja Hotel"
    },
    {
        "id": 8510982,
        "name": "Grand Dafam Signature International Airport Yogyakarta"
    },
    {
        "id": 576313,
        "name": "Grand Zuri Malioboro"
    },
    {
        "id": 2761236,
        "name": "Grand Rohan Jogja"
    },
    {
        "id": 2278674,
        "name": "Grand Keisha Yogyakarta"
    },
    {
        "id": 1830077,
        "name": "GAIA Cosmo Hotel"
    },
    {
        "id": 1863174,
        "name": "Swiss-Belboutique Yogyakarta"
    },
    {
        "id": 267339,
        "name": "Sahid Raya Hotel & Convention Yogyakarta"
    },
    {
        "id": 335157,
        "name": "Kimaya Sudirman Yogyakarta by Harris"
    },
    {
        "id": 1957322,
        "name": "Platinum Adisucipto Hotel & Conference Center"
    },
    {
        "id": 238289,
        "name": "Hotel Santika Premiere Jogja"
    },
    {
        "id": 1314871,
        "name": "The Alana Yogyakarta Hotel and Convention Center"
    },
    {
        "id": 1322941,
        "name": "The Alana Hotel & Conference Center Malioboro Yogyakarta by ASTON"
    },
    {
        "id": 5230327,
        "name": "Novotel Suites Yogyakarta Malioboro"
    },
    {
        "id": 1623833,
        "name": "The Atrium Hotel & Resort Yogyakarta"
    },
    {
        "id": 1037300,
        "name": "Crystal Lotus Hotel Yogyakarta"
    },
    {
        "id": 245703,
        "name": "Hotel New Saphir Yogyakarta"
    },
    {
        "id": 2303435,
        "name": "INNSiDE by Meliá Yogyakarta"
    },
    {
        "id": 3539462,
        "name": "Sofia Boutique Residence"
    },
    {
        "id": 740643,
        "name": "Eastparc Hotel Yogyakarta"
    },
    {
        "id": 2761737,
        "name": "Yogyakarta Marriott Hotel"
    },
    {
        "id": 239849,
        "name": "The Phoenix Hotel Yogyakarta - MGallery Collection"
    },
    {
        "id": 259081,
        "name": "Hyatt Regency Yogyakarta"
    },
    {
        "id": 176870,
        "name": "Melia Purosani Yogyakarta"
    },
    {
        "id": 353499,
        "name": "Jambuluwuk Malioboro Hotel Yogyakarta"
    },
    {
        "id": 1850023,
        "name": "Grand Mercure Yogyakarta Adi Sucipto"
    },
    {
        "id": 383557,
        "name": "Sheraton Mustika Yogyakarta Resort and Spa"
    }
]

def find_hotel_by_name(name):
    return next((hotel for hotel in idAgoda if hotel["name"] == name), None)

def search_booking(nameHotel, start_date, end_date):
  # Parse the input string as UTC time
  start_date_local = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.UTC)
  end_date_local = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.UTC)


  # Convert UTC time to Jakarta time
  jakarta_timezone = pytz.timezone('Asia/Jakarta')
  start_date_jakarta = start_date_local.astimezone(jakarta_timezone)
  end_date_jakarta = end_date_local.astimezone(jakarta_timezone)


  # Extract the date part and format as a new string
  start_date_locale = start_date_jakarta.strftime("%Y-%m-%d")
  end_date_locale = end_date_jakarta.strftime("%Y-%m-%d")

  url = "https://www.booking.com/searchresults.id.html"

  headers = {
    "authority":"www.booking.com",
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"accept-language":"en-US,en;q=0.9",
"cache-control":"no-cache",
"cookie":'_ga=GA1.1.623670587.1699415621; _ga_G0GLDX0JXR=GS1.1.1699418177.2.1.1699418576.0.0.0; xp=02UmFuZG9tSVYkc2RlIyh9YbxZGyl9Y5%2BP9yO5wNjICwLLnoExTB7%2Bpt82ioMFaZfXH2j8Ad8ZFKM%3D; px_init=0; cors_js=1; bkng_sso_ses=e30; bkng_sso_session=e30; OptanonConsent=implicitConsentCountry=nonGDPR&implicitConsentDate=1699434302995; _pxvid=f2ac3850-7e15-11ee-b761-0ab65491e29c; _gcl_au=1.1.1542706869.1699434304; _gcl_aw=GCL.1699434304.Cj0KCQiAgK2qBhCHARIsAGACuzlfrsOHc-1jvmNrYFUfH3ab2EoUhEt5Bk7wkNlpE_bCUtfwH9re6IUaAnU2EALw_wcB; _scid=22a1bcc2-560d-4237-8f6c-67559162354f; FPID=FPID2.2.J7ELmj1a0fGrm9oPdJMaaOb2ghy4YY%2B2d6YP7p3Zq08%3D.1699415621; _pin_unauth=dWlkPU5HUTNObVF6WXpNdFlUZzFZeTAwTXpFMExUZzRPVGN0TldVME9XRXdZVFZrTVdRNA; pcm_consent=consentedAt%3D2023-11-21T02%3A31%3A04.550Z%26countryCode%3DID%26expiresAt%3D2024-05-19T02%3A31%3A04.550Z%26implicit%3Dfalse%26regionCode%3DYO%26regulation%3Dnone%26legacyRegulation%3Dnone%26consentId%3D963d1c02-a326-4f10-b4fe-ea3d9cf82668%26analytical%3Dtrue%26marketing%3Dtrue; bkng_sso_auth=CAIQsOnuTRpyrxSW/D/D3VcyUiz9dz2GVonaSZ+cltiV20JD2e/4Qr2kHHkU/sFNJh33FvyJ5S9WvqmUJ74/vLzSVVrB4sGCyLSaLebHAMwaUzKoJxyWJBLGrDVYs3oFaUlVSy3/wD4roymr/k1kjOBOJxnh1igajU3Y; bkng_sso_auth_1700533864=CAIQsOnuTRpyrxSW/D/D3VcyUiz9dz2GVonaSZ+cltiV20JD2e/4Qr2kHHkU/sFNJh33FvyJ5S9WvqmUJ74/vLzSVVrB4sGCyLSaLebHAMwaUzKoJxyWJBLGrDVYs3oFaUlVSy3/wD4roymr/k1kjOBOJxnh1igajU3Y; BJS=-; b=%7B%22countLang%22%3A4%7D; _pxhd=UToUmQiGiByipJb-NbWM2AN-4L2m1%2FfXKEuOfDeOf-PvpNZzb256CsEvtzwRZYR88c6oJtfUZlssTHmQ%2FvJj1Q%3D%3D%3A02o-w-KCeQ12LuxGyNvUeoYFSu9ng332pHYigCSYPh-rJNdukLPMRm%2Fvbm4hZGPFOs%2FwMTwrg9OYkwumYbqk5qfmJMI1XHO2xfYbIuES6X0%3D; pxcts=07ab9240-8816-11ee-95ae-e2204db813a1; _pxff_cfp=1; _pxff_ddtc=1; bkng_prue=1; _ga_A12345=GS1.1.1700533849.3.0.1700533849.0.0.0; _px3=587e46110b9e8a83318251fb078f5990c96b83e781a503a44da2d5e3bbbdfadd:RPiIQTnx9hiyIpvzM8Ip3uxsD16w9gEQ51iXBYNK1mK/9EBacrI0NAfGuGYT7xej0sXqABbZXOcslf8e1iM+Vg==:1000:Yjo7TCjZUuQkL8vvhx4CLO0BHl4FNxKMSjRVheXvrqCCAceae0moOp/THpsRvfeNTu2tpo33AwkLNaqVs3YIZG+n6LaEsnAS2ru2rpLUu8/mZZidprB56RMejSAnMZ56FvglQ3vG5/5c/ek5r/RwiGwuC6kSPP3EOg3nf9ATAKxxitmPy/iv2Go5K6sCOmBVQR7aaNzKWwGFKQd6iI4wRz6N2eP8/GC4gFkhwLwat2c=; _pxde=01e143d6666c0f2a586fe506a4f58957bb4d3ad617cd7d45212d6bce4cf65aaa:eyJ0aW1lc3RhbXAiOjE3MDA1MzM4NzIzMDUsImZfa2IiOjAsImlwY19pZCI6W119; _uetsid=fbd97b50881511eea10f4d2b46dc5cad; _uetvid=e7b95ef07e1511eea758f3755b36d2a6; _scid_r=22a1bcc2-560d-4237-8f6c-67559162354f; FPLC=JDQqmuWmV53hdQzJWdlbaTA7FkKr3%2B9iNP5EyEze0BrNTRKESvHmLRlEFDZve%2Fl5vGGOwtlfw9hiMlirjGqyw2hZhHSDGfWxUxEhUaW5p5M2o4wexlSz5iHhP573sA%3D%3D; _sctr=1%7C1700499600000; g_state={"i_p":1700541051980,"i_l":1}; lastSeen=0; bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbiKbS0JOgDBKtCN8f0CTZfZWIlQrjUlVoRUbEVbC0oVPNbGL5sFBeX9A4VQBOKBM6FqgBkqkbkuwQTxJkj6Je1DZU0EFrg5TahDIUozfetQxcSy7ETFKQw2ZrohehOFIKvx%2FD3q6bYoF0KCYGzYrrywyr%2FKBsgHQ7xRUqmLjC3rw%3D; _ga_FPD6YLJCJ7=GS1.1.1700533849.3.1.1700533865.44.0.0',
"dnt":"1",
"pragma":"no-cache",
"referer":"https://www.booking.com/index.id.html?aid=397594&label=gog235jc-1DCAEoggI46AdIM1gDaGiIAQGYARK4ARfIAQzYAQPoAQGIAgGoAgO4Auis8KoGwAIB0gIkYmM1ODNiNDctOWY4Ny00YzgyLThiZTUtYTQyOGE2NzRlZGNj2AIE4AIB&sid=73355aaac8b9c7490a20182d5cf8fb72&keep_landing=1&sb_price_type=total&",
"sec-ch-ua":'"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
"sec-ch-ua-mobile":"?0",
"sec-ch-ua-platform":"Windows",
"sec-fetch-dest":"document",
"sec-fetch-mode":"navigate",
"sec-fetch-site":"same-origin",
"sec-fetch-user":"?1",
"upgrade-insecure-requests":"1",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
  
  params = {
    "ss": nameHotel,
    "ssne": "Yogyakarta",
    "ssne_untouched": "Yogyakarta",
    "label": "gog235jc-1DCAEoggI46AdIM1gDaGiIAQGYARK4ARfIAQzYAQPoAQGIAgGoAgO4Auis8KoGwAIB0gIkYmM1ODNiNDctOWY4Ny00YzgyLThiZTUtYTQyOGE2NzRlZGNj2AIE4AIB",
    "sid": "6afbac45bd42a09d7b5f6c4214a06335",
    "aid": "397594",
    "lang": "id",
    "sb": "1",
    "src_elem": "sb",
    "src": "index",
    "search_selected": True,
    "search_pageview_id": "cd7f11b4a2650078",
    "dest_id": find_hotel_by_name(nameHotel),
    "dest_type": "hotel",
    "checkin": start_date_locale,
    "checkout": end_date_locale,
    "group_adults": "2",
    "no_rooms": "1",
    "group_children": "0",
    "sb_travel_purpose": "leisure",
  }
  print(start_date_locale)
  print(end_date_locale)
  print(nameHotel)
  result = send_request(url, headers, "GET", params=params)
  # Parse the HTML using BeautifulSoup
  soup = BeautifulSoup(result, 'html.parser')

  
  # Find all script tags
  script_tags = soup.find_all('script', {'type': 'application/json'})

  # Iterate over script tags
  for script_tag in script_tags:
      # Extract the content of the script tag
      script_content = script_tag.string

      if script_content:
          # Parse the script content as JSON
          try:
              json_data = json.loads(script_content)
          except json.JSONDecodeError:
              continue  # Skip to the next script tag if not valid JSON
          # Check if the "__typename" is "Query"
          if json_data.get('ROOT_QUERY', {}).get('__typename') == 'Query':
              data = json_data["ROOT_QUERY"]["searchQueries"]
              if data and isinstance(data, dict):
                  results_value = None
                  for key, value in data.items():
                      if isinstance(value, dict) and "results" in value:
                          results_value = value["results"]
                          break

                  if results_value:
                      return results_value
                  else:
                      return data
              else:
                  return None



  print("No JSON data with '__typename' as 'Query' found.")

  return result