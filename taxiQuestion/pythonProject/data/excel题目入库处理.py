from openpyxl import load_workbook


def getExcelTestData(self, excel_path):
    # 打开 excel 文件，获取数据列表
    openExcelFile = load_workbook( excel_path )
    # 读取第一 sheet 页的数据
    getSheet = openExcelFile.active
    # 获取工作表
    dataList = []
    # 数据List
    for row in getSheet.rows:
        list1 = []
        for cell in row:
            if cell.value == None:
                cell.value = ""
            list1.append( cell.value )
        dataList.append( list1 )
    dataList.pop( 0 )
    return dataList