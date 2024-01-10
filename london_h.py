import csv
import math
def london_h(id):
    with open('london_stations.csv') as csv_file:
        hDict = {}
        reader = csv.reader(csv_file, delimiter=',')
        first_row = next(reader, None)
        data = list(reader)
        for row in data:
            if row[0] == str(id):
                targetLat = float(row[1])
                targetLong = float(row[2])
                p = (targetLat, targetLong)
                print(p)
        count = 0
        for row in data:
            count += 1
            lat = float(row[1])
            long = float(row[2])
            q = (lat, long)
            hDict[int(row[0])] = math.dist(p,q)
        print(count)
        return hDict

print(london_h(1))
