import bpy

class TEXT_ON_FACES_OT_operator(bpy.types.Operator):
    bl_idname = "object.text_on_faces_operator"
    bl_label = "Text on Faces"

    def execute(self, context):
        arial_cyrillic_font_path = "C:/Windows/Fonts/Arial.ttf"
        
        # Функция для проверки наличия шрифта в Blender и его загрузки
        def get_font():
            font = bpy.data.fonts.get("Arial Regular")
            if not font:
                bpy.ops.font.open(filepath=arial_cyrillic_font_path)
                font = bpy.context.object.data.font
                if font:
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
        
        # Функция для создания текста с заданным текстом, шрифтом и материалом
        def create_text(text, font, material):
            bpy.ops.object.text_add()
            text_obj = bpy.context.object
            text_obj.data.body = text
            text_obj.data.font = font
            text_obj.active_material = material
            
            # Устанавливаем параметр экструзии, привязанный к размеру текста (в пропорции 0.2)
            initial_scale = text_obj.scale.copy()  # Запоминаем исходный размер текста
            text_obj.data.extrude = initial_scale[0] * 0.2  # Привязываем экструзию к размеру текста
            
            return text_obj
        
        # Функция для создания текста на гранях выбранного объекта MESH
        def create_text_on_faces(selected_obj, material_baze_text):
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
                            
                            text_obj = create_text(material_name, font, material_baze_text)
                            text_obj.location = center
                            text_obj.rotation_mode = 'QUATERNION'
                            text_obj.rotation_quaternion = normal.to_track_quat('Z', 'Y')
                            text_obj.scale *= 2  # Измените этот множитель по вашему усмотрению 
        
        # Получаем все выбранные объекты MESH
        selected_objects = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
        material_baze_text = get_or_create_material()
        
        # Для каждого выбранного объекта MESH создаем текст на его гранях
        for selected_obj in selected_objects:
            create_text_on_faces(selected_obj, material_baze_text)
        
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

def register():
    bpy.utils.register_class(TEXT_ON_FACES_OT_operator)
    bpy.utils.register_class(TEXT_ON_FACES_PT_Panel)

def unregister():
    bpy.utils.unregister_class(TEXT_ON_FACES_OT_operator)
    bpy.utils.unregister_class(TEXT_ON_FACES_PT_Panel)

if __name__ == "__main__":
    register()
