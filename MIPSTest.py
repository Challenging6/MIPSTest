import subprocess
import os
import re

project_location = "D:\\Challenging\jizu\p5new\\"  # 修改你的project地址
mars_location = "C:\\Users\Challenging\Desktop\mars.jar"  # 修改你的mars位置(注意是魔改版的mars)
asm_location = "C:\\Users\Challenging\Desktop\mips1.asm"  # 修改你的汇编地址
print("执行汇编.........")

Result = subprocess.getoutput("java -jar " + mars_location + " 10000 db mc CompactDataAtZero nc " + asm_location)
subprocess.getoutput(
    "java -jar " + mars_location + " 10000 db mc CompactDataAtZero  dump .text HexText " + project_location + "code.txt " + asm_location)
marsResult = Result.split("\n")
marsResult = [item for item in marsResult if item != "" and len(item) < 40]
marsResult = [item for item in marsResult if item[0:3] != "$ 0"]

files = os.listdir(project_location)
verilog = [file for file in files if file[-2:] == ".v"]

os.chdir(project_location)
command = "iverilog "
for file in verilog:
    command = command + file + " "

print("开始仿真:" + command + "\n")
subprocess.getoutput(command)
answer = subprocess.getoutput("vvp a.out")

sim = re.findall(r"\d+@.*?: .*?<= .{8}?", answer)
simResult_temp = [re.search("\d+@.*?: (.*?<= .{8}?)", item).group(1) for item in sim]
cycle = re.findall(r"(\d+)@.*?: .*?<= .{8}?", answer)
for j in range(len(sim) - 1):
    if (cycle[j] == cycle[j + 1]) and simResult_temp[j][0] == "*" and simResult_temp[j + 1][0] == "$":
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
            if re.search("^.*? <= .{2}?$", marsResult[i]):

                local = int(re.search("^(.*?) <= .{2}?$", marsResult[i]).group(1)[-1:], 16) % 4
                if local == 0:
                    if re.search("^.*? <= (.{2}?)$", marsResult[i]).group(1) != re.search("^.*? <= (.{8}?)$",
                                                                                          simResult[i]).group(1)[-2:]:
                        # print(re.search("^.*? <= (.{8}?)$", simResult[i]).group(1)[-2:])
                        print("we got: " + sim[i] + " when we expected: " + marsResult[i])
                elif local == 1:
                    if re.search("^.*? <= (.{2}?)$", marsResult[i]).group(1) != re.search("^.*? <= (.{8}?)$",
                                                                                          simResult[i]).group(1)[-4:-2]:
                        # print(re.search("^.*? <= (.{8}?)$", simResult[i]).group(1)[-4:-1])
                        print("we got: " + sim[i] + " when we expected: " + marsResult[i])
                elif local == 2:
                    if re.search("^.*? <= (.{2}?)$", marsResult[i]).group(1) != re.search("^.*? <= (.{8}?)$",
                                                                                          simResult[i]).group(1)[-6:-4]:
                        # print(re.search("^.*? <= (.{8}?)$", simResult[i]).group(1)[-6:-3])
                        print("we got: " + sim[i] + " when we expected: " + marsResult[i])
                elif local == 3:
                    if re.search("^.*? <= (.{2}?)$", marsResult[i]).group(1) != re.search("^.*? <= (.{8}?)$",
                                                                                          simResult[i]).group(1)[-8:-6]:
                        # print(re.search("^.*? <= (.{8}?)$", simResult[i]).group(1)[-8:-5])
                        print("we got: " + sim[i] + " when we expected: " + marsResult[i])

            elif re.search("^.*? <= .{4}?$", marsResult[i]):
                local = int(re.search("^(.*?) <= .{4}?$", marsResult[i]).group(1)[-1:], 16) % 4
                if local == 0:
                    if re.search("^.*? <= (.{4}?)$", marsResult[i]).group(1) != re.search("^.*? <= (.{8}?)$",
                                                                                          simResult[i]).group(1)[-4:]:
                        # print(re.search("^.*? <= (.{8}?)$", simResult[i]).group(1)[-2:])
                        print("we got: " + sim[i] + " when we expected: " + marsResult[i])
                elif local == 2:
                    if re.search("^.*? <= (.{4}?)$", marsResult[i]).group(1) != re.search("^.*? <= (.{8}?)$",
                                                                                          simResult[i]).group(1)[-8:-4]:
                        # print(re.search("^.*? <= (.{8}?)$", simResult[i]).group(1)[-6:-3])
                        print("we got: " + sim[i] + " when we expected: " + marsResult[i])
                else:
                    print("sh location error")

            else:
                print("we got: " + sim[i] + " when we expected: " + marsResult[i])
                flag = 0
if flag == 1:
    print("AC!")

else:
    print("WA!")
print("\nMARS Result:\n" + "\n".join(marsResult) + "\n")
print("Simulate Result:\n" + "\n".join(sim))
