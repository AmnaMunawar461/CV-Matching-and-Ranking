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
def conversion_word(inputs):
    file = 'C:/Users/HOME/CV/cvs/'+ inputs+'.txt'
    doc = Document()
    with open(file, 'r', encoding='utf-8',errors='ignore') as openfile:
        line = openfile.read()
        s=line.replace('\ufeff----------------------- Page 1-----------------------\n\n','').replace('Page 1','').replace('-','').replace('Page 2','').replace('Page 3','').replace('\n','')
    s=clean(s)
    doc.add_paragraph(s)
    doc.save(file + ".docx")
    
def parse_skills(inputs):
    list1=[]
    data=ResumeParser('C:/Users/Home/CV/cvs/'+inputs+'.txt.docx').get_extracted_data()
    list1.append(data['skills'])
    li = [0 for i in range(len(lists))]
    for l in range(len(lists)):
        if lists[l] in list1:
            li[l]=1
        else:
            li[l]=0
    find = [0 for i in range(len(vocab_))] 
   
    file = 'C:/Users/HOME/CV/cvs/'+ inputs+'.txt'

    with open(file, 'r', encoding='utf-8',errors='ignore') as openfile:
    
        line = openfile.read()
    for v in range(len(vocab_)):
        if vocab_[v] in line:
            find[v]=1
        else:
            find[v]=0
    return li,find
def csv_features(inputs,li,find):
    with open('cv.csv', 'w', newline='') as f:
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
        data=ResumeParser('C:/Users/Home/CV/cvs/'+inputs+'.txt.docx').get_extracted_data()
        writer.writerow([data['name'],data['email'],data['mobile_number'],
li[0],li[1],li[2],li[3],li[4],li[5],li[6],li[7],li[8],li[9],li[10],li[11],li[12],li[13],li[14],li[15],li[16],li[17],li[18],li[19],
li[20],
                         li[21],li[22],li[23],li[24],li[25],li[26],li[27],li[28],li[29],li[30],li[31],li[32],li[33],li[34],
                         li[35],li[36],li[37],li[38],li[39],li[40],li[41],li[42],
                         li[43],li[44],li[45],li[46],li[47],li[48],li[49],li[50],
                         li[51],li[52],li[53],li[54],li[55],li[56],li[57],li[58],
                         li[59],li[60],li[61],li[62],li[63],li[64],li[65],li[66],
                         li[67],li[68],li[69],li[70],li[71],li[72],li[73],li[74],
                         li[75],li[76],li[77],li[78],li[79],li[80],li[81],li[82],
                         li[83],li[84],li[85],li[86],li[87],li[88],li[89],li[90],
                         li[91],li[92],li[93],li[94],li[95],li[96],li[97],li[98],
                         li[99],li[100],li[101],li[102],li[103],li[104],li[105],li[106],
                         li[107],li[108],li[109],li[110],li[111],li[112],li[113],li[114],
                         li[115],li[116],li[117],li[118],li[119],li[120],li[121],li[122],
                         li[123],li[124],li[125],li[126],li[127],li[128],li[129],li[130],
                    li[131],li[132],li[133],li[134],li[135],li[136],li[137],li[138],
                         li[139],li[140],li[141],li[142],li[143],li[144],li[145],li[146],
                         li[147],li[148],li[149],
                         li[150],li[151],li[152],li[153],li[154],li[155],li[156],li[157],
                         li[158],li[159],li[160],li[161],li[162],
                         find[0],find[1],find[2],find[3],find[4],find[5],find[6],find[7],find[8],find[9],find[10],find[11],
                        find[12],find[13],find[14],find[15],find[16],find[17],find[18],find[19],find[20],
                         find[21],find[22],find[23],find[24],find[25],find[26],find[27],find[28],find[29],find[30],
                                      find[31],find[32],find[33],find[34],
                         find[35],find[36],find[37],find[38],find[39],find[40],find[41],find[42],
                         find[43],find[44],find[45],find[46],find[47],find[48],find[49],find[50],
                         find[51],find[52],find[53],find[54],find[55],find[56],find[57],find[58],
                         find[59],find[60],find[61],find[62],find[63],find[64],find[65],find[66],
                         find[67],find[68],find[69],find[70],find[71],find[72],find[73],find[74],
                         find[75],find[76],find[77],find[78],find[79],find[80],find[81],find[82],
                         find[83],find[84],find[85],find[86],find[87],find[88],find[89],find[90],
                         find[91],find[92],find[93],find[94],find[95],find[96],find[97],find[98],
                         find[99],find[100],find[101],find[102],find[103],find[104],find[105],find[106],
                         find[107],find[108],find[109],find[110],find[111],find[112],find[113],find[114],
                         find[115],find[116],find[117],find[118],find[119],find[120],find[121],find[122],
                         find[123],find[124],find[125],find[126],find[127],find[128],find[129],find[130],
                         find[131],find[132],find[133],find[134],find[135],find[136],find[137],find[138],
                         find[139],find[140],find[141],find[142],find[143],find[144],find[145],find[146],
                         find[147],find[148],find[149],
                         find[150],find[151],find[152],find[153],find[154],find[155],find[156],find[157],
                         find[158],find[159],find[160],find[161],find[162],find[163],find[164],find[165],
                         find[166],find[167],find[168],find[169],find[170],find[171],find[172],find[173],
                         find[174],find[175],find[176],find[177],find[178],find[179],find[180],find[181],
                         find[182],find[183],find[184],find[185],find[186],find[187],find[188],find[189],
                         find[190],find[191],find[192],find[193],find[194],find[195],find[196],find[197],
                         find[198],find[199],find[200],find[201],find[202],find[203],find[204],find[205],
                         find[206],find[207],find[208],find[209],find[210],find[211],find[212],find[213],
                         find[214],find[215],find[216],find[217],find[218],find[219],find[220],find[221],
                         find[222],find[223],find[224],find[225],find[226],find[227],find[228],find[229],
                         find[230],find[231],find[232],find[233],find[234],find[235],find[236],find[237],
                         find[238],find[239],find[240],find[241],find[242],find[243],find[244],find[245],
                         find[246],find[247],find[248],find[249],find[250],find[251],find[252],find[253],
                         find[254],find[255],find[256],find[257],find[258],find[259],find[260],find[261],
                         find[262]
                                           ])
       
def classification():
    df = pd.read_csv('cv.csv')
    x = df.iloc[:, 2:].values
    #print(x)
    #classifier.predict_proba(x_test)
    filename = 'C:/Users/HOME/CV/finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    ynew = loaded_model.predict(x)
# show the inputs and predicted probabilities
    if ynew == 1:
        return 'Class is Lab Instructor',ynew[0]
    elif ynew == 2:
        return 'Class is Research Assistant',ynew[0]
    else:
        return 'Class is Research Assistant -lab instructor',ynew[0]
    

# s=input('enter file number')                            
# conversion_word(s)
# li,find=parse_skills(s)
# csv_features(s)
# classification()

        