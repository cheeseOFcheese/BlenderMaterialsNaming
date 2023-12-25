import bpy

class TEXT_ON_FACES_OT_Operator(bpy.types.Operator):
    bl_idname = "object.text_on_faces_operator"
    bl_label = "Text on Faces"

    def execute(self, context):
        # Путь к шрифту Arial с поддержкой кириллицы на вашем компьютере
        arial_cyrillic_font_path = "C:/Windows/Fonts/Arial.ttf"  # Измените на путь к вашему шрифту Arial или другому шрифту с кириллицей

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

        # Ваша функция create_text_on_faces внутри execute
        def create_text_on_faces(selected_obj, material_baze_text):
            # Оставляем вашу логику без изменений
            pass
        
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
    bpy.utils.register_class(TEXT_ON_FACES_OT_Operator)
    bpy.utils.register_class(TEXT_ON_FACES_PT_Panel)

def unregister():
    bpy.utils.unregister_class(TEXT_ON_FACES_OT_Operator)
    bpy.utils.unregister_class(TEXT_ON_FACES_PT_Panel)

if __name__ == "__main__":
    register()
