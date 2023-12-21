import zipfile

with (open("tozip1.txt","w") as file1):
      file1.write("content1")
with (open("tozip2.txt","w") as file2):
      file2.write("content2")

zipped=zipfile.ZipFile("zipped","w")
zipped.write("tozip1.txt",compress_type=zipfile.ZIP_DEFLATED)
zipped.write("tozip2.txt",compress_type=zipfile.ZIP_DEFLATED)
zipped.close()

zipped=zipfile.ZipFile("zipped","r")
zipped.extractall("extracted")
