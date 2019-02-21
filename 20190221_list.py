mathScores = [60, 70, 10, 20, 81, 63, 4]
print(mathScores[2])
print(mathScores[2:6])
print(mathScores[-1])
print(mathScores[:5])
print(mathScores[2:])
print(len(mathScores))
print(sum(mathScores))
print(max(mathScores))
print(min(mathScores))
print(sum(mathScores)/len(mathScores))

# --------------

ls = []
ls.append(2)
ls.append(3)
ls.append('5')
ls.append(10)
ls.insert(2, 99)
print(ls)


del ls[1:4]
print(ls)
ls.remove(10)
print(ls)
ls[0] = 99
print(ls)
print(99 in ls)
print(ls.count(99))

ls1 = ['a', 'b', 'c', 'd']
ls2 = [1, 2, 3, 4]
print(ls1 + ls2)
# -----------

ls3 = [[1, 3], [6, 5], 0, 3]
print(ls3[0])   # 第一個[0]讀外層的值
print(ls3[0][0])   # 第二個[0]讀內層的值

# -------課堂練習

grades = [[5, 14, 7], [23, 36, 28], [88, 80, 92]]
print(grades[2])
chinese = sum(grades[0])/len(grades[0])
english = sum(grades[1])/len(grades[1])
math = sum(grades[2])/len(grades[2])
print(chinese)
print(english)
print(math)
grades.append([94, 90, 96])
print(grades)


