# Name: polygonFromGZ.py
#       J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Python\polygonFromGZ.py
# Author: Stuart Wallace - 28 Aug 2019
# Description: make a shapefile of polygons based on points of every .gz in the OSMM data folders

import arcpy, os, types, time, csv, sys, re, shutil

#print ' '

# check for at least one argument. Folder name is required.
if len(sys.argv) < 2:
	#sys.argv[1:] = ["-h"]
	print ' '
	print '  this script needs the root path of the OSMM dataset, ie > polygonFromGZ.py "J:\Reference\BaseMapping\OSMasterMap\\2019 complete GB dataset"'
	sys.exit(0)

datetime = time.asctime( time.localtime(time.time()) )
dts = datetime.split(" ")
#print dts[4]
#print dts[2]
#print dts[1]
#sys.exit(0)

# Use the base argument from the command line as the working folder
workF = sys.argv[0].split('Python')[0]   # note: the name of the "Python" folder is case sensitive!

# Use the first argument from the command line for the location of the OSMM gz files
gzFolder = sys.argv[1]
if not os.path.exists(gzFolder):
	print '  the folder ' + gzFolder +' does not exist'
	sys.exit(0)

# default BNG projection feature - use the projection of this feature when creating the output polygon features
defaultBNG = "J:\GISprojects\Ordnance Survey MasterMap\Derived Data\GDB\DefaultBNG.gdb/hwpbng"

# build a list of all the .gz file names
my_listGZ = []
for root, dirs, files in os.walk(gzFolder):
	for fname in files:
		if fname.endswith(".gz"):
			my_listGZ.append(os.path.join(root, fname))
print len(my_listGZ)

# use SHUTIL to copy the default empty gdb to a new empty gdb if it doesn't exist.
emptyGDB = workF + "GDB\\DefaultEmpty.gdb"
featureGDB = workF + 'Data\\GDB\\Coverage_GZzipFile_5km_polygons.gdb'
arcpy.env.workspace = featureGDB    
arcpy.env.overwriteOutput = True
#if os.path.exists(featureGDB):
#	print ' Delete the existing gdb ' + featureGDB + '\n'
#	shutil.rmtree(featureGDB)
if not os.path.exists(featureGDB):
	shutil.copytree(emptyGDB, featureGDB)

# create a new feature with today's date in the name. And add a column called gzPathName to hold the path names of the .gz files.
featureName = 'polygonFromGZ' + '_' + dts[2] + '_' + dts[1] + '_' + dts[4]
arcpy.CreateFeatureclass_management(featureGDB, featureName, "POLYGON", '#', '#', '#', defaultBNG)
#featureNameGDB = featureGDB + '\\' + featureName
fieldName = "gzPathName"
arcpy.AddField_management(featureName, fieldName, "TEXT")
#sys.exit(0)

