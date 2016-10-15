import urllib2
proxylist=['202.141.80.24:3128','10.11.2.60:8080','172.16.116.71:3128']
l=[]
proxy = ''
for proxy in proxylist :
	proxy_support = urllib2.ProxyHandler({'http':'http://c.nivsarkar:bunny@'+proxy})
	opener = urllib2.build_opener(proxy_support)
	try:
		f = opener.open("http://google.com/")
		f.read(1)
		l.append(proxy)
		print proxy
	except Exception:
		x=0
print l