"""
hw6.py by Haley Uyeunten
"""

a = r'[0-46-9]*5[0-46-9]*5[0-46-9]*'
b = r'([1-9]|1[0-2]):([0-5][0-9])\s(PM|AM)'
c = r'(?:(?:[^0-9]\w+,\s)*[^0-9]\w+)*'
d = r'(?:(?P<a>\w*)\s*<(?P<equal>=?)\s*(?P<b>\w*))+'
d_sub = r'\g<b> >\g<equal> \g<a>'

