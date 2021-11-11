
filepath = '/home/laz/Desktop/hackathon/maaad/pretend/tools/osin/laz_aats.txt'
s= 'woohoo'

with open('laz_aats.txt','r') as f:
    data = f.read().replace('\n','')

inde = data.find("Woohoo")
print(inde)
inde = inde + 16
c_index = inde + 3

print(data[inde:c_index])
