import subprocess
import os
import cgi
import re

BASE_DIR = os.getcwd()
SHERLOCK_DIR = BASE_DIR + '/sherlock/sherlock'
OSINT_DIR = BASE_DIR + '/osint/'

def instagram(a):
    b = 'bash verif.sh ' + a
    c = 'bash tag.sh ' + a
    subprocess.check_call(b,shell=True)
    subprocess.check_call(c,shell=True)
    j = a + '.txt'
    inde = text_search(j,'VERIFIED')
    busi = text_search(j,'BUSINESS')
    print(inde,' ',busi)


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
    string = open(name).read()
    new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
    open(b, 'w').write(new_str)

