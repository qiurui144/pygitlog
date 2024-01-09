##对git日志的body进行解析
import requests
from  pygitlog.gitoperation import *

#获取kerywords的wiki url
def get_wikipage(keyword):
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {"action": "opensearch","namespace": "0","search": "","limit": "1","format": "json"}
    PARAMS['search'] = keyword
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    print(DATA)
    #print(DATA[3][0])
    return DATA[3][0]

#处理abbr没有keyword的特殊情况
def deal_spec_abbr(hash,keywords):
    keyword_list = get_commit_diff_files(hash).split("\n")
    #print(keyword_list)
    file_name = "/home/qiurui/Documents/git-tools/pygitlog/keywords.txt"
    for key in keyword_list:
        #print(key)
        with open(file_name,"r") as file:
            for line in file:
                #print(line.replace('\n',''))
                if line.replace('\n','') in key:
                    #print(line)
                    return get_true_keyword(line.replace('\n',''),hash)
    return keywords

#获取实际的keyword
#异常情况：PR-number
def get_true_keyword(keywords,hash):
    #print(keywords)
    if keywords == "md":
        keyword = "mdadm"
    elif keywords == "atm":
        keyword = "Asynchronous Transfer Mode"
    elif "nft" in keywords:
        keyword = "netfilter"
    elif "dm" in keywords:
        keyword = "Device Mapper"
    elif "avb" in keywords :
        keyword = "Audio Video Bridging"
    elif "gsm" in keywords :
        keyword = "gsm"
    elif keywords.startswith("PR"): 
        keyword = deal_spec_abbr(hash,keywords)
    elif keywords.startswith("special"): 
        keyword = deal_spec_abbr(hash,keywords)
    else:
        keyword = keywords
    return keyword

#获取commit的关键词，如ext4
#逻辑：先获取oneline的描述，然后进行切分
def get_commit_keyword(abbr,hash):
    #print(abbr.split())
    keywords = ""
    for abb in abbr.split():
        if abb.endswith(":"):
            temp_word = abb.split(":")
            keywords = temp_word[0]
    #print(keywords)
    if keywords == "":
        keywords = "special"
    for key in keywords.split('/'):
        keyword = get_true_keyword(key,hash)
        return "[" + keyword + "](" + get_wikipage(keyword) + ")"

#获取commit的类型，如
def get_commit_type(body):
    for line in body.split("\n"):
        #print(line)
        if line.startswith("category"):
            return line.replace('category:','')
    return ""

def get_CVE_code(body):
    return ""