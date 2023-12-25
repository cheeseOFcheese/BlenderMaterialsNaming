bl_info = {
    "name": "Text on Faces",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy

class TEXT_ON_FACES_OT_operator(bpy.types.Operator):
    bl_idname = "object.text_on_faces_operator"
    bl_label = "Text on Faces"

    def execute(self, context):
        arial_cyrillic_font_path = "C:/Windows/Fonts/Arial.ttf"
        
        def get_font():
            # Ваша функция get_font()
            pass

        def get_or_create_material():
            # Ваша функция get_or_create_material()
            pass

        def create_text(text, font, material):
            # Ваша функция create_text()
            pass

        def create_text_on_faces(selected_obj, material_baze_text):
            # Ваша функция create_text_on_faces()
            pass

        selected_objects = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
        material_baze_text = get_or_create_material()

        for selected_obj in selected_objects:
            create_text_on_faces(selected_obj, material_baze_text)
        
        return {'FINISHED'}

def register():
    bpy.utils.register_class(TEXT_ON_FACES_OT_operator)

def unregister():
    bpy.utils.unregister_class(TEXT_ON_FACES_OT_operator)

if __name__ == "__main__":
    register()
