# CIFY -Web information scanning

# 版本 1.1

# 描述
## 该脚本主要为了渗透测试做收集信息准备工作，收集了渗透测试中大部分需要的信息。

# 运行环境
## python 3.5及以上
## 需要安装nmap、whois工具


# 功能
* 备案信息 （基于whois）
* cms 检测 (目前只添加了wordpress检测插件)
* 端口扫描（基于nmap）
* CDN 检测 
* waf 检测 
* 子域名扫描（计划）
* 目录爆破（计划）

# 目录结构
* common 通用函数
* log 日志文件
* plugins 插件目录
* worker 工作目录
* data 系统所需文件目录
* lib 离线第三方模块

# 使用方法
## 参数
* -u or --url :扫描的url

## 输出结果txt
### data/result下生成以host为名的txt文件

# 示例
```
python main.py -u  http://www.xxxx.cn
       _____ ________ 
__________(_)___  __/_____  __
_  ___/__  / __  /_  __  / / /
/ /__  _  /  _  __/  _  /_/ / 
\___/  /_/   /_/     _\__, /  
                     /____/  
Copyright [2018.9] [zii]

[+]Starting CIFY 1.1  
[+]Detecting CDN
[+]Checking WAF
[+]Found waf,name:Safedog(安全狗)
[+]Checking cms
[+]Starting scaning port
[+]Start whois
+----------------------------------------+
|                  port                  |
+-------+-------+--------------+---------+
|  port | state | service_name | version |
+-------+-------+--------------+---------+
|   21  |  open |     ftp      |   None  |
|   30  |  open |  tcpwrapped  |   None  |
|   80  |  open |     http     |   None  |
|  311  |  open |  tcpwrapped  |   None  |
|  443  |  open |     http     |   None  |
|  705  |  open |  tcpwrapped  |   None  |
|  912  |  open |  tcpwrapped  |   None  |
|  1055 |  open |  tcpwrapped  |   None  |
|  1296 |  open |  tcpwrapped  |   None  |
|  2034 |  open |  tcpwrapped  |   None  |
|  5200 |  open |  tcpwrapped  |   None  |
|  5566 |  open |  tcpwrapped  |   None  |
|  6106 |  open |  tcpwrapped  |   None  |
| 14238 |  open |  tcpwrapped  |   None  |
| 32784 |  open |  tcpwrapped  |   None  |
| 55055 |  open |  tcpwrapped  |   None  |
+-------+-------+--------------+---------+
+----------------------------------------------+
|                    whois                     |
+-----------------+----------------------------+
|        项       |             值             |
+-----------------+----------------------------+
|   domain_name   |         safedog.cn         |
|    registrar    | 阿里云计算有限公司（万网） |
|  creation_date  |    2010-09-06 12:38:38     |
| expiration_date |    2026-09-06 12:38:38     |
|   name_servers  |     f1g1ns1.dnspod.net     |
|                 |     f1g1ns2.dnspod.ne      |
|      status     |             ok             |
|      emails     |    zhangzhx@safedog.cn     |
|      dnssec     |          unsigned          |
|       name      |  厦门服云信息科技有限公司  |
+-----------------+----------------------------+
+-----+-----------------+
|  项 |        值       |
+-----+-----------------+
| CDN | 183.252.199.196 |
| waf | Safedog(安全狗) |
| cms |       None      |
+-----+-----------------+

```
  
