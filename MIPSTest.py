import subprocess
import os
import re
import logging

'''
1.需要配合iverilog使用 下载地址:http://bleyer.org/icarus/ 并添加一下iverilog的环境变量(比如安装在C:\iverilog, 就将C:\iverilog\bin 添加到环境变量) 配合上届学长的升级版mars很好用

升级版下载地址:https://github.com/depctg/Mockingbirds/blob/master/Mars.jar

2.注意汇编不要写死循环,不然执行不出来(比如给的样例的机器码需要删除最后两行)

3.请将测试脚本放到需要测试的project目录下(因为很多都默认的相对路径)

4.需要在project里包含mips的testbench,需要在initial里包含以下两行: #10000; //表示仿真的时间 $finish; //表示结束仿真,不然不会结束
'''


project_location = "C:\\Users\Challenging\Desktop\p5"      #修改你的project地址(请将该脚本放到project目录下)
mars_location = "C:\\Users\Challenging\Desktop\mars.jar"   #修改你的mars位置
asm_location = "C:\\Users\Challenging\Desktop\mips1.asm"   #修改你的汇编地址
print("执行汇编.........")

Result = subprocess.getoutput("java -jar "+ mars_location +" db mc CompactDataAtZero nc "+asm_location)
subprocess.getoutput("java -jar " + mars_location + " a dump .text HexText "+project_location+"\code.txt "+asm_location)
marsResult = Result.strip().split("\n")
marsResult = [item for item in marsResult if item[0:3]!="$ 0"]

file = os.listdir(project_location)
verilog = [i for i in file if i[-2:] == ".v"]

command = "iverilog"
for i in verilog:
    command=command+" "+ i

print("开始仿真:"+command)


subprocess.getoutput(command)
answer = subprocess.getoutput("vvp a.out")


sim = re.findall(r"\d+@.*?: .*?<= .{8}?", answer)
cycle = re.findall(r"(\d+)@.*?: .*?<= .{8}?", answer)
for j in range(len(sim)-1):
    if (cycle[j] == cycle[j+1]) and sim[j]> sim[j+1]:
        sim[j], sim[j+1] = sim[j+1], sim[j]

simResult = [re.search("\d+@.*?: (.*?<= .{8}?)", item).group(1) for item in sim]

simResult = [item for item in simResult if item[0:3]!="$ 0"]

flag = 1
if (len(marsResult) > len(simResult)) or (len(marsResult) < len(simResult)):
    print("your answer is less or more than we expected")
    for i in range(min(len(simResult), len(marsResult))):
        print("we got: " + result[i]+"  when we expected: " + marsResult[i], end="")
        if simResult[i] == marsResult[i]:
            print("    ac")
        else:
            print("    wa")
    print("..........................")
    flag = 0

if flag==1:
    for i in range(len(marsResult)):
        if marsResult[i] != simResult[i]:
            print("we got: "+result[i]+" when we expected: " + marsResult[i])
            flag = 0
if flag==1:
    print("AC!")

else:
    print("WA!")
