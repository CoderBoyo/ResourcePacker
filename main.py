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
    material = {1, 2, 3, 4, 5}
    if "Output" not in os.listdir():
        print("Output directory not found creating\n")
        create_tree()
    else:
        print("Output directory found... Replacing\n")
        shutil.rmtree("Output")
        create_tree()

    entries = os.listdir("Files")
    for entry in entries:
        name = entry.split("!")[0]
        item = entry.split("!")[1].split("^")[0]
        cmd = entry.split("!")[1].split("^")[1].split(".")[0]

        print("Name: " + name)
        print("Item: " + item)
        print("CMD: " + cmd + "\n")

        open("Output/assets/minecraft/models/item/" + item + ".json", "w")
        open("Output/assets/minecraft/models/item/texture_models/" + name + ".json", "w")

        textureModel = open("Output/assets/minecraft/models/item/texture_models/" + name + ".json", "a")

        texture = {
            "parent": "minecraft:item/generated",
            "textures": {
                "layer0": "minecraft:item/" + name
            }
        }

        textureModel.write(json.dumps(texture, indent=2))

        file = open("Output/assets/minecraft/models/item/" + item + ".json", "a")

        finalStr = ""

        if item not in material:
            materialData = '''{
                "parent": "item/handheld",
                "textures": {
                    "layer0": "item/"''' + item + '''
                },
                "overrides": ['''
            finalStr += materialData.replace(" ", "").replace('\n', "").replace('\"', "")

        material.add(item)

        modelData = '''
                {
                    "predicate": {
                        "custom_model_data": ''' + cmd + '''
                    },
                    "model": "item/texture_models/"''' + name + '''
                },'''

        finalStr += modelData.replace(" ", "").replace('\n', "").replace('\"', "")

        file.write(json.dumps(finalStr, indent=2).replace('"', ""))

    for image in glob.iglob(os.path.join("Files", "*.png")):
        shutil.copy(image, "Output/assets/minecraft/textures/item/")

    for image in os.listdir("Output/assets/minecraft/textures/item/"):
        os.rename("Output/assets/minecraft/textures/item/" + image,
                  "Output/assets/minecraft/textures/item/" + image.split("!")[0] + ".png")

    shutil.make_archive("pack", "zip", "Output")


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
            print("\nProject Created in Directory \"Files\"")
        else:
            print("\nProject has already been created! Aborting")

    if int(input("Select Option: ")) == 3:
        print("\n")
        rp_create()

