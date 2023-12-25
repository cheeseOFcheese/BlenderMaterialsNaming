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
        
        # Функция для проверки наличия шрифта в Blender и его загрузки
        def get_font():
            font = bpy.data.fonts.get("Arial Regular")
            if not font:
                bpy.ops.font.open(filepath=arial_cyrillic_font_path)
                font = bpy.context.object.data.font
                bpy.data.fonts.remove(font, do_unlink=True)
                font = bpy.data.fonts.get("Arial Regular")
            return font
        
        # Функция для получения или создания материала "BazeText"
        def get_or_create_material():
            material_baze_text = bpy.data.materials.get("BazeText")
            if not material_baze_text:
                material_baze_text = bpy.data.materials.new(name="BazeText")
                material_baze_text.diffuse_color = (0.0, 0.5, 1.0)  # Настройте цвет по вашему усмотрению
            return material_baze_text
        
        # Функция для создания текста с заданным текстом, шрифтом, размером, межбуквенным интервалом и материалом
        def create_text(text, font, material, size, spacing):
            bpy.ops.object.text_add()
            text_obj = bpy.context.object
            text_obj.data.body = text
            text_obj.data.font = font
            text_obj.active_material = material
            
            # Устанавливаем параметры размера и интервала между буквами текста
            text_obj.scale *= size
            text_obj.data.extrude = size * 0.2  # Привязываем экструзию к размеру текста
            text_obj.data.space_character = spacing
            
            return text_obj
        
        # Функция для создания текста на гранях выбранного объекта MESH
        def create_text_on_faces(selected_obj, material_baze_text, size, spacing):
            if selected_obj and selected_obj.type == 'MESH':
                mesh = selected_obj.data
                materials_dict = {mat.name: mat for mat in selected_obj.data.materials}
                font = get_font()
                
                for face in mesh.polygons:
                    material_index = face.material_index
                    
                    if material_index != -1:
                        face_material = materials_dict.get(selected_obj.data.materials[material_index].name)
                        
                        if face_material:
                            material_name = face_material.name
                            center = selected_obj.matrix_world @ face.center
                            normal = face.normal
                            
                            text_obj = create_text(material_name, font, material_baze_text, size, spacing)
                            text_obj.location = center
                            text_obj.rotation_mode = 'QUATERNION'
                            text_obj.rotation_quaternion = normal.to_track_quat('Z', 'Y')
        
        # Получаем все выбранные объекты MESH
        selected_objects = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
        material_baze_text = get_or_create_material()
        
        # Для каждого выбранного объекта MESH создаем текст на его гранях
        for selected_obj in selected_objects:
            create_text_on_faces(selected_obj, material_baze_text, self.text_size, self.letter_spacing)
        
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
