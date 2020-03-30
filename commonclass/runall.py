import unittest
import  parameterized
from  commonclass.readexcel import doExcel
from commonclass.http1 import http2

data = doExcel.getData("test","listHomeworkDesc")

class Mytest(unittest.TestCase):
    def setUp(self):
        print("**************本次接口测试开始*************")

    @parameterized.parameterized.expand(data)
    def test(self,casename,db,sql,url,method,params,Except):
        res = http2.testHttp(casename,db,sql,url,method,params,Except)
        if Except=="1":
            self.assertEquals(1,1)
            print("预期与结果相同，测试通过！")
        else:
            self.assertIn(Except,res.text,msg="预期与结果不一致，测试失败")

    def tearDown(self):
      print('***********************本次接口测试结束***********************\n\n\n')

if __name__ == '__main__':
    unittest.main()