for valPath in my_listGZ:
	pIndex = valPath.split('\\data')
	thisPath = pIndex[1]
	#print thisPath

	thisMF = thisPath[12:14]

	thisX = thisPath[14:16]
	thisY = thisPath[16:18]

	# 100 km square OS two digits
	if thisMF == "HP":
		thisMFx = "4"
		thisMFy = "12"
	elif thisMF == "HT":
		thisMFx = "3"
		thisMFy = "11"
	elif thisMF == "HU":
		thisMFx = "4"
		thisMFy = "11"
	elif thisMF == "HW":
		thisMFx = "1"
		thisMFy = "10"
	elif thisMF == "HX":
		thisMFx = "2"
		thisMFy = "10"
	elif thisMF == "HY":
		thisMFx = "3"
		thisMFy = "10"
	elif thisMF == "HZ":
		thisMFx = "4"
		thisMFy = "10"
	elif thisMF == "MC": # Rockall
		thisMFx = "-3"
		thisMFy = "9"
	elif thisMF == "NA":
		thisMFx = "0"
		thisMFy = "9"
	elif thisMF == "NB":
		thisMFx = "1"
		thisMFy = "9"
	elif thisMF == "NC":
		thisMFx = "2"
		thisMFy = "9"
	elif thisMF == "ND":
		thisMFx = "3"
		thisMFy = "9"
	elif thisMF == "NF":
		thisMFx = "0"
		thisMFy = "8"
	elif thisMF == "NG":
		thisMFx = "1"
		thisMFy = "8"
	elif thisMF == "NH":
		thisMFx = "2"
		thisMFy = "8"
	elif thisMF == "NJ":
		thisMFx = "3"
		thisMFy = "8"
	elif thisMF == "NK":
		thisMFx = "4"
		thisMFy = "8"
	elif thisMF == "NL":
		thisMFx = "0"
		thisMFy = "7"
	elif thisMF == "NM":
		thisMFx = "1"
		thisMFy = "7"
	elif thisMF == "NN":
		thisMFx = "2"
		thisMFy = "7"
	elif thisMF == "NO":
		thisMFx = "3"
		thisMFy = "7"
	elif thisMF == "NR":
		thisMFx = "1"
		thisMFy = "6"
	elif thisMF == "NS":
		thisMFx = "2"
		thisMFy = "6"
	elif thisMF == "NT":
		thisMFx = "3"
		thisMFy = "6"
	elif thisMF == "NU":
		thisMFx = "4"
		thisMFy = "6"
	elif thisMF == "NW":
		thisMFx = "1"
		thisMFy = "5"
	elif thisMF == "NX":
		thisMFx = "2"
		thisMFy = "5"
	elif thisMF == "NY":
		thisMFx = "3"
		thisMFy = "5"
	elif thisMF == "NZ":
		thisMFx = "4"
		thisMFy = "5"
	elif thisMF == "OV":
		thisMFx = "5"
		thisMFy = "5"
	elif thisMF == "SC":
		thisMFx = "2"
		thisMFy = "4"
	elif thisMF == "SD":
		thisMFx = "3"
		thisMFy = "4"
	elif thisMF == "SE":
		thisMFx = "4"
		thisMFy = "4"
	elif thisMF == "SH":
		thisMFx = "2"
		thisMFy = "3"
	elif thisMF == "SJ":
		thisMFx = "3"
		thisMFy = "3"
	elif thisMF == "SK":
		thisMFx = "4"
		thisMFy = "3"
	elif thisMF == "SM":
		thisMFx = "1"
		thisMFy = "2"
	elif thisMF == "SN":
		thisMFx = "2"
		thisMFy = "2"
	elif thisMF == "SO":
		thisMFx = "3"
		thisMFy = "2"
	elif thisMF == "SP":
		thisMFx = "4"
		thisMFy = "2"
	elif thisMF == "SR":
		thisMFx = "1"
		thisMFy = "1"
	elif thisMF == "SS":
		thisMFx = "2"
		thisMFy = "1"
	elif thisMF == "ST":
		thisMFx = "3"
		thisMFy = "1"
	elif thisMF == "SU":
		thisMFx = "4"
		thisMFy = "1"
	elif thisMF == "SV":
		thisMFx = "0"
		thisMFy = "0"
	elif thisMF == "SW":
		thisMFx = "1"
		thisMFy = "0"
	elif thisMF == "SX":
		thisMFx = "2"
		thisMFy = "0"
	elif thisMF == "SY":
		thisMFx = "3"
		thisMFy = "0"
	elif thisMF == "SZ":
		thisMFx = "4"
		thisMFy = "0"
	elif thisMF == "TA":
		thisMFx = "5"
		thisMFy = "4"
	elif thisMF == "TF":
		thisMFx = "5"
		thisMFy = "3"
	elif thisMF == "TG":
		thisMFx = "6"
		thisMFy = "3"
	elif thisMF == "TL":
		thisMFx = "5"
		thisMFy = "2"
	elif thisMF == "TM":
		thisMFx = "6"
		thisMFy = "2"
	elif thisMF == "TQ":
		thisMFx = "5"
		thisMFy = "1"
	elif thisMF == "TR":
		thisMFx = "6"
		thisMFy = "1"
	elif thisMF == "TV":
		thisMFx = "5"
		thisMFy = "0"
	else:
		thisMFx = "NovalPath"

	thisMFxx = int(thisMFx + thisX + "000")
	thisMFyy = int(thisMFy + thisY + "000")

	thisMFxxTop = thisMFxx + 5000
	thisMFyyTop = thisMFyy + 5000

	arrayP = arcpy.Array([arcpy.Point(thisMFxx, thisMFyy),
						 arcpy.Point(thisMFxx, thisMFyyTop),
						 arcpy.Point(thisMFxxTop, thisMFyyTop),
						 arcpy.Point(thisMFxxTop, thisMFyy)
						 ])
	polygonP = arcpy.Polygon(arrayP)

	cursorB = arcpy.da.InsertCursor(featureName, ("SHAPE@", fieldName))
	cursorB.insertRow([polygonP,valPath])

del cursorB

