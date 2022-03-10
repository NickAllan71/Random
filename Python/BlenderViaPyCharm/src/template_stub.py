import sys
import os
import bpy

blend_dir = os.path.dirname(bpy.data.filepath)
sys.path.append(blend_dir)

import main
import importlib

importlib.reload(main)
main.main()
