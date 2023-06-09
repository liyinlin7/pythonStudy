import requests
import json


class request_SG(object):
    '''
        补充赛果接口
    '''
    def csgo_reuqes_sg(self, ex_id, status=0):  # 0是测试环境
        '''
        CSGO补充赛果接口
        :param self:
        :param id: ex_id
        :param status: 0是测试环境
        :return:
        '''
        if status == 0:
            url = "47.114.172.33:5000"
        else:
            url = "8.210.97.229:5000"
        base_url = "http://"+url + "/csgo/result"
        print(base_url)
        data = {"ids": [{"id": int(ex_id), "stage": [1, 2, 3, 4, 5]}], "type": 1}
        r = requests.post(url=base_url, json=data)
        print(r.text)
        assert r.status_code == 200 and r.json()["status"] == "success", "系列赛ID" + str(ex_id) + "请求CSGO补充赛果接口失败"
        return True

    def lol_reuqes_sg(self, ex_id, status=0):  # 0是测试环境
        '''
        CSGO补充赛果接口
        :param self:
        :param id: ex_id
        :param status: 0是测试环境
        :return:
        '''
        if status == 0:
            url = "47.114.172.33:5000"
        else:
            url = "8.210.97.229:5000"
        base_url = "http://"+url + "/lol/matches"
        print(base_url)
        data = {"ids": [{"id": int(ex_id), "stage": [1, 2, 3, 4, 5]}], "type": 1}
        r = requests.post(url=base_url, json=data)
        print(r.text)
        assert r.status_code == 200 and r.json()["status"] == "success", "系列赛ID" + str(ex_id) + "请求LOL补充赛果接口失败"
        return True


# if __name__ == '__main__':
    # request_SG1 = request_SG()
