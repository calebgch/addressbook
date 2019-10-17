import openpyxl
import json
from excel_reader import *


dict_yfzx = {"col_count": 5,
             "position": 0,
             "name": 1,
             "tel": 2,
             "mobile": 3,
             "office": 4
             }
dict_sjzx = {"col_count": 5,
             "position": 0,
             "name": 1,
             "office": 2,
             "tel": 3,
             "mobile": 4
             }
dict_gfgs = {"col_count": 4,
             "position": 0,
             "name": 1,
             "office": 2,
             "tel": 3,
             "mobile": 3
             }

dict_all = {"北京研发中心": dict_yfzx,
            "上海数据中心": dict_sjzx,
            "股份公司": dict_gfgs}

reader = ExcelReader("D:\\公司电话簿.xlsx", dict_all)
#reader.read_sheet("北京研发中心")
#reader.read_sheet("上海数据中心")
reader.read_sheet("股份公司")

reader.write_file("d:\\names.json")



#sheet4 = wb['SQL']
#for sheet in wb:
#    print(sheet.title)


#print(ws['A1']) # 获取A列的第一个对象
#print(ws['A1'].value)

#c = ws['B1']
#print('Row {}, Column {} is {}'.format(c.row, c.column, c.value)) # 打印这个单元格对象所在的行列的数值和内容
#print('Cell {} is {}\n'.format(c.coordinate, c.value)) # 获取单元格对象的所在列的行数和值
