import re
workingdir = input("Please enter your working directory. Example: /mnt/c/Users/josep/Desktop/ --> ")
filename = input("Please enter your file name --> ")
fileopen = open(workingdir + filename, "r")
fileread = fileopen.read()
items = re.findall(' (.*)</span>', fileread)
fileopen.close()
with open(workingdir + "updated.log", 'w') as filewopen:
    for item in items:
        filewopen.write("%s\n" % item)
#filewopen = open(workingdir + "updated.csv", "w")
#filewopen.write(items)
#filewritewopen.close()
print("Please check your working directory to ensure an updated.log file was created and has info in it.")
