import os
import subprocess

#切换到工作目录
def get_repo(repopath):
    os.chdir(repopath)

#切换tag
def checkout_tag(version):
    os.system("git checkout"+" "+version)

#获取两个commit/version/tag之间的commit数量
def get_commits_commit_count(commit1,commit2):
    cmd = "git log" + " " + commit1 + ".." + commit2 + " --oneline|wc -l"
    return os.system(cmd)

#获取两个commit之间的hash列表
def get_commit_hash(commit1,commit2):
    cmd = "git log" + " '" + commit1 + "'.." + commit2 + " --oneline  --pretty=format:'%h'"
    hash = []
    multiline_str = os.popen(cmd)
    for line in multiline_str.readlines():
        hash.append(line.replace('\n',''))
    return hash

#获取某个commit的time
def get_commit_time(hash):
    cmd = "git log" + " " + hash + " -1 --pretty=format:'%ad'"
    process = os.popen(cmd)
    preprocessed = process.read()
    process.close()
    return preprocessed

#获取某个commit的author
def get_commit_author(hash):
    cmd = "git log" + " " + hash + " -1 --pretty=format:'%an'"
    process = os.popen(cmd)
    preprocessed = process.read()
    process.close()
    return preprocessed

#获取某个commit的email
def get_commit_email(hash):
    cmd = "git log" + " " + hash + " -1 --pretty=format:'%ae'"
    process = os.popen(cmd)
    preprocessed = process.read()
    process.close()
    return preprocessed

#获取某个commit的body
def get_commit_body(hash):
    cmd = "git log" + " " + hash + " -1 --pretty=format:'%B'"
    process = os.popen(cmd)
    preprocessed = process.read()
    process.close()
    return preprocessed

#获取某个commit的修改文件
def get_commit_diff_files(hash_list,hash_commit):
    num = list.index(hash_list)
    cmd = "git diff" + " --name-only " + hash[1] + " "  + hash[0]
    process = os.popen(cmd)
    preprocessed = process.read()
    process.close()
    return preprocessed
