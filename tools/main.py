import subprocess
import os
import cgi
import re

from maaad.pretend.tools.check import PRIVATE_acc

BASE_DIR = os.getcwd()
OSINT_DIR = BASE_DIR + '/osint/'

form = cgi.FieldStorage()
username = form.getvalue('username')

#SEARCHES FOR INDEX IN FILE
def text_search(name,text):
    b = name + '.txt'
    with open(b,'r') as f:
        data = f.read().replace('\n','')

    index = data.find(text)
    return index    

#SEARCHES FOR TEXT WITH INDEX VALUE
def word_back(name,ind,c_ind):
    b = name + '.txt'
    with open(b,'r') as f:
        data = f.read().replace('\n','')

    return data[ind:c_ind]

#IN CASE YOU WANT TO DELETE ALL UNWANTED STUFF
def clean_text(a):
    b = a + '.txt'
    string = open(b).read()
    new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
    open(b, 'w').write(new_str)

def instagram(a):
    b = 'bash verif.sh ' + a 
    subprocess.check_call(b,shell=True)
    j = a + '_info.txt'
    inde = text_search(j,'VERIFIED')
    busi = text_search(j,'BUSINESS')
    accc = text_search(j,'PRIVATE PROFILE')
    PRIVATE_acc = int(accc)
    foll = text_search(j,'FOLLOWED')
    c_inde = inde + 29
    e_inde = c_inde + 5
    VERIFIED_acc = word_back(j,c_inde,e_inde)
    c_inde = busi + 29
    e_inde = c_inde + 5 
    BUSINESS_acc = word_back(j,c_inde,e_inde)
    c_inde = foll + 21
    e_inde = c_inde + 4
    FOLLOWERS_acc = word_back(j,c_inde,e_inde)
    