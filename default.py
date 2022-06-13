"""This module contains default values used by the plugin.
"""

# Algorithm parameters
CD_SOURCE_FOLDER = 'Source folder'
CD_SOURCE_CRS = 'Source Coordinate System'
CD_OUTPUT_CRS = 'Output Coordinate System'
CD_DESTINATION_FOLDER = 'Destination folder'

RASTERIZE_TYPE = 'Rasterize algorithm'

ALLOWED_FORMATS = [
    '.ort',
    '.ORT',
    '.xyz',
    '.XYZ'
]

ALLOWED_VECTOR_FORMATS = [
    '.gpkg',
    '.GPKG',
    '.shp',
    '.SHP'
]

STR_SPLIT_CHARS = [
    '\n',
    '\t',
    ' '
]

DELIMITER_CHAR = ' '
COLUMN_COUNT = 3
X_INDEX = 0
Y_INDEX = 1
ELEV_INDEX = 2
ELEV_MIN_THRESHOLD = -100
ELEV_MAX_THRESHOLD = 8000

NEARSET_NEIGHBOUR = 'Nearest neighbour (NN)'
IDW = 'Inverse distance interpolation (IDW)'
TIN = 'Triangulated irregular network (TIN)'

RASTERIZE_OPTIONS = [
    NEARSET_NEIGHBOUR,
    IDW,
    TIN
]
