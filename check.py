#!/usr/bin/env python2.7

import os
import sys
import re
import shutil
import ConfigParser
from dszendesk import ZenDesk
tickets = [ ]
directories = [ ]
path = ""

def main():
    print ">>> Checking zendesk login ..."
    # Ensure our authentication is correct
    global zd 
    global path
    zd = ZenDesk()
    zd.authenticate()
    path = zd.download_directory
    print ">>> Using download directory",zd.download_directory,"from",zd.configfile,"..."

def check_tickets():
    print ">>> Checking ticket status ..."
    # define regex pattern and path
    pattern = "(^[0-9]{5}$)"
    print "=== Searching for ", pattern, " in ", path, " ===== Hit CTRL+C to abort! ==="
    # Use os.walk to find all the directories under the path
    for dirname, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            matched = re.match( pattern, dir, re.M)
            if matched:
                # put ticket names into list
                tickets.append (matched.group(0))
                # put dirctory paths into list
                directories.append (dirname+"/"+dir)

    # Find the ticket status
    for idx in range (0, len(tickets)-1):
        print "checking ", tickets[idx], directories[idx], "...",
        status = zd.get_ticket_status(tickets[idx])
        # Issue the deletion statements if status is closed
        if (status == "closed") or (status == "solved"):
            print status, "- removing"
            shutil.rmtree(directories[idx])
        else:
            print status

def check_dirs():
    # Check all customer directories to see if they're empty
    print ">>> Checking unused customer directories..."
    for cust_dir in os.listdir(path):
        if os.path.isdir(cust_dir) and not os.listdir(cust_dir):
            print cust_dir + ' is empty, -- removing'
            shutil.rmtree(cust_dir)

if __name__ == "__main__":
    try:
        main()
        check_dirs()
        check_tickets()
    except KeyboardInterrupt:
        print
