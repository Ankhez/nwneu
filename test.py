# -*- coding: utf-8 -*-
import Tkinter
import json

c = {None: "хер"}
print type(c)
with open("data.json", "w+") as f:
    json.dump(c, f, ensure_ascii=False)
