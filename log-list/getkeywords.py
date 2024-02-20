import re

log_file_name = "/home/qiurui/Documents/pygitlog/log-list/el8_8/kernel-4.18.0-477.13.1.el8_8full"
key_filename = log_file_name + "_keyword.txt"
result_key_list = []
count = 0
with open(log_file_name,mode="r") as file:
    log_list = file.readlines()
    for line in log_list:
        #- iwlwifi: 
        #- [s390] s390/qdio:
        result_list = re.findall(r"[-](.*?)[:]",line)
        if(len(result_list) != 0 ):
            if " [" in result_list[0]:
                result_list = re.findall(r"[]](.*?)[:]",line)
            if( "4.18" not in result_list[0]):
                #print(result_list[0])
                if( "Revert" in result_list[0] or "Reinstate" in result_list[0]):
                    string = result_list[0].replace('Revert','')
                    string = string.replace('Reinstate','')
                    string = string.replace('"','')
                else:
                    string = result_list[0]
                string = string.replace(' ','')
                result_key_list.append(string)
                count = count + 1

#list to set type for get keywords types
aset = set(result_key_list)
result_key_list_normal = list(aset)
length = len(result_key_list_normal)
sort_result_key_list = []
i = 0
for i in range(length):
    sort_result_key_list.append([result_key_list_normal[i],result_key_list.count(result_key_list_normal[i])])
    i = i + 1

#sort by keywords count
sort_result_key_list = sorted(sort_result_key_list, key=lambda x: (x[1]), reverse=True)
with open(key_filename,mode="a+") as file:
    file.write("count = ")
    file.write(str(count) + "\n")
for i in range(length):
    with open(key_filename,mode="a+") as file:
        file.write(sort_result_key_list[i][0]+" ")
        file.write(str(sort_result_key_list[i][1])+"\n")