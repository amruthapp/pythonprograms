
import csv
with open("song.csv","w",newline='') as file:
 write=csv.writer(file)
 write.writerow(["Sl No","song","singer"])
 write.writerow(["1","Nee mukhilo","Sithara"])
 write.writerow(["2","Perfect","Ed Shareen"])
 write.writerow(["3", "Enna Sona", "Arjith Singh"])
with open("song.csv") as csvfile:
 data=csv.DictReader(csvfile)
 for r in data:
   print(r['Sl No'],r['song'])