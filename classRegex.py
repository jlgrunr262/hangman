import re
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('All good men must come to the aid of THEIR BROTHERS')
print(mo)

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo1 = consonantRegex.findall('All good men MUST come to the aid of their BROTHERS')
print(mo1)
