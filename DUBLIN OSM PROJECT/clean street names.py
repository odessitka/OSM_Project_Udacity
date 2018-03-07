import csv
import re


mapping = {'Ave': 'Avenue',
           'St.': 'Street',
           'Rd.': 'Road',
           'Roafd': 'Road',
           'St': 'Street',
           'Rd': 'Road',
           'Avevnue': 'Avenue',
           'Nouth': 'North'}

street_type_re = re.compile(r'\b\S+\.?$')

# cleaning the csv files which include street names (these are _tag.csv with 'key' = 'street' and 'value' = street name
def cleaning(csv_file):
   # reading the csv file
   file1 = open(csv_file, 'rb')
   reader = csv.reader(file1)
   new_rows_list = [] # rows for writing into the file
   for row in reader:
      new_value = row[2] # the street name for audit and correction
      if row[1] == 'street':
         m = street_type_re.search(row[2])
         if m:
            street_type = m.group()
            if street_type in mapping.keys():
               better_street_type = mapping[m.group()]
               new_value = street_type_re.sub(better_street_type, row[2])
      new_row = [row[0], row[1], new_value, row[3]]
      new_rows_list.append(new_row)
   file1.close()

   #writing the csv file
   file2 = open(csv_file, 'wb')
   writer = csv.writer(file2)
   writer.writerows(new_rows_list)
   file2.close()


cleaning('nodes_tags.csv')
cleaning('ways_tags.csv')
