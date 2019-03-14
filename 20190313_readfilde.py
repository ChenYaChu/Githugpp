# file_path = 'hello.txt'
# # f = open(file_path, 'r')  # 讀檔、w=寫檔
# # fr = f.read()
# # print(fr)
# # f.close()  # 關閉檔案
# #
# # # 寫入檔案
# # g = open(file_path, 'w')  # 開啟檔案
# # data = 'abc'  # 資料內容
# # g.write(data)  #
# # f.close()
# #可將以上用with代替
# with open(file_path, 'r') as f:
#     fr = f.read()
#     print(fr)
import csv
#
# file_path = 'df.csv'
#
# with open(file_path, 'r',encoding='utf-8') as csvfile:
#     rows = csv.DictReader(csvfile)
#
#     for row in rows:
#         print(row)

# members = [{'name': 'weihan',
#             'sex': 'f',
#             'height': 150
# }, {'name': 'lisa',
#     'sex': 'f',
#     'height': 160
# }, {'name': 'jack',
#     'sex': 'm',
#     'height': 180
# }]
# with open('scores.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['姓名', '性別', '身高'])
#     for item in members:
#         writer.writerow([item['name'], item['sex'], item['height']])
#
# import traceback
# file_path = 'abc.txt'
# data = ''
# try:
#     with open (file_path, 'r') as f:
#         fr = f.read()
#         print(fr)
#         data = fr
# # except Exception as e:
# #     print(e)
# #     print('some error')
# except:
#     traceback.print_exc()
#
# print(data)
