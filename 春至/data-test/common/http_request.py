import requests
import logging
from common import my_logger


class HttpRequest:
    def http_request(self, url, request_data, method, cookies, headers):

        if method.lower() == 'get':
            try:
                res = requests.get(url, request_data, cookies=cookies, headers=headers)
            except Exception as e:
                logging.error('get请求出错了，错误是：{0}'.format(e))
                raise e
        elif method.lower() == 'post':
            try:
                res = requests.post(url, request_data, cookies=cookies)
            except Exception as e:
                logging.error('post请求出错了，错误是：{0}'.format(e))
                raise e
        else:
            return '参数方式错误'
        return res


if __name__ == '__main__':
    from common.do_sign import DoSign
    cookies = {}
    url = 'http://47.114.175.98:8080/api/team'
    param = {'game_id': 1, 'is_hot': 1, 'limit': 50, 'begin_id': 0, 'time_stamp': 1595476114}
    header = {'Sign': DoSign().get_sign(param)}
    res = HttpRequest().http_request(url, param, 'get', cookies, header)
    print(res.json())