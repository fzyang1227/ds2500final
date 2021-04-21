"""
Visualization: Outcomes Based On Goals
    
Create a line graph that compares successful / failed projects to project goals


"""

# import all required modules
from os import listdir
from os.path import isfile, join
import csv

mypath = "clean_data/" # path doesn't need to be changed if downloaded from GitHub file 

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# create dictionaries for 12 goal ranges (from less than $1000 to greater than $50,000)

d_1={"failed":0,"successful":0,"canceled":0,"total":0}
d_2={"failed":0,"successful":0,"canceled":0,"total":0}
d_3={"failed":0,"successful":0,"canceled":0,"total":0}
d_4={"failed":0,"successful":0,"canceled":0,"total":0}
d_5={"failed":0,"successful":0,"canceled":0,"total":0}
d_6={"failed":0,"successful":0,"canceled":0,"total":0}
d_7={"failed":0,"successful":0,"canceled":0,"total":0}
d_8={"failed":0,"successful":0,"canceled":0,"total":0}
d_9={"failed":0,"successful":0,"canceled":0,"total":0}
d_10={"failed":0,"successful":0,"canceled":0,"total":0}
d_11={"failed":0,"successful":0,"canceled":0,"total":0}
d_12={"failed":0,"successful":0,"canceled":0,"total":0}
for i in onlyfiles:
    with open('clean_data/'+i) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            # add values based on each row looped through: add count based on state of project
            else:
                if (float(row[5])<=1000):
                    succ=d_1["successful"]
                    fail=d_1["failed"]
                    canc=d_1["canceled"]
                    total=d_1["total"]
                    if(row[12]=="successful"):
                        succ=succ+1
                        d_1["successful"]=succ
                    elif(row[12]=="failed"):
                        fail=fail+1
                        d_1["failed"]=fail
                    else:
                        canc=canc+1
                        d_1["canceled"]=canc
                    total=total+1
                    d_1["total"]=total	
                    
                elif (float(row[5])>1000 and float(row[5])<=4999):
                    succ=d_2["successful"]
                    fail=d_2["failed"]
                    canc=d_2["canceled"]
                    total=d_2["total"]
                    if(row[12]=="successful"):
                        succ=succ+1
                        d_2["successful"]=succ
                    elif(row[12]=="failed"):
                        fail=fail+1
                        d_2["failed"]=fail
                    else:
                        canc=canc+1
                        d_2["canceled"]=canc
                    total=total+1
                    d_2["total"]=total

                elif (float(row[5])>4999 and float(row[5])<=9999):
                    succ=d_3["successful"]
                    fail=d_3["failed"]
                    canc=d_3["canceled"]
                    total=d_3["total"]
                    if(row[12]=="successful"):
                        succ=succ+1
                        d_3["successful"]=succ
                    elif(row[12]=="failed"):
                        fail=fail+1
                        d_3["failed"]=fail
                    else:
                        canc=canc+1
                        d_3["canceled"]=canc
                    total=total+1
                    d_3["total"]=total

                elif (float(row[5])>9999 and float(row[5])<=14999):
                    succ=d_4["successful"]
                    fail=d_4["failed"]
                    canc=d_4["canceled"]
                    total=d_4["total"]
                    if(row[12]=="successful"):
                        succ=succ+1
                        d_4["successful"]=succ
                    elif(row[12]=="failed"):
                        fail=fail+1
                        d_4["failed"]=fail
                    else:
                        canc=canc+1
                        d_4["canceled"]=canc
                    total=total+1
                    d_4["total"]=total

                elif (float(row[5])>14999 and float(row[5])<=19999):
                    succ=d_5["successful"]
                    fail=d_5["failed"]
                    canc=d_5["canceled"]
                    total=d_5["total"]
                    if(row[12]=="successful"):
                        succ=succ+1
                        d_5["successful"]=succ
                    elif(row[12]=="failed"):
                        fail=fail+1
                        d_5["failed"]=fail
                    else:
                        canc=canc+1
                        d_5["canceled"]=canc
                    total=total+1
                    d_5["total"]=total

                elif (float(row[5])>19999 and float(row[5])<=24999):
                    succ=d_6["successful"]
                    fail=d_6["failed"]
                    canc=d_6["canceled"]
                    total=d_6["total"]
                    if(row[12]=="successful"):
                        succ=succ+1
                        d_6["successful"]=succ
                    elif(row[12]=="failed"):
                        fail=fail+1
                        d_6["failed"]=fail
                    else:
                        canc=canc+1
                        d_6["canceled"]=canc
                    total=total+1
                    d_6["total"]=total

                elif (float(row[5])>24999 and float(row[5])<=29999):
                    succ=d_7["successful"]
                    fail=d_7["failed"]
                    canc=d_7["canceled"]
                    total=d_7["total"]
                    if(row[12]=="successful"):
                        succ=succ+1
                        d_7["successful"]=succ
                    elif(row[12]=="failed"):
                        fail=fail+1
                        d_7["failed"]=fail
                    else:
                        canc=canc+1
                        d_7["canceled"]=canc
                    total=total+1
                    d_7["total"]=total

                elif (float(row[5])>29999 and float(row[5])<=34999):
                    succ=d_8["successful"]
                    fail=d_8["failed"]
                    canc=d_8["canceled"]
                    total=d_8["total"]
                    if(row[12]=="successful"):
                        succ=succ+1
                        d_8["successful"]=succ
                    elif(row[12]=="failed"):
                        fail=fail+1
                        d_8["failed"]=fail
                    else:
                        canc=canc+1
                        d_8["canceled"]=canc
                    total=total+1
                    d_8["total"]=total

                elif (float(row[5])>34999 and float(row[5])<=39999):
                    succ=d_9["successful"]
                    fail=d_9["failed"]
                    canc=d_9["canceled"]
                    total=d_9["total"]
                    if(row[12]=="successful"):
                        succ=succ+1
                        d_9["successful"]=succ
                    elif(row[12]=="failed"):
                        fail=fail+1
                        d_9["failed"]=fail
                    else:
                        canc=canc+1
                        d_9["canceled"]=canc
                    total=total+1
                    d_9["total"]=total

                elif (float(row[5])>39999 and float(row[5])<=44999):
                    succ=d_10["successful"]
                    fail=d_10["failed"]
                    canc=d_10["canceled"]
                    total=d_10["total"]
                    if(row[12]=="successful"):
                        succ=succ+1
                        d_10["successful"]=succ
                    elif(row[12]=="failed"):
                        fail=fail+1
                        d_10["failed"]=fail
                    else:
                        canc=canc+1
                        d_10["canceled"]=canc
                    total=total+1
                    d_10["total"]=total

                elif (float(row[5])>44999 and float(row[5])<=49999):
                    succ=d_11["successful"]
                    fail=d_11["failed"]
                    canc=d_11["canceled"]
                    total=d_11["total"]
                    if(row[12]=="successful"):
                        succ=succ+1
                        d_11["successful"]=succ
                    elif(row[12]=="failed"):
                        fail=fail+1
                        d_11["failed"]=fail
                    else:
                        canc=canc+1
                        d_11["canceled"]=canc
                    total=total+1
                    d_11["total"]=total

                elif (float(row[5])>49999):
                    succ=d_12["successful"]
                    fail=d_12["failed"]
                    canc=d_12["canceled"]
                    total=d_12["total"]
                    if(row[12]=="successful"):
                        succ=succ+1
                        d_12["successful"]=succ
                    elif(row[12]=="failed"):
                        fail=fail+1
                        d_12["failed"]=fail
                    else:
                        canc=canc+1
                        d_12["canceled"]=canc
                    total=total+1
                    d_12["total"]=total                    
                

                line_count += 1



