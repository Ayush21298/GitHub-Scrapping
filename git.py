import requests
from bs4 import BeautifulSoup


base_url='https://api.github.com'
user=raw_input("Enter GitHub ID : ")

#f=open('a','w')
res=requests.get(base_url+'/users/'+user+'/repos').text.encode('utf-8')
#print >> f,res
soup=BeautifulSoup(res,"lxml")
c=0
# for i in range(len(res)-6):
# 	if res[i:i+6]=='"name"':
# 		s=''
# 		for h in res[i+8:]:
# 			if h=='"':
# 				break
# 			else:
# 				s+=h
# 		print s
s=user+','
for i in range(len(res)-6):
	if res[i:i+6]=='"name"':

		for h in res[i+8:]:
			if h=='"':
				s+=','
				break
			else:
				s+=h
f=open('a.txt','w')
print >>f,s
