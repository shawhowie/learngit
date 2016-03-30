# -*- coding: utf-8 -*-
# Title      : 谷歌host修改脚本
# Author  : 2016-03-30 09:55:55
# Date     :  Shaw
#【使用说明】
#请确保在当“前用户对host可写”前提下使用；

import sys,os
import re
import urllib.request as urllib2

#更新Host
def update_host():
    #load host from 360kb
    host_url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
    print('Get data from %s' % host_url)
    html = urllib2.urlopen(host_url)
    data = html.read()
    hosthtml = data.decode('utf-8')
    regex = r'# Copyright.*# Modified hosts end'
    pattern = re.compile(regex, re.S)
    host = pattern.search(hosthtml)
    if host:
        hostdata = host.group()
        with open(r'c:\Windows\System32\drivers\etc\hosts', 'r+') as f:
            oldHost = f.read()
            newHost = re.sub(regex, hostdata, oldHost, flags = re.S)
            if oldHost == newHost:
                newHost += '\r\n' + hostdata
            f.seek(0)
            f.write(newHost)
        print('Successfully update hosts.')
    else:
        print('Not found host data.')

if __name__ == '__main__':
    update_host()
