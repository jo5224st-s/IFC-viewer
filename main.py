import sys

sys.path.append("/Users/macbookair/PycharmProjects/xeopy")

print(sys.path)

from xeopy import *
import random

content = []  # Starting a content for the file

content.append(Viewer())  # Adding Viewer with default settings
content.append(CameraSettings())  # Adding Camera with default settings

# Setting up the IFC setup
content.append(IFCAPIInitiationStart())  # WebIFCLoaderPlugin needs this IFC API initiation start

content.append(WebIFCLoaderPlugin(variable_name="ifcLoader"))  # Creating WebIFCLoaderPlugin required to load IFC
print("Choose IFC file(s) to visualize (separate with comma if multiple files):")
path = input().split(",") # Creates a list of IFC files

for i in range(len(path)): # Runs SceneModelLoading once for each file
    content.append(SceneModelLoading(path=path[i], variable_name = "sceneModel" +str(i+1), loader_variable_name="ifcLoader"))

content.append(End())  # WebIFCLoaderPlugin needs this IFC API initiation to end

# Creating a file

xeokit = Xeokit(content=content, file_path="ifc_viewer.html")
xeokit.create_and_save()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass


