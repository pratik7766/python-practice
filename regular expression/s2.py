import re
pattern=r"object"
text="C++ is object orented programming"
result=re.search(pattern,text)
print(result)