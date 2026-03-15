import csv
try:
    with open('contacts.csv','w') as file:
        #print("customers csv file created")
        writer_obj = csv.writer(file)
        lines = [['name','mobile'],['srinu','9099009093'],['babu','90940004']]
        writer_obj.writerows(lines)
except Exception as e:
    print("Error: ",e) 