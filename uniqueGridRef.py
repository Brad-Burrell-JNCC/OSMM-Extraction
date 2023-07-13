# Name: uniqueGridRef.py
# Author: Stuart Wallace - 17 Dec 2018
# Description: make a list file of unique values got from a shapefile field

import arcpy, os, types, time, csv, sys, re

#print ' '

# check for at least one argument. Folder name is required.
if len(sys.argv) < 2:
	#sys.argv[1:] = ["-h"]
	print ' '
	print 'need shapefile path, ie > uniqueGridRef.py .shp'
	sys.exit(0)

datetime = time.asctime( time.localtime(time.time()) )
dts = datetime.split(" ")
#print dts[4]

# Use the first argument from the command line as the working folder
shp = sys.argv[1]
outputF = "J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Data\Output"

# write to text file into which the unique grid refs will be added
filename = "unique_gridref.txt"
fw = open(outputF + os.sep + filename, "a")

my_list = []
countR = 0

cursor = arcpy.da.SearchCursor(shp, ['gridref'])
for val in cursor:
    #print(val)
	my_list.append(val[0])
	countR += 1

my_list = list(set(my_list))

print countR
print len(my_list)

for param in my_list:
	fw.write(str(param) + "\n")

fw.close()


