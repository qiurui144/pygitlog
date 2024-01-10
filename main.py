from  pygitlog.gitoperation import *
from  pygitlog.mdoperation import *
from pygitlog.example_module import example_function
import sys

if __name__=="__main__":
    example_function()
    #"""
    ###v5.10后的euler社区修改
    source = "euler"
    version_new = "f04289acdae57aa4066adee541dadd70b062ac88"
    version_old = "2c85ebc57b3e1817b6ce1a6b703928e113a90442"
    """
    ###v5.10前的upstream社区修改
    source = "upstream"
    version_new = "2c85ebc57b3e"
    version_old = "33dc9614dc20"
    """
    if source == "euler":
        repopath = "/home/qiurui/Documents/kernel/euler/kernel"
    elif source == "upstream":
        repopath = "/home/qiurui/Documents/kernel/stable-linux/linux"
    else:
        print("请输入正确的代码来源")
        sys.exit()
    file_name = initmd(version_new,version_old,source)
    #print(file_name)  
    get_repo(repopath) 
    count = get_commits_commit_count(version_old,version_new)
    hash_list = get_commit_hash(version_old,version_new)
    a = 0
    for hash in hash_list:
        print(hash)
        a = a + 1
        print(a)
        add_commit_info(file_name,hash)
