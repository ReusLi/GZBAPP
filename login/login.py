
import warnings
import unittest
import HTMLTestReportCN
import time


class LoginTest(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = DriverClient().getDriver()

    # 验证用户登录
    def user_login(self, username, password):
        print('username=' + username)
        print('password=' + password)
        self.driver.find_element_by_id(
            'com.jiahe.gzb:id/input_phone_num').send_keys(username)
        self.driver.find_element_by_id(
            'com.jiahe.gzb:id/input_password').send_keys(password)
        self.driver.find_element_by_id('com.jiahe.gzb:id/btn_login').click()

    def test_login(self):
        openAppUtil.openapp(self.driver)

    def test_login0(self):
        # 用户名、密码为空登录
        self.user_login('', '')
        print('用户名密码为空时，测试通过')

    def test_login1(self):
        # 用户名正确,密码为空
        self.user_login('13813807003', '')
        print('用户名正确、密码为空时，测试通过')

    def test_login2(self):
        # 用户名为空,密码正确
        self.user_login('', '123456')
        print('用户名为空、密码正确时，测试通过')

    def test_login3(self):
        # 用户名密码正确
        self.user_login('13813807002', '123456')
        print('用户名密码正确时，测试通过')

    def tearDown(self):
        print('test finished')


if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    suite = unittest.TestSuite([suite1])

    #设置测试报告保存路径
    file_path = 'F:\\GZBAPP\\login\\a.html'
    #获取系统当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    #设置报告文件名称
    report_name = file_path + now + "Login_test_Report.html"

    fp = open(report_name, 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, tester='潘颖', title='login_report', description='report_description')
    runner.run(suite)
    fp.close()