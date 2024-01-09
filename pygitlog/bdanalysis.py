##对git日志的body进行解析
import requests

#获取kerywords的wiki url
def get_wikipage(keyword):
    if keyword.startswith("PR"):
        return ""
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {"action": "opensearch","namespace": "0","search": "","limit": "1","format": "json"}
    PARAMS['search'] = keyword
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    #print(DATA)
    #print(DATA[3][0])
    return DATA[3][0]

def get_true_keyword(keywords):
    if keywords == "md":
        keyword = "mdadm"
    elif "avb" in keywords :
        keyword = "Audio Video Bridging"

    else:
        keyword = keywords
    return keyword

#获取commit的关键词，如ext4
def get_commit_keyword(abbr):
    #print(abbr.split())
    for abb in abbr.split():
        if abb.endswith(":"):
            keywords = abb.replace(':','')
    for key in keywords.split('/'):
        keyword = get_true_keyword(key)
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