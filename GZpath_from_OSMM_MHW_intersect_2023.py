# Name: GZpath_from_OSMM_MHW_intersect.py
#          J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Python\GZpath_from_OSMM_MHW_intersect.py
#
# Author: Stuart Wallace - 30 Aug 2019
#
# Description: make a shapefile of coverage polygons for every .gz in the entire OSMM dataset...
#              ...intersect the coverage shapefile with the OSMM MHW coastline of the entire GB...
#              ...use the attribute in the coverage layer to make a list of .gz file pathnames that intersect
#
## NOTE: the naming convention of the .gz files in the OSMM delivery must remain the same between years.
##        check the names are the same before running this script - format like 4308021-HP4500.gz
#
## ----------------------------------------------------------------------------------------------------------

import arcpy, os, types, time, csv, sys, re, shutil

# check for argument. Folder name is required.
if len(sys.argv) < 2:
	#sys.argv[1:] = ["-h"]
	print ' '
	print '  this script needs the root path of the OSMM gz file folder, ie > GZpath_from_OSMM_MHW_intersect.py "J:\Reference\BaseMapping\OSMasterMap\\2019 complete GB dataset"'
	sys.exit(0)

# check that the gz folder exists
gzFolder = sys.argv[1]
if not os.path.exists(gzFolder):
	print '  the folder ' + gzFolder +' does not exist'
	sys.exit(0)

# set date time values
datetime = time.asctime( time.localtime(time.time()) )
dts = datetime.split(" ")

# Use the argv[0] argument from the command line to set the working folder
workF = sys.argv[0].split('Python')[0]   # note: the name of the "Python" folder is case sensitive!

# default BNG projection feature - the projection of this feature is used when creating the output polygon features
defaultBNG = workF + 'data\GDB\DefaultBNG.gdb/hwpbng'

# build a list of all the .gz file names
gz_path_listGZ = []
for root, dirs, files in os.walk(gzFolder):
	for fname in files:
		if fname.endswith(".gz"):
			gz_path_listGZ.append(os.path.join(root, fname))
print ' '
print '  Count of .gz files in the OSMM dataset: ' + str(len(gz_path_listGZ))

# use SHUTIL to copy the default empty gdb to a new empty gdb (only if it doesn't already exist).
emptyGDB = workF + 'data\GDB\DefaultEmpty.gdb'
featureGDB = workF + 'data\GDB\Coverage_GZzipFile_5km_polygons.gdb'
arcpy.env.workspace = featureGDB
arcpy.env.overwriteOutput = True
if not os.path.exists(featureGDB):
	shutil.copytree(emptyGDB, featureGDB)

# create a new polygon feature with today's date in the name.
# Rename the feature if an earlier version from the same daya already exists - add hr min sec to the name.
# then add a field called gzPathName to hold the path names of the .gz files.
featureName = 'polygonFromGZ_MHW_' + dts[2] + '_' + dts[1] + '_' + dts[4]
if arcpy.Exists(featureName):
	print '  A datestamped polygonFromGZ feature from earlier today already exists, add hr:min:sec to the feature name: '
	hmsIndex = dts[3].split(':')
	featureName = 'polygonFromGZ_MHW_' + dts[2] + '_' + dts[1] + '_' + dts[4] + '_' + hmsIndex[0] + '_' + hmsIndex[1] + '_' + hmsIndex[2]
	print featureName
arcpy.CreateFeatureclass_management(featureGDB, featureName, "POLYGON", '#', '#', '#', defaultBNG)
fieldName = "gzPathName"
arcpy.AddField_management(featureName, fieldName, "TEXT")
#sys.exit(0)

# create 5km2 polygons of the .gz containing MHW.
## NOTE: this for-loop requires the naming convention of the .gz files in the OSMM delivery to remain the same.
##        check the file names are the same before running this script: 
for valPath in gz_path_listGZ:
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


# intersect the gz polygons with an exisitng OSMM MHW polylines to find only those gz polygons that likely contain a mhw feature
inFeatures = [featureName, workF + 'data\GDB\OSMM_MHW_feature_polylines_2015.gdb/MHW']
intersectFeatureName = 'gzPolygon_MHW_intersect' + '_' + dts[2] + '_' + dts[1] + '_' + dts[4]
clusterTolerance = 1.5    
arcpy.Intersect_analysis(inFeatures, intersectFeatureName)


# build a list of the gz pathnames
gz_path_list = []
cursor = arcpy.da.SearchCursor(intersectFeatureName, ['gzPathName'])
for val in cursor:
	gz_path_list.append(val)

# turn the list into a set to remove duplicates
#print len(gz_path_list)
gz_path_list = list(set(gz_path_list))
print ''
print '  Count of gz files containing MHW features: ' + str(len(gz_path_list))

# the text file into which the unique file pathnames will be written
filename = workF + "Python\Output" + os.sep + 'GZpath_from_OSMM_MHW_' + '_' + dts[4] + dts[2] + '_' + dts[1] + '.txt'
if os.path.exists(filename):
	os.remove(filename)
fw = open(filename, "a")
for val in gz_path_list:
	fw.write(val[0] + "\n")
fw.close()

print ''
print filename
