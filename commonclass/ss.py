import  os
import xlrd
import  json
from commonclass.readConfig import readConfig
import unittest

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.dirname(current_dir)
path = parent_path + '\\testfile' + '\\test'+'\\listHomeworkDesc.xls'
# path = parent_path+'\\'+'testcase'+'\\'+'test'
# caselistfile = os.path.join(parent_path,"caselist.txt")
# casefile = os.path.join(parent_path,"testcase")
# caselist= []
# print("1:"+caselistfile)
# fb = open(caselistfile)
# # fb.readlines()
# for value in fb.readlines():
#     data =str(value)
#     caselist.append(data.replace("\n",""))
# print("2:"+str(caselist))
# test_suite= unittest.TestSuite()
# suite_moudel=[]
# for case in caselist:
#     casename = case.split("/")[-1]
#     print(casename+'.py')
# discover =unittest.defaultTestLoader.discover(casefile,pattern=casename+".py",top_level_dir=None)
# # suite_moudel.append(discover)
# # print('suite_module:'+str(suite_moudel))
# print(discover)
# for suite in discover:
#     for casename in suite:
#         test_suite.addTest(casename)
#         print("3:"+ str(suite))
#         print("4:"+str(casename))
# runner= unittest.TextTestRunner()
# runner.run(test_suite)





excel = xlrd.open_workbook(path)
sheet = excel.sheets()[0]
cls = []
nrows = int(sheet.nrows)
i = 1
while i < nrows:
    cls.append(sheet.row_values(i))
    i = i + 1
    # list= [[1.0, '登陆', '', ' http://ip.taobao.com/service/getIpInfo.php?ip=2', '{}', '"ip":"2"1111'], [2.0, '正常请求', "kkl_tai#update tai_teacher_auth set subject_id=1 and subject_name='语文' where id=212;\nkkl_tai#select from a where name=c", 'http://www.baidu.com', '  { "param": "{\\"loginInfo\\":{\\"password\\":\\"e10adc3949ba59abbe56e057f20f883e\\",\\"loginName\\":\\"jacky001\\",\\"rememberMe\\":true,\\"deviceId\\":\\"111111\\"}}",\n    "service_name": "authservice.LoginServiceFacade.login",\n    "sign": "5A5462338475E9FEB62E5AF223F865F1",\n    "secret_state": "9929FCCA656CBD149999F1E28DB023D7",\n    "strategy": "dubbo",\n    "client_id": "1","token":"{token}"}', "message': '网关处理请求发生异常，请联系管理员！1'"], [3.0, '删除数据', '', 'http://www.baidu.com', '{\n"token":"{token}"\n}', '1']]
    print(cls)
    x=len(cls)
    i = 1
    dic = {i: cls[i - 1]}
    print(dic)
    while i <= x:
        dic[i] = list[i - 1][5]
        i = i + 1
    print(dic)
    x = len(list)
    i = 1
    dic = {i: list[i-1]}
    print(dic)


