# ---------課堂練習1
#x = int(input('輸入元直徑'))
#print(((x/2)**2)*3.14)

score = [10, 30, 40, 90, 100, 60]
ss = sum(score)
print(round(ss/5))

score[0] = round(score[0]**0.5*10)
score[1] = round(score[1]**0.5*10)
score[2] = round(score[2]**0.5*10)
score[3] = round(score[3]**0.5*10)
score[4] = round(score[4]**0.5*10)
score[5] = round(score[5]**0.5*10)
print(score)

# ----------------

x = 10
y = 6
print(x <= y)
a = 28
b = 8
print(x <= y and a >= b)
print(x <= y or a >= b)

# -------
high = int(input('請輸入身高'))
sex = str(input('請輸入性別(男生或女生'))
if sex == '男生' and high > 190:
    print('就打籃球吧')
elif sex == '女生' and high > 170:
    print('就打排球吧')
else:
    print('不用打球囉~')

num = int(input('請輸入數字'))
if num % 2 == 0:
    print('你輸入的是偶數')
else:
    print('你輸入的是奇數')
