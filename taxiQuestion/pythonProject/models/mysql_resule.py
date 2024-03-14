from sqlalchemy import inspect

def result_all_one(result):
    '''
     单表查询结果解析
    :param result:
    :return:
    '''
    dict_list = []
    for obj in result:
        inspector = inspect( type( obj ) )
        dict_row = {attr.key: getattr( obj, attr.key, None ) for attr in inspector.attrs}
        dict_list.append( dict_row )
    return dict_list

def result_leftjoin_all_many(result, fields_dict, table_names ):
    '''

    :param result:  查询的结果
    :param fields_dict: 辅表的字段集  {'useransewer': ['question_id', 'user_answer', 'answer_bool']}
    :param table_names: 链接查询的所有表明  ['questions', 'useranswer']
    :return:
    '''
    # 将结果转换为字典列表
    dict_list = []
    for row in result:
        objects = list( row )  # 将行数据转为列表
        dict_row = {}
        if row is not None:
            for obj, table_name in zip( objects, table_names ):  # 遍历列表中的每一个对象和对应的表名
                if obj is not None:  # 如果对象不为None，获取对象的所有字段值
                    inspector = inspect( obj )
                    for attr in inspector.attrs.keys():
                        dict_row[attr] = getattr( obj, attr, None )
                elif obj is None:  # 如果对象为None但表在fields_dict中
                    for table in table_names:
                        if fields_dict.get(table) is not None:
                            for field in fields_dict.get(table):  # 遍历对应表的字段列表
                                dict_row.setdefault(field, None)
            dict_list.append( dict_row )
    return dict_list
