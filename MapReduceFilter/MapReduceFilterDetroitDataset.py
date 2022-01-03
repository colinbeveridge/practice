# program that takes the detroit 911 calls dataset and reads it into several python dictionaries
import csv

filename = '911_Calls_for_Service_(Last_30_Days).csv'
mydict = {}

with open(filename,'r') as inp:
    reader = csv.DictReader(inp)
    print(len(list(reader)))
    print(list(reader)[0])
    



if __name__ == '__main__':
    a = 3
    
