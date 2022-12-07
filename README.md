                                   Londly 

一款红队在大量的资产中实现自动化全端口扫描、标题识别、指纹识别、爆破、漏扫的工具
 
	
	开始 • 更新日志 • 支持选项 • 指纹识别规则 • 实际效果 • TODO • 感谢列表 
	
0x00 项目起源
     在红蓝对抗中，将真实ip放到ip.txt中，实现自动化快速打点，原理：将ip进行CDN过滤，masscan全端口扫描，Fscan扫描，httpx标题识别，将整理的URL进行Finger+observer双重指纹识别，xray+nuclei漏扫。
     
0x01 使用方法
     将xray nuclei Finger observer fscan masscan httpx放到根目录下
