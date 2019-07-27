import smtplib  # 导入邮件服务器
from email.mime.text import MIMEText  # 支持HTML格式的邮件
from you_jian_fa_song.configTool import configTool
from email.utils import formataddr  # 格式化邮件消息头，不把自己的发送的邮件当成垃圾邮件


class emailTool(object):

    def __init__(self):
        self.conf = configTool()
        # 发件人的邮箱账号
        self.conf.buid(r'D:\Python项目\自动化学习项目\Python24-09\you_jian_fa_song\config.ini')
        #                   读取当前文件位置               这个拼接不对
        # self.conf.buid(self.conf.getCurrentPath() + r"\..\config.ini")
        self.sender = self.conf.get('email', 'sender')
        self.password = self.conf.get('email', 'password')
        # 用 逗号 截取多个需要发送的邮箱
        self.receiver = self.conf.get('email', 'receiver').split(',')

    def _domail(self, subject, context, type):
        try:
            msg = MIMEText(context, type, 'utf-8')
            msg['from'] = formataddr(["发件人", "utf-8"])
            msg['To'] = formataddr(["收件人", "utf-8"])
            # 邮件标题
            msg['subject'] = subject

            # 邮件固定格式
            # 创建服务器                 服务器名字   端口号
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)
            # 登录
            server.login(self.sender, self.password)
            # 传输文件的格式                 收件人地址   字符串格式
            server.sendmail(self.sender, self.receiver, msg.as_string())
            server.quit()
        except:
            return False
        return True

    def doMail_html(self, subject, context):
        return self._domail(subject, context, 'html')

    def doMail_text(self, subject, context):
        return self._domail(subject, context, 'plain')


if __name__ == '__main__':
    t = emailTool()
    print(t.doMail_html("lebo", '哈哈'))
    print(t.doMail_text("好威", 'heihei'))
