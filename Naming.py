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

    def execute(self, context):
        arial_cyrillic_font_path = "C:/Windows/Fonts/Arial.ttf"
        
        # Остальной код остается без изменений...

        # Функция для создания текста с заданным текстом, шрифтом, размером и материалом
        def create_text(text, font, material, size):
            bpy.ops.object.text_add()
            text_obj = bpy.context.object
            text_obj.data.body = text
            text_obj.data.font = font
            text_obj.active_material = material
            
            # Устанавливаем параметры размера и экструзии текста
            text_obj.scale *= size
            text_obj.data.extrude = size * 0.2  # Привязываем экструзию к размеру текста
            
            return text_obj

        # Получаем все выбранные объекты MESH
        selected_objects = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
        material_baze_text = get_or_create_material()
        
        # Для каждого выбранного объекта MESH создаем текст на его гранях
        for selected_obj in selected_objects:
            create_text_on_faces(selected_obj, material_baze_text, self.text_size)
        
        return {'FINISHED'}

    # Остальной код остается без изменений...

    def draw(self, context):
        layout = self.layout
        layout.operator("object.text_on_faces_operator").text_size

def register():
    bpy.utils.register_class(TEXT_ON_FACES_OT_operator)
    bpy.utils.register_class(TEXT_ON_FACES_PT_Panel)

def unregister():
    bpy.utils.unregister_class(TEXT_ON_FACES_OT_operator)
    bpy.utils.unregister_class(TEXT_ON_FACES_PT_Panel)

if __name__ == "__main__":
    register()
