import re

str1 = "Hello, World!"
match = re.match("Hello", str1)
if match:
    print("Match found")
else:
    print("No match found")