#!/usr/bin/python

import thread
import time
import subprocess
from bs4 import BeautifulSoup
import urllib2

# Define a function for the thread

def print_time(threadName, full_link):
    command='axel -n 1000 -a '+ full_link
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
      print line
    retval = p.wait()

link_id=0
url='http://dl.funsaber.net/serial/The%20Shannara%20Chronicles/season%202/480/'
resp = urllib2.urlopen(url)
soup = BeautifulSoup(resp, "html5lib")
for link in soup.find_all('a', href=True):
    thread_name ='Thread-'+str(link_id)
    links=link['href']
    if(links=='../'):
        i=0
    else:
        link_id=link_id+1
        full_link = url+links
        try:
           print "Request by %s: at %s: Starting download ..." % ( thread_name, time.ctime(time.time()))
           thread.start_new_thread( print_time, (thread_name, full_link))
        except:
           print "Error: unable to start thread"
while 1:
   pass
