import os
import shutil


def create_tree():
    os.mkdir("Output")
    os.mkdir("Output/assets")
    os.mkdir("Output/assets/minecraft")
    os.mkdir("Output/assets/minecraft/models")
    os.mkdir("Output/assets/minecraft/models/item")


if "Output" not in os.listdir():
    print("Output directory not found creating\n")
    create_tree()
else:
    print("Output directory found... Replacing\n")
    shutil.rmtree("Output")
    create_tree()

entries = os.listdir("Files")
for entry in entries:
    print("Name: " + entry.split("!")[0])
    print("Item: " + entry.split("!")[1].split("^")[0])
    open("Output/assets/minecraft/models/item/" + entry.split("!")[1].split("^")[0] + ".json","w")
    file = open("Output/assets/minecraft/models/item/" + entry.split("!")[1].split("^")[0] + ".json","a")
    file.write("test")
    print("CMD: " + entry.split("!")[1].split("^")[1].split(".")[0] + "\n")
''