def remove_and_strip(string, word):
    newStr = string.replace(word,"")
    return newStr.strip()

    this = "   i am good    "
    remove_and_strip(this, good)