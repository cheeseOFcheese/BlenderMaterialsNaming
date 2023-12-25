import bpy

bl_info = {
    "name": "Text on Faces",
    "blender": (2, 80, 0),
    "category": "Object",
}

class TEXT_ON_FACES_OT_operator(bpy.types.Operator):
    bl_idname = "object.text_on_faces_operator"
    bl_label = "Text on Faces"

    def execute(self, context):
        # Ваш код здесь
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

classes = (
    TEXT_ON_FACES_OT_operator,
    TEXT_ON_FACES_PT_Panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
