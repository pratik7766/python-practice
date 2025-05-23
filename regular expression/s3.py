import re
pattern=r"object"
text="C++ is object orented programming"
result=re.findall(pattern,text)
print(result)