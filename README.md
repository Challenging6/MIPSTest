# MIPSTest

#使用前请仔细阅读!!! 

#使用的python版本为3.6

1.需要配合iverilog使用  下载地址:http://bleyer.org/icarus/ 
  并添加一下iverilog的环境变量(比如安装在C:\iverilog, 就将C:\iverilog\bin 添加到环境变量)

2.需要配合上届学长的升级版mars 

  升级版下载地址:https://github.com/depctg/Mockingbirds/blob/master/Mars.jar
  

4.需要在project里包含mips的testbench,需要在initial里包含以下两行:
    #20000;     //表示仿真的时间(根据情况调整, 可能仿真时间不一定够)
    $finish;    //表示结束仿真,不然不会结束

5.没有添加相关的错误处理,可能会运行报错

6.不保证本程序所验证的结果一定正确, 所以还是请大家自行认真测试检查

7.文件夹中最好不要包含一些无关的文件