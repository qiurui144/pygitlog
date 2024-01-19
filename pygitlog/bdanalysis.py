##对git日志的body进行解析
import requests
from requests.adapters import HTTPAdapter
from  pygitlog.gitoperation import *
from  pygitlog.mdoperation import *
from  pygitlog.fsoperation import *

#获取kerywords的wiki url
def get_wikipage(keyword,file_name):
    i = 0
    S = requests.Session()
    #避免因为wiki网络问题导致的异常hang死
    S.mount('http://', HTTPAdapter(max_retries=3))
    S.mount('https://', HTTPAdapter(max_retries=3))
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {"action": "opensearch","namespace": "0","search": "","limit": "1","format": "json"}
    PARAMS['search'] = keyword
    #print(keyword)
    if keyword in get_wiki_list(file_name):
            index = get_wiki_list(file_name).index(keyword)
            wiki_page = get_wiki_list_url(index,file_name)
            #print("have wiki result")
            return wiki_page
    elif keyword == "":
        return ""
    else:
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        if len(DATA) == 0 :
            if keyword not in get_wiki_list(file_name):
                with open(file_name,mode="a+") as file:
                    file.write("| " + keyword + " ")
                    file.write("| no search result |\n")
                #print("no search result")
            return ""
        else:
            #print("DATA=",DATA)
            if len(DATA[3]) == 0:
                if keyword not in get_wiki_list(file_name):
                    with open(file_name,mode="a+") as file:
                        file.write("| " + keyword + " ")
                        file.write("| no match result |\n")
                    #print("no match result")
                return ""
            else:
                if keyword not in get_wiki_list(file_name):
                    with open(file_name,mode="a+") as file:
                        file.write("| " + keyword + " ")
                        file.write("| " + DATA[3][0] + " |\n")
                    #print("add wiki result")
                    return DATA[3][0]

#获取commit的关键词，如ext4
#逻辑：先获取oneline的描述，然后进行切分
def get_commit_keyword(abbr,hash,wiki_file_name):
    #print(abbr.split())
    keywords = ""
    for abb in abbr.split():
        if abb.endswith(":"):
            temp_word = abb.split(":")
            keywords = temp_word[0]
    #print(keywords)
    if keywords == "":
        return keywords
    else:
        for key in keywords.split('/'):
            key = key.replace('"','')
            return "[" + key + "](" + get_wikipage(key,wiki_file_name) + ")"

#获取commit的类型，如
def get_commit_type(body,abbr):
    for line in body.split("\n"):
        #print(line)
        if line.startswith("category"):
            return line.replace('category:','')
    if "fix" in abbr.lower():#bug修复
        return "bugfix"
    if "add" in abbr.lower():#增强
        return "enhance"
    return ""

def get_CVE_code(body):
    return ""