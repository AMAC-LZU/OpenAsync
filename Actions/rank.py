# 遍历工作目录
from pathlib import Path
import os
import re
fileList=os.walk("./")
print("当前目录下的文件：")
nameList=[]
work_Line_dic={}
work_File_dic={}
# rep=r'reviewer:\[(.*)\]'
pattern = r'reviewer:\[(.*)\]'
print(re.search(pattern, 'reviewer:[yangjinyu]'))
print("gogogo")
for path,dir_lst,file_lst in fileList:
    # print(file_lst)
    for file in file_lst:
        if file.endswith('.txt') or file.endswith('.java') or file.endswith('.c') or file.endswith('.cpp') or file.endswith('.h') or file.endswith('.js') or file.endswith('.html') or file.endswith('.css') or file.endswith('.php') or file.endswith('.sql') or file.endswith('.xml') or file.endswith('.json') or file.endswith('.yaml') or file.endswith('.yml') or file.endswith('.md'):
        # 输出文件文本信息
# 获取文件行数
            print(path+'/'+file)
            f=open(path+'/'+file, 'r', encoding='utf-8',newline="\n") 
            # print(f.read())
            opgg=f.read()
            print(opgg)
            line_count = opgg.count('\n')+1 
            count=re.search(pattern, opgg)
            print(count)
            if count!=None:
                nameList.append(count.group(1))
                work_Line_dic[nameList[-1]]=line_count
                if nameList[-1] not in work_File_dic:
                    work_File_dic[nameList[-1]] = 1
                else:
                    work_File_dic[nameList[-1]]+=1
            # 生成Excel表
            f.close()
print("文件行数统计：")
for name in work_Line_dic:
    print(f"{name}: {work_Line_dic[name]}行")
print("文件数量统计：")
for name in work_File_dic:
    print(f"{name}: {work_File_dic[name]}个文件")
f=open("./README.md", 'r', encoding='utf-8',newline="\n")
opgg=f.read()
f.close()
f=open("./README.md", 'w', encoding='utf-8',newline="\n")
f.truncate()
pattern=r'Rank \| Name \| Sum_Line\| Sum_File\|.*---'
dotall = re.compile(pattern, re.DOTALL)
print(dotall.search(opgg))
# print(test)
class rank:
    def __init__(self, name, line, file):
        self.name = name
        self.line = line
        self.file = file
    def __lt__(self, other):
        return self.line > other.line
list_rank = []
repl=r'Rank | Name | Sum_Line| Sum_File| \r\n ----| ----| ---- | ----|\r\n'
for name in work_Line_dic:
    list_rank.append(rank(name, work_Line_dic[name], work_File_dic[name]))
list_rank.sort(key=lambda x: x.file*x.line, reverse=True) 
    # repl+=f"| {name} | {work_Line_dic[name]} | {work_File_dic[name]}|\r\n"
ranknum=0
for i in range(len(list_rank)):
    ranknum+=1
    repl+=f"{ranknum}| {list_rank[i].name} | {list_rank[i].line} | {list_rank[i].file}|\r\n"
repl+=r'---'
# print(dotall,repl,opgg)
new_file = re.sub(dotall, repl, opgg)
f.write(new_file)
print("文件内容替换完成")
f.close()
# 