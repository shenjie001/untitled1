import os
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
        header='ssss'
        fd.write(header)
        url='ssss'
        fd.write(url)
        str='sss'
        fd.write(str)
        fd.close()
if __name__== '__main__':
    createtest.mkdir('test','listHomeworkDesc')


