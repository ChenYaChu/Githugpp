import pandas as pd

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 20)
#
# df = pd.read_json('df.json')
# print(df.shape)
# print(df.describe())
# print(df.head(10))
# print(df.tail())
# print(df.loc[:, 'speed'])

# ls = [1, 2, 3, 4]
# new_df = pd.DataFrame(ls)
# print(new_df)
# df.append(new_df)
# print(df.loc[:, 'new_df'])
# 練習

df = pd.read_json('df.json')
df1 = df[df['volume'].between(60, 180)]
# print(df1)
df2 = df[df['datacollecttime'] == '2018-11-01 04:00:00']
# print(df2)
df3 = df[df['laneoccupy'] > 2.0]
# print(df3)
xx = df.sort_values(by='volume', ascending=True)
# df4 = xx['volume'].head(5)
print(xx.head(5))
