import csv
data = csv.reader(open('testcsv.csv', 'r'))

for user in data:
    print(user)
    print(user[1])