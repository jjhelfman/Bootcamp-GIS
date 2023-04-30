import arcpy
arcpy.ImportToolbox(r"@\Conversion Tools.tbx")
arcpy.conversion.FeatureClassToShapefile(
    Input_Features="Wildfires_from_1992-2015",
    Output_Folder=r"C:\Bootcamp GIS\Data"
)
