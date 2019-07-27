from you_jian_fa_song.emailTool import emailTool, MIMEText
import psutil, os

# process and system utiliter

# 获取主机名字
host = os.popen("hostname").read().strip()
# 获取CPU个数
cpu = psutil.cpu_count()
msg = """
            <table color="CCCC33" width="800" BORDER="10" CELLPADDING="5" text-align="center">
                <tr>
                    <td text-align="center">name</td>
                    <td text-align="center">name</td>
                    <td >haha</td>
                    <td >heihie</td>
                    <td >ehhehe</td>
                </tr>
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>asdas</td>
                    <td>sadas</td>
                    <td>hahah</td>
                </tr>
        
            </table>
        """ % (host, cpu)
t = emailTool()
print(msg)
print(t.doMail_html("lebo", msg))
print("邮件内容： %s， %s" % (host, cpu))
# print(t.doMail_text("好威", 'heihei'))
