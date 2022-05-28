import os
import string

# Change the current working directory.
os.chdir("C:\\Users\\jegat\\Desktop\\py_work\\work\\bots\\ppt\\composites")

# Store images directory.
jpeg_files = os.listdir()
print(jpeg_files)

for i in range(len(jpeg_files)):
    os.rename(jpeg_files[i], f"{jpeg_files[i][5:-4]}")

just_files = os.listdir()
print(just_files)

just_files = [int(just_files[i]) for i in range(len(just_files))]
just_files.sort()
just_files = [str(just_files[i]) for i in range(len(just_files))]


print(just_files)

for i in range(len(just_files)):
    os.rename(just_files[i], f"{string.ascii_uppercase[i]}.JPG")
