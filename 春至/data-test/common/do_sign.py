import hashlib
import base64
import rsa
import time
from common import read_path
from common.read_config import ReadConfig


class DoSign:

    def deal_param(self, param):
        """处理请求参数"""
        s = ''
        param['time_stamp'] = int(time.time())
        keys = sorted(list(param.keys()))
        for i in keys:
            s += i + '=' + str(param[i]) + '&'
        p_str = s.strip('&')
        m = hashlib.md5(p_str.encode()).hexdigest()
        return m

    def rsa_sign(self, content):
        """SHAWithRSA

        :param content: 签名内容
        :type content: str

        :return: 签名内容
        :rtype: str
        """
        # 获取环境flag
        env_flag = ReadConfig().read_config(read_path.conf_path, 'MODE', 'env_flag')
        if env_flag == '0':  # 如果是0，表示测试环境
            privateKey_path = read_path.privateKey_path
        else:   # 如果是1，表示生产环境
            privateKey_path = read_path.privateKeyPro_path
        with open(privateKey_path, 'rb') as f:
            read_key = f.read()
            pri_key = rsa.PrivateKey.load_pkcs1(read_key, format='PEM')
            sign_result = rsa.sign(bytes(content, encoding='utf-8'), pri_key, 'SHA-256')
            return base64.b64encode(sign_result)

    def get_sign(self, param):
        sign = self.rsa_sign(self.deal_param(param))
        return str(sign, encoding='utf-8')


if __name__ == '__main__':
    s = {'game_id': 1, 'limit': 100, 'begin_id': 770}
    # s = {'game_id': 1, 'match_id': 1301}
    aa = DoSign().get_sign(s)
    print(int(time.time()))
    print(aa)