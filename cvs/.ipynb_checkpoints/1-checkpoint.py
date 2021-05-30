import pandas as pd
import pickle
import numpy as np
from sklearn import metrics 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')
import en_core_web_sm
nlp=en_core_web_sm.load()
import csv
from pyresparser import ResumeParser
import json
f=open('C:/Users/HOME/CV/describe_job.json',)
vocab_=json.load(f)
f_=open('C:/Users/HOME/CV/skills.json',)
lists=json.load(f_)

from docx import Document
import glob
import os
from curses import ascii
def clean(text):
    return str(''.join(
            ascii.isprint(c) and c or ' ' for c in text
            )) 
def conversion_word():
    for i in range(1,5):
        file = 'C:/Users/HOME/CV/cvs/'+ str(i)+'.txt'
        doc = Document()
        with open(file, 'r', encoding='utf-8',errors='ignore') as openfile:
            line = openfile.read()
            s=line.replace('\ufeff----------------------- Page 1-----------------------\n\n','').replace('Page 1','').replace('-','').replace('Page 2','').replace('Page 3','').replace('\n','')
        s=clean(s)
        doc.add_paragraph(s)
        doc.save(file + ".docx")
    
def parse_skills():
    list1=[]
    for i in range(1,5):
        data=ResumeParser('C:/Users/Home/CV/cvs/'+str(i)+'.txt.docx').get_extracted_data()
        list1.append(data['skills'])
    
    li = [[0 for i in range(len(lists))] for j in range(4)]
    for i in range(len(list1)):
        for l in range(len(lists)):
            if lists[l] in list1[i]:
                li[i][l]=1
            else:
                li[i][l]=0
          
    find = [[0 for i in range(len(vocab_))] for j in range(4)]
    for i in range(1,5):
        
        file = 'C:/Users/HOME/CV/cvs/'+ str(i)+'.txt'

        with open(file, 'r', encoding='utf-8',errors='ignore') as openfile:
    
            line = openfile.read()
        for v in range(len(vocab_)):
            if vocab_[v] in line:
                find[i-1][v]=1
            else:
                find[i-1][v]=0
        
    return li,find
