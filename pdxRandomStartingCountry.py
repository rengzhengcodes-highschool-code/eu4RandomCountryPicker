import csv
import random


acceptable_countries = []
bad_tags = ['Special game tag', 'Releasable', 'Formable']
with open('eu41.28Countries.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if not row['Notes'] in bad_tags:
            acceptable_countries.append(row['Country'])
acceptable_countries.sort()
print(acceptable_countries[random.randint(0,len(acceptable_countries) - 1)])
input('Press ENTER to exit')
