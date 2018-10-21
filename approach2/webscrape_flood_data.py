import urllib
from bs4 import BeautifulSoup
import pandas as pd


#-----------------------------------------------------------------------
def get_table(url):
    
    page=urllib.request.urlopen(url)
    soup=BeautifulSoup(page)
    #print(soup.prettify())
    
    x=soup.find('table')

    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]

    for row in x.findAll('tr',class_="yellow"):
        #print(row)
        cells=row.findAll('td')
        #print(cells[0])
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        F.append(cells[6].find(text=True))

    df=pd.DataFrame(A,columns=['Number'])
    df['River name']=B
    df['Flood site']=C
    df['Nearest town']=D
    df['State']=E
    df['Warning level(M)']=F
    
    return(df)

#------------------------------------------------------------------------------------
 
above_normal = "http://www.india-water.gov.in/ffs/flood-forecasted-bulletins/for-level-forecasted-sites/low-flood-situation-report/"
severe="http://www.india-water.gov.in/ffs/flood-forecasted-bulletins/for-level-forecasted-sites/high-flood-situation-report/"
extreme="http://www.india-water.gov.in/ffs/flood-forecasted-bulletins/for-level-forecasted-sites/unprecedented-flood-situation-report-00001/"

AN=get_table(above_normal)
SV=get_table(severe)
EX=get_table(extreme)

if AN.empty:
    print('NO FLOODS IN INDIA')
else:
    print("FLOOD IN....")
    print(AN,'\n')
    AN.to_csv("above_normal.csv")
    
    
    
if SV.empty:
    print('NO SEVERE FLOODS IN INDIA,AT THE MOMENT')
else:
    print("FLOOD IN....")
    print(SV,'\n')
    SV.to_csv("severe.csv", sep='\t')
    
if EX.empty:
    print('NO EXTREME FLOODS IN INDIA,AT THE MOMENT')
else:
    print("FLOOD IN....")
    print(EX)
    EX.to_csv("extreme.csv", sep='\t')

    