def csv_features():
    with open('C:/Users/HOME/CV/abc.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name','email','mobile_number'])
    
    df = pd.read_csv("cv.csv")
    for l in lists:
        df[l]=''
    for vocab in vocab_:
        df[vocab]=''
    df.to_csv("cv.csv", index=False)
    with open('cv.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        
        for i in range(1,5):
            data=ResumeParser('C:/Users/Home/CV/cvs/'+str(i)+'.txt.docx').get_extracted_data()
            
            writer.writerow([data['name'],data['email'],data['mobile_number'],
                         li[i-1][0],li[i-1][1],li[i-1][2],li[i-1][3],li[i-1][4],li[i-1][5],li[i-1][6],li[i-1][7],li[i-1][8],li[i-1][9],li[i-1][10],li[i-1][11],li[i-1][12],li[i-1][13],li[i-1][14],li[i-1][15],li[i-1][16],li[i-1][17],li[i-1][18],li[i-1][19],li[i-1][20],li[i-1][21],li[i-1][22],li[i-1][23],li[i-1][24],li[i-1][25],li[i-1][26],li[i-1][27],li[i-1][28],li[i-1][29],li[i-1][30],li[i-1][31],li[i-1][32],li[i-1][33],li[i-1][34],li[i-1][35],li[i-1][36],li[i-1][37],li[i-1][38],li[i-1][39],li[i-1][40],li[i-1][41],li[i-1][42],li[i-1][43],li[i-1][44],li[i-1][45],li[i-1][46],li[i-1][47],li[i-1][48],li[i-1][49],li[i-1][50],li[i-1][51],li[i-1][52],li[i-1][53],li[i-1][54],li[i-1][55],li[i-1][56],li[i-1][57],li[i-1][58],li[i-1][59],li[i-1][60],li[i-1][61],li[i-1][62],li[i-1][63],li[i-1][64],li[i-1][65],li[i-1][66],li[i-1][67],li[i-1][68],li[i-1][69],li[i-1][70],li[i-1][71],li[i-1][72],li[i-1][73],li[i-1][74],li[i-1][75],li[i-1][76],li[i-1][77],li[i-1][78],li[i-1][79],li[i-1][80],li[i-1][81],li[i-1][82],li[i-1][83],li[i-1][84],li[i-1][85],li[i-1][86],li[i-1][87],li[i-1][88],li[i-1][89],li[i-1][90],
                         li[i-1][91],li[i-1][92],li[i-1][93],li[i-1][94],li[i-1][95],li[i-1][96],li[i-1][97],li[i-1][98],
                         li[i-1][99],li[i-1][100],li[i-1][101],li[i-1][102],li[i-1][103],li[i-1][104],li[i-1][105],li[i-1][106],
                         li[i-1][107],li[i-1][108],li[i-1][109],li[i-1][110],li[i-1][111],li[i-1][112],li[i-1][113],li[i-1][114],
                         li[i-1][115],li[i-1][116],li[i-1][117],li[i-1][118],li[i-1][119],li[i-1][120],li[i-1][121],li[i-1][122],
                         li[i-1][123],li[i-1][124],li[i-1][125],li[i-1][126],li[i-1][127],li[i-1][128],li[i-1][129],li[i-1][130],
                         li[i-1][131],li[i-1][132],li[i-1][133],li[i-1][134],li[i-1][135],li[i-1][136],li[i-1][137],li[i-1][138],
                         li[i-1][139],li[i-1][140],li[i-1][141],li[i-1][142],li[i-1][143],li[i-1][144],li[i-1][145],li[i-1][146],
                         li[i-1][147],li[i-1][148],li[i-1][149],
                         li[i-1][150],li[i-1][151],li[i-1][152],li[i-1][153],li[i-1][154],li[i-1][155],li[i-1][156],li[i-1][157],
                         li[i-1][158],li[i-1][159],li[i-1][160],li[i-1][161],li[i-1][162],
                         find[i-1][0],find[i-1][1],find[i-1][2],find[i-1][3],find[i-1][4],find[i-1][5],find[i-1][6],find[i-1][7],find[i-1][8],find[i-1][9],find[i-1][10],find[i-1][11],find[i-1][12],find[i-1][13],find[i-1][14],find[i-1][15],find[i-1][16],find[i-1][17],find[i-1][18],find[i-1][19],find[i-1][20],
                         find[i-1][21],find[i-1][22],find[i-1][23],find[i-1][24],find[i-1][25],find[i-1][26],find[i-1][27],find[i-1][28],find[i-1][29],find[i-1][30],find[i-1][31],find[i-1][32],find[i-1][33],find[i-1][34],
                         find[i-1][35],find[i-1][36],find[i-1][37],find[i-1][38],find[i-1][39],find[i-1][40],find[i-1][41],find[i-1][42],find[i-1][43],find[i-1][44],find[i-1][45],find[i-1][46],find[i-1][47],find[i-1][48],find[i-1][49],find[i-1][50],find[i-1][51],find[i-1][52],find[i-1][53],find[i-1][54],find[i-1][55],find[i-1][56],find[i-1][57],find[i-1][58],find[i-1][59],find[i-1][60],find[i-1][61],find[i-1][62],find[i-1][63],find[i-1][64],find[i-1][65],find[i-1][66],find[i-1][67],find[i-1][68],find[i-1][69],find[i-1][70],find[i-1][71],find[i-1][72],find[i-1][73],find[i-1][74],find[i-1][75],find[i-1][76],find[i-1][77],find[i-1][78],find[i-1][79],find[i-1][80],find[i-1][81],find[i-1][82],find[i-1][83],find[i-1][84],find[i-1][85],find[i-1][86],find[i-1][87],find[i-1][88],find[i-1][89],find[i-1][90],find[i-1][91],find[i-1][92],find[i-1][93],find[i-1][94],find[i-1][95],find[i-1][96],find[i-1][97],find[i-1][98],find[i-1][99],find[i-1][100],find[i-1][101],find[i-1][102],find[i-1][103],find[i-1][104],find[i-1][105],find[i-1][106],find[i-1][107],find[i-1][108],find[i-1][109],find[i-1][110],find[i-1][111],find[i-1][112],find[i-1][113],find[i-1][114],find[i-1][115],find[i-1][116],find[i-1][117],find[i-1][118],find[i-1][119],find[i-1][120],find[i-1][121],find[i-1][122],find[i-1][123],find[i-1][124],find[i-1][125],find[i-1][126],find[i-1][127],find[i-1][128],find[i-1][129],find[i-1][130],find[i-1][131],find[i-1][132],find[i-1][133],find[i-1][134],find[i-1][135],find[i-1][136],find[i-1][137],find[i-1][138],find[i-1][139],find[i-1][140],find[i-1][141],find[i-1][142],find[i-1][143],find[i-1][144],find[i-1][145],find[i-1][146],find[i-1][147],find[i-1][148],find[i-1][149],
                         find[i-1][150],find[i-1][151],find[i-1][152],find[i-1][153],find[i-1][154],find[i-1][155],find[i-1][156],find[i-1][157],
                         find[i-1][158],find[i-1][159],find[i-1][160],find[i-1][161],find[i-1][162],find[i-1][163],find[i-1][164],find[i-1][165],
                         find[i-1][166],find[i-1][167],find[i-1][168],find[i-1][169],find[i-1][170],find[i-1][171],find[i-1][172],find[i-1][173],
                         find[i-1][174],find[i-1][175],find[i-1][176],find[i-1][177],find[i-1][178],find[i-1][179],find[i-1][180],find[i-1][181],
                         find[i-1][182],find[i-1][183],find[i-1][184],find[i-1][185],find[i-1][186],find[i-1][187],find[i-1][188],find[i-1][189],
                         find[i-1][190],find[i-1][191],find[i-1][192],find[i-1][193],find[i-1][194],find[i-1][195],find[i-1][196],find[i-1][197],
                         find[i-1][198],find[i-1][199],find[i-1][200],find[i-1][201],find[i-1][202],find[i-1][203],find[i-1][204],find[i-1][205],
                         find[i-1][206],find[i-1][207],find[i-1][208],find[i-1][209],find[i-1][210],find[i-1][211],find[i-1][212],find[i-1][213],
                         find[i-1][214],find[i-1][215],find[i-1][216],find[i-1][217],find[i-1][218],find[i-1][219],find[i-1][220],find[i-1][221],
                         find[i-1][222],find[i-1][223],find[i-1][224],find[i-1][225],find[i-1][226],find[i-1][227],find[i-1][228],find[i-1][229],
                         find[i-1][230],find[i-1][231],find[i-1][232],find[i-1][233],find[i-1][234],find[i-1][235],find[i-1][236],find[i-1][237],
                         find[i-1][238],find[i-1][239],find[i-1][240],find[i-1][241],find[i-1][242],find[i-1][243],find[i-1][244],find[i-1][245],
                         find[i-1][246],find[i-1][247],find[i-1][248],find[i-1][249],find[i-1][250],find[i-1][251],find[i-1][252],find[i-1][253],
                         find[i-1][254],find[i-1][255],find[i-1][256],find[i-1][257],find[i-1][258],find[i-1][259],find[i-1][260],find[i-1][261],
                         find[i-1][262]])
        
        print(find)    
    
        
def classification():
    df = pd.read_csv('cv.csv')
    x = df.iloc[:, 2:].values
    print(x)
    #classifier.predict_proba(x_test)
    filename = 'C:/Users/HOME/CV/finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    ynew = loaded_model.predict(x)
    for i in range(len(x)):
        print("X=%s, Predicted=%s" % (x[i], ynew[i]))
# show the inputs and predicted probabilities
#     if ynew == 1:
#         print('Class is Lab Instructor',ynew[0])
#     elif ynew == 2:
#         print('Class is Research Assistant',ynew[0])
#     else:
#         print('Class is Research Assistant-Lab Instructor',ynew[0])
    

#s=input('enter file number')                            
conversion_word()
li,find=parse_skills()
csv_features()
classification()

        