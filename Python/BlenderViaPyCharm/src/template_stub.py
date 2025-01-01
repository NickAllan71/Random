import sys
import os
import bpy
import main
import importlib

blend_dir = os.path.dirname(bpy.data.filepath)
sys.path.append(blend_dir)


importlib.reload(main)
main.main()
