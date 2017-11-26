#!/usr/bin/python

import thread
import time
import subprocess
from bs4 import BeautifulSoup
import urllib2

# pass your base url here
url='http://dl.funsaber.net/serial/The%20Shannara%20Chronicles/season%202/480/'

url= raw_input('Enter your url:')

def print_time(threadName, full_link):
    command='axel -n 1000 -a '+ full_link + '| awk -W interactive' + "'$0~/\[/{printf'" + "%s'$'\r''"+ '", $0}"'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    retval = p.wait()
    print(''+threadName+ 'finished downloading.')
link_id=0
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
        #    print "Request by %s: at %s: Starting download ..." % ( thread_name, time.ctime(time.time()))
           print('Donwload job started for link '+ str(link_id) +'by  '+ thread_name)
           thread.start_new_thread( print_time, (thread_name, full_link))
        except:
           print "Error: unable to start thread"
while 1:
   pass
