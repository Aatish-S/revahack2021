import subprocess
import os
import cgi
import re

BASE_DIR = os.getcwd()
SHERLOCK_DIR = BASE_DIR + '/sherlock/sherlock'
OSINT_DIR = BASE_DIR + '/osint/'
OSINT_RUN = 'bash osint.sh ' + OSINT_DIR + ' '
VERIF_RUN = 'bash verif.sh ' + OSINT_DIR + ' '

form = cgi.FieldStorage()
pyre = 'python3 sherlock.py'


#RUNS INSTAGRAM SHERLOCK SEARCH FOR THE ACCOUNT
def instagramcheck():
    username = form.getvalue('username')
    cmd = pyre + ' --site instagram ' + username
    p = subprocess.check_call(cmd,shell=True)
    osintdata(username)
    return


#RUNS OSINTGRAM MODULE TO GET INFO ON TARGET
def osintdata(name):
    shelldat = OSINT_RUN + name
    verifdat = OSINT_RUN + name
    subprocess.check_call(shelldat,shell=True) 
    subprocess.check_call(verifdat,shell=True)
    return

#HELPS YOU RETURN A INDEX VALUE WRT TO TEXT SEARCH (NEEDS TEXT INPUT)
def text_search(name,text):
    with open(name,'r') as f:
        data = f.read().replace('\n','')

    index = data.find(text)
    return index

#RETURNS INT VALUE OF THE NUMBER OF PICS THE TARGET IS TAGGED IN
def osi_tags(index,name):
    c_index = index + 16
    with open(name,'r') as f:
        data = f.read().replace('\n','')

    inde = data.find("Woohoo")
    print(inde)
    inde = inde + 16
    c_index = inde + 3
    ale = data[inde:c_index]
    ale = ale.replace(" ","")
    x = int(ale)
    return x

def osi_veri(index,name):
    c_index = index + 6
        
def clean_text(name):
    string = open(name).read()
    new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
    open(name, 'w').write(new_str)