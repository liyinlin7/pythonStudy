from selenium import webdriver
import os


# 创建截图方法
def insert_img(driver, filename):
    # 获取当前模块所在的路径
    # os.path.dirname(__file__):返回当前文件的上一级目录
    func_path = os.path.dirname(__file__)
    print("func_path:"+func_path)
    # 获取test_case目录
    base_dir = os.path.dirname(func_path)
    print("base_dir:"+base_dir)
    # 对路径的字符串进行替换
    base_dir = base_dir.replace('\\', '/')
    print("base_dir:"+base_dir)

    # 获取到上一级website的目录
    base1 = os.path.dirname(base_dir)
    print("base1:"+base1)
    # 获取项目文件的根目录路径
    base = base_dir.split('/Website')[0]
    print("base:"+base)
    # 指定截图存放路径
    # filepath = base+'/Website/screenshot/'+filename
    filepath = base1+"/screenshot/"+filename

    # 截图的方法
    driver.get_screenshot_as_file(filepath)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.sogou.com")
    insert_img(driver, "sogou2.png")
    driver.quit()
