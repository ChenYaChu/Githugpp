tuple1 = (1, 2, 3, 4, 5)
tuple2 = '1', '2', '3', '4', '5'
tuple3 = (5, 9, 3, 5, 20, 97, 54, 63, 10)

print(tuple2[3])
print(tuple2.index('4'))
print(tuple2.count('3'))
print(tuple1 + tuple2)
print(sorted(tuple3))

tuple4 = ('lisa', 23, 'female')
name, age, sex = tuple4
print(name, age, sex)
print(tuple4[0:2])
tuple5 = ('a', 'b')
print(tuple4 + tuple5)

# -------------課堂練習

gradesTuple = ((5, 14, 7), (23, 36, 28), (88, 80, 92))
mathsc = gradesTuple[2]
print(mathsc)
chinesesc = gradesTuple[0]
englishsc = gradesTuple[1]
avgchin = sum(chinesesc)/len(chinesesc)
avgeng = sum(englishsc)/len(englishsc)
avgmath = sum(mathsc)/len(mathsc)
print(avgchin, avgeng, avgmath)

scinsc = ((94, 90, 96), )
print('加入自然成績後變成:', gradesTuple + scinsc)



