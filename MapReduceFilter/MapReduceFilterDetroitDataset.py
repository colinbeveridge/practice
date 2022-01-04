# program that takes the detroit 911 calls dataset and reads it into several python dictionaries
import csv
import functools as FT
import time
import json
filename = '911_Calls_for_Service_(Last_30_Days).csv'
def make_dictionaries_from_csv(csvfile):
    with open(csvfile,'r',encoding='utf-8-sig') as inp:
        reader = csv.DictReader(inp)
        readerlist = list(reader)
        dictlist = []
        # now we have a list object to be converted to dictionaries
        for row in readerlist:
            # finaldict is one dictionary from one row of readerlist
            finaldict = dict(row)
            dictlist.append(dict(row))
    return dictlist

dictlist = make_dictionaries_from_csv(filename)
# filter out all null values in neighborhood and all averages we are trying to calculate. filter all zeros for zip_code
filtered_dict_list = list(filter(lambda x: x['zip_code'] != '0' and x['neighborhood'] != '',dictlist))

# filter for total response time
# first filter out null values
trt_dict_list = list(filter(lambda x: x['totalresponsetime'] != '',filtered_dict_list))
# put all values into floats and then into trt_values list
trt_values = [float(x['totalresponsetime']) for x in trt_dict_list]
trt_total = FT.reduce(lambda time1,time2: time1+time2,trt_values)
trt_avg_outer = trt_total/len(trt_values)

# filter for dispatch time
# first filter out null values
dt_dict_list = list(filter(lambda x: x['dispatchtime'] != '',filtered_dict_list))
# put all values into floats and then into trt_values list
dt_values = [float(x['dispatchtime']) for x in dt_dict_list]
dt_total = FT.reduce(lambda time1,time2: time1+time2,dt_values)
dt_avg_outer = dt_total/len(dt_values)


# filter for total time
# first filter out null values
tt_dict_list = list(filter(lambda x: x['totaltime'] != '',filtered_dict_list))
# put all values into floats and then into trt_values list
tt_values = [float(x['totaltime']) for x in tt_dict_list]
tt_total = FT.reduce(lambda time1,time2: time1+time2,tt_values)
tt_avg_outer = tt_total/len(tt_values)

# assign all unique neighborhood names to list variable
neighborhoodnames = [dictionary['neighborhood'] for dictionary in filtered_dict_list]
neighborhoodnames = list(set(neighborhoodnames))

# define a function to get the average of an entry in a dictionary
def get_avg(dictionarylist,neighborhoodname,timefieldname):
    # function only works when timefieldname is one of the time fields in original dictionary
    # eliminate blanks from that time field
    neighborhoodvals = list(filter(lambda x: x['neighborhood'] == neighborhoodname,dictionarylist))

    # using list comprehension, get values from the timefield we want
    vals = list(map(lambda x: float(x[timefieldname]),neighborhoodvals))

    # now use reduce to sum vals
    total = FT.reduce(lambda time1,time2: time1+time2,vals)

    # calc avg of time field for a given neighborhood
    avg = total/len(vals)
    return avg

    


neighborhooddicts = []
tic = time.time()
print(len(neighborhoodnames))
for name in neighborhoodnames:
    trt_avg = get_avg(trt_dict_list,name,'totalresponsetime')
    dt_avg = get_avg(dt_dict_list,name,'dispatchtime')
    tt_avg = get_avg(tt_dict_list,name,'totaltime')
    
    # now put calculated averages into a new dictionary
    singledict = {'neighborhood': name, 'avg_total_response_time': trt_avg, 'avg_dispatch_time': dt_avg, 'avg_total_time': tt_avg}
    neighborhooddicts.append(singledict)
toc = time.time()
print(f'Time: {toc-tic}')


if __name__ == '__main__':
    with open('neighborhood_avgtimedata','w') as fout:
        json.dump(neighborhooddicts,fout)
    
