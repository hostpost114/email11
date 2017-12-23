from POM.Testcase import *
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
def sendReport(file_path):
    sendfile=open(file_path, 'rb').read()##读取测试报告路径
    msg = MIMEText(sendfile,'base64', 'utf-8')
    msg['Content-Type']='application/octet-stream'
    msg['Content-Disposition']='attachment;filename=test.html'#test.html为邮件附件名称
    msgRoot=MIMEMultipart('related')
    msgRoot.attach(msg)
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = '1552904****.com'  # 发件地址
    msg['To'] = 'lixianghah***.com'  # 收件人地址，多人以分号分隔
    smtp = smtplib.SMTP('smtp.163.com',25)
    smtp.set_debuglevel(1)
    smtp.login('1552904****@163.com', 'li****')  # 登录邮箱的账户和密码
    smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())
    smtp.quit()
    print('test report has send out!')
def newReport(testReport):
    lists = os.listdir(testReport)#返回测试报告所在目录下的所有文件列表
    lists2 = sorted(lists)#获得按升序排序后的测试报告列表
    file_new = os.path.join(testReport, lists2[-1])#获取最后一个即最新的测试报告地址
    print(file_new)
    return file_new
if __name__=="__main__":
    suit =unittest.TestSuite()
    x=[Touch('test000'),Touch('test001'), Touch('test002')]
    suit.addTests(x)
    # test_dir = 'E:\\unittest\\POM'  # 测试用例所在目录
    test_report = 'E:\\unittest\\POM'  # 测试报告所在目录
    # suit.addTest(MyTestCase('test_something'),MyTestCase('test_wec'))
    runner = unittest.TextTestRunner(verbosity=2)
    f =open('test.html','wb')
    runner =HTMLTestRunner(stream=f,
                           title=u'测试报告',
                           description=u'测试用例执行情况')
    runner.run(suit)
    new_report = newReport(test_report)  # 获取最新报告文件
    sendReport(new_report)  # 发送最新的测试报告
    # sendReport(newReport(te
    # -st_report))