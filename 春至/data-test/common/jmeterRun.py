import os, sys

run_path = os.getcwd()


def jmeterRun():
    report_path = run_path + r'/Report'
    print(report_path)
    report_file = os.listdir(report_path)
    print(report_file)
    if 'WFX_AutomationReport.html' and 'WFX_AutomationReport.jtl' in report_file:
        print('文件存在，需要进行删除')
        os.remove(report_path + '/WFX_AutomationReport.html')
        os.remove(report_path + '/WFX_AutomationReport.jtl')
        print('文件删除成功，接下来将重新生成')
        os.system(r'cd ./common/megaJmeter/mega && ant')
    else:
        print("文件不存在，不需要删除")
        os.system(r'cd ./megaJmeter/mega && ant')


if __name__ == '__main__':
    jmeterRun()
