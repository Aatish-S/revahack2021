import subprocess


def instagram(a):
    b = 'bash verif.sh ' + a
    p = subprocess.check_call(b,shell=True)
    j = a + '.txt'
    inde = text_search(j,'VERIFIED')
    busi = text_search(j,'BUSINESS')
    c_inde = inde 


def text_search(name,text):
    b = name + '.txt'
    with open(b,'r') as f:
        data = f.read().replace('\n','')

    index = data.find(text)
    return index    




b = 'bash verif.sh ' 
subprocess.check_call(b,shell=True)




#CAN ONLY EXECUTE IF ACCOUNT IS PUBLIC
c = 'bash tag.sh '
subprocess.check_call(c,shell=True)