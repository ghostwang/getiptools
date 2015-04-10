#!/usr/bin/python
from pyquery import PyQuery as pq
d = pq('https://www.whatismyip.com/my-ip-information/')
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
