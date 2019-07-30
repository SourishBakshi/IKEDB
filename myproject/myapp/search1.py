import re, math
from collections import Counter
import openpyxl
import nlp

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def search(text1):
    text1=nlp.create_keyword(text1)
    global l,l1,l3,l2,l4,l7,l6,l5,l8,l9
    vector1 = text_to_vector(text1)
    max=0
    i=1
    l=list()
    l2=list()
    l4=list()
    l6=list()
    l1=list()
    l3=list()
    l5=list()
    l7=list()
    l8=list()
    l9=list()


    wb = openpyxl.load_workbook("c:\\Python27\\myproject\\myapp\\MASTER.xlsx")
    first_sheet = wb.get_sheet_names()[0]
    worksheet = wb.get_sheet_by_name(first_sheet)

    #here you iterate over the rows in the specific column
    for row in range(1,worksheet.max_row+1):
        for column in "D":  #Here you can add or reduce the columns
            cell_name = "{}{}".format(column, row)
            cell_name1="{}{}".format("B",row)
            cell_name2="{}{}".format("C",row)
            cell_name3="{}{}".format("E",row)
            cell_name4="{}{}".format("A",row)
            text2=worksheet[cell_name].value # the value of the specific cell
            text3=worksheet[cell_name1].value
            text4=worksheet[cell_name2].value
            text5=worksheet[cell_name3].value
            text6=worksheet[cell_name4].value
            vector2 = text_to_vector(text2)
            cosine = get_cosine(vector1, vector2)
            print cosine
            l.append(cosine)
            l2.append(text3)
            l4.append(text4)
            l6.append(text5)
            l8.append(text6)
            if max<cosine:
                temp=cosine
                cosine=max
                max=temp
    print 'Cosine:', max
    l1=[x for (x,y,z,w,v) in sorted(zip(l,l2,l4,l6,l8), reverse=True) if x>0.25  ]
    l3=[y for (x,y,z,w,v) in sorted(zip(l,l2,l4,l6,l8), reverse=True) if x>0.25  ]
    l5=[z for (x,y,z,w,v) in sorted(zip(l,l2,l4,l6,l8),reverse=True) if x>0.25 ]
    l7=[w for (x,y,z,w,v) in sorted(zip(l,l2,l4,l6,l8),reverse=True) if x>0.25 ]
    l9=[v for (x,y,z,w,v) in sorted(zip(l,l2,l4,l6,l8),reverse=True) if x>0.25]

    print l1
    print l3

def get_knownerror():
    return l9


def get_search_result(s):
    search(s)
    return l3

def pre():
    return l7

def get_file_name():
    fl=[]
    print l5
    for j in l5:
        k=j.split("\\")
        print k
        k1=k[-1]
        leng=len(k1)
        i1=k1[0:leng-5:]
        fl.append(i1)
    print fl
    return fl
