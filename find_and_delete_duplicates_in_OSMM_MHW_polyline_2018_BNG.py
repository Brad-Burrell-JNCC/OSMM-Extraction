# Name: find_and_delete_duplicates_in_OSMM_MHW_polyline_2018_BNG.py
#       J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Python\find_and_delete_duplicates_in_OSMM_MHW_polyline_2018_BNG.py
# Author: Stuart Wallace - Sept 2019
# Description: find duplicate linework. Delete all but one element.
#

# Import system modules
import arcpy
from arcpy import env

env.overwriteOutput = True

# Set workspace environment
env.workspace = "J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Data\GDB\OSMM_FME_MHW_feature.gdb"

# Set input feature class
#in_dataset = "OSMM_BL_CountryBorder_polyline_2018_BNG_attributed"
in_dataset = "OSMM_MHW_polyline_2018_BNG"

# Set the field upon which the identicals are found
fields = ["TOID"]

# Execute Delete Identical 
arcpy.DeleteIdentical_management(in_dataset, fields)