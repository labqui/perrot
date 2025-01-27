#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

# import pero enums
from pero.enums import *

# define constants
DATA_FRAME = 'data_frame'

GRID_MAJOR_Z = 20
GRID_MINOR_Z = 10

AXIS_Z = 10
COLOR_BAR_Z = 1000
TITLE_Z = 5000

SERIES_Z = 1000
PIE_Z = 1000
VENN_Z = 1000

LABELS_Z = 2000
ANNOTS_Z = 3000
LEGEND_Z = 4000

VENN_CIRCLE_Z = 1000
VENN_REGION_Z = 1100

# define values
MAJOR = 'major'
MINOR = 'minor'

FULL = 'full'
SEMI = 'semi'

# define gridlines modes
GRID_MAJOR = MAJOR
GRID_MINOR = MINOR

GRID_MODE = Enum(
    MAJOR = GRID_MAJOR,
    MINOR = GRID_MINOR)

# define venn diagram modes
VENN_NONE = NONE
VENN_SEMI = SEMI
VENN_FULL = FULL

VENN_MODE = Enum(
    NONE = VENN_NONE,
    SEMI = VENN_SEMI,
    FULL = VENN_FULL)
