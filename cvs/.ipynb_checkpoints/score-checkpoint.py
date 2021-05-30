from flask import Flask, redirect, render_template, request, url_for
import re


## REQUIRED FUNCTIONS
def RA():
describe_1=[]
for i in range(1,23):
    file = 'C:/Users/HOME/CV/cvs/'+ str(i)+'.txt'
    with open(file, 'r', encoding='utf-8',errors='ignore') as openfile:    
        line = openfile.read()
        line=re.sub('[^A-Za-z]+', ' ', line)
    describe_1.append(line)
with open('C:/Users/HOME/CV/cvs/JD 1.txt') as openfile:
    line2=openfile.read()
    line2=re.sub('[^A-Za-z]+', ' ', line2)
    describe_1.append(line2)
    
    
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer1 = TfidfVectorizer(stop_words='english')
X = vectorizer1.fit(describe_1)
d1=vectorizer1.vocabulary_
vocab_1=[]
for i in d1.keys():
    vocab_1.append(i)
    
find1 = [[0 for i in range(len(vocab_1))] for j in range(23)]
   
for i in range(1,24):
    file = 'C:/Users/HOME/CV/cvs/'+ str(i)+'.txt'

    with open(file, 'r', encoding='utf-8',errors='ignore') as openfile:
    
            line = openfile.read()
    for v in range(len(vocab_1)):
        if vocab_1[v] in line:
                find1[i-1][v]=1
        else:
                find1[i-1][v]=0
q1=[]
for v in range(len(vocab_1)):
    if vocab_1[v] in line2:
        q1.append(1)
    else:
        q1.append(0)

#print(q)
#print(find[0])
rank1=[]
for j in range(0,23):
    c=0
    for i in range(len(vocab_1)):
            c+= q1[i]*find1[j][i]
    cosine = c / float((sum(q1)*sum(find1[j]))**0.5)
    print("similarity: for document %d are ",j, cosine)
    rank1.append(cosine)
rank1.sort(reverse=True)
print(rank1)



## GUI WITH FLASK

app = Flask(__name__)
app.config['SECRET_KEY'] = "project"

@app.route('/')
def index():
    render_template("base.html")