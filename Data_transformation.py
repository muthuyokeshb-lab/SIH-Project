#Averaging out data
import csv
import numpy

f1=open("weather_dataset_city_aggr.csv","r")
f2=open("new_weather_data.csv","a")
reader=csv.reader(f1)
store={}
for row in reader:
	if row[0]!="Location":
		if row[0] in store:
			store[row[0]]+=[row]
		else:
			store[row[0]]=[row]
new_store={}
for k in store:
	temp=[store[k][0][0],store[k][0][2]]
	for j in range(3,8):
		temp.append(str(round(numpy.average([float(store[k][p][j]) for p in range(len(store[k]))]),2)))
	new_store[k]=temp
f1.close()
writer=csv.writer(f2)
writer.writerow(["Location","Time","Temperature","Feels like","Humidity","Wind","Rain"])
writer.writerows(list(new_store.values()))
f2.close()
