from openpyxl import load_workbook

# def getExcelTestData(excel_path):
#     from xlrd import open_workbook
#     # 打开 excel 文件，获取数据列表
#     openExcelFile = open_workbook(excel_path)
#     # 读取第一 sheet 页的数据
#     getSheet = openExcelFile.sheets()[0]
#     # 获取工作表
#     rowNumber = getSheet.nrows
#     # 获取行数
#     dataList = []
#     # 数据List
#     for i in range(1, rowNumber):
#         # 从第二行开始遍历每一行
#         dataList.append(getSheet.row_values(i))
#         # 把每个单元格的数值存放到dataList中
#     print(dataList)
#     return dataList


def read_excel(xls_name):
    worksheet = load_workbook(xls_name)
    ws = worksheet.active
    ddts = []
    for row in ws.rows:
        list1 = []
        for cell in row:
            if cell.value == None:
                cell.value = ""
            list1.append(cell.value)
        ddts.append(list1)
    ddts.pop(0)
    print(ddts)

if __name__ == "__main__":
    read_excel(r"E:\gitlab\t-locationpc\data\requireements_excedValues\场地需求之活动信息.xlsx")
    # getExcelTestData(r"E:\gitlab\t-locationpc\data\requireements_excedValues\场地需求之活动信息.xlsx")
