import pandas as pd
import datetime
import os
pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 20)
#
# df = pd.read_csv('nyc_taxi_sample.csv')
# df.describe()
# df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
# datetime_value = df['pickup_datetime'].apply(lambda i: i.strftime('%Y-%m'))
#
# # 取得各日期
# datetime_uni = datetime_value.unique()
# dir = 'dataset2019'
# os.makedirs(dir)
# for item in datetime_uni:   # datetime_uni內的項目為字串，這裡將字串轉乘datetime格式
#     time = datetime.datetime.strptime(item, '%Y-%m')
#     year = time.year  # 取得年
#     month = time.month  # 取得月
#     con = df['pickup_datetime'].dt.year == year  # 條件一
#     con1 = df['pickup_datetime'].dt.month == month  #條件二
#     select = df[con & con1]  # 選擇對應年、月的資料
#
#     # 檔案命名
#     filename = dir + '/' + str(year) +'-'+ str(month) + '.csv'
#
#     # 輸出檔案
#     select.to_csv(filename, encoding='utf-8', index=False)

df = pd.read_csv('dataset2019/2014-2.csv')
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['date'] = df['pickup_datetime'].dt.date
date_group = df.groupby('date')
# print(date_group.size())

df['day of week'] = df['pickup_datetime'].dt.dayofweek
day_of_week_group = df.groupby('day of week')  # Monday = 0,Sunday = 6
print(day_of_week_group.size())