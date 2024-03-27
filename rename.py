import os
import re

files = os.listdir("./data")
os.chdir("./data")

for file in files:
    os.rename(file, "Saaransh_" + re.match("WhatsApp\sChat\swith\s(.+)", file).group(1))
