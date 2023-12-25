bl_info = {
    "name": "Text on Faces",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
import os

class TEXT_ON_FACES_OT_operator(bpy.types.Operator):
    bl_idname = "object.text_on_faces_operator"
    bl_label = "Text on Faces"
    bl_options = {'REGISTER', 'UNDO'}

    text_size: bpy.props.FloatProperty(
        name="Text Size",
        default=1.0,
        min=0.1,
        max=5.0,
        description="Size of the text"
    )

    def execute(self, context):
        arial_cyrillic_font_path = "C:/Windows/Fonts/Arial.ttf"

        def get_font():
            # Логика для проверки наличия и загрузки шрифта
            pass

        def get_or_create_material():
            # Логика для получения или создания материала
            pass

        def create_text(text, font, material):
            # Логика для создания текста на гранях
            pass

        def create_text_on_faces(selected_obj, material_baze_text):
            # Логика для создания текста на гранях выбранного объекта
            pass

        # Получаем все выбранные объекты MESH
        selected_objects = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
        material_baze_text = get_or_create_material()

        # Для каждого выбранного объекта MESH создаем текст на его гранях
        for selected_obj in selected_objects:
            create_text_on_faces(selected_obj, material_baze_text)

        return {'FINISHED'}


def register():
    bpy.utils.register_class(TEXT_ON_FACES_OT_operator)

    # Создаем необходимые директории
    local_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "4.0")
    user_directory = os.path.join(os.path.expanduser("~"), ".config", "blender", "4.0")
    system_directory = "/usr/share/blender/4.0"

    os.makedirs(local_directory, exist_ok=True)
    os.makedirs(user_directory, exist_ok=True)
    # В системной директории находятся только файлы, они создаются по мере необходимости, не требуется создание папок


def unregister():
    bpy.utils.unregister_class(TEXT_ON_FACES_OT_operator)


if __name__ == "__main__":
    register()
