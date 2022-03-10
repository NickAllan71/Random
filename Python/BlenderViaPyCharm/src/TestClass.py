import bpy


class TestClass:
    def __init__(self):
        print("Constructed!!")

    @staticmethod
    def draw_monkey():
        bpy.ops.mesh.primitive_monkey_add()
