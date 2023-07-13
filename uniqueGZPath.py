# Name: uniqueGZPath.py
#       J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Python\uniqueGZPath.py
# Author: Stuart Wallace - 08 Mar 2019
# Description: make a list of .gz file path names based on the values in the fullPath field in feature layer
#              J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Data\GDB\OSMM_Derived.gdb\polygonGZ_MHW

import arcpy, os, types, time, csv, sys, re

print ' '

# check for at least one argument. Feature name is required.
if len(sys.argv) < 2:
	#sys.argv[1:] = ["-h"]
	print ' '
	print 'need feature name, ie > uniqueGZPath.py "J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Data\GDB\GZpolygons.gdb\polygonFromGZ_path_28_Aug_2019"'
	sys.exit(0)

# set date time
datetime = time.asctime( time.localtime(time.time()) )
dts = datetime.split(" ")
#print dts[4]

# Use the first argument from the command line as the feature name
featureName = sys.argv[1]

# output folder
outputF = "J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Data\Output"

my_list = []

cursor = arcpy.da.SearchCursor(featureName, ['gzPathName'])
for val in cursor:
	my_list.append(val)

# turning a list into a set removes duplicates
print len(my_list)
my_list = list(set(my_list))
print len(my_list)

# the text file into which the unique file pathnames will be written
featureNameS = featureName.split('\\')
filename = featureNameS[-1] + '.txt'
fw = open(outputF + os.sep + filename, "a")

for val in my_list:
	fw.write(val[0] + "\n")

fw.close()


