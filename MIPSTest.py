import subprocess
import os
import re
import logging


project_location = "C:\\Users\Challenging\Desktop\p5"      #修改你的project地址
mars_location = "C:\\Users\Challenging\Desktop\mars.jar"   #在这里修改你的mars位置
asm_location = "C:\\Users\Challenging\Desktop\mips1.asm"   #修改你的汇编地址
print("执行汇编.........")

marsResult = subprocess.getoutput("java -jar "+ mars_location +" db mc CompactDataAtZero nc "+asm_location)
subprocess.getoutput("java -jar "+mars_location + " a dump .text HexText "+project_location+"\code.txt "+asm_location)
marsResult = marsResult.strip().split("\n")


file = os.listdir(project_location)
verilog = [i for i in file if i[-1] == "v"]

command = "iverilog"
for i in verilog:
    command=command+" "+ i

print("开始仿真:"+command)


subprocess.getoutput(command)
answer = subprocess.getoutput("vvp a.out")


simResult = re.findall(r"@.*?: (.*?<= .{8}?)", answer)
result = re.findall(r"(@.*?: .*?<= .{8}?)", answer)
flag = 1
if (len(marsResult) > len(simResult)) or (len(marsResult) < len(simResult)):
    print("your answer is less or more than we expected")

    for i in range(min(len(simResult), len(marsResult))):
        print("we got: "+result[i]+"  when we expected: "+marsResult[i], end="")
        if simResult[i] == marsResult[i]:
            print("    ac")
        else:
            print("    wa")
    print("..........................")
    flag = 0

if flag==1:
    for i in range(len(marsResult)):
        if marsResult[i] != simResult[i]:
            print("we got "+simResult[i]+" when we expected" + marsResult)
            flag = 0
if flag==1:
    print("AC!")

else:
    print("WA!")
