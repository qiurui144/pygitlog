from  pygitlog.gitoperation import *
from  pygitlog.mdoperation import *
from pygitlog.listoperation import *
from pygitlog.example_module import example_function
import sys
import threading
from time import time

if __name__=="__main__":
    example_function()
    #"""
    ###v5.10后的euler社区修改
    source = "euler"
    version_new = "f04289acdae5"
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
    wiki_file_name = initwikimd()
    file_name = initmd(version_new,version_old,source)
    #print(file_name)  
    #print(get_wiki_list(wiki_file_name))  
    get_repo(repopath) 
    print("总计数量为:")
    get_commits_commit_count(version_old,version_new)
    hash_list_summary = get_commit_hash(version_old,version_new)
    #判断文本文件是否无实际内容，如果没有实际内容，将hash_list赋值，假如有实际内容，将hash_list赋值为未完成的段落（暂时只支持接尾巴）
    if get_first_commit_count(file_name,hash_list_summary) == -1:
        hash_list = get_operation_hash_list(0,hash_list_summary,file_name)
    else:
        hash_list = get_operation_hash_list(get_last_commit_count(file_name,hash_list_summary),hash_list_summary,file_name)
    n = len(hash_list) / 10
    new_hash_list = list_of_groups(hash_list,int(n))
    start_time = time()
    threads = []
    threadLock = threading.Lock()
    for i in range(0,len(new_hash_list)):
        for hash in new_hash_list[i]:
            thread = threading.Thread(target=add_commit_info_threads, args=[threadLock,file_name,wiki_file_name,hash,hash_list_summary])
            thread.start()
            threads.append(thread)
        for t in threads:
            t.join()
        
    print(f"用时{time() - start_time}秒")
    sys.exit(0)
