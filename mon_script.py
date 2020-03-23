##### mon script : csv To json 
#!/usr/bin/python
import csv , json   

csvFilePath = "liste-coordonnees-gps-des-monuments.csv"
jsonFilePath = "file.json"
arr = []
#read the csv and add the arr to a arrayn

with open (csvFilePath,encoding = "ISO-8859-1") as csvFile:
    csvReader = csv.DictReader(csvFile)
    print(csvReader)
    for csvRow in csvReader:
        arr.append(csvRow)

print()

# write the data to a json file
with open(jsonFilePath, "w") as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 4))
# file.json
