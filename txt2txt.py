# Name: txt2txt.py
# Author: Stuart Wallace - Sept 2015
# Description: read in .txt and merge every 4 rows into one row output in new file 

import os, time, sys, datetime
from arcpy import env

#print ' '

# check for at least one argument. Folder name is required.
if len(sys.argv) < 2:
	#sys.argv[1:] = ["-h"]
	print ' '
	print '  need input folder name, ie >txt2txt.py com_vin.txt'
	print ' '
	print '  put file in J:\\GISprojects\\Ordnance Survey MasterMap\\Derived Data\\Data\\PDF\\'
	print ' '
	sys.exit(0)

dTime = time.asctime( time.localtime(time.time()) )
dts = dTime.split(" ")
#print dts[4] + dts[1] + dts[2]

# The first argument from the command line is the file name
#workF = sys.argv[0].split('Python')[0]   # name of "Python" folder is case sensitive!
argFilNam = sys.argv[1]

workfolder = "J:\\GISprojects\\Ordnance Survey MasterMap\\Derived Data\\Data\\PDF\\"
inputFile = workfolder + argFilNam
outputFile = workfolder + "out_" + argFilNam

# Output file
if os.path.exists(outputFile):
	os.remove(outputFile)
fw = open(outputFile, "a")

#sys.exit(0)

num = 0
mod = 4   # Modulus - change this number to change how many rows are concatenated into a single new row
newrow = ""
x = 0
delim = ","

# INPUT
with open(inputFile) as f:
	content = f.readlines()

	for row in content:
		row = row[:-1]
		#print row
		if x != 0:
			newrow = newrow + delim + row
		else:
			newrow = row

		num += 1
		x = num % mod
		#print x

		if x == 0:
			#print newrow
			fw.write(newrow + "\n")
			newrow = ""

print num

fw.close()

print "\n\n Output FILE: " + (outputFile + "\n")



