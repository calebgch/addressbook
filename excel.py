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


