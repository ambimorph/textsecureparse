import sys, codecs
from recluse.utils import open_with_unicode
from bs4 import BeautifulSoup
import datetime

filename, first, second = sys.argv[1:]
if filename == '-': f = sys.stdin
else: f = open_with_unicode(filename, 'r')

speaker = {'1': first, '2': second}
out = codecs.getwriter('utf-8')(sys.stdout)

for line in f:

    s = BeautifulSoup(line, "xml")
    date = datetime.datetime.fromtimestamp(float(s.sms.attrs['date'])/1000).strftime('%Y-%m-%d %H:%M:%S')
    print date,
    print speaker[s.sms.attrs['type']] + ": ",
    out.write( s.sms.attrs['body'] )
    print
