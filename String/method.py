# methods

# lower()-It convert upper case string onto lower case
name="NIGAM"
print(name.lower()) 
""" ans-nigam"""

# upper()-It convert lower case sting into upper case
txt="nigam"
print(txt.upper()) 
"""ans-NIGAM"""

# capitalize()-It convert lower/upper case sting into capitalize 
word="nigam"
print(word.capitalize())
"""ans-Nigam"""

# strip()-it basicaly used for delete the space from starting and ending drom a string
string="   Nigam Bisoyi   "
print(string)  #ans-   Nigam Bisoyi   
print(string.strip()) #ans-Nigam Bisoyi

# replacewith()-it replace the string 
msg=" i love java"
print(msg.replace("java","python"))

# startswith()-it will check the string that the string start with given string or not (return-boolian)
url="https://google.com"
print(url.startswith("https"))

# endswith()-it will check the string that the string end with with given string or not (return-boolian)
email="nigam.bisoyi@gmail.com"
print(email.endswith("in"))