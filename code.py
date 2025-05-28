st1="am am going is again not is going is again"
l1=[]
dict1={}
k1=""
for chr in st1:
  if chr==" ":
    l1.append(k1)
    k1=""
  else:
    k1=k1+chr
l1.append(k1)
for i in l1:
  if i in dict1:
    dict1[i]=dict1[i]+1
  else:
    dict1[i]=1
print(dict1)