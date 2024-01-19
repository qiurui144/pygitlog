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
    
def get_wiki_list(wiki_file_name):
    with open(wiki_file_name,mode="r") as file:
        lines = file.readlines()  # 读取所有行
        wiki_lines = lines[3:]
        wiki_list = []
        a = 0
        for line in wiki_lines:
            for word in line.split("|"):
                a = a + 1
                if a == 2:
                    word = word.replace(" ","")
                    wiki_list.append(word)
                    a = 0
                    break
    return wiki_list

def get_wiki_list_url(index,wiki_file_name):
    with open(wiki_file_name,mode="r") as file:
        lines = file.readlines()  # 读取所有行
        wiki_line = lines[3 + index]
        a = 0
        for word in wiki_line.split("|"):
            a = a + 1
            if a == 3:
                word = word.replace(" ","")
                return word
    