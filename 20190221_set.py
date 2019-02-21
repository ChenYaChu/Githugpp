fruits = {'apple', 'banana', 'guava', 'guava'}
print(fruits)
print(len(fruits))
print('pineapple' in fruits)

fruits1 = {'strawberry', 'papaya', 'banana'}
print(fruits | fruits1)   # 聯集
print(fruits.intersection(fruits1))   # 交集
print(fruits & fruits1)   # 交集
print(fruits-fruits1)   # 差集

fruits.add('watermelon')
fruits.remove('apple')
fruits.discard('apple')
fruits1.clear()
print(fruits1)
print(fruits)

# ------課堂練習
allStudents = {'John', 'Eva', 'Jill', 'Eric', 'Andy', 'Albert', 'Polina', 'Kristin', 'Angela'}
danceClub = {'John', 'Eva', 'Jill', 'Eric','Andy'}
guitarClub = {'Eric', 'Andy', 'Polina', 'Kristin', 'Albert'}

print('兩個都有參加的', danceClub & guitarClub)
print('參加吉他沒有熱舞的', guitarClub-danceClub)
print('都沒有參加的', allStudents-(danceClub | guitarClub))