# Name: uniqueGridRefPath.py
#       J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Python\uniqueGridRefPath.py
# Author: Stuart Wallace - 08 Mar 2019
# Description: make a list file of .gz file path values based on a shapefile attribute field held in this .shp below for example
#              J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Data\ShapeFile\OSGB1kmGrid_Intersect.shp
#              note: this .shp contains an intersection of 1km grids and the OSMM MHW coaastline

import arcpy, os, types, time, csv, sys, re

print ' '

# check for at least one argument. Shapefile name is required.
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

# output folder
outputF = "J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Data\Output"

# write to text file into which the unique grid refs will be added
filename = "unique_gridref_gz_path.txt"
fw = open(outputF + os.sep + filename, "a")

# build a list of all .gz 
my_listGZ = []
#for root, dirs, files in os.walk(r"J:\Reference\BaseMapping\OSMasterMap\2015 complete GB dataset\Part 1 of 11\data"):
for root, dirs, files in os.walk(r"J:\Reference\BaseMapping\OSMasterMap\2015 complete GB dataset"):
	for fname in files:
		if fname.endswith(".gz"):
			my_listGZ.append(os.path.join(root, fname))

#print (my_listGZ[0])
print len(my_listGZ)
#sys.exit(0)

def findgz(pattern):
	#print 'A: ' + pattern
	for fname in my_listGZ:
		if pattern in fname:
			#print 'B :' + fname
			return os.path.join(root, fname)

my_list = []
#my_listPath = []
countR = 0
countPath = 0
countMatch = 0

cursor = arcpy.da.SearchCursor(shp, ['gridref'])
for val in cursor:
	#print(val)

	# convert the 1km tile format to a 5km format, ie NR6144 becomes NR6000 and HR6788 becomes 6585
	stVal = val[0]
	#print(stVal)
	stValGr = stVal[0:2]
	#print(stValGr)
	stValA = stVal[2:3]
	#print(stValA)
	stValB = stVal[3:4]
	#print(stValB)
	if (stValGr != 'NF' and stValGr != 'NA'):
		if (int(stValB) > 4):
			stValB = '5'
		else:
			stValB = '0'
	#print(stValB)
	stValC = stVal[4:5]
	#print(stValC)
	stValD = stVal[5:6]
	#print(stValD)
	if (int(stValD) > 4):
		stValD = '5'
	else:
		stValD = '0'
	#print(stValD)

	newStr = stValGr + stValA + stValB + stValC + stValD
	#print(newStr)

	#if (newStr == 'HU2070'):
	#	print(val[0])
	#	print(newStr)

	my_list.append(newStr)
	countR += 1

#sys.exit(0)

print countR
# making a list into a set removes duplicates
my_list = list(set(my_list))
print len(my_list)

for val in my_list:
	#print(val)

	# run the function findgz
	fullPath = findgz(val)
	#print(fullPath)

	#my_listPath.append(val[0])
	#countPath += 1
	if str(fullPath) != 'None':
		countMatch += 1

	fw.write(val + ' ' + str(fullPath) + "\n")

print countMatch
#print len(my_list)

#for param in my_listPath:
#	fw.write(stVal(param) + "\n")

fw.close()


