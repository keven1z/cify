# CIFY -Web information scanning

# 版本 1.0

# 描述
## 该脚本主要为了渗透测试做收集信息准备工作，收集了渗透测试中大部分需要的信息。

# 运行环境
## python 3.5及以上
## 需要安装nmap、whois工具


# 功能
* 备案信息 
* cms 检测 (目前只添加了wordpress检测插件)
* 端口扫描
* CDN 检测 
* waf 检测 

# 目录结构
* common 通用函数
* log 日志文件
* plugins 插件目录
* worker 工作目录
* data 系统所需文件目录

# 使用方法
## 参数
* -u or --url :扫描的url
* -p or --port :是否扫描端口，default:true

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

[+]Starting CIFY 1.0  
[+]Detecting CDN
[+]Not detect CDN,ip:*.*.*.*
[+]Checking WAF
[+]Found waf,name:Safedog(安全狗)
[+]Checking cms
[+]Not checking cms
[+]Starting scaning port
[+]Nmap scan report for www.********.cn (*.*.*.*)
****************************************************************************
*                               PORT RESULT                               *
****************************************************************************
  PORT     STATE         SERVICE
   80/tcp  open          http (product: nginx)
  443/tcp  open          http (product: nginx)
****************************************************************************
*                                   END                                    *
****************************************************************************
[+]Nmap done at Sat Dec 29 14:23:18 2018; 1 IP address (1 host up) scanned in 24.51 seconds
[+]Starting whois www.********.cn
****************************************************************************
*                               RESULT WHOIS                               *
****************************************************************************
Domain Name: ********.cn
ROID: ********-cn
Domain Status: ok
Registrant ID: hc6447669367131
Registrant: ********
Registrant Contact Email:********@********.cn
Sponsoring Registrar: 阿里云计算有限公司（万网）
Name Server: f1g1ns1.dnspod.net
Name Server: f1g1ns2.dnspod.net
Registration Time: 2010-09-06 12:38:38
Expiration Time: 2026-09-06 12:38:38
DNSSEC: unsigned

****************************************************************************
*                                   END                                    *
****************************************************************************
[+]Whois done

```
  
