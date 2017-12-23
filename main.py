from POM.Testcase import *
if __name__=="__main__":
    suit =unittest.TestSuite()
    x=[Touch('test000'),Touch('test001'), Touch('test002')]
    suit.addTests(x)
    # suit.addTest(MyTestCase('test_something'),MyTestCase('test_wec'))
    runner = unittest.TextTestRunner(verbosity=2)
    f =open('test.html','wb')
    runner =HTMLTestRunner(stream=f,
                           title=u'测试报告',
                           description=u'测试用例执行情况')
    runner.run(suit)
