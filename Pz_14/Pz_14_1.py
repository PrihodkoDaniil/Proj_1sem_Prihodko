# Из исходного текстового файла (experience.txt) выбрать стаж работы.
# Посчитать количество полученных элементов.
import re
p=re.compile(r'\d.+')
with open('experience.txt','r',encoding='utf-8')as file:
     text = file.read()
     stage=re.findall(p,text)
     print(f'{stage}\nКоличество элементов: {len(stage)}')
