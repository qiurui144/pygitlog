import re,os

log_file_name = "/home/qiurui/Documents/pygitlog/log-list/el8_8/kernel-4.18.0-477.13.1.el8_8full"
#log_file_name = "/home/qiurui/Documents/pygitlog/log-list/el8_0/kernel-4.18.0-80.el8"
key_filename = log_file_name + "_keyword.txt"
if(os.path.isfile(key_filename)):   
    os.remove(key_filename)
result_key_list = []
count = 0
linenum = 0
with open(log_file_name,mode="r") as file:
    log_list = file.readlines()
    for line in log_list:
        #print(linenum)
        #- iwlwifi: 
        #- [s390] s390/qdio:
        result_list = re.findall(r"[-](.*?)[:]",line)
        if(len(result_list) != 0 ):
            if " [" in result_list[0]:
                result_list = re.findall(r"[]](.*?)[:]",line)
            #忽略版本行的影响
            if( "4.18" not in result_list[0]):
                #print(result_list[0])
                string = result_list[0].lower()
                if( "revert" in string or "reinstate" in string):
                    #print(string)
                    result_list = re.findall(r'["](.*?)[:]',line)
                    if(len(result_list) != 0 ):
                        string = result_list[0].lower()
                        if( "revert" in string or "reinstate" in string):
                            print(string)
                            string = string.split('"')[1]
                            if( "[" in string):
                                string = string.split('[')[1]
                                string = string.split(']')[0]
                            print(string)
                    elif(len(result_list) == 0 ):
                        #print(string)
                        result_list = re.findall(r'[:](.*?)[:]',line)
                        if(len(result_list) != 0 ):
                            string = result_list[0].lower()
                        elif(len(result_list) == 0 ):
                            #print(string)
                            result_list = re.findall(r'[-](.*?)[:]',line)
                            string = result_list[0].lower()
                            string = string.replace("revert","")
                    #print(linenum)
                #全部转换为小写
                result_key_list.append(string.strip())
                count = count + 1
        linenum = linenum + 1

#list to set type for get keywords types
#为了方便技术，进行list转set形式，排除多余种类
aset = set(result_key_list)
result_key_list_normal = list(aset)
length = len(result_key_list_normal)
sort_result_key_list = []
i = 0
for i in range(length):
    sort_result_key_list.append([result_key_list_normal[i],result_key_list.count(result_key_list_normal[i])])
    i = i + 1

#sort by keywords count
#根据keyword对应的补丁量进行排序
sort_result_key_list = sorted(sort_result_key_list, key=lambda x: (x[1]), reverse=True)
print(count)
#写入数量
with open(key_filename,mode="a+") as file:
    file.write("count = ")
    file.write(str(count) + "\n")
#写入kewords对应的补丁量
for i in range(length):
    with open(key_filename,mode="a+") as file:
        file.write(sort_result_key_list[i][0]+" ")
        file.write(str(sort_result_key_list[i][1])+"\n")
