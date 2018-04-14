import csv

users = []

# # Getting data from csv file
with open('ch1.csv') as csvfile:
        csv = csv.DictReader(csvfile)
        users = list(csv)
        print(users)