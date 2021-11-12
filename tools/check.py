import subprocess

a = 'monisha._.prabhakar'

def text_search(name,text):
    b = name + '.txt'
    with open(b,'r') as f:
        data = f.read().replace('\n','')

    index = data.find(text)
    return index    

def word_back(name,ind,c_ind):
    b = name + '.txt'
    with open(b,'r') as f:
        data = f.read().replace('\n','')

    return data[ind:c_ind]

j = a + '_info'
inde = text_search(j,'VERIFIED')
busi = text_search(j,'BUSINESS')
PRIVATE_acc = text_search(j,'PRIVATE PROFILE')
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

print(PRIVATE_acc, ' ',VERIFIED_acc, ' ',BUSINESS_acc, ' ',FOLLOWERS_acc)