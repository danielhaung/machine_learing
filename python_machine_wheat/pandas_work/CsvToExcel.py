#https://blog.csdn.net/qq_33689414/article/details/78307031
#pip  install openpyxl  安裝 openpyxl https://blog.csdn.net/aic1999/article/details/79825982
import pandas as pd

def csv_to_xlsx_pd():
    csv = pd.read_csv('food_info.csv', encoding='utf-8')
    csv.to_excel('food_info.xlsx', sheet_name='data')


if __name__ == '__main__':
    csv_to_xlsx_pd()




#!!!!!!!!!!!!!!!!!無法使用!!!!!!!!!!!!!!
#################################################################################################
# import csv
# #pip install xlwt  這是一個供開發人員用來生成與Microsoft Excel 95到2003版兼容的電子表格文件的庫
# import xlwt  

# def csv_to_xlsx():
#     with open('food_info.csv', 'r', encoding='utf-8') as f:
#         read = csv.reader(f)
#         workbook = xlwt.Workbook()
#         sheet = workbook.add_sheet('data')  # 创建一个sheet表格
#         l = 0
#         for line in read:
#             print(line)
#             r = 0
#             for i in line:
#                 print(i)
#                 sheet.write(l, r, i)  # 一个一个将单元格数据写入
#                 r = r + 1
#             l = l + 1

#         workbook.save('food_info.xlsx')  # 保存Excel



# if __name__ == '__main__':
#     csv_to_xlsx()

#################################################################################################




