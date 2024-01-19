import os

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path) 

#文档内容删除，head代表从第几行开始要，tail表示倒数第几行开始不要
def delete_lines(file_name, head,tail):
    fin = open(file_name, 'r')
    a = fin.readlines()
    fout = open(file_name, 'w')
    b = ''.join(a[head:-tail])
    fout.write(b)

##实现body的展开功能（attr为summary）
def format(str1,str2):
    list = "<details><summary>" + str1 + "</summary> " 
    list = list + str2.replace('\n','<br>')+"</details>"
    return list

##实现文件差别的展开功能（首行summary）
def format_diff(str):
    a = 0
    if str.count('\n') > 1:
        for line in str.split('\n'):
            if a == 0:
                #防止首行为空，其实没必要
                if line != '':
                    list = "<details><summary>" + line + "</summary> "
                    a = 1  
            else:
                list = list + line + '<br>'
        return list + "</details>"
    else:
        return str.replace('\n','')