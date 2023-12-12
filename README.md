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
