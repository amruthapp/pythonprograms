
import csv
with open("amrutha.csv","w",newline='') as file:
 write=csv.writer(file)
 write.writerow(["sl no","song","singer"])
 write.writerow(["1","Chayapettu","Sithara"])
 write.writerow(["2","Perfect","Ed Shareen"])
 write.writerow(["3", "Enna Sona", "Arjith Singh"])
with open("amrutha.csv") as csvfile:
 data=csv.reader(csvfile)
 for r in data:
  print(r)