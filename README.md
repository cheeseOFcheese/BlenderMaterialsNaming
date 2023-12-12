## Blender 3D Text Material Labeling
Этот скрипт для Blender предназначен для автоматической разметки граней 3D-модели текстом, отображающим имя примененного материала. Скрипт поддерживает шрифты с кириллицей и позволяет пользователю выбирать путь к шрифту на компьютере.

Использование
Настройка пути к шрифту:
Замените переменную arial_cyrillic_font_path на фактический путь к шрифту Arial или другому шрифту с поддержкой кириллицы на вашем компьютере.

Запуск скрипта:
Выберите меш (тип объекта 'MESH'), который вы хотите разметить, затем выполните скрипт. Текст с названиями материалов будет автоматически размещен в центре каждой грани.

Настройка параметров:
При необходимости вы можете настроить масштаб и другие параметры размещения текста, редактируя соответствующие строки в конце скрипта.

Зависимости
Blender 2.8 и выше.
    Примечания
    Для улучшения производительности материалы меша сохраняются в словарь для быстрого доступа.
    При отсутствии шрифта в Blender производится его загрузка, и после использования удаляется.
    Пример использования
    python
    Copy code
    # Загрузка скрипта в Blender
    import bpy
    
    # ... (вставьте код сюда)
    
    # Выбор объекта типа MESH
    selected_obj = bpy.context.object
    
    # Запуск скрипта для разметки граней текстом
    if selected_obj and selected_obj.type == 'MESH':
        # ... (вставьте код сюда)
    Важно
Перед запуском скрипта убедитесь, что объект выбран и является типом 'MESH'.
При необходимости адаптируйте размер текста и другие параметры согласно вашим предпочтениям.
Enjoy labeling your 3D models with ease!
