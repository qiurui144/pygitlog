##markdown操作函数
from  pygitlog.gitoperation import *
from pygitlog.bdanalysis import *

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path) 
        print (path + " 创建成功")
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path + " 目录已存在")

#初始化kernel log summary的markdown文件
def initmd(version1,version2,source):
    dir = os.getcwd() + "/output/"
    mkdir(dir)
    filename = dir + source + version1 + "_" + version2 + ".md"
    with open(filename,mode="w") as file:
        file.write("# kernel log summary\n")
        file.write("## " + source + " from " + version1 + " to " + version2 + "\n")
        file.write("|  hash  |  time  |  editor |  email |  body | type  |  keywords |  diff-files  | \n")
        file.write("|  :---- | :----  |  :----  |  :---- |  :--- | :---- |  :------- |  :---------  | \n")
    os.chmod(filename,448)
    return  filename

def format(str):
    return str.replace('\n','<br>')

#参考格式
#| 2af9b20dbb39  | Sat Oct 28 08:15:07 2023 -1000 | Linus Torvalds | torvalds@linux-foundation.org 
#| Merge tag 'x86-urgent-2023-10-28' of git://git.kernel.org/pub/scm/linux/kernel/git/tip/tip<br> Pull misc x86 fixes from Ingo Molnar<br> - Fix a possible CPU hotplug deadlock bug caused by the new TSC synchronization code<br> - Fix a legacy PIC discovery bug that results in device troubles on affected systems, such as non-working keybards, etc<br> - Add a new Intel CPU model number to <asm/intel-family.h><br> * tag 'x86-urgent-2023-10-28' of git://git.kernel.org/pub/scm/linux/kernel/git/tip/tip:<br> &emsp;x86/tsc: Defer marking TSC unstable to a worker<br> &emsp;x86/i8259: Skip probing when ACPI/MADT advertises PCAT compatibility<br> &emsp;x86/cpu: Add model number for Intel Arrow Lake mobile processor 
#| fix<br> add model| X86 CPU | arch/x86/include/asm/i8259.h<br> arch/x86/include/asm/intel-family.h<br> arch/x86/kernel/acpi/boot.c<br> arch/x86/kernel/i8259.c<br>  arch/x86/kernel/tsc_sync.c<br>
def add_commit_info(filename,hash):
    with open(filename,mode="a+") as file:
        file.write("| " + hash + " ")
        file.write("| " + get_commit_time(hash) + " ")
        file.write("| " + get_commit_author(hash) + " ")
        file.write("| " + get_commit_email(hash) + " ")
        file.write("| " + format(get_commit_body(hash)) + " ")
        file.write("| " + get_commit_type(get_commit_body(hash)) + "<br> ")
        file.write("| " + get_commit_kerywords(get_commit_abbr(hash)) + "<br> ")
        file.write("| " + format(get_commit_diff_files(hash)) + " |\n")
    file.close()