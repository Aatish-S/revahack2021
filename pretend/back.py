import subprocess
import os
import re

REAL = 0

username = input('Enter username:')



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
    new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', a)
    return new_str

def photo(a):
    c = 'bash tag.sh '+ a
    subprocess.check_call(c,shell=True)
    j = a + '_tag'
    inde = text_search(j,'Woohoo')
    c_index = inde + 16
    e_index = c_index + 3
    tag = word_back(j,c_index,e_index)
    tag1 = tag.strip()
    TAGGED = int(tag1)
    if TAGGED > 1:
        if FOLLOWERS_acc > 250:
            REAL = 1
    


def instagram(a):
    global PRIVATE
    global VERIFIED_acc
    global FOLLOWERS_acc
    global BUSINESS_acc
    j = a + '_info'
    inde = text_search(j,'VERIFIED')
    busi = text_search(j,'BUSINESS')
    accc = text_search(j,'PRIVATE PROFILE')
    PRIVATE = int(accc)
    foll = text_search(j,'FOLLOWED')
    c_inde = inde + 29
    e_inde = c_inde + 5
    VERIFIED_acc = word_back(j,c_inde,e_inde)
    c_inde = busi + 29
    e_inde = c_inde + 5 
    BUSINESS_acc = word_back(j,c_inde,e_inde)
    c_inde = foll + 21
    e_inde = c_inde + 4
    c = word_back(j,c_inde,e_inde)
    c = c.strip()
    c = clean_text(c)
    FOLLOWERS_acc = int(c)
    if PRIVATE<100:
        photo(a)
        finder()
    else:
        finder()


def finder():
    if VERIFIED_acc == 'True':
        REAL = 1

    if BUSINESS_acc == 'True':
        REAL = 1
        
    if FOLLOWERS_acc > 250:
        REAL = 1
    else:
        REAL = 0
    
    if REAL == 1:
        print('NOT A BOT!')
    else:
        print('BOTTT!!!!!')

def run(a):
    b = 'bash verif.sh ' + a 
    h = 0
    try:
        # universal_newlines - makes manual decoding of subprocess.stdout unnecessary
        output = subprocess.check_output(b,stderr=subprocess.STDOUT,universal_newlines=True)

        # Print out command's standard output (elegant)
        self.textEdit_CommandLineOutput.insertPlainText(output)
        self.isCommandExecutionSuccessful = True

    except subprocess.CalledProcessError as error:
        self.isCommandExecutionSuccessful = False
        h=1
        print(h)
        errorMessage = ">>> Error while executing:\n"+ b+ "\n>>> Returned with error:\n" + str(error.output)
        self.textEdit_CommandLineOutput.append(errorMessage)

    except FileNotFoundError as error:
        errorMessage = error.strerror
        h=1

    print(h)


def filedel(name):
    b = 'bash filerem.sh ' + name + '_info.txt'
    c = 'bash filerem.sh ' + name + '_tag.txt'
    subprocess.check_call(b,shell=True)
    subprocess.check_call(c,shell=True)
    return

        
run(username)


