import zipfile
import os
import re

zipped_instructions="unzip_me_for_instructions.zip"
instructions="puzzle_instructions"
instructions_content=instructions+"\extracted_content"
zipfile.ZipFile(zipped_instructions,"r").extractall(instructions)
for item in os.listdir(instructions_content):
    if item.endswith(".txt"):
        with open(instructions_content+"\\"+item,"r") as file:
            print(file.read())
            print("============================================================")

for folder,subfolders,files in os.walk(instructions_content):
    for file in files:
        with open(os.path.join(folder,file),"r") as tmp:
            content=tmp.read()
            result=re.search(r'\d{3}-\d{3}-\d{4}',content)

            if result is not None:
                print(result.group())

