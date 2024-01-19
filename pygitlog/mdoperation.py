##markdown操作函数
from  pygitlog.gitoperation import *
from pygitlog.bdanalysis import *
from pygitlog.fsoperation import *

#初始化kernel log summary的markdown文件
def initmd(version1,version2,source):
    dir = os.getcwd() + "/output/"
    mkdir(dir)
    filename = dir + source + version1 + "_" + version2 + ".md"
    if os.path.exists(filename):
        os.chmod(filename,448)
        return  filename
    else:
        with open(filename,mode="w") as file:
            file.write("# kernel log summary\n")
            file.write("## " + source + " from " + version1 + " to " + version2 + "\n")
            file.write("|number |  hash  |  time  |  editor |  email |  body | type  |  keywords |  diff-files  | \n")
            file.write("| :---- |  :---- | :----  |  :----  |  :---- |  :--- | :---- |  :------- |  :---------  | \n")
        os.chmod(filename,448)
        return  filename

#参考格式
#| 2af9b20dbb39  | Sat Oct 28 08:15:07 2023 -1000 | Linus Torvalds | torvalds@linux-foundation.org 
#| Merge tag 'x86-urgent-2023-10-28' of git://git.kernel.org/pub/scm/linux/kernel/git/tip/tip<br> Pull misc x86 fixes from Ingo Molnar<br> - Fix a possible CPU hotplug deadlock bug caused by the new TSC synchronization code<br> - Fix a legacy PIC discovery bug that results in device troubles on affected systems, such as non-working keybards, etc<br> - Add a new Intel CPU model number to <asm/intel-family.h><br> * tag 'x86-urgent-2023-10-28' of git://git.kernel.org/pub/scm/linux/kernel/git/tip/tip:<br> &emsp;x86/tsc: Defer marking TSC unstable to a worker<br> &emsp;x86/i8259: Skip probing when ACPI/MADT advertises PCAT compatibility<br> &emsp;x86/cpu: Add model number for Intel Arrow Lake mobile processor 
#| fix<br> add model| X86 CPU | arch/x86/include/asm/i8259.h<br> arch/x86/include/asm/intel-family.h<br> arch/x86/kernel/acpi/boot.c<br> arch/x86/kernel/i8259.c<br>  arch/x86/kernel/tsc_sync.c<br>
def add_commit_info(filename,hash,hash_list):
    count = hash_list.index(hash)
    print(hash)
    print(count)
    with open(filename,mode="a+") as file:
        file.write("| " + str(count) + " ")
        file.write("| " + hash + " ")
        file.write("| " + get_commit_time(hash) + " ")
        file.write("| " + get_commit_author(hash) + " ")
        file.write("| " + get_commit_email(hash) + " ")
        file.write("| " + format(get_commit_abbr(hash),get_commit_body(hash)) + " ")
        file.write("| " + get_commit_type(get_commit_body(hash)) + "<br> ")
        file.write("| " + get_commit_keyword(get_commit_abbr(hash),hash) + "<br> ")
        file.write("| " + format_diff(get_commit_diff_files(hash)) + " |\n")

#add_commit_info多线程版本
def add_commit_info_threads(lock,filename,hash,hash_list):
    lock.acquire()
    count = hash_list.index(hash)
    print(hash)
    print(count)
    with open(filename,mode="a+") as file:
        file.write("| " + str(count) + " ")
        file.write("| " + hash + " ")
        file.write("| " + get_commit_time(hash) + " ")
        file.write("| " + get_commit_author(hash) + " ")
        file.write("| " + get_commit_email(hash) + " ")
        file.write("| " + format(get_commit_abbr(hash),get_commit_body(hash)) + " ")
        file.write("| " + get_commit_type(get_commit_body(hash)) + "<br> ")
        file.write("| " + get_commit_keyword(get_commit_abbr(hash),hash) + "<br> ")
        file.write("| " + format_diff(get_commit_diff_files(hash)) + " |\n")
    lock.release()

#获取文档第一行在对应hash_list的位置，-1为无实际内容
def get_first_commit_count(file_name,hash_list):
    with open(file_name,mode="r") as file:
        lines = file.readlines()  # 读取所有行
        if len(lines) < 5:
            return -1 ##无实际内容
        else:
            first_line = lines[5]  # 取日志相关的首行
            a = 0
            for word in first_line.split("|"):
                a = a + 1
                if a == 3:
                    word = word.replace(" ","")
                    return hash_list.index(word)

#获取文档最后一行在对应hash_list的位置
def get_last_commit_count(file_name,hash_list):
    with open(file_name,mode="r") as file:
        lines = file.readlines()  # 读取所有行
        last_line = lines[-1]  # 取最后一行
        a = 0
        for word in last_line.split("|"):
            a = a + 1
            if a == 3:
                word = word.replace(" ","")
                return hash_list.index(word)

#获取实际要操作的hash_list
#假如源文件有实际内容，避免最后一行为不完整行，对源文件进行最后一行删除处理
def get_operation_hash_list(index,hash_list,file_name):
    operation_hash_list = hash_list[index:-1]
    if index != 0:
        delete_lines(file_name,0,1)
    return operation_hash_list