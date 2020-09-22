import unittest
import  parameterized
from  commonclass.readexcel import doExcel
from commonclass.http1 import http2
import os

# data = doExcel.getData("test","listHomeworkDesc")
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(current_dir)
case_path = os.path.join(parent_path+"\\testcase")
class Mytest(unittest.TestCase):
    def __init__(self):
        self.caselistfile = os.path.join(parent_path,"caselist.txt")
        self.casefile = os.path.join(case_path,"test")
        self.caselist = []

    def set_case_list(self):
        fb = open(self.caselistfile)
        for value in fb.readlines():
                data = str(value)
                if data !="" and not data.startswith("#"):
                    self.caselist.append(data.replace("\n",""))
                fb.close()

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module=[]
        for case in  self.caselist:
            case_name = case.split("/")[-1]
            print(case_name+".py")
            discover =unittest.defaultTestLoader.discover(self.casefile,pattern=case_name+".py",top_level_dir=None)
            suite_module.append(discover)
            print('suite_module:'+str(suite_module))
        if  len(suite_module)> 0:
            for suite in  discover:
                for test_name in suite:
                    test_suite.addTest(test_name)

        else:
                print("无测试套件")
                return  None
        return test_suite
    def run(self):
        try:
            suit =self.set_case_suite()
            if suit is not None:
                print("正在执行接口测试")
            else:
                print("暂无可执行的用例")
        except Exception as ex:
            print(str(ex))


    # def setUp(self):
    #     print("**************本次接口测试开始*************")
    #
    #
    # @parameterized.parameterized.expand(data)
    # def test(self,casename,db,sql,url,method,params,Except):
    #     res = http2.testHttp(casename,db,sql,url,method,params,Except)
    #     if Except=="1":
    #         self.assertEquals(1,1)
    #         print("预期与结果相同，测试通过！")
    #     else:
    #         self.assertIn(Except,res.text,msg="预期与结果不一致，测试失败")
    #
    # def tearDown(self):
    #   print('***********************本次接口测试结束***********************\n\n\n')

if __name__ == '__main__':
    Mytest.run()
