import bpy

class TEXT_ON_FACES_OT_operator(bpy.types.Operator):
    bl_idname = "object.text_on_faces_operator"
    bl_label = "Text on Faces"

    text_size: bpy.props.FloatProperty(
        name="Text Size",
        description="Size of the generated text",
        default=2.0,
        min=0.1,
        max=10.0
    )

    letter_spacing: bpy.props.FloatProperty(
        name="Letter Spacing",
        description="Spacing between letters",
        default=0.1,
        min=0.0,
        max=1.0
    )

    def execute(self, context):
        arial_cyrillic_font_path = "C:/Windows/Fonts/Arial.ttf"
        
        # Остальной код без изменений...

        return {'FINISHED'}

    def draw(self, context):
        layout = self.layout
        layout.operator("object.text_on_faces_operator")
        layout.prop(self, "text_size")
        layout.prop(self, "letter_spacing")

def register():
    bpy.utils.register_class(TEXT_ON_FACES_OT_operator)

def unregister():
    bpy.utils.unregister_class(TEXT_ON_FACES_OT_operator)

if __name__ == "__main__":
    register()
