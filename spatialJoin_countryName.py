# Name: spatialJoin_countryName.py
#       J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Python\spatialJoin_countryName.py
# Author: Stuart Wallace - Sept 2019
# Description: set the country name of each country polygon using a spatial join with the country bubble layer
#

# Import system modules
import arcpy
import os

# Set local variables
workspace = r"J:\GISprojects\Ordnance Survey MasterMap\Derived Data\Data\GDB\OSMM_FME_MHW_Polygon.gdb"

targetFeatures = os.path.join(workspace, "OSMM_MHW_polygon_country_2018_BNG")
joinFeatures = os.path.join(workspace, "OSMM_MHW_polygon_country_bubble_attributes")

# Output will be a new feature
outfc = os.path.join(workspace, "OSMM_MHW_polygon_country_attributes_2018_BNG")

# Create a new fieldmappings object and add the two input feature classes.
fieldmappings = arcpy.FieldMappings()
fieldmappings.addTable(targetFeatures)
fieldmappings.addTable(joinFeatures)

# Set the output field's properties as a field object
fieldIndex = fieldmappings.findFieldMapIndex("CountryName")
fieldmap = fieldmappings.getFieldMap(fieldIndex)
field = fieldmap.outputField

# Rename the field and pass the updated field object back into the field map
field.name = "CountryNameOut"
field.aliasName = "CountryNameOut"
fieldmap.outputField = field

# Replace the old fieldmap in the mappings object
fieldmappings.replaceFieldMap(fieldIndex, fieldmap)

#Run the Spatial Join tool, using the defaults for the join operation and join type
arcpy.SpatialJoin_analysis(targetFeatures, joinFeatures, outfc, "#", "#", fieldmappings)
