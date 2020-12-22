# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import codecs


file = open("Wikibooks.txt")
temp = file.read()
file.close()

temp = temp.replace("<math>", "")
temp = temp.replace("</math>}}", "")
temp = temp.replace("</math>", "")
temp = temp.replace("{{Formel|", "")

temp = temp.replace("align", "array")
temp = temp.replace("OliveGreen", "208000")

file = open("Wikibooks.txt","w")
file.write(temp)
file.close()

#print(temp)

