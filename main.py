from  pygitlog.gitoperation import *
from  pygitlog.mdoperation import *
from pygitlog.example_module import example_function
import sys
import threading
from time import time

def list_of_groups(init_list, childern_list_len):
    '''
    init_list为初始化的列表,childern_list_len初始化列表中的几个数据组成一个小列表
    :param init_list:
    :param childern_list_len:
    :return:
    '''
    list_of_group = zip(*(iter(init_list),) *childern_list_len)
    end_list = [list(i) for i in list_of_group]
    count = len(init_list) % childern_list_len
    end_list.append(init_list[-count:]) if count !=0 else end_list
    return end_list

if __name__=="__main__":
    example_function()
    #"""
    ###v5.10后的euler社区修改
    source = "euler"
    #version_new = "f04289acdae5"
    version_new = "9ffcbab21847"
    #version_old = "2c85ebc57b3e1817b6ce1a6b703928e113a90442"
    #version_old = "40a06eb91ba8"
    version_old = "2c85ebc57b3e"
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
        sys.exit(0)
    file_name = initmd(version_new,version_old,source)
    #print(file_name)  
    get_repo(repopath) 
    print("总计数量为:")
    get_commits_commit_count(version_old,version_new)
    hash_list = get_commit_hash(version_old,version_new)
    n = len(hash_list) / 10
    new_hash_list = list_of_groups(hash_list,int(n))
    start_time = time()
    threads = []
    threadLock = threading.Lock()
    for i in range(0,len(new_hash_list)):
        for hash in new_hash_list[i]:
            thread = threading.Thread(target=add_commit_info_threads, args=[threadLock,file_name,hash,hash_list])
            thread.start()
            threads.append(thread)
        for t in threads:
            t.join()
    """
    threads = []
    for hash in hash_list:

        add_commit_info(file_name,hash)
        
        thread = threading.Thread(target=add_commit_info_threads, args=[thread_lock,file_name,hash,hash_list])
        thread.start()
        threads.append(thread)
        
    for t in threads:
        t.join()
    """
        
    print(f"用时{time() - start_time}秒")
    sys.exit(0)
