import os
from  commonclass.readexcel import doExcel
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(current_dir)


class createtest():
    def mkdir(testFileName,pyName):
        path = parent_path+'\\'+'testcase'+'\\'+testFileName
        floder = os.path.exists(path)

        if not floder:
             os.makedirs(path)
             print("-----目录创建成功！----")
             print(path)
        else:
             print("-----目录已存在！----")
             print(path)


        print("--------------------------")


        pypath =path+'\\'+"test_"+pyName+".py"
        floder1 = os.path.exists(pypath)

        if not floder1:
            f=open(pypath,"w")
            f.close()
            print("------正在创建py文件—————")
            print("------创建py文件成功---------")
            print(pypath)
        else:
            print("文件已存在")
            print(pypath)
        fd=open(pypath,"w",encoding='utf-8')
        fd.write("import unittest\n")
        fd.write("from  commonclass.http1 import http2\n")
        fd.write("from  commonclass.readexcel import doExcel\n")
        fd.write("import  parameterized\n")
        # header='ssss'
        # fd.write(header)
        # url='ssss'
        # fd.write(url)
        # str='sss'
        # fd.write(str)
        # fd.close()
        # data =str(doExcel.getData("test","listHomeworkDesc2"))
        fd.write("data = doExcel.getData('test','listHomeworkDesc2')\n")
        fd.write( "class Mytest(unittest.TestCase):\n")
        fd.write("      def setUp(self):\n")
        fd.write("          print('**************本次接口测试开始*************')\n")
        fd.write("      def tearDown(self):\n")
        fd.write("          print('**************本次接口测试结束*************')\n")
        fd.write( "      @parameterized.parameterized.expand(data)\n"
                 +"      def test(self,casename,db,sql,url,method,params,Except):\n"
                 +"         res = http2.testHttp(casename,db,sql,url,method,params,Except)\n"
                 +"         if Except=='1':\n"
                 +"                self.assertEquals(1,1)\n"
                 +"                print('预期与结果相同，测试通过！')\n"
                 +"         else:\n"
                 +"                self.assertIn(Except,res.text,msg='预期与结果不一致，测试失败')\n"
                 +"if __name__ == '__main__':\n"
                 +"    unittest.main()\n")


if __name__== '__main__':
    createtest.mkdir('test','listHomeworkDesc')



