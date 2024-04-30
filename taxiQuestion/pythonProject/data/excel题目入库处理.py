from openpyxl import load_workbook
from common import read_path
import os
from question_insert import QuestionInsert
import uuid

class insert_excel_data(object):
    """
        将数据入库
    """
    def __init__(self):
        self.pro_path = read_path.pro_path
        self.country_name = '全国题.xlsx'
        self.region_name = '区域题.xlsx'
        self.region_operation_name = '区域实操题.xlsx'
        self.question_insert = QuestionInsert()
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
                    try:
                        cell.value = ""
                    except:
                        pass
                list1.append( cell.value )
            dataList.append( list1 )
        return dataList
    def country_question_insert(self):
        excel_path = os.path.join( self.pro_path, 'data', self.country_name )
        dataList = self.getExcelTestData( excel_path )
        type = ''
        question_type = None
        for data in dataList:
            question_id = uuid.uuid4()
            if data[0]  is not None and data[1] is None  and data[2] is None:
                value = data[0]
                if '判断' in value:
                    question_type = 2
                    type = data[0].split('（')[0]
                elif '单选' in value:
                    question_type = 1
                else:
                    question_type = 0
            elif '答案' == data[1]:
                    continue
            else:
                question_answer = data[1]
                number = data[0]
                question_title = data[2]
                value_data = {
                    'question_id': question_id,
                    'question_answer': question_answer,
                    'number': number,
                    'question_title': question_title,
                    'question_type': question_type,
                    'range': 2,
                    'type': type
                }
                self.question_insert.question_insert( value_data )
    def region_question_insert(self):
        excel_path = os.path.join( self.pro_path, 'data', self.region_name )
        # 获取数据列表
        dataList = self.getExcelTestData( excel_path )
        type = ''
        question_type = None
        for data in dataList:
            question_id = uuid.uuid4()
            if data[0] is not None and data[1] is None and data[2] is None:
                value = data[0]
                if '判断' in value:
                    question_type = 2
                    type = data[0].split( '（' )[0]
                elif '单选' in value:
                    question_type = 1
                else:
                    question_type = 0
            elif '答案' == data[1]:
                continue
            else:
                question_answer = data[1]
                number = data[0]
                question_title = data[2]
                value_data = {
                    'question_id': question_id,
                    'question_answer': question_answer,
                    'number': number,
                    'question_title': question_title,
                    'question_type': question_type,
                    'range': 1,
                    'type': type
                }
                self.question_insert.question_insert( value_data )
    def region_operation_insert(self):
        excel_path = os.path.join( self.pro_path, 'data', self.region_operation_name )
        # 获取数据列表
        dataList = self.getExcelTestData( excel_path )
        type = ''
        question_type = None
        correct_answer = None
        for data in dataList:
            question_id = uuid.uuid4()
            if data[0] is not None and data[1] is None and data[2] is None:
                value = data[0]
                if '判断' in value:
                    question_type = 2
                    type = data[0].split( '（' )[0]
                elif '单选' in value:
                    question_type = 1
                elif '服务五句话' in value:
                    question_type = 3
                else:
                    question_type = 0
            elif '答案' == data[1]:
                continue
            else:
                question_answer = data[1]
                number = data[0]
                question_title = data[2]
                correct_answer = data[3]
                value_data = {
                    'question_id': question_id,
                    'question_answer': question_answer,
                    'number': number,
                    'question_title': question_title,
                    'question_type': question_type,
                    'correct_answer': correct_answer,
                    'range': 1,
                    'type': type
                }
                self.question_insert.operation_insert( value_data )

if __name__ == '__main__':
    insert_excel_data = insert_excel_data()
    # insert_excel_data.country_question_insert()
    # insert_excel_data.region_question_insert()
    # insert_excel_data.region_operation_insert()