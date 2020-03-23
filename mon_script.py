##### mon script : csv To json 
import csv , json   

fichierCSV_chemin = "liste-coordonnees-gps-des-monuments.csv"
fichierJSON_chemin = "file.json"
arr = []


with open (fichierCSV_chemin,encoding = "ISO-8859-1") as csvFile:
    csvReader = csv.DictReader(csvFile)
    print(csvReader)
    for csvRow in csvReader:
        arr.append(csvRow)

print()

with open(fichierJSON_chemin, "w") as jsonFile:
    jsonFile.write(json.dumps(arr, indent = 4))
# file.json
