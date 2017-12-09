# MIPSTest

#使用前请仔细阅读!!! 

#使用的python版本为3.6

1.需要配合iverilog使用  下载地址:http://bleyer.org/icarus/ 
  并添加一下iverilog的环境变量(比如安装在C:\iverilog, 就将C:\iverilog\bin 添加到环境变量)

2.需要配合上届学长的升级版mars 

  升级版下载地址:https://github.com/depctg/Mockingbirds/blob/master/Mars.jar
  
3.注意汇编不要写死循环,不然执行不出来(比如给的样例的机器码需要删除最后两行)

4.请将测试脚本放到需要测试的project目录下(因为很多都默认的相对路径)

5.需要在project里包含mips的testbench,需要在initial里包含以下两行:
    #10000;     //表示仿真的时间
    $finish;    //表示结束仿真,不然不会结束

6.没有添加相关的错误处理,可能会运行报错

7.不保证本程序所验证的结果一定正确, 所以还是请大家自行认真测试检查