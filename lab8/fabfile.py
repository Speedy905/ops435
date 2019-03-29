#!/usr/bin/env python3

# Antonio Karlo Mijares

from fabric.api import *

env.user = 'root'

# Will get the hostname of this worker:
def getHostname():
    name = run("hostname")
    print(name)

# Will set up a working web server with a pre-built website
def setupWebServer():
    run("hostnamectl set-hostname www")
    run("yum -y -d1 install httpd")
    run("systemctl enable httpd")
    run("systemctl start httpd")
    with cd("/var/www/html"):
        put("webcontents.tar.bz2", ".")
        run("tar xvf webcontents.tar.bz2")
        run("rm webcontents.tar.bz2")

# Will uninstall firewalld and replace it with iptables
def setupFirewall():
	run("systemctl disable firewalld")
	run("systemctl stop firewalld")
	run("yum -y -d1 remove firewalld")
	run("yum -y -d1 install iptables-services")
	run("systemctl enable iptables")
	run("systemctl start iptables")
	with settings(warn_only=True):
		firewallAlreadySetUp = run("iptables -C INPUT -p tcp --dport 80 -j ACCEPT")
        if firewallAlreadySetUp.return_code == 1:
        	run("iptables -I INPUT -p tcp --dport 80 -j ACCEPT")
    		run("iptables-save > /etc/sysconfig/iptables")

def getLog():
  result = run('last -iwF')
  print(result)