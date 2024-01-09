from  pygitlog.gitoperation import *
from  pygitlog.mdoperation import *
from pygitlog.example_module import example_function

if __name__=="__main__":
    example_function()
    repopath = "/home/qiurui/Documents/kernel/euler/kernel"
    version_new = "f04289acdae57aa4066adee541dadd70b062ac88"
    version_old = "95982be1aa8140f22bbb90b0edf3e6644167f729"
    source = "euler"
    file_name = initmd(version_new,version_old,source)
    print(file_name)  
    get_repo(repopath) 
    count = get_commits_commit_count(version_new,version_old)
    hash_list = get_commit_hash(version_new,version_old)
    for hash in hash_list:
        add_commit_info(file_name,hash)