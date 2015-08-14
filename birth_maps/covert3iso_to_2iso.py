import csv

f1 = open("wikipedia-iso-country-codes.csv", 'rt')
f2 = open("data.csv", 'rU')

mapCode = {}
try:
    reader = csv.reader(f1)
    for row in reader:
        # print row
        mapCode[row[2]]=row[1]
    reader = csv.reader(f2)
    
    output = csv.writer(open('ouput.csv', 'w'))

    for i,row in enumerate(reader):
        if i is 0:      
            output.writerow(row)
            continue
        
        # row = row[0].split(",")

        if not row[0] in mapCode:
            continue
        row[0] = mapCode[row[0]]
        output.writerow(row)
finally:
    f1.close()
    f2.close()

# print mapCode