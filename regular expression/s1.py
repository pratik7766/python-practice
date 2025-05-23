import re
pattern=r"C++"
text="C++ is object orented programming"
result=re.match(pattern,text)
print(result)