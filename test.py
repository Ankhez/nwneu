# -*- coding: utf-8 -*-
import Tkinter
import json

a = u'привет'
c = u'Иван'
b = {c: a}
print b
s = json.dumps(c, ensure_ascii=False)

print s
#print b


#print type(c)
#print c
