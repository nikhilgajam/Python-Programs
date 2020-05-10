import zipfile
import os

os.chdir("C:\\Users\\DELL\\Downloads")
# You can add a folder to compress group of things
zips = zipfile.ZipFile("Zipped.zip", "w")
# Here
zips.write("a.txt", compress_type=zipfile.ZIP_DEFLATED)

zips.close()
