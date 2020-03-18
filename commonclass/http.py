import requests
import json
from commonclass.DB import sqlclass
class http():
    def sendpost(URL,params,header,timeout):
        try:
            if params =='':
                return
            else:
                xparams = json.loads(params)
                print("请求地址"+URL)
                print("请求参数"+params)
                respose = requests.post(url=URL,params=xparams,headers=header,timeout=timeout)
                return respose
        except:
            print("请求失败")

    def gethttp(URL):
        respose = requests.get(URL)
        return  respose
    def gettoken(x):
        if x is None:
            return
        else:
            dic = json.loads(x)
            token = dic["data"]["token"]
            return  token


    def testHttp(casename,db,sql,url,params,Except):
        sqlclass.ExcuteSql(db,sql)
        caseName = casename
        Except = Except
        header = {'Content-Type': 'application/json'}
        print("用例名称"+caseName)
        respose = http.sendpost(url,params,header,15)
        print("实际结果"+respose.text)
        print("预期结果"+Except)
        return  respose



