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
        
        # Ваши функции get_font(), get_or_create_material(), create_text(), create_text_on_faces()
        # ...

        return {'FINISHED'}

class TEXT_ON_FACES_PT_Panel(bpy.types.Panel):
    bl_label = "Text on Faces Panel"
    bl_idname = "TEXT_ON_FACES_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.text_on_faces_operator")
        layout.operator("object.set_name_operator")  # Это кнопка Set Name

class SET_NAME_OT_operator(bpy.types.Operator):
    bl_idname = "object.set_name_operator"
    bl_label = "Set Name"

    def execute(self, context):
        # Здесь можно добавить логику для изменения имени объекта
        return {'FINISHED'}

def register():
    bpy.utils.register_class(TEXT_ON_FACES_OT_operator)
    bpy.utils.register_class(TEXT_ON_FACES_PT_Panel)
    bpy.utils.register_class(SET_NAME_OT_operator)

def unregister():
    bpy.utils.unregister_class(TEXT_ON_FACES_OT_operator)
    bpy.utils.unregister_class(TEXT_ON_FACES_PT_Panel)
    bpy.utils.unregister_class(SET_NAME_OT_operator)

if __name__ == "__main__":
    register()
