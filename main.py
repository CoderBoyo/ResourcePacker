import os
import shutil
import json
import glob


def create_tree():
    os.mkdir("Output")
    os.mkdir("Output/assets")
    os.mkdir("Output/assets/minecraft")
    os.mkdir("Output/assets/minecraft/models")
    os.mkdir("Output/assets/minecraft/models/item")
    os.mkdir("Output/assets/minecraft/models/item/texture_models")

    os.mkdir("Output/assets/minecraft/textures")
    os.mkdir("Output/assets/minecraft/textures/item")

    open("Output/LICENSE", "w")
    license = open("Output/LICENSE", "a")
    license.write("This resource pack was generated with SwordOfSouls#7843 ResourcePacker")
    open("Output/pack.mcmeta", "w")
    meta = open("Output/pack.mcmeta", "a")
    metaInfo = {
        "pack": {
            "pack_format": 8,
            "description": "ResourcePacker Generated Pack"
        }
    }
    meta.write(json.dumps(metaInfo, indent=2))

def rp_create():
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
        print("CMD: " + entry.split("!")[1].split("^")[1].split(".")[0] + "\n")

        open("Output/assets/minecraft/models/item/" + entry.split("!")[1].split("^")[0] + ".json", "w")
        open("Output/assets/minecraft/models/item/texture_models/" + entry.split("!")[0] + ".json", "w")

        textureModel = open("Output/assets/minecraft/models/item/texture_models/" + entry.split("!")[0] + ".json", "a")

        texture = {
            "parent": "minecraft:item/generated",
            "textures": {
                "layer0": "minecraft:item/" + entry.split("!")[0]
            }
        }

        textureModel.write(json.dumps(texture, indent=2))

        file = open("Output/assets/minecraft/models/item/" + entry.split("!")[1].split("^")[0] + ".json", "a")
        modelData = {
            "parent": "item/handheld",
            "textures": {
                "layer0": "item/" + entry.split("!")[1].split("^")[0]
            },
            "overrides": [
                {
                    "predicate": {
                        "custom_model_data": entry.split("!")[1].split("^")[1].split(".")[0]
                    },
                    "model": "item/texture_models/" + entry.split("!")[0]
                }
            ]
        }
        file.write(json.dumps(modelData, indent=2))

    for image in glob.iglob(os.path.join("Files", "*.png")):
        shutil.copy(image, "Output/assets/minecraft/textures/item/")

    for image in os.listdir("Output/assets/minecraft/textures/item/"):
        os.rename("Output/assets/minecraft/textures/item/" + image,"Output/assets/minecraft/textures/item/" + image.split("!")[0] + ".png")

print("Welcome to ResourcePacker please choose an option: ")
print("1: Tutorial")
print("2: Create Project")
print("3: Run Pack Maker")
while True:
    if int(input("Select Option: ")) == 1:
        print("To create a new item put the .png of it in the \"Files\" folder")
        print("Syntax: <name>!<minecraft_item>^<CMD>")
        print("Example: speed_boots!iron_boots^1")
    if int(input("Select Option: ")) == 2:
        if "Files" not in os.listdir():
            os.mkdir("Files")
        else:
            shutil.rmtree("Files")
            os.mkdir("Files")
        print("Project Created in Directory \"Files\"")
    if int(input("Select Option: ")) == 3:
        rp_create()