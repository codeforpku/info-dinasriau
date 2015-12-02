from urllib2 import urlopen
from bs4 import BeautifulSoup as bs
from string import digits
import json

exception = ['Support by : Diskominfo Provinsi Riau\nAplikasi Informatika : webmaster[at]riau.go.id'
             ,' \n ',
             'No',
             'Instansi',
             'Email']

def getdata():
    soup = bs(urlopen("http://subdomain.riau.go.id/"))
    raw = [d.text.encode('ascii').strip('\n') for d in soup.findAll("td") if d.text not in exception]
    excepts = [' \n0',
            ' \n1',
            ' \n2',
            ' \n3',
            ' \n4',
            ' \n5',
            ' \n6',
            ' \n7',
            ' \n8',
            ' \n9',
            ' \n10',
            ' \n11',]

    datraw = [x for x in raw if '\n' not in x]
    email = [datraw[x].strip(' ') for x in range(len(datraw)) if x%2 == 1]
    skpd = [datraw[x].strip(' ') for x in range(len(datraw)) if x%2 == 0]
    info = {"skpd-email": dict(zip(skpd, email))}
    return info
