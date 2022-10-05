# Detect double spaces in a String

from dataclasses import replace

str="I am learning python  currently"
doublespace=str.find("  ")
print(doublespace)

# Replace the double spaces with single spaces

str=(str.replace("  "," "))
print(str)