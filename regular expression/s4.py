import re
pattern=r"programming"
text="C++ is object orented programming"
result=re.sub(pattern," ",text)
print(result)