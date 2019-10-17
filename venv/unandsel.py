# coding=utf-8
import unittest
from time import sleep
from selenium import webdriver
import HTMLTestRunner


class YouJiuyeTest(unittest.TestCase):
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.get("http://xue.ujiuye.com/foreuser/login/")
        print("1")

    def test_login_password(self):
        username_d1 = self.chrome.find_element_by_id("username_dl")
        password_dl = self.chrome.find_element_by_id("password_dl")
        button = self.chrome.find_elements_by_class_name("lamination1")
        print('2')
        username_d1.send_keys("13331153361")
        password_dl.send_keys("123")
        button[0].click()
        print('3')
        text = self.chrome.find_element_by_id("J_usernameTip").text
        print(text)
        self.assertEqual("密码应该为6-20位之间！", text, "密码太短提示内容有误")
        print("333")

    def test_login_username(self):
        username_d1 = self.chrome.find_element_by_id("username_dl")
        password_dl = self.chrome.find_element_by_id("password_dl")
        button = self.chrome.find_elements_by_class_name("loginbutton1")
        print("4")
        username_d1.send_keys("13331153361")
        password_dl.send_keys("123456789")
        button[0].click()
        print("44444")
        sleep(2)
        text = self.chrome.find_element_by_id("J_usernameTip").text
        print(text)
        self.assertEqual("账号不存在", text, "提示内容有误")

    def tearDown(self):
        sleep(10)
        self.chrome.close()
        print("6")


if __name__ == '__main__':
    test_suite = unittest.TestSuite()  # 创建一个测试集合
    # test_suite.addTest(MyTest('test_run1'))#测试套件中添加测试用例
    test_suite.addTest(unittest.makeSuite(YouJiuyeTest))  # 使用makeSuite方法添加所有的测试方法
    fp = open('res2.html', 'wb')  # 打开一个保存结果的html文件

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='api测试报告', description='测试情况')
    # 生成执行用例的对象
    print("1")
    runner.run(test_suite)
    # 执行测试套件
    print("结束")
