import bpy

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
        def get_font():
            font = bpy.data.fonts.get("Arial Regular")
            if not font:
                arial_cyrillic_font_path = "C:/Windows/Fonts/Arial.ttf"
                bpy.ops.font.open(filepath=arial_cyrillic_font_path)
                font = bpy.context.object.data.font
                if font:
                    bpy.data.fonts.remove(font, do_unlink=True)
                    font = bpy.data.fonts.get("Arial Regular")
            return font

        def get_or_create_material():
            material_baze_text = bpy.data.materials.get("BazeText")
            if not material_baze_text:
                material_baze_text = bpy.data.materials.new(name="BazeText")
                material_baze_text.diffuse_color = (0.0, 0.5, 1.0)
            return material_baze_text

        def create_text(text, font, material, size):
            bpy.ops.object.text_add()
            text_obj = bpy.context.object
            text_obj.data.body = text
            text_obj.data.font = font
            text_obj.active_material = material
            text_obj.data.extrude = size * 0.2
            return text_obj

        def create_text_on_faces(selected_obj, material_baze_text, size):
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

                            text_obj = create_text(material_name, font, material_baze_text, size)
                            text_obj.location = center
                            text_obj.rotation_mode = 'QUATERNION'
                            text_obj.rotation_quaternion = normal.to_track_quat('Z', 'Y')
                            text_obj.scale *= 2

        selected_objects = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
        material_baze_text = get_or_create_material()

        for selected_obj in selected_objects:
            create_text_on_faces(selected_obj, material_baze_text, self.text_size)

        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        return context.object and context.object.type == 'MESH'


def register():
    bpy.utils.register_class(TEXT_ON_FACES_OT_operator)


def unregister():
    bpy.utils.unregister_class(TEXT_ON_FACES_OT_operator)


if __name__ == "__main__":
    register()
