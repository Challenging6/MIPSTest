import subprocess
import os
import re


project_location = "D:\\Challenging\jizu\p5new\\"           # 修改你的project地址(注意最后有两个斜杠)
mars_location = "C:\\Users\Challenging\Desktop\mars.jar"   # 修改你的mars位置(注意是魔改版的mars)
asm_location = "C:\\Users\Challenging\Desktop\mips1.asm"   # 修改你的汇编地址
print("执行汇编.........")

Result = subprocess.getoutput("java -jar " + mars_location + " 10000 db mc CompactDataAtZero nc " + asm_location)
subprocess.getoutput(
    "java -jar " + mars_location + " 10000 db mc CompactDataAtZero  dump .text HexText " + project_location + "code.txt " + asm_location)
marsResult = re.findall(r".*? <= .{8}?", Result)
marsResult = [item for item in marsResult if item[0:3] != "$ 0"]

files = os.listdir(project_location)
verilog = [file for file in files if file[-2:] == ".v"]

os.chdir(project_location)
command = "iverilog "
for file in verilog:
    command = command + file + " "

print("开始仿真:" + command+"\n")
subprocess.getoutput(command)
answer = subprocess.getoutput("vvp a.out")

sim = re.findall(r"\d+@.*?: .*?<= .{8}?", answer)
simResult_temp = [re.search("\d+@.*?: (.*?<= .{8}?)", item).group(1) for item in sim]
cycle = re.findall(r"(\d+)@.*?: .*?<= .{8}?", answer)
for j in range(len(sim) - 1):
    if (cycle[j] == cycle[j + 1]) and simResult_temp[j][0] == "*" and simResult_temp[j+1][0] == "$":
        sim[j], sim[j + 1] = sim[j + 1], sim[j]

simResult = [re.search("\d+@.*?: (.*?<= .{8}?)", item).group(1) for item in sim]

simResult = [item for item in simResult if item[0:3] != "$ 0"]
sim = [item for item in sim if re.search("\d+@.*?: (.*?) <= .{8}?", item).group(1) != "$ 0"]

flag = 1
if (len(marsResult) > len(simResult)) or (len(marsResult) < len(simResult)):
    print("your answer is less or more than we expected")
    for i in range(min(len(simResult), len(marsResult))):
        print("we got: " + sim[i] + "  when we expected: " + marsResult[i], end="")
        if simResult[i] == marsResult[i]:
            print("    ac")
        else:
            print("    wa")
    print("..........................")
    flag = 0

if flag == 1:
    for i in range(len(marsResult)):
        if marsResult[i] != simResult[i]:
            print("we got: " + sim[i] + " when we expected: " + marsResult[i])
            flag = 0
if flag == 1:
    print("AC!")

else:
    print("WA!")
print("\nMARS Result:\n"+"\n".join(marsResult)+"\n")
print("Simulate Result:\n"+"\n".join(sim))
