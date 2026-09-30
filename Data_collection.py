#obtaining data
import requests
import json
import csv
from datetime import datetime, timedelta
import numpy
API_KEY="##Your API Key##"

start_date = datetime(YYYY, MM, DD)
end_date = datetime(YYYY, MM, DD)
year=YYYY

Train_data={"Train_no1":{"City1":"hour","City2":"hour"},
"Train_no2":{"City1":"hour","City2":"hour"}}

for Train_no in Train_data:
	city=Train_data[Train_no]
	rows = []
	for i in range((end_date - start_date).days + 1):
		try:
			for ci in city.keys():
				current_date=start_date+timedelta(days=i)
				date=current_date.strftime("%Y-%m-%d")
				found=False
				url="<<Weather API URL>>"
				response=requests.get(url,params={"key":API_KEY,"q":ci,"date":date,"tp":1,"format":"json"},timeout=10)
				response.raise_for_status()
				data = response.json()
				for day in data["data"]["weather"]:
					for hour in day["hourly"]:
						if hour["time"] == city[ci]:								
							rows.append({"Location": ci,"Date": date,"Time": hour["time"],"Temperature": hour["tempC"],"Feels like": hour["FeelsLikeC"],"Humidity": hour["humidity"],"Wind": hour["windspeedKmph"],"Rain": hour["precipMM"],"Condition": hour["weatherDesc"][0]["value"]})
							found = True
				if not found:
					print("No weather record found for that time.")
		except requests.exceptions.Timeout:
			print(f"Timeout error on {current_date.date()}")
			continue
		except requests.exceptions.RequestException as e:
			print(f"API error on {current_date.date()}: {e}")
			continue
	print(rows)

#storing data
new_data=rows
new_fieldnames = [
            "Location",
            "Time",
            "Temperature",
            "Feels like",
            "Humidity",
            "Wind",
            "Rain",
                ]
try:
        with open(f"weather_dataset_city_aggr.csv","a",newline="",encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=new_fieldnames)
                writer.writeheader()
                writer.writerows(new_data)

        print("Saved:", len(new_data), "stations")
except Exception as e:
        print(f"API error on {current_date.date()}: {e}")
