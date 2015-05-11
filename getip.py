#!/usr/bin/python
from pyquery import PyQuery as pq
import urllib2
opener = urllib2.build_opener()
opener.addheaders = [('User-agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36')]
page = opener.open('https://www.whatismyip.com/my-ip-information/')
#d = pq('https://www.whatismyip.com/my-ip-information/')
d = pq(page.read())
ip = d('.ip').text()
print "Your Ip Address is:",
print "".join(ip.split(':')[1].split())
print d('.proxy').text()
print d('.city').text()
print d('.state:eq(0)').text()
print " ".join(d('.country').text().split()[:2])
print d('.state:eq(1)').text()
print d('.state:eq(2)').text()
print d('.isp').text()
print d('.state:eq(3)').text()
print d('.state:eq(4)').text()
