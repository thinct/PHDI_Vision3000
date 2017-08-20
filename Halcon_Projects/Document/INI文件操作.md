## INI文件操作 ##
	
	#!/usr/bin/python
	#-*-coding:utf-8-*-
	
	# 那就可以通过下面这些代码得到MD5的值，简单吧
	import ConfigParser
	config = ConfigParser.ConfigParser()
	config.readfp(open('C:\Users\SUNRISE\Desktop\update.ini'))
	a = config.get("ZIP","MD5")
	print a
	
	# 写也很简单：
	import ConfigParser
	
	config = ConfigParser.ConfigParser()
	# set a number of parameters
	config.add_section("book")
	config.set("book", "title", "the python standard library")
	config.set("book", "author", "fredrik lundh")
	config.add_section("ematter")
	config.set("ematter", "pages", 250)
	# write to file
	config.write(open('C:\Users\SUNRISE\Desktop\update.ini', "w"))
	
	# 修改也不难（添加内容）：
	# !/usr/bin/env python
	# -*- coding: utf-8 -*-
	import ConfigParser
	
	config = ConfigParser.ConfigParser()
	config.read('C:\Users\SUNRISE\Desktop\update.ini')
	a = config.add_section("md5")
	config.set("md5", "value", "1234")
	config.write(open('C:\Users\SUNRISE\Desktop\update.ini', "r+"))  # 可以把r+改成其他方式，看看结果:)
	
	# 修改内容：
	# !/usr/bin/env python
	# -*- coding: utf-8 -*-
	import ConfigParser
	
	config = ConfigParser.ConfigParser()
	config.read('1.ini')
	config.set("md5", "value", "kingsoft")  # 这样md5就从1234变成kingsoft了
	config.write(open('1.ini', "r+"))