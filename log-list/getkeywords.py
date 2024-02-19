import re

log_file_name = "/home/qiurui/Documents/pygitlog/log-list/el8_8/kernel-4.18.0-477.10.1.el8_8"
key_filename = log_file_name + "_keyword.txt"
result_key_list = []
with open(log_file_name,mode="r") as file:
    log_list = file.readlines()
    for line in log_list:
        #- iwlwifi: 
        result_list = re.findall(r"[- ](.*?)[:]",line)
        if(len(result_list) != 0 ):
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
for i in range(length):
    with open(key_filename,mode="a+") as file:
        file.write(sort_result_key_list[i][0]+" ")
        file.write(str(sort_result_key_list[i][1])+"\n")