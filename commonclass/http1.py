import requests
import json
from commonclass.DB import sqlclass
class http2():
    def sendpost(URL,params,header,timeout):
        try:
            if params =='':
                return
            else:
                xparams = json.loads(params)
                print("请求地址:"+URL)
                print("请求参数:"+params)
                respose = requests.post(url=URL,params=xparams,headers=header,timeout=timeout)
                return respose
        except:
            print("请求失败")
    def sendget(URL,params,header,timeout):
        try:
            if params == "":
                return
            else:

                print("请求地址:"+URL)
                print("请求参数:"+params)

                respose = requests.get(url=URL,params=params,headers=header,timeout=timeout)

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


    def testHttp(casename,db,sql,url,method,params,Except):
        sqlclass.ExcuteSql(db,sql)
        caseName = casename
        Except = Except
        header = {'Content-Type': 'application/json'}
        print("用例名称:"+caseName)
        respose = None
        if method == 'post':
            respose=http2.sendpost(url,params,header,15)
            # res=str(respose)
            print("实际结果:"+respose.text)
            print("预期结果："+Except)
        elif method=='get':
            respose=http2.sendget(url,params,header,15)
            print("实际结果" + respose.text)
            print("预期结果" + Except)
        else:
            print("方法错误")

        return  respose

# if __name__ == '__main__':
#    # result1=http2.sendget('http://127.0.0.1:5000/login',"name=xiaoming&pwd=111",{'Content-Type': 'application/json'},15)
#    result2 = http2.testHttp("get登录", "", "", "http://127.0.0.1:5000/login", 'get', 'name=jacky&pwd=111', '"code": 200')
#    result3 = http2.testHttp("post登录", "", "", "http://127.0.0.1:5000/login", 'post', '{"name": "jacky", "pwd": "222"}','"code": -1')
#    print(result2.text)
#    print(result3.text)
#    # print(result1.text)

