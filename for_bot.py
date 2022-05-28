import os
import sys

os.chdir("C:\\Users\\jegat\\Desktop\\py_work\\work\\bots")

files = os.listdir()
print(files)
last_bot = max(files, key=os.path.getctime)

absolute_filename = fr"C:\Users\jegat\Desktop\py_work\bat_files\{last_bot[:-3]}.bat"

bot_input = fr"@py.exe C:\Users\jegat\Desktop\py_work\work\bots\{last_bot} %*"


if len(sys.argv) > 1:
    with open(absolute_filename, "w") as bat_file:
        bat_file.write(bot_input)
        bat_file.write("\n@pause")
else:
    with open(absolute_filename, "w") as bat_file:
        bat_file.write(bot_input)
