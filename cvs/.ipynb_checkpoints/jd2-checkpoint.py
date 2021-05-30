import re
def lab_instructor():
describe_=[]
for i in range(1,23):
    file = 'C:/Users/HOME/CV/cvs/'+ str(i)+'.txt'
    with open(file, 'r', encoding='utf-8',errors='ignore') as openfile:    
        line = openfile.read()
        line=re.sub('[^A-Za-z]+', ' ', line)
    describe_.append(line)
with open('C:/Users/HOME/CV/cvs/JD 2.txt') as openfile:
    line1=openfile.read()
    line1=re.sub('[^A-Za-z]+', ' ', line1)
    describe_.append(line1)
    
    
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit(describe_)
d=vectorizer.vocabulary_
vocab_=[]
for i in d.keys():
    vocab_.append(i)
    
find = [[0 for i in range(len(vocab_))] for j in range(23)]
   
for i in range(1,24):
    file = 'C:/Users/HOME/CV/cvs/'+ str(i)+'.txt'

    with open(file, 'r', encoding='utf-8',errors='ignore') as openfile:
    
            line = openfile.read()
    for v in range(len(vocab_)):
        if vocab_[v] in line:
                find[i-1][v]=1
        else:
                find[i-1][v]=0
q=[]
for v in range(len(vocab_)):
    if vocab_[v] in line1:
        q.append(1)
    else:
        q.append(0)

#print(q)
#print(find[0])
rank=[]
for j in range(0,23):
    c=0
    for i in range(len(vocab_)):
            c+= q[i]*find[j][i]
    cosine = c / float((sum(q)*sum(find[j]))**0.5)
    print("similarity for document {0:d} are {1:f}".format(j, cosine))
    rank.append(cosine)
rank.sort(reverse=True)
print(rank[:3])