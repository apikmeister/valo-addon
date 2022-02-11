bl_info = {
    "name": "Valorant Weapon Variants",
    "author": "apikmeister",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "support": "COMMUNITY",
    "description": "skins :)",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}


import bpy
from bpy.props import (FloatProperty,
                        StringProperty,
                        BoolProperty,
                        EnumProperty,
                        PointerProperty )
                        
class ImportProps():

    fVariant : IntProperty(
            name = "Variant",
            description = " ",
            default = 1, min = 1, max = 4, step = 1,
            )

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
