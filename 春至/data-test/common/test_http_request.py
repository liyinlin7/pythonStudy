import unittest
import logging
import time
from common import my_logger
from ddt import ddt, data
from common.http_request import HttpRequest
from common.do_excel import DoExcel
from common import read_path
from common.deal_with_data import DealWithData
from common.do_mysql import DoMySql
from common.do_sign import DoSign

COOKIES = {}
DoExcel(read_path.test_data_path).clear_test_data('test_data')  # 清除测试结果
test_data = DoExcel(read_path.test_data_path).get_test_data('test_data')


@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        self.t = DoExcel(read_path.test_data_path)
        self.cnn = DoMySql().connect()

    def tearDown(self):
        self.cnn.close()
        logging.info('关闭数据库连接---------')

    def main_process(self, item, sheet_name):
        # 1、HTTP请求
        run_flag = True
        final_res = []
        fail_msg = ''
        param = eval(item['Param'])
        while run_flag:
            param['time_stamp'] = int(time.time())
            logging.info('请求参数是：{}'.format(str(param)))
            sign = {'Sign': DoSign().get_sign(param)}
            response = HttpRequest().http_request(item['Url'], param, item['Method'], COOKIES, sign)
            res = response.json()
            # 判断每次请求是否成功
            if item['Expected'] == res['code']:
                http_check = 'PASS'
                self.t.write_back(item['Case_Id'] + 1, 8, http_check, sheet_name)
            else:
                logging.error('请求失败，请求结果是：{}'.format(res))
                http_check = 'FAIL'
                fail_msg += 'http请求失败\n'
                self.t.write_back(item['Case_Id'] + 1, 8, http_check, sheet_name)
                break

            final_res += res['result']
            # 如果请求数量少于limit，请求结束
            if len(res['result']) < param['limit']:
                run_flag = False
            else:
                # 更新begin_id
                begin_id = res['result'][-1]['id'] + 1
                param['begin_id'] = begin_id

        # 2、处理接口返回数据
        logging.info('开始处理接口返回数据---------')
        final_res = DealWithData().sort_li(final_res, 'id')
        if item['AddDict']:
            final_res = DealWithData().sort_dic(final_res, eval(item['AddDict']))

        # 3、获取数据库数据
        logging.info('开始获取并处理数据库数据---------')
        if item['AddDict']:     # 组装参数
            sql_res = DealWithData().package_dic(item['SqlCheck'], eval(item['AddDict']), cnn=self.cnn)
        else:
            sql_res = DoMySql().select(self.cnn, item['SqlCheck'])
        if item['TransDic']:    # 替换为对应代码
            sql_res = DealWithData().trans_name(sql_res, eval(item['TransDic']))

        # 4、数据量对比
        logging.info('开始进行数据量对比---------')
        if len(final_res) == len(sql_res):
            # 数据量一致进入下一步
            count_check = 'PASS'
            # 5、数据正确性对比
            logging.info('开始进行数据正确性对比---------')
            fail_msg_data = ''
            for i in range(len(final_res)):
                if str(final_res[i]) == str(sql_res[i]).replace(" ", ""):
                    continue
                else:
                    msg = 'id为{0}的数据校验不一致\n接口数据：\n{1}\n数据库数据：\n{2}'.format(final_res[i]['id'], final_res[i], sql_res[i])
                    fail_msg_data += msg + '\n'
            if not fail_msg_data:
                data_check = 'PASS'
            else:
                data_check = 'FAIL'
            fail_msg += str(fail_msg_data)
            self.t.write_back(item['Case_Id'] + 1, 10, data_check, sheet_name)

        else:
            # 数据量不一致，测试不通过，结果写回
            count_check = 'FAIL'
            fail_msg += '数据量不一致：接口数据量为{}，数据库数据量为{}\n'.format(len(final_res), len(sql_res))
        self.t.write_back(item['Case_Id'] + 1, 9, count_check, sheet_name)
        return fail_msg

    def replace_param(self, item, key, fail_msg):
        # 如果请求参数中包含关键字，则先获取关键字id列表，然后进行参数替换
        # 1、获取关键字id列表
        key_sql = item['KeySql']
        res_key_ids = DoMySql().select(self.cnn, key_sql)
        key_ids = [i['id'] for i in res_key_ids]

        # 参数替换
        item_list = []
        for i in range(len(key_ids)):
            new_item = item.copy()
            # 1、替换请求参数
            new_item['Param'] = new_item['Param'].replace(key, str(key_ids[i]))
            # 2、替换sql
            new_item['SqlCheck'] = new_item['SqlCheck'].format(key_ids[i])
            item_list.append(new_item)
            fail_msg += self.main_process(item_list[i], 'test_data')
        return fail_msg

    @data(*test_data)
    def test_api(self, item):
        logging.info('正在执行第{0}条用例：{1}'.format(item['Case_Id'], item['Title']))
        logging.info('发起请求的地址是：{0}'.format(item['Url']))

        fail_msg = ''
        # 判断请求参数中是否包含${team_id}
        if item['Param'].find('${team_id}') != -1:
            fail_msg = self.replace_param(item, '"${team_id}"', fail_msg)
        elif item['Param'].find('${league_id}') != -1:
            fail_msg = self.replace_param(item, '"${league_id}"', fail_msg)
        elif item['Param'].find('${series_id}') != -1:
            fail_msg = self.replace_param(item, '"${series_id}"', fail_msg)
        else:
            fail_msg += self.main_process(item, 'test_data')

        # 判断测试结果，如果fail_msg不为空，则运行不通过
        # logging.info('--------------失败原因-----------------')
        # logging.info(fail_msg)
        # logging.info('--------------失败原因-----------------')
        if not fail_msg.replace('\n', ''):
            test_result = 'PASS'
        else:
            test_result = 'FAIL'

        try:
            self.assertEqual(test_result, 'PASS')
        except Exception as e:
            logging.error('出错了，错误是' + fail_msg)
            raise e
        finally:
            self.t.write_back(item['Case_Id'] + 1, 11, fail_msg, 'test_data')
            self.t.write_back(item['Case_Id'] + 1, 12, test_result, 'test_data')
