# Blender 3D Text Material Labeling

This Blender script automates the labeling of faces on a 3D model with text displaying the name of the applied material. The script supports fonts with Cyrillic characters and allows users to specify the path to the font on their computer.

## Usage

1. **Setting up the font path:**
   Replace the variable `arial_cyrillic_font_path` with the actual path to the Arial font or another font supporting Cyrillic characters on your computer.

2. **Running the script:**
   Select a mesh (object type 'MESH') that you want to label, then execute the script. Text displaying material names will be automatically placed at the center of each face.

3. **Adjusting parameters:**
   If necessary, you can adjust the scale and other text placement parameters by editing the corresponding lines at the end of the script.

## Dependencies

- Blender 2.8 and above.

## Notes

- Mesh materials are stored in a dictionary for quick access to enhance performance.
- If the font is not available in Blender, it is loaded and removed after use.

## Example Usage

```python
# Load the script in Blender
import bpy

# ... (paste the code here)

# Select an object of type MESH
selected_obj = bpy.context.object

# Run the script to label faces with text
if selected_obj and selected_obj.type == 'MESH':
    # ... (paste the code here)

# Разметка материалов 3D-текстом в Blender

Этот скрипт для Blender автоматизирует добавление текста на грани 3D-модели с отображением названия примененного материала. Скрипт поддерживает шрифты с кириллицей и позволяет пользователю указать путь к шрифту на своем компьютере.

## Использование

1. **Настройка пути к шрифту:**
   Замените переменную `arial_cyrillic_font_path` на фактический путь к шрифту Arial или другому шрифту с поддержкой кириллицы на вашем компьютере.

2. **Запуск скрипта:**
   Выберите меш (тип объекта 'MESH'), который вы хотите разметить, затем выполните скрипт. Текст с названиями материалов будет автоматически размещен в центре каждой грани.

3. **Настройка параметров:**
   При необходимости вы можете настроить масштаб и другие параметры размещения текста, отредактировав соответствующие строки в конце скрипта.

## Зависимости

- Blender 2.8 и выше.

## Примечания

- Материалы меша сохраняются в словаре для повышения производительности.
- Если шрифт недоступен в Blender, он загружается и удаляется после использования.

## Пример использования

```python
# Загрузка скрипта в Blender
import bpy

# ... (вставьте код сюда)

# Выбор объекта типа MESH
selected_obj = bpy.context.object

# Запуск скрипта для разметки граней текстом
if selected_obj and selected_obj.type == 'MESH':
    # ... (вставьте код сюда)
