#!/usr/bin/env python
import urllib2
import re
import hashlib

base_url = "http://blog.iso50.com/page/"


def main ():
  for i in range (1, 2):
    page_url = "%s%d" % (base_url, i)
    page = urllib2.urlopen(page_url)
    for line in page:
      print line.strip()
      #files = re.findall("soundFile=.*\.mp3", line)
      #for file in files:
      #  f = urllib2.unquote(file.lstrip("soundFile="))
      #  print "%s\t%s" % (f, hashlib.md5(f).hexdigest() )

if __name__== "__main__":
  main()
