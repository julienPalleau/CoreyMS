import pathlib
import unicodedata
import re
from pprint import pp

# Create a Path object
desktop = pathlib.Path(r"W:\Perso\backup\IT stuff\Cours de programmation\Python\COURS PYTHON\RealPython")

############################################
# GETTING A LIST OF FILES AND DIRECTORIES
############################################

# Conditional listing using glob patterns
# pp(list(desktop.glob("*.pdf")))  # Does not recurse
result = list(desktop.glob("*.pdf"))
file_list = []
file = open("RealPython.txt", "a")

# print(ord('-'))
# print(ord('—'))
# print(chr(45))
# print(chr(8212))
# print("")

compteur = 0

# str="Hello! Welcome to Tutorialspoint. - —"
# str_encoded= str.encode('utf_32', 'strict')
# print("The encoded string is: ", str_encoded)
# str_decoded=str_encoded.decode('utf_32', 'strict')
# print("The decoded string is: ", str_decoded)
# print(str_decoded.find('-'))
# print(str_decoded.find('—'))


for line in result:
    str_encoded = str(line).encode('utf8', 'strict')
    # print(str_encoded.decode("utf8").replace(u"–", "-").split("-")[1])
    file_list.append(str_encoded.decode("utf8").replace(u"–", "-").split("-")[1])

    # emdash = '\u2014'
    # hyphen = '\u002D'
    # result = str(line).replace(emdash, hyphen)
    # print(result.split('-')[-1])


    # result = unicodedata.normalize('NFD', str(line))
    # print(unicodedata.name('-'))

    # str_encoded = str(line).encode('cp1252', 'strict')
    # # print("The encoded string is: ", str_encoded)
    # str_decoded = str_encoded.decode('cp1252', 'strict')
    # print("The decoded string is: ", str_decoded)
    # print(str_decoded.split('u"\u8211"|u"\u45"')[0])
    # print(ord('–'), chr(ord('–')))
    # print(ord('-'), chr(ord('-')))



    # line = str(line).replace(u"\0151", "-")
    # print(re.split(r'—', line)[0])
    # print(str(line).replace("—", "-"))

    # print(unicodedata.name('—'))
    # print(unicodedata.name('-'))

    # line = str(line).replace(u"\0151", "-")
    # print(re.split(r'—', str(line).replace(u"\0151", "-"))[-1])
    # files_list = str(str(str(line).split("\\")[-1].split("_")[:-2:]).split('—')[0])
    # print(files_list)

for line in sorted(file_list):
    print(line)
# if compteur == 0:
#     result = []
#     for carac in (str(line).split("\\")[-1]):
#         result += carac
#     print(result)
#     for carac in result:
#         if carac == "—":
#             print(carac)
#     compteur += 1
#
# print(str(line).split("\\")[-1])
# files_list = str(str(str(line).split("\\")[-1].split("_")[:-2:]).split(chr(45))[1])
# print(files_list.replace('[', '').replace(']', '').replace(',', '').replace('\\', '').replace('"', '').replace('\'', ''))
# print(files_list)
# files_list = files_list.replace('[', '').replace(']', '').replace(',', '').replace('\\', '').replace('"', '').replace('\'', '')+'\n'
# print(files_list)
for line in sorted(file_list):
    file.write(line+"\n")

file.close()
