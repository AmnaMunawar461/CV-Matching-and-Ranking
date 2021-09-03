from flask import Flask, redirect, render_template, request, url_for
import re
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from model import conversion_word,parse_skills,classification,csv_features
# import json
# f=open('C:/Users/HOME/CV/describe_job.json',)
# vocab_=json.load(f)
# f_=open('C:/Users/HOME/CV/skills.json',)
# lists=json.load(f_)
from docx import Document
import glob
import os
from curses import ascii
name=['Adnan Ahmed','Awais Anwar','Ebad Ali','Hafiz Muhammad','Faisal khan ','Faizan Asghar',
'Ghulam Jaffar','Habib -ur-Rehman','Hafiz Muhammad Ali','Haris Ahmed','Hitesh','Jawad Ahmed','Muhammad Azmi','Muhammad Umaid',
'Tayyab','Saad 1','Saad 2','Sana','Shawana','Umair','Urooj','Waqas','Zohaib']


## GUI WITH FLASK

app = Flask(__name__)

app.config['SECRET_KEY'] = "project"
app.config['UPLOAD_FOLDER'] = 'C:/Users/HOME/CV/csv'
app.config['MAX_CONTENT_PATH'] = 1200

from flask import send_from_directory



@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    print(app.root_path)
    full_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    print(full_path)
    return send_from_directory(full_path, filename)


## REQUIRED FUNCTIONS
@app.route('/RA', methods = ['GET', 'POST'])
def RA():
    describe_1=[]
    for i in range(1,24):
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
                        find1[i-1][v]=find1[i-1][v]+1
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
    for j in range(23):
        c=0
        for i in range(len(vocab_1)):
                c+= q1[i]*find1[j][i]
        cosine = round((c / float((sum(q1)*sum(find1[j]))**0.5)),3)

        #print("similarity: for document %d are ",j, cosine)
        rank1.append((cosine,j+1))
    
    rank1.sort(key = lambda x: x[0],reverse=True)
    global name
    w=[]
    new_name=[]
    for i in range(1,24):
        li,find=parse_skills(str(i))
        csv_features(str(i),li,find)
        r, s = classification()
        if s == 2 or s== 0 :
            w.append(i)
    for i in range(23):
        if rank1[i][1] in set(w):
            new_name.append((rank1[i][0],rank1[i][1]))
    #print(new_name)     
    length_new_name=len(new_name)       
    return render_template("RA.html", rank=new_name,name=name,length=length_new_name) 



@app.route('/')
def index():
    return render_template("cv.html")


# @app.route('/cvclassify.html')
# def classify():

#     return render_template("cvclassify.html")

f = "cccmnbc"


#############
@app.route('/cvclassify', methods = ['GET', 'POST'])
def classify():
    
    return render_template("cvclassify.html")
######

@app.route('/result.html',methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        global f
        q = request.files['files']
        if q.filename == '' or q.filename == None:
            return render_template('cvclassify.html')
        q.save(secure_filename(q.filename))
        f=q.filename
                 
        #7.txt->7
        f=f.strip('.txt')                   
        if f == '' or f == None:
            return render_template('invalid.html')
        conversion_word(f)
        li,find=parse_skills(f)
        csv_features(f,li,find)
        r, s = classification()
        return render_template('result.html', word=r, word2=s)

    return render_template('result.html', word=f)


@app.route('/rank1', methods = ['GET', 'POST'])
def rank1():
    return render_template('rank1.html')

import re

@app.route('/lab_instructor',methods=['GET','POST'])
def lab_instructor():
    describe_=[]
    for i in range(1,24):
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
                    find[i-1][v]=find[i-1][v]+1
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
    for j in range(23):
        c=0
        for i in range(len(vocab_)):
            c+= q[i]*find[j][i]
        cosine = c / float((sum(q)*sum(find[j]))**0.5)
        #print("similarity for document {0:d} are {1:f}".format(j, cosine))
        rank.append((round(cosine,3),j+1))
    rank.sort(key = lambda x: x[0],reverse=True)
    w=[]
    new_name=[]
    for i in range(1,24):
        li,find=parse_skills(str(i))
        csv_features(str(i),li,find)
        r, s = classification()
        if s == 2 or s== 0 :
            w.append(i)
    for i in range(23):
        if rank[i][1] in set(w):
            new_name.append((rank[i][0],rank[i][1]))
    #print(new_name)     
    length_new_name=len(new_name)       
    return render_template("LI.html", rank=new_name,name=name,length=length_new_name) 


if __name__ == "__main__":
    app.run(debug=True)
#RA()