from typing import Any, Union

family = {'dad': 'homar',
          'mom': 'marge',
          'son': 'bart',
          'daughter': 'lisa'}

print(family['dad'])
print(family.get('dad'))
print('dad' in family)
print('cousin' in family)

family.update({'uncle': 'john', 'cousin': 'mary'})
print(family)
family['dad'] = 'Andy'
print(family)

print(family.keys())
print((family.values()))
print(family.items())

print(family.pop('dad'))
print(family)
# ---------課堂練習
gradesDict = {'chinese': [5, 14, 7],
              'english': [23, 36, 28],
              'math': [94, 90, 96]}

mathsc = gradesDict['math']
print(mathsc)
chinesesc = gradesDict['chinese']
englishsc = gradesDict['english']
avgchin = sum(chinesesc)/len(chinesesc)
avgeng = sum(englishsc)/len(englishsc)
avgmath: Union[float, Any] = sum(mathsc)/len(mathsc)
print(avgchin, avgeng, avgmath)
gradesDict.update({'scinece': [94, 90, 96]})
print(gradesDict)
