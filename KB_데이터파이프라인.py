#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
import numpy as np
from time import sleep
import re
from tqdm import tqdm
import pymysql 
from sqlalchemy import create_engine
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns 
sns.set()
pymysql.install_as_MySQLdb()
import MySQLdb


# In[2]:


def gas(x):
    if '가솔린' in x:
        return '가솔린'
    if '디젤' in x:
        return '디젤'
    if '전기' in x:
        return '전기'
    if 'CNG' in x:
        return '가솔린'
    if '수소' in x:
        return '수소'
    if '가솔린+전기' in x:
        return '하이브리드'
    if 'LPG+전기' in x:
        return '하이브리드'
    if '가솔린+LPG' in x:
        return '바이퓨얼'
    if '하이브리드' in x:
        return '하이브리드'
    if '디젤+전기' in x:
        return '하이브리드'
    if '530e' in x:
        return '하이브리드'
    if '30e' in x:
        return '하이브리드'
    if 'LPi' in x:
        return 'LPG'
    if 'VVT' in x:
        return '가솔린'
    if 'GDi' in x:
        return '가솔린'
    if 'T-GDI' in x:
        return '가솔린'
    if 'CVVL' in x:
        return '가솔린'
    if 'VGT' in x:
        return '디젤'
    if 'e-VGT' in x:
        return '디젤'
    if 'ECO Dynamics' in x:
        return '디젤'
    if 'ECO' in x:
        return '전기'
    if 'Electir' in x:
        return '전기'
    if 'GDe' in x:
        return '가솔린'
    if 'TCE' in x:
        return '가솔린'
    if 'dci' in x:
        return '가솔린'
    if 'LPe' in x:
        return 'LPG'
    if 'XDi' in x:
        return '디젤'
    if 'CGi' in x:
        return '가솔린'
    if 'CDi' in x:
        return '디젤'
    if 'BLUETEC' in x:
        return '디젤'
    if 'TFSi' in x:
        return '가솔린'
    if 'TDi' in x:
        return '디젤'
    if 'TSI' in x:
        return '디젤'
    if 'GTI' in x:
        return '디젤'
    if 'CRDI' in x:
        return '디젤'
    if 'GDI' in x:
        return '가솔린'
    if 'M235i' in x:
        return '가솔린'
    if '320i' in x:
        return '가솔린'
    if 'M340i' in x:
        return '가솔린'
    if '330i' in x:
        return '가솔린'
    if '428i' in x:
        return '가솔린'
    if 'M440i' in x:
        return '가솔린'
    if  '420i' in x:
        return '가솔린'
    if '430i' in x:
        return '가솔린'
    if  '528i' in x:
        return '가솔린'
    if '545i' in x:
        return '가솔린'
    if '520i' in x:
        return '가솔린'
    if '530i' in x:
        return '가솔린'
    if '540i' in x:
        return '가솔린'
    if '535i' in x:
        return '가솔린'
    if '650i' in x:
        return '가솔린'
    if '750iL' in x:
        return '가솔린'
    if '750Li' in x:
        return '가솔린' 
    if '740Li' in x:  
        return '가솔린'
    if '840i' in x:
        return '가솔린'
    if '20i' in x:
        return '가솔린'
    if '25i' in x:
        return '가솔린'
    if '5.0i'in x:
        return '가솔린'
    if '40i'  in x:
        return '가솔린'
    if '118d' in x:
        return '디젤'
    if '218d' in x:
        return '디젤'
    if '320d' in x:
        return '디젤'
    if '325d' in x:
        return '디젤'
    if '420d' in x:
        return '디젤'
    if '520d' in x:
        return '디젤'
    if '535d' in x:
        return '디젤'
    if '523d' in x:
        return '디젤'
    if '525d' in x:
        return '디젤'
    if '530d' in x:
        return '디젤'
    if 'M550d' in x:
        return '디젤'
    if '730Ld' in x:
        return '디젤'
    if '740d' in x:
        return  '디젤'
    if '730d' in x:
        return '디젤'
    if '840d' in x:
        return '디젤'
    if '18d' in x:
        return '디젤'
    if '20d' in x:
        return '디젤'
    if '2.0d' in x:
        return '디젤'
    if '2.3d' in x:
        return '디젤'
    if '30d' in x:
        return '디젤'
    if '40d' in x:
        return '디젤'
    if '3.0d' in x:
        return '디젤'
    if 'M50D' in x:
        return '디젤'
    if 'M50i' in x:
        return '가솔린'
    if '330Ci' in x:
        return '가솔린'
    if 'LPG' in x:
        return 'LPG'
    else:
        return np.nan
    


# In[3]:


def selector(x):
            if '2021년' in x:
                return '2021'
            if '2020년' in x:
                return '2020'
            if '2019년' in x:
                return '2019'
            if '2018년' in x:
                return '2018'
            if '2018년' in x:
                return '2018'
            if '2017년' in x:
                return '2017'
            if '2016년' in x:
                return '2016'
            if '2015년' in x:
                return '2015'
            if '2014년' in x:
                return '2014'
            if '2013년' in x:
                return '2013'
            if '2012년' in x:
                return '2012'
            if '2011년' in x:
                return '2011'
            if '2010년' in x:
                return '2010'
            if '2009년' in x:
                return '2009'
            if '2008년' in x:
                return '2008'
            if '2007년' in x:
                return '2007'
            if '2006년' in x:
                return '2006'
            if '2005년' in x:
                return '2005'
            if '2004년' in x:
                return '2004'
            if '2003년' in x:
                return '2003'
            if '2002년' in x:
                return '2002'
            if '2001년' in x:
                return '2001'
            if '2000년' in x:
                return '2000'
            if '1999년' in x:
                return '1999'
            if '1998년' in x:
                return '1998'
            if '1997년' in x:
                return '1997'
            if '1996년' in x:
                return '1996'
            if '1995년' in x:
                return '1995'
            if '1994년' in x:
                return '1994'
            if '1993년' in x:
                return '1993'
            if '1992년' in x:
                return '1992'
            if '1991년' in x:
                return '1991'
            if '1990년' in x:
                return '1990'


# In[5]:


def spec(x):
    if '콰트로' in x:
        return '4WD'
    if '4matic' in x:
        return '4WD'
    if 'xdrive' in x:
        return '4WD'
    if '4WD'   in x:
        return '4WD'
    if '2WD'  in x:
        return '2WD'
    if 'htrac' in x:
        return '4WD'
    if 'AWD' in x:
        return 'AWD'
    if 'e-awd' in x:
        return '4WD'
    if 'FWD' in x:
        return '2WD'
    if  '4MOTION' in x:
        return '4WD'
    if 'ALL4' in x:
        return '4WD'
    if 'Q4' in x:
        return '4WD'
    if '르반떼' in x:
        return '4WD'
    else:
        return '2WD'


# In[6]:


def option(x):
    if '스포츠 리미티드' in x:
        return '스포츠 리미티드'
    if '스포츠 팩1' in x:
        return '스포츠 팩1'
    if'CS 25주년' in x:
        return'CS 25주년'
    if '조이 퍼스트 에디션' in x:
        return '조이 퍼스트 에디션'
    if '페인트워크 에디션' in x:
        return '페인트워크 에디션'
    if 'M 스포츠 쉐도우' in x:
        return 'M 스포츠 쉐도우'
    if '페인트워크 에디션' in x:
        return '페인트워크 에디션'
    if 'M 스포츠 퍼스트 에디션' in x:
        return 'M 스포츠 퍼스트 에디션'
    if 'M 퍼포먼스 에디션 25th' in x:
        return 'M 퍼포먼스 25주년 에디션'
    if 'M4 쿠페 컨패티션 헤리티지' in x:
        return 'M4 쿠페 컴패티션 헤리티지'
    if 'M 에어로다이나믹 스페셜 에디션' in x:
        return 'M 에어로다이나믹 스페셜 에디션'
    if 'i 퍼포먼스' in x:
        return 'i 퍼포먼스'
    if '인디비주얼' in x:
        return '인디비주얼'
    if '럭셔리 플러스' in x:
        return '럭셔리 플러스'
    if '컴페티션 에디션' in x:
        return '컴페티션 에디션'
    if '스페셜 에디션' in x:
        return '스페셜 에디션'
    if '디자인 퓨어 엑셀런스' in x:
        return '디자인 퓨어 엑셀런스'
    if '프리미엄' in x:
        return '프리미엄'
    if '블랙 앤 화이트' in x:
        return '블랙 앤 화이트'
    if '컴패티션' in x:
        return '컴패티션'
    if '스포츠 섀도우' in x:
        return'M 스포츠 쉐도우'
    if 'M 스포츠 플러스' in x:
        return 'M 스포츠 플러스'
    if '스포츠 라인' in x:
        return '스포츠'
    if '스포츠 스페셜'   in x:
        return '스포츠 스페셜'
    if 'Advantage'  in x:
        return '어드밴티지'
    if 'Luxury Line' in x:
        return '럭셔리'
    if 'M Sport Edition' in x:
        return 'M 스포츠'
    if '기본형' in x:
        return '기본형'
    if '이피션트' in x:
        return '이피션트'
    if  'M스포츠' in x:
        return 'M 스포츠'
    if 'M Sport Package' in x:
        return 'M 스포츠'
    if 'M Sport' in x:
        return 'M 스포츠'
    if ' 330e Luxury ' in x:
        return '럭셔리'
    if 'DPE'  in x:
        return 'DPE'
    if '디자인 퓨어 엑설런스' in x:
        return '디자인 퓨어 엑설런스'
    if 'M 에어로 다이나믹' in x:
        return 'M 에어로 다이나믹'
    if 'M 스포츠 플러스' in x:
        return 'M 스포츠 플러스'
    if 'ED에디션' in x:
        return 'ED 에디션'
    if 'M 스포츠 쉐도우' in x:
        return 'M 스포츠 쉐도우'
    if '어반 팩1 5도어' in x:
        '어판 팩1'
    if 'M 스포츠 프리미엄' in x:
        return 'M 스포츠 프리미엄'
    if 'M Sport Plus' in x:
        return 'M 스포츠 플러스'
    if '솔+' in x:
        return '솔+'
    if 'M 스포츠 섀도우'in x:
        return 'M 스포츠 쉐도우'
    if '조이 퍼스트 에디션'in x:
        return '조이 퍼스트 에디션'
    if 'M 스포츠 퍼스트 에디션'in x:
        return 'M 스포츠 퍼스트 에디션'
    if 'M 스포츠 리미티드 ' in x:
        return 'M 스포츠 리미티드'
    if '컨패티션 헤리티지' in x:
        return '컴패티션 헤리티지 에디션'
    if '프리미엄' in x:
        return '프리미엄'
    if 'M 스포츠' in x:
        return 'M 스포츠'
    if '스포츠' in x:
        return 'M 스포츠'
    if '럭셔리' in x:
        return '럭셔리'
    if '스페셜 에디션' in x:
        'M 스포츠 스페셜 에디션'
    if 'Luxury' in x:
        return '럭셔리'
    if 'xLine' in x:
        return 'xLine'
    if 'M 퍼포먼스' in x:
        return 'M 퍼포먼스'
    if '조이' in x:
        return '조이'
    if 'M 스포츠 에디션' in x:
        return 'M 스포츠'
    if '하이' in x:
        return '하이'
    if '에어로다이나믹' in x:
        return 'M 에어로 다이나믹'
    if '어반' in x:
        return '어반'
    if '프레스티지' in x:
        return '프레스티지'
    if '팩1' in x:
        return '어반 팩1'
    if 'F20' in x:
        return 'F20'
    if 'G20' in x:
        return 'G20'
    if 'F32' in x:
        return 'F32'
    if 'G01' in x:
        return 'G01'
    if 'G11' in x:
        return 'G11'
    
    else:
        return 'nan'
   
 


# In[8]:


def model(x):
    if '그란쿠페 220' in x:
        return '그란쿠페 220'
    elif '그란쿠페 218' in x:
        return '그란쿠페 218'
    elif '그란쿠페 235' in x:
        return '그란쿠페 235'
    elif '340' in x:
        return '340'
    elif '330C 쿠페' in x:
        return '330C 쿠페'
    elif '428 컨버터블' in x:
        return '428 컨버터블'
    elif '730L' in x:
        return '730L'
    elif '740L' in x:
        return '740L'
    elif '750L' in x:
        return '750L'
    elif '420 컨버터블' in x:
        return '420 컨버터블'
    elif '440 Coupe' in x:
        return '440 쿠페'
    elif '325' in x:
        return '325'
    elif '118' in x:
        return '118'
    elif '320' in x:
        return '320'
    elif '330' in x:
        return '330'
    elif '530' in x:
        return '530'
    elif '520' in x:
        return '520'
    elif 'X1' in x:
        return 'X1'
    elif 'X5' in x:
        return 'X5'
    elif 'X6' in x:
        return 'X6'
    elif 'Z4'  in x:
        return 'Z4'
    elif '325C 컨버터블' in x:
        return '325C 컨버터블'
    elif '428 컨버터블' in x:
        return '428 컨버터블'
    elif '640 그란쿠페' in x:
        return '640 그란쿠페'
    elif '640 그란투리스모':
        return '640 그란투리스모'
    elif '528' in x:
        return '528'
    elif '730' in x:
        return '730'
    elif '328 컨버터블' in x:
        return '328 컨버터블'
    elif '420 그란쿠페' in x:
        return '420 그란쿠페'
    elif '740' in x:
        return '740'
    elif '750' in x:
        return '750'
    elif 'i3' in x:
        return 'i3'
    elif '523' in x:
        return '523'
    elif 'X4' in x:
        return 'X4'
    elif'428 쿠페' in x:
        return '428 쿠페'
    elif 'X7' in x:
        return 'X7'
    elif '525' in x:
        return '525'
    elif '640 그란쿠페' in x:
        return '640 그란쿠페'
    elif '335 컨버터블' in x:
        return '335 컨버터블'
    elif '535' in x:
        return '535'
    elif '550'in x:
        return '550'
    elif '420 쿠페' in x:
        return '420 쿠페' 
    elif 'X2' in x:
        return 'X2'
    elif 'X3' in x:
        return 'X3'   
    else: 
        return 'nan'


# In[9]:


def level(x):
    if '조이 퍼스트 에디션' in x:
        return '1'
    if '조이' in x:
        return '1'
    if '스포츠 리미티드' in x:
        return '4'
    if 'M 스포츠 플러스'in x:
        return '3'
    if 'M 스포츠 쉐도우' in x:
        return '4'
    if '스포츠' in x:
        return '2'
    if '럭셔리 플러스'in x:
        return '2'
    if '럭셔리' in x:
        return '3'
    if 'ED 에디션' in x:
        return '1'
    if 'xLine' in x:
        return '1'
    if '스페셜 에디션' in x:
        return '3'
    if '프레스티지' in x:
        return '4'
    if 'M 에어로 다이나믹' in x:
        return '4'
    if '솔+' in x:
        return '2'
    if '인디비주얼' in x:
        return '3'
    if '디자인 퓨어 엑셀런스' in x:
        return '3'
    if '어반' in x:
        return '1'
    if '기본형' in x:
        return '1'
    if '이피션트' in x:
        return '1'
    if 'F20' in x:
        return '1'
    if 'G20' in x:
        return '1'
    if 'F32' in x:
        return '1'
    if 'G01' in x:
        return '1'
    if 'G11' in x:
        return '1'
    else: 
        return np.nan


# In[10]:


def sam(x):
    if "PE" in x:
        return "1"

    if "SE 플러스" in x:
        return "1"

    if "SE 블랙" in x:
        return "1"

    if "SE 플레져" in x:
        return "1"

    if "SE" in x:
        return "1"

    if "XE" in x:
        return "1"

    if "LE 플러스" in x:
        return "2"

    if "LE 익스클루시브" in x:
        return "2"

    if "LE" in x:
        return "2"

    if "RE 시그니처" in x:
        return "3"

    if "RE" in x:
        return "3"

    if "Premiere" in x:
        return "4"

    if "인텐스" in x:
        return "2"

    if "프레스티지" in x:
        return "4"

    if "클래식" in x:
        return "1"

    if "씨티" in x:
        return "1"

    if "D 프리미엄" in x:
        return "1"

    else:
        return np.nan


    


# In[11]:


def gene(x):
    if "3.3 프리미엄 럭셔리" in x:
        return "2"
    if "3.3 프레스티지" in x:
        return "2"
    if "3.3t 프리미엄 럭셔리" in x:
        return "2"
    if "3.3t 스포츠" in x:
        return "3"
    if "3.8 프리미엄 럭셔리" in x:
        return "2" 
    if "3.8 럭셔리" in x:
        return "2" 
    if "3.8 프레스티지" in x:
        return "3" 
    if "5.0 리무진" in x:
        return "4" 
    if "5.0 프레스티지" in x:
        return "4" 
    if "럭셔리" in x:
        return "2" 
    if "2.0t" in x:
        return "1"
    if "2.0" in x:
        return "1"
    if "2.2" in x:
        return "1"
    if "2.5t" in x:
        return "1"
    if "2.5" in x:
        return "1"
    if "3.0" in x:
        return "1"
    if "3.3t" in x:
        return "2"
    if "3.3" in x:
        return "1"
    if "3.5t" in x:
        return "1"
    if "3.5" in x:
        return "1"
    if "3.8" in x:
        return "1"
    if "5.0" in x:
        return "1"
    if "" in x:
        return "2"
    else:
        return np.nan


# In[12]:


def hyun(x):
    if "스타일" in x:
        return "1"
    if "벨류 플러스" in x:
        return "1"
    if "케어플러스" in x:
        return "1"
    if "스마트" in x:
        return "1"
    if "모던 베이직" in x:
        return "1"
    if "모던" in x:
        return "1"
    if "프리미엄" in x:
        return "2"
    if "프리미엄스페셜" in x:
        return "2"
    if "익스클루시브" in x:
        return "3"
    if "익스클루시브 스페셜" in x:
        return "3"
    if "셀러브리티" in x:
        return "3" 
    if "프레스티지" in x:
        return "4" 
    if "인스퍼레이션" in x:
        return "4" 
    if "디럭스" in x:
        return "1" 
    if "럭셔리" in x:
        return "2" 
    if "프리미어" in x:
        return "3" 
    if "프라임" in x:
        return "4"
    else:
        return np.nan
        


# In[100]:


#KB 차차차 색깔별 추출
# brand groupby로 짜르기
# Mercedes = Mercedes.groupby('name').filter(lambda x : len(x)>10) 나중에 page 많이 긁어올때는 groupby 추가
# Mercedes = Mercedes.groupby('info').filter(lambda x : len(x)>15)
def color(webdriver):
    dr = webdriver.Chrome(ChromeDriverManager().install())
    brand_a=[]
    year_a=[]
    info_a=[]
    price_a=[]
    brand_b=[]
    year_b=[]
    info_b=[]
    price_b=[]
    brand_c=[]
    year_c=[]
    info_c=[]
    price_c=[]
    brand_d=[]
    year_d=[]
    info_d=[]
    price_d=[]
    brand_e=[]
    year_e=[]
    info_e=[]
    price_e=[]
    brand_f=[]
    year_f=[]
    info_f=[]
    price_f=[]
    brand_g=[]
    year_g=[]
    info_g=[]
    price_g=[]
    brand_h=[]
    year_h=[]
    info_h=[]
    price_h=[]
    brand_i=[]
    year_i=[]
    info_i=[]
    price_i=[]
    brand_j=[]
    year_j=[]
    info_j=[]
    price_j=[]
    brand_k=[]
    year_k=[]
    info_k=[]
    price_k=[]
    brand_l=[]
    year_l=[]
    info_l=[]
    price_l=[]
    for color in range(6001,6013,1):
        for domain in range(1,501,1):
            page='https://www.kbchachacha.com/public/search/main.kbc#!?_menu=buy&page='+str(domain)+'sort=-orderDate&accidentYn=Y&color=00'+str(color)
            dr.get(page)
            sleep(randint(2,6))
            soup= bs(dr.page_source,'html.parser')
            brands=soup.find_all(class_=["tit"])
            pages=soup.find_all(class_=['first'])
            infos=soup.find_all(class_=['data-in'])
            prices=soup.find_all(class_=['pay'])
            

            if color == 6001:

                for brand in brands:
                        brand_a.append(brand.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for page in pages:
                        year_a.append(page.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for info in infos:
                        info_a.append(info.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for price in prices:
                        price_a.append(price.get_text().replace('\t','').replace('\n','').replace('실차주',''))
                    
            elif color == 6002:
                
                for brand in brands:
                        brand_b.append(brand.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for page in pages:
                        year_b.append(page.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for info in infos:
                        info_b.append(info.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for price in prices:
                        price_b.append(price.get_text().replace('\t','').replace('\n','').replace('실차주',''))
            
            elif color == 6003:
                for brand in brands:
                        brand_c.append(brand.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for page in pages:
                        year_c.append(page.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for info in infos:
                        info_c.append(info.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for price in prices:
                        price_c.append(price.get_text().replace('\t','').replace('\n','').replace('실차주',''))
            
            elif color == 6004:
                for brand in brands:
                    brand_d.append(brand.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for page in pages:
                    year_d.append(page.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for info in infos:
                    info_d.append(info.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for price in prices:
                    price_d.append(price.get_text().replace('\t','').replace('\n','').replace('실차주',''))
            
            elif color == 6005:
                for brand in brands:
                    brand_e.append(brand.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for page in pages:
                    year_e.append(page.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for info in infos:
                    info_e.append(info.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for price in prices:
                    price_e.append(price.get_text().replace('\t','').replace('\n','').replace('실차주',''))
                    
            elif color == 6006:
                for brand in brands:
                    brand_f.append(brand.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for page in pages:
                    year_f.append(page.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for info in infos:
                    info_f.append(info.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for price in prices:
                    price_f.append(price.get_text().replace('\t','').replace('\n','').replace('실차주',''))
                    
            elif color == 6007:
                for brand in brands:
                    brand_g.append(brand.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for page in pages:
                    year_g.append(page.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for info in infos:
                    info_g.append(info.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for price in prices:
                    price_g.append(price.get_text().replace('\t','').replace('\n','').replace('실차주',''))
                    
            elif color == 6008:
                for brand in brands:
                    brand_h.append(brand.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for page in pages:
                    year_h.append(page.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for info in infos:
                    info_h.append(info.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for price in prices:
                    price_h.append(price.get_text().replace('\t','').replace('\n','').replace('실차주',''))
                    
            elif color == 6009:
                for brand in brands:
                    brand_i.append(brand.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for page in pages:
                    year_i.append(page.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for info in infos:
                    info_i.append(info.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for price in prices:
                    price_i.append(price.get_text().replace('\t','').replace('\n','').replace('실차주',''))
                    
            elif color == 6010:
                for brand in brands:
                    brand_j.append(brand.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for page in pages:
                    year_j.append(page.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for info in infos:
                    info_j.append(info.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for price in prices:
                    price_j.append(price.get_text().replace('\t','').replace('\n','').replace('실차주',''))
                     
            elif color == 6011:
                for brand in brands:
                    brand_k.append(brand.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for page in pages:
                    year_k.append(page.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for info in infos:
                    info_k.append(info.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for price in prices:
                    price_k.append(price.get_text().replace('\t','').replace('\n','').replace('실차주','')) 
                    
            elif color == 6012:
                for brand in brands:
                    brand_l.append(brand.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for page in pages:
                    year_l.append(page.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for info in infos:
                    info_l.append(info.get_text().replace('\t','').replace('\n','').replace('실차주',''))

                for price in prices:
                    price_l.append(price.get_text().replace('\t','').replace('\n','').replace('실차주',''))                           
                                   
                    
    dr.quit()
    brand_a=pd.DataFrame(brand_a)            
    year_a=pd.DataFrame(year_a)
    info_a=pd.DataFrame(info_a)
    price_a=pd.DataFrame(price_a)
    brand_b=pd.DataFrame(brand_b)            
    year_b=pd.DataFrame(year_b)
    info_b=pd.DataFrame(info_b)
    price_b=pd.DataFrame(price_b)
    brand_c=pd.DataFrame(brand_c)            
    year_c=pd.DataFrame(year_c)
    info_c=pd.DataFrame(info_c)
    price_c=pd.DataFrame(price_c)
    brand_d=pd.DataFrame(brand_d)
    year_d=pd.DataFrame(year_d)
    info_d=pd.DataFrame(info_d)
    price_d=pd.DataFrame(price_d)
    brand_e=pd.DataFrame(brand_e)
    year_e=pd.DataFrame(year_e)
    info_e=pd.DataFrame(info_e)
    price_e=pd.DataFrame(price_e)
    brand_f=pd.DataFrame(brand_f)
    year_f=pd.DataFrame(year_f)
    info_f=pd.DataFrame(info_f)
    price_f=pd.DataFrame(price_f)
    brand_g=pd.DataFrame(brand_g)
    year_g=pd.DataFrame(year_g)
    info_g=pd.DataFrame(info_g)
    price_g=pd.DataFrame(price_g)
    brand_h=pd.DataFrame(brand_h)
    year_h=pd.DataFrame(year_h)
    info_h=pd.DataFrame(info_h)
    price_h=pd.DataFrame(price_h)
    brand_i=pd.DataFrame(brand_i)
    year_i=pd.DataFrame(year_i)
    info_i=pd.DataFrame(info_i)
    price_i=pd.DataFrame(price_i)
    brand_j=pd.DataFrame(brand_j)
    year_j=pd.DataFrame(year_j)
    info_j=pd.DataFrame(info_j)
    price_j=pd.DataFrame(price_j)
    brand_k=pd.DataFrame(brand_k)
    year_k=pd.DataFrame(year_k)
    info_k=pd.DataFrame(info_k)
    price_k=pd.DataFrame(price_k)
    brand_l=pd.DataFrame(brand_l)
    year_l=pd.DataFrame(year_l)
    info_l=pd.DataFrame(info_l)
    price_l=pd.DataFrame(price_l)
    results=pd.concat([brand_a,year_a,info_a,price_a],axis=1)
    results['color']='검정색'
    results['accident']='무사고'
    symbols=['brand','year','info','price','color','accident']
    results.columns=symbols
    results_b=pd.concat([brand_b,year_b,info_b,price_b],axis=1)
    results_b['color']='흰색'
    results_b['accident']='무사고'
    results_b.columns=symbols
    results_c=pd.concat([brand_c,year_c,info_c,price_c],axis=1)
    results_c['color']='회색'
    results_c['accident']='무사고'
    results_c.columns=symbols
    results_d=pd.concat([brand_d,year_d,info_d,price_d],axis=1)
    results_d['color']='흰색'
    results_d['accident']='무사고'
    results_d.columns=symbols
    results_e=pd.concat([brand_e,year_e,info_e,price_e],axis=1)
    results_e['color']='흰색'
    results_e['accident']='무사고'
    results_e.columns=symbols
    results_f=pd.concat([brand_f,year_f,info_f,price_f],axis=1)
    results_f['color']='기타'
    results_f['accident']='무사고'
    results_f.columns=symbols
    results_g=pd.concat([brand_g,year_g,info_g,price_g],axis=1)
    results_g['color']='기타'
    results_g['accident']='무사고'
    results_g.columns=symbols
    results_h=pd.concat([brand_h,year_h,info_h,price_h],axis=1)
    results_h['color']='기타'
    results_h['accident']='무사고'
    results_h.columns=symbols
    results_i=pd.concat([brand_i,year_i,info_i,price_i],axis=1)
    results_i['color']='기타'
    results_i['accident']='무사고'
    results_i.columns=symbols
    results_j=pd.concat([brand_j,year_j,info_j,price_j],axis=1)
    results_j['color']='기타'
    results_j['accident']='무사고'
    results_j.columns=symbols
    results_k=pd.concat([brand_k,year_k,info_k,price_k],axis=1)
    results_k['color']='기타'
    results_k['accident']='무사고'
    results_k.columns=symbols
    results_l=pd.concat([brand_l,year_l,info_l,price_l],axis=1)
    results_l['color']='기타'
    results_l['accident']='무사고'
    results_l.columns=symbols
    result=pd.concat([results,results_b,results_c,results_d,results_e,results_f,results_g,results_h,results_i,results_j,results_k,results_l],ignore_index=True,sort=True)
   

    result['info'] = result['info'].astype('str')
    result[['mile','location']] = result['info'].str.split("km",expand=True,)
    result['brand'] = (result['brand'].str.replace('더','').str.replace('뉴','').str.replace('올','').str.replace('NEW','')
                   .str.replace('The New','').str.replace('넥스트','').str.replace('ALL NEW','').str.replace('all new','')
                   .str.replace('직거래','').str.replace('New','').str.replace('ALL','').str.replace('9-5','').str.replace('뷰티플','').str.replace('All',''))
    result['price'] = result['price'].str.replace('\D', '')
    result=result.join(result['brand'].str.split(' ', expand=True).fillna(np.nan))
    result=result.replace(r'^\s*$', np.nan, regex=True)
    

    result=result.dropna(subset=[1])
    result['model'] =result[2].fillna(result[3]).fillna(result[4]).fillna(result[5]).fillna(result[6]).fillna(result[7]).fillna(result[8])
    result['models']=result[3].fillna(result[4]).fillna(result[5]).fillna(result[6]).fillna(result[7]).fillna(result[8]).fillna(result[9])
    result['modelx']=result[4].fillna(result[5]).fillna(result[6]).fillna(result[7]).fillna(result[8]).fillna(result[9])
    result['modely'] = result[result.columns[19:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
    result['modely']=(result['modely'].str.replace("(","").str.replace(")",""))
    
    result['years'] = result['year'].apply(selector)
    result=result[[0,1,'modely','mile','years','accident','color','location','price']]
    result.columns=['brand','info','trim','km','year','accident','color','location','price']
    

    result['type']= result['trim'].apply(gas)
    result = result.dropna(axis=0, subset=['type'])
    result['wd']= result['info'].apply(spec)
    result = result[['brand','info','trim','type','km','year','accident','color','location','price','wd']]
    del result['location']
    result.to_csv('kb크롤링종합.csv',mode='w',header=True,encoding='UTF-8',index=False)


# In[34]:


color(webdriver)


# In[67]:


#브랜드별 추출
def data():
    #BMW 
    df=pd.read_csv('kb크롤링종합.csv',encoding='UTF-8')
    df1= df[df.brand.str.contains('BMW',case=False)]
    df1['info'] = df1['info'].astype('str') 
    df1['trim'] = df1['trim'].str.replace(r"\(.*\)","")
    df1['info'] = df1['info'].str.replace(r"\(.*\)","")
    df1.replace(re.compile('F.*'), '', inplace=True)
    df1['info']=(df1['info'].str.replace('GT',''))
    df1['infos']=df1['trim']+df1['info']

    df1['trim']= df1['trim'].apply(option)
    df1['infos'] = (df1['infos'].str.replace('5시리즈','').str.replace('3시리즈','')
    .str.replace('7시리즈','').str.replace('4시리즈','').str.replace('1시리즈','').str.replace('5시리즈 GT','')
    .str.replace('3시리즈 GT','').str.replace('6시리즈','').str.replace('2시리즈 액티브 투어러','')
    .str.replace('6시리즈 GT','').str.replace('1시리즈','').str.replace('2시리즈 그란쿠페','')
    .str.replace('2시리즈','').str.replace('8시리즈','').str.replace('6시리즈',''))
    df1['infos'] = (df1['infos'].str.replace('xLine','').str.replace('DPE','').str.replace('디자인 퓨어 엑설런스','')
    .str.replace('M 에어로 다이나믹','')
    .str.replace('럭셔리','')
    .str.replace('i 퍼포먼스','')
    .str.replace('인디비주얼','')
    .str.replace('럭셔리 플러스','')
    .str.replace('컴페티션 에디션','')
    .str.replace('스페셜 에디션' ,'')
    .str.replace('디자인 퓨어 엑셀런스','')
    .str.replace('프리미엄','')
    .str.replace('블랙 앤 화이트' ,'')
    .str.replace('컴패티션','')
    .str.replace('스포츠 리미티드','')
    .str.replace('스포츠 팩1' ,'')
    .str.replace('CS 25주년' ,'')
    .str.replace('조이 퍼스트 에디션','')
    .str.replace('페인트워크 에디션' ,'')
    .str.replace('M 스포츠 쉐도우' ,'')
    .str.replace('페인트워크 에디션' ,'')
    .str.replace('M 스포츠 퍼스트 에디션' ,'')
    .str.replace('M 퍼포먼스' ,'')
    .str.replace('M 퍼포먼스 에디션 25th' ,'')
    .str.replace('M4 쿠페 컨패티션 헤리티지','')
    .str.replace('M 에어로다이나믹 스페셜 에디션','')
    .str.replace('스포츠 섀도우','')
    .str.replace('조이','')
    .str.replace('M 스포츠 에디션','')
    .str.replace('스포츠 리미티드','')
    .str.replace('M 스포츠 플러스','')
    .str.replace('스포츠 라인','')
    .str.replace('스포츠 스페셜','')
    .str.replace('Advantage','')
    .str.replace('Luxury Line','')
    .str.replace('M Sport Edition','')
    .str.replace('기본형','')
    .str.replace('이피션트','')
    .str.replace('M스포츠','')
    .str.replace('M Sport Package','')
    .str.replace('M Sport','')
    .str.replace(' 330e Luxury ','')
    .str.replace('Luxury','')
    .str.replace('스포츠','')
    .str.replace('xLine','')
    .str.replace('DPE','')
    .str.replace('디자인 퓨어 엑설런스','')
    .str.replace('M 에어로 다이나믹','')
    .str.replace('M 에어로 다이나믹','')
    .str.replace('럭셔리','')
    .str.replace('M','')
    .str.replace('M 스포츠 플러스','')
    .str.replace('5도어','')
    .str.replace('ED에디션','')
    .str.replace('어반 팩1 5도어','')
    .str.replace('M 스포츠 프리미엄','')
    .str.replace('M Sport Plus','')
    .str.replace('솔+','')
    .str.replace('M 스포츠 섀도우','')
    .str.replace('조이 퍼스트 에디션','')
    .str.replace('M 스포츠 퍼스트 에디션','')
    .str.replace('M 스포츠 리미티드 ','')
    .str.replace('컨패티션 헤리티지','')
    .str.replace('프리미엄','')
    .str.replace('스페셜 에디션','')
    .str.replace('Plus','')
    .str.replace('어반팩 1','')
    .str.replace('세단 CP','')
    .str.replace('어반','')
    .str.replace('프레스티지','')
    .str.replace('i퍼포먼스','')
    .str.replace('xDrive','')
    .str.replace('i','').str.replace('d','').str.replace('e',''))
    df1['km']=df1['km'].str.replace(',','')
    df1.columns.str.strip()
    df1.infos = df1.infos.replace('\s+', ' ', regex=True)
    df1.trim = df1.trim.replace('\s+', ' ', regex=True)

    df1['infos']=df1['infos'].apply(model)
    df1 = df1[df1['infos'].notna()]
    df1['trim'] = df1['trim'].astype('str') 
    df1=df1[['brand','infos','trim','type','km','year','accident','color','wd','price']]
    df1.columns=['brand','name','trim','type','km','year','accident','color','wd','price']
    df1.to_csv('BMW추출.csv',mode='w',header=True,encoding='UTF-8',index=False)
    
    
    #벤츠
    
    
    df2=df[df.brand.str.contains('벤츠',case=False)]
    df2['info'] = df2['info'].str.replace('A-클래스 W176', 'A-클래스')
    df2['info'] = df2['info'].str.replace('A-클래스 W177', 'A-클래스')

    df2['info'] = df2['info'].str.replace('B-클래스 W245', 'B-클래스')
    df2['info'] = df2['info'].str.replace('B-클래스 W246', 'B-클래스')
    df2['info'] = df2['info'].str.replace('-클래스', '')
    df2['info'] = df2['info'].str.replace('클래스', '')
    
    df2['trim'] = df2['trim'].str.replace('2matic', '')
    df2['trim'] = df2['trim'].str.replace('4matic', '')
    df2['trim'] = df2['trim'].str.replace('4maitc', '')
    df2['trim'] = df2['trim'].str.replace('line', '')
    df2['trim'] = df2['trim'].str.replace('하이브리드', '') 
    df2['trim'] = df2['trim'].str.replace(' d', '') 
    df2['trim'] = df2['trim'].str.replace('에디션1', '')
    df2['trim'] = df2['trim'].str.replace('스탠다드', '')
    df2['trim'] = df2['trim'].str.replace('디젤', '')
    df2['trim'] = df2['trim'].str.replace('가솔린', '')

    df2['trim'] = df2['trim'].str.replace('블루이피션시', 'cdi')
    df2['trim'] = df2['trim'].str.replace('아방가르드', '')
    df2['trim'] = df2['trim'].str.replace('익스클루시브', '')
    df2['trim'] = df2['trim'].str.replace('프리미엄', '')
    df2['trim'] = df2['trim'].str.replace('인텔리전트 드라이브', '')
    df2['trim'] = df2['trim'].str.replace('intelligent drive', '')
    df2['trim'] = df2['trim'].str.replace('()', '')
    df2['trim'] = df2['trim'].str.replace('vip', '')
    df2['trim'] = df2['trim'].str.replace('데지뇨 에디션', '')
    df2['trim'] = df2['trim'].str.replace('그랜드 에디션', '')
    df2['trim'] = df2['trim'].str.replace('스타일패키지', '')
    df2['trim'] = df2['trim'].str.replace('패키지', '')
    df2['trim'] = df2['trim'].str.replace('에디션 c', '')
    df2['trim'] = df2['trim'].str.replace('나이트 패키지', '')
    df2['trim'] = df2['trim'].str.replace('나이트', '')
    df2['trim'] = df2['trim'].str.replace('에디션 10', '')
    df2['trim'] = df2['trim'].str.replace('에디션 463', '')
    df2['trim'] = df2['trim'].str.replace('퍼포먼스 에디션', '')
    df2['trim'] = df2['trim'].str.replace('데지뇨  에디션', '')
    df2['trim'] = df2['trim'].str.replace('슈팅브레이크', '')
    df2['trim'] = df2['trim'].str.replace('파노라마 썬루프', '')
    df2['trim'] = df2['trim'].str.replace('스포츠팩', '')
    df2['trim'] = df2['trim'].str.replace('cgi', '')
    df2['trim'] = df2['trim'].str.replace('스포츠', '')
    df2['trim'] = df2['trim'].str.replace('디지뇨', '')
    df2['trim'] = df2['trim'].str.replace('+', '')
    
                                
    df2['s'] = np.where(df2['trim'].str.contains('카브리올레'),'카브리올레',
                        np.where(df2['trim'].str.contains('쿠페'),'쿠페',
                                np.where(df2['trim'].str.contains('프리미엄 쿠페'),'프리미엄 쿠페',
                                            np.where(df2['trim'].str.contains('해치백'),'해치백',
                                                    np.where(df2['trim'].str.contains('세단'),'세단',
                                                            np.where(df2['trim'].str.contains('엘레강스'),'엘레강스',
                                                                        np.where(df2['trim'].str.contains('스포츠 패키지'),'스포츠 패키지',
                                                                                np.where(df2['trim'].str.contains('에스테이트'),'에스테이트',
                                                                                        np.where(df2['trim'].str.contains('마이바흐'),'마이바흐',
                                                                                                      np.where(df2['trim'].str.contains('amg'),'amg', ''))))))))))
    df2['trim'] = df2['trim'].fillna('') + ' '+ df2['s'].fillna('')    
    df2['trim'] = df2['trim'].str.replace('아방가르드', '')
    df2['trim'] = df2['trim'].str.replace('avantgarde', '')                                
    df2['trim'] = df2['trim'].str.replace('익스클루시브', '') 
    df2['trim'] = df2['trim'].str.replace('exclusive', '') 
    df2['trim'] = df2['trim'].str.replace('(w213)', '')                                     
    df2['trim'] = df2['trim'].str.replace('카브리올레', '')
    df2['trim'] = df2['trim'].str.replace('카브레올레', '')
    df2['trim'] = df2['trim'].str.replace('쿠페', '')
    df2['trim'] = df2['trim'].str.replace('프리미엄 쿠페', '')
    df2['trim'] = df2['trim'].str.replace('해치백', '')
    df2['trim'] = df2['trim'].str.replace('세단', '')
    df2['trim'] = df2['trim'].str.replace('엘레강스', '')
    df2['trim'] = df2['trim'].str.replace('스포츠 패키지', '')
    df2['trim'] = df2['trim'].str.replace('엘에스테이트레강스', '')
    df2['trim'] = df2['trim'].str.replace('마이바흐', '')
    df2['trim'] = df2['trim'].str.replace('에스테이트', '')
    df2['trim'] = df2['trim'].str.replace('에디션', '')
    df2['trim'] = df2['trim'].str.replace('amg', '')
    df2['trim'] = df2['trim'].str.replace('롱바디', '')
    
    df2['trim'] = df2['trim'].str.strip()
    df2['trim'] = df2['trim'].str.lstrip()
    
    df2['trim'] = df2['trim'].str.replace('4.0l', '4.0')
    df2['trim'] = df2['trim'].str.replace('4.0d', '4.0')
    df2['trim'] = df2['trim'].str.replace('s 4.0 에디션1', 's 4.0')
    df2['trim'] = df2['trim'].str.replace('s63 amg+', 's63 amg')
    df2['trim'] = df2['trim'].str.replace('s550v', 's550')
    df2['trim'] = df2['trim'].str.replace('s550l', 's550')
    df2['trim'] = df2['trim'].str.replace('s560el', 's560')
    df2['trim'] = df2['trim'].str.replace('s560l', 's560')
    df2['trim'] = df2['trim'].str.replace('s600l', 's600')
    df2['trim'] = df2['trim'].str.replace('230k', '230')
    df2['trim'] = df2['trim'].str.replace('e220d', 'e220')
    df2['trim'] = df2['trim'].str.replace('s63 amg +', 's63 amg')
    df2['trim'] = df2['trim'].str.replace('glc300e', 'glc300')
    df2['trim'] = df2['trim'].str.replace('s63 amg + 쿠페', 's63 amg 쿠페')
    df2['trim'] = df2['trim'].str.replace('e220   스포츠', 'e220d  amg')
    df2['trim'] = df2['trim'].str.replace('e300e', 'e300')
    df2['trim'] = df2['trim'].str.replace('마이바흐 s650 풀만', '마이바흐 s650')
    df2['trim'] = df2['trim'].str.replace('230ge', '230')
    df2['trim'] = df2['trim'].str.replace('280sel', '280')
    df2['trim'] = df2['trim'].str.replace('300d', '300')
    df2['trim'] = df2['trim'].str.replace('300sd', '300')
    df2['trim'] = df2['trim'].str.replace('300sel', '230')
    df2['trim'] = df2['trim'].str.replace('500sel', '500')
    df2['trim'] = df2['trim'].str.replace('560sel', '560')
    df2['trim'] = df2['trim'].str.replace('a180 스타일', 'a180')
    df2['trim'] = df2['trim'].str.replace('a180 나이트', 'a180')
    df2['trim'] = df2['trim'].str.replace('a200d', 'a200')
    df2['trim'] = df2['trim'].str.replace('amg g63 에디선', 'amg g63')
    df2['trim'] = df2['trim'].str.replace('amg glc63 +', 'amg glc63')
    df2['trim'] = df2['trim'].str.replace('amg glc63 s +', 'amg glc63 s')
    df2['trim'] = df2['trim'].str.replace('c180k', 'c180')
    df2['trim'] = df2['trim'].str.replace('c200  amg', 'c200 amg')
    df2['trim'] = df2['trim'].str.replace('cla45 amg  50주년 에디션', 'c200 amg')
    df2['trim'] = df2['trim'].str.replace('glss 4.0', 'glss 4.0d')
    df2['trim'] = df2['trim'].str.replace('s63 amg+ 카브리올레', 's63 amg 카브리올레')
    df2['trim'] = df2['trim'].str.replace('s63 amg카브리올레', 's63 amg 카브리올레')
    df2['trim'] = df2['trim'].str.replace('s500l 데지뇨 에디션', 's500')
    df2['trim'] = df2['trim'].str.replace('s 4.04도어 63 s +', 's 4.0')
    df2['trim'] = df2['trim'].str.replace('s 4.04도어 63 s +', 's s 4.0')
    df2['trim'] = df2['trim'].str.replace('sp', '')
    df2['trim'] = df2['trim'].str.replace('\(\) e220', 'e220')
    del df2['s']
    df2=df2[['brand','info','trim','type','km','year','accident','color','wd','price']]
    df2.columns=['brand','name','trim','type','km','year','accident','color','wd','price']
    df2.to_csv('벤츠추출.csv',mode='w',header=True,encoding='utf-8',index=False)
    

    
    #아우디
    
    df3=df[df.brand.str.contains('아우디',case=False)]
    df3['trim'] = df3.apply(lambda x: x['trim'].strip('콰트로'), axis = 1)
    df3['trim'] = df3.apply(lambda x: x['trim'].replace('콰트로',''), axis = 1)
    df3['upgrade'] = ""

    for i in range(0, len(df3)):
        if df3['trim'].str.contains('엔트리')[i]:
            df3['upgrade'][i] = '엔트리'
        elif df3['trim'].str.contains('스포트라인')[i]:
            df3['upgrade'][i] = '스포트라인'

        elif df3['trim'].str.contains('다이나믹')[i]:
            df3['upgrade'][i] = '다이나믹'

        elif df3['trim'].str.contains('리미티드')[i]:
            df3['upgrade'][i] = '리미티드'

        elif df3['trim'].str.contains('프레스티지')[i]:
            df3['upgrade'][i] = '프레스티지'

        elif df3['trim'].str.contains('프리미엄')[i]:
            df3['upgrade'][i] = '프리미엄'

        elif df3['trim'].str.contains('S-LINE')[i]:
            df3['upgrade'][i] = 'S-LINE'

        elif df3['trim'].str.contains('S-line')[i]:
            df3['upgrade'][i] = 'S-line'

        elif df3['trim'].str.contains('S-Line')[i]:
            df3['upgrade'][i] = 'S-Line'

        elif df3['trim'].str.contains('쿠페')[i]:
            df3['upgrade'][i] = '쿠페'

        elif df3['trim'].str.contains('카브리올레')[i]:
            df3['upgrade'][i] = '카브리올레'

        elif df3['trim'].str.contains('스포츠')[i]:
            df3['upgrade'][i] = '스포츠'

        elif df3['trim'].str.contains('스파이더')[i]:
            df3['upgrade'][i] = '스파이더'

        else :
            return np.nan
   
    df3.drop(['trim'], axis = 1, inplace = True)
    df3['info'] = df3.apply(lambda x: x['info'].replace('(4S)',''), axis = 1)
    df3['info'] = df3.apply(lambda x: x['info'].replace('(8V)',''), axis = 1)
    df3['info'] = df3.apply(lambda x: x['info'].replace('(8P)',''), axis = 1)
    df3['info'] = df3.apply(lambda x: x['info'].replace('뉴',''), axis = 1)
    df3['info'] = df3.apply(lambda x: x['info'].strip(), axis = 1)
    df3=df3[['brand','info','upgrade','type','km','year','accident','color','wd','price']]
    df3.columns = ['brand','name','trim','type','km', 'year','accident','color','wd','price']
    df3.to_csv('아우디추출.csv',mode='w',header=True,encoding='UTF-8',index=False)

    
    # 기아
    df4 = df[df.brand.str.contains('기아',case=False)]
    K5 = df4[df4['info'] == 'K5']
    K5.reset_index(inplace = True)
    K5.drop(['index'], axis = 1,inplace = True)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('가솔린',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('디젤',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('4WD',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('2WD',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('AWD',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('3세대',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('2세대',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('하이브리드',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('세부등급 없음',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].strip(), axis = 1)
    
    K5['upgrade'] = ""

    for i in range(0, len(K5)):

        if K5['trim'].str.contains('스탠다드')[i]:
            K5['upgrade'][i] = '스탠다드'

        elif K5['trim'].str.contains('스마트 스페셜')[i]:
            K5['upgrade'][i] = '스마트 스페셜'

        elif K5['trim'].str.contains('스마트')[i]:
            K5['upgrade'][i] = '스마트'


        elif K5['trim'].str.contains('디럭스')[i]:
            K5['upgrade'][i] = '디럭스'

        elif K5['trim'].str.contains('럭셔리 스페셜')[i]:
            K5['upgrade'][i] = '럭셔리 스페셜'

        elif K5['trim'].str.contains('럭셔리트렌디')[i]:
            K5['upgrade'][i] = '럭셔리 트렌디'

        elif K5['trim'].str.contains('럭셔리트랜디')[i]:
            K5['upgrade'][i] = '럭셔리 트렌디'

        elif K5['trim'].str.contains('럭셔리')[i]:
            K5['upgrade'][i] = '럭셔리'

        elif K5['trim'].str.contains('스타일 에디션')[i]:
            K5['upgrade'][i] = '스타일 에디션'

        elif K5['trim'].str.contains('트렌디')[i]:
            K5['upgrade'][i] = '트렌디'

        elif K5['trim'].str.contains('트랜디')[i]:
            K5['upgrade'][i] = '트렌디'

        elif K5['trim'].str.contains('W 스페셜')[i]:
            K5['upgrade'][i] = 'W 스페셜'

        elif K5['trim'].str.contains('프레스티지')[i]:
            K5['upgrade'][i] = '프레스티지'

        elif K5['trim'].str.contains('스페셜 에디션')[i]:
            K5['upgrade'][i] = '스페셜 에디션'

        elif K5['trim'].str.contains('노블레스 스페셜')[i]:
            K5['upgrade'][i] = '노블레스 스페셜'

        elif K5['trim'].str.contains('노블레스')[i]:
            K5['upgrade'][i] = '노블레스'

        elif K5['trim'].str.contains('시그니쳐')[i]:
            K5['upgrade'][i] = '시그니쳐'

        elif K5['trim'].str.contains('시그니처')[i]:
            K5['upgrade'][i] = '시그니쳐'

        elif K5['trim'].str.contains('인텔리전트')[i]:
            K5['upgrade'][i] = '시그니쳐'

        elif K5['trim'].str.contains('GT LINE')[i]:
            K5['upgrade'][i] = 'GT LINE'

        elif K5['trim'].str.contains('GT')[i]:
            K5['upgrade'][i] = 'GT'

        else :
            K5['upgrade'][i] = '스탠다드'
            
        # trim 행의 문자열 제거
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('스탠다드',''), axis = 1) 
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('스마트',''), axis = 1) 
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('디럭스',''), axis = 1) 
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('스타일',''), axis = 1)   
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('럭셔리',''), axis = 1)       
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('트랜디',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('W 스페셜',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('에디션',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('스페셜',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('인텔리전트',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('GT LINE',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('GT',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('프레스티지',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('트렌디',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('노블레스',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('시그니쳐',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('시그니처',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('렌터카용',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('수출형옵티마',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('기본형',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace('(',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].replace(')',''), axis = 1)
    K5['trim'] = K5.apply(lambda x: x['trim'].strip(), axis = 1)
    K5['type'] = K5.apply(lambda x: x['type'].replace('(일반인 구입)',''), axis = 1)
    K5['type'] = K5.apply(lambda x: x['type'].strip(), axis = 1)
   
    
    # trim 행의 문자열 제거
    K7 = df4[df4['info'] == 'K7']
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('가솔린',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('디젤',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('하이브리드',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('세부등급 없음',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].strip(), axis = 1)
    
    K7.reset_index(inplace = True)
    K7.drop(['index'], axis = 1,inplace = True)
    
    # trim열의 프리미엄 스포츠 여부를 upgrade 열에 추가
    K7['upgrade'] = ""

    for i in range(0, len(K7)):

        if K7['trim'].str.contains('스탠다드')[i]:
            K7['upgrade'][i] = '스탠다드'

        elif K7['trim'].str.contains('디럭스스페셜')[i]:
            K7['upgrade'][i] = '스마트 스페셜'

        elif K7['trim'].str.contains('디럭스')[i]:
            K7['upgrade'][i] = '디럭스'

        elif K7['trim'].str.contains('트렌디')[i]:
            K7['upgrade'][i] = '트렌디'

        elif K7['trim'].str.contains('럭셔리 스페셜')[i]:
            K7['upgrade'][i] = '럭셔리 스페셜' 

        elif K7['trim'].str.contains('럭셔리 프리미엄')[i]:
            K7['upgrade'][i] = '럭셔리 스페셜' 

        elif K7['trim'].str.contains('럭셔리')[i]:
            K7['upgrade'][i] = '럭셔리'

        elif K7['trim'].str.contains('프레스티지 스페셜')[i]:
            K7['upgrade'][i] = '프레스티지 스페셜'

        elif K7['trim'].str.contains('프레스티지 프리미엄')[i]:
            K7['upgrade'][i] = '프레스티지 스페셜'

        elif K7['trim'].str.contains('프레스티지')[i]:
            K7['upgrade'][i] = '프레스티지'

        elif K7['trim'].str.contains('리미티드')[i]:
            K7['upgrade'][i] = '리미티드'

        elif K7['trim'].str.contains('리미티드 에디션')[i]:
            K7['upgrade'][i] = '리미티드'

        elif K7['trim'].str.contains('노블레스 스페셜')[i]:
            K7['upgrade'][i] = '노블레스 스페셜'

        elif K7['trim'].str.contains('노블레스 프리미엄')[i]:
            K7['upgrade'][i] = '노블레스 스페셜'

        elif K7['trim'].str.contains('노블레스')[i]:
            K7['upgrade'][i] = '노블레스'

        elif K7['trim'].str.contains('월드컵')[i]:
            K7['upgrade'][i] = '월드컵 에디션'

        elif K7['trim'].str.contains('X 에디션')[i]:
            K7['upgrade'][i] = 'X 에디션'

        elif K7['trim'].str.contains('시그니쳐')[i]:
            K7['upgrade'][i] = '시그니쳐'

        elif K7['trim'].str.contains('시그니처')[i]:
            K7['upgrade'][i] = '시그니쳐'

        elif K7['trim'].str.contains('2.4 GDI 스페셜')[i]:
            K7['upgrade'][i] = '프레스티디 스페셜'

        else :
            K7['upgrade'][i] = '스탠다드'
            
        # trim 행의 문자열 제거
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('스탠다드',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('디럭스스페셜',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('디럭스',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('트렌디',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('럭셔리 스페셜',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('럭셔리 프리미엄',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('럭셔리',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('프레스티지 스페셜',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('프레스티지 프리미엄',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('프레스티지',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('리미티드',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('리미티드 에디션',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('노블레스 스페셜',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('노블레스 프리미엄',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('노블레스',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('월드컵',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('X 에디션',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('월드컵',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('시그니쳐',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('시그니처',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('스페셜',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('프리미어',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('(렌터카)',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('렌터카',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('수출형',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('기본형',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('일반인',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('(일반인)',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('(장애인용)',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('()',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('플러스',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('에디션',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].replace('택시형',''), axis = 1)
    K7['trim'] = K7.apply(lambda x: x['trim'].strip(), axis = 1)
    
    #모하비
    mohave = df4[df4['info'] == '모하비']
    mohave.reset_index(inplace = True)
    mohave.drop(['index'], axis = 1,inplace = True)
    mohave['trim'] = mohave.apply(lambda x: x['trim'].replace('가솔린',''), axis = 1)
    mohave['trim'] = mohave.apply(lambda x: x['trim'].replace('디젤',''), axis = 1)
    mohave['trim'] = mohave.apply(lambda x: x['trim'].replace('하이브리드',''), axis = 1)
    mohave['trim'] = mohave.apply(lambda x: x['trim'].replace('세부등급 없음',''), axis = 1)
    mohave['trim'] = mohave.apply(lambda x: x['trim'].replace('4WD',''), axis = 1)
    mohave['trim'] = mohave.apply(lambda x: x['trim'].replace('2WD',''), axis = 1)
    mohave['trim'] = mohave.apply(lambda x: x['trim'].strip(), axis = 1)
    
    mohave['upgrade'] = ""

    for i in range(0, len(mohave)):

        if mohave['trim'].str.contains('노블레스')[i]:
            mohave['upgrade'][i] = '노블레스'

        elif mohave['trim'].str.contains('프레지던트')[i]:
            mohave['upgrade'][i] = '프레지던트'

        elif mohave['trim'].str.contains('VIP')[i]:
            mohave['upgrade'][i] = 'VIP'

        elif mohave['trim'].str.contains('마스터즈')[i]:
            mohave['upgrade'][i] = '마스터즈'

        elif mohave['trim'].str.contains('플래티넘')[i]:
            mohave['upgrade'][i] = '플래티넘' 

        elif mohave['trim'].str.contains('KV460')[i]:
            mohave['upgrade'][i] = '기본형' 

        elif mohave['trim'].str.contains('KV300')[i]:
            mohave['upgrade'][i] = '기본형' 

        elif mohave['trim'].str.contains('QV300')[i]:
            mohave['upgrade'][i] = '기본형' 

        elif mohave['trim'].str.contains('JV300')[i]:
            mohave['upgrade'][i] = '기본형' 

        else :
            mohave['upgrade'][i] = '기본형'
        
        # trim 행의 문자열 제거
    mohave['trim'] = mohave.apply(lambda x: x['trim'].replace('노블레스',''), axis = 1)
    mohave['trim'] = mohave.apply(lambda x: x['trim'].replace('프레지던트',''), axis = 1)
    mohave['trim'] = mohave.apply(lambda x: x['trim'].replace('VIP',''), axis = 1)
    mohave['trim'] = mohave.apply(lambda x: x['trim'].replace('마스터즈',''), axis = 1)
    mohave['trim'] = mohave.apply(lambda x: x['trim'].replace('플래티넘',''), axis = 1)
    mohave['trim'] = mohave.apply(lambda x: x['trim'].strip(), axis = 1)
    
    #스포티지
    sport = df4[df4['info'] == '스포티지']
    sport.reset_index(inplace = True)
    sport.drop(['index'], axis = 1,inplace = True)
    sport['upgrade'] = ""

    for i in range(0, len(sport)):
    
        if sport['trim'].str.contains('스탠다드')[i]:
            sport['upgrade'][i] = '스탠다드'

        elif sport['trim'].str.contains('스텐다드')[i]:
            sport['upgrade'][i] = '스탠다드'

        elif sport['trim'].str.contains('LX')[i]:
            sport['upgrade'][i] = '스탠다드'

        elif sport['trim'].str.contains('럭셔리')[i]:
            sport['upgrade'][i] = '럭셔리'

        elif sport['trim'].str.contains('TLX 고급형')[i]:
            sport['upgrade'][i] = '럭셔리'

        elif sport['trim'].str.contains('TLX 최고급형')[i]:
            sport['upgrade'][i] = '트렌디' 

        elif sport['trim'].str.contains('트렌디')[i]:
            sport['upgrade'][i] = '트렌디'

        elif sport['trim'].str.contains('TLX')[i]:
            sport['upgrade'][i] = '럭셔리 트렌디' 

        elif sport['trim'].str.contains('W 스페셜')[i]:
            sport['upgrade'][i] = 'W 스페셜' 

        elif sport['trim'].str.contains('스타일 에디션')[i]:
            sport['upgrade'][i] = '스타일 에디션' 

        elif sport['trim'].str.contains('에이스')[i]:
            sport['upgrade'][i] = '스타일 에디션' 

        elif sport['trim'].str.contains('노블레스스페셜')[i]:
            sport['upgrade'][i] = '노블레스 스페셜' 

        elif sport['trim'].str.contains('노블레스 스페셜')[i]:
            sport['upgrade'][i] = '노블레스 스페셜' 

        elif sport['trim'].str.contains('노블레스 그래비티')[i]:
            sport['upgrade'][i] = '노블레스 스페셜' 

        elif sport['trim'].str.contains('노블레스')[i]:
            sport['upgrade'][i] = '노블레스'

        elif sport['trim'].str.contains('시그니처 스페셜')[i]:
            sport['upgrade'][i] = '시그니처 스페셜' 

        elif sport['trim'].str.contains('시그니처 그래비티')[i]:
            sport['upgrade'][i] = '시그니처 스페셜' 

        elif sport['trim'].str.contains('시그니처')[i]:
            sport['upgrade'][i] = '시그니처' 

        elif sport['trim'].str.contains('시그니쳐')[i]:
            sport['upgrade'][i] = '시그니처' 

        elif sport['trim'].str.contains('인텔리전트')[i]:
            sport['upgrade'][i] = '시그니처'

        elif sport['trim'].str.contains('리미티드')[i]:
            sport['upgrade'][i] = '리미티드'

        elif sport['trim'].str.contains('LIMITED')[i]:
            sport['upgrade'][i] = '리미티드'

        elif sport['trim'].str.contains('프레스티지')[i]:
            sport['upgrade'][i] = '프레스티지' 

        elif sport['trim'].str.contains('TLX 세이프티')[i]:
            sport['upgrade'][i] = '프레스티지' 

        else :
            sport['upgrade'][i] = '스탠다드'
     
    # trim 행의 문자열 제거
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('가솔린',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('디젤',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('하이브리드',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('세부등급 없음',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('2WD',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('4WD',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].strip(), axis = 1)
    
    # trim 행의 문자열 제거
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('스텐다드',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('LX',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('럭셔리',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('TLX',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('고급형',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('최',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('트렌디',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('W 스페셜',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('스타일 에디션',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('에이스',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('노블레스',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('스페셜',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('그래비티',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('시그니처',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('시그니쳐',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('인텔리전트',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('리미티드',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('LIMITED',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('프레스티지',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].replace('세이프티',''), axis = 1)
    sport['trim'] = sport.apply(lambda x: x['trim'].strip(), axis = 1)
    
    df4['info'] = df4.apply(lambda x: x['info'].replace('카렌스2','카렌스'), axis = 1)
    
    
    #카니발
    carnival = df4[df4['info'] == '카니발']
    carnival.reset_index(inplace = True)
    carnival.drop(['index'], axis = 1,inplace = True)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('세부등급 없음',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].strip(), axis = 1)
    
    carnival['upgrade'] = ""

    for i in range(0, len(carnival)):

        if carnival['trim'].str.contains('럭셔리')[i]:
            carnival['upgrade'][i] = '럭셔리'

        elif carnival['trim'].str.contains('디럭스')[i]:
            carnival['upgrade'][i] = '디럭스'

        elif carnival['trim'].str.contains('노블레스 스페셜')[i]:
            carnival['upgrade'][i] = '노블레스 스페셜'

        elif carnival['trim'].str.contains('프레스티지')[i]:
            carnival['upgrade'][i] = '프레스티지'

        elif carnival['trim'].str.contains('시그니처')[i]:
            carnival['upgrade'][i] = '시그니처' 

        elif carnival['trim'].str.contains('VIP')[i]:
            carnival['upgrade'][i] = 'VIP'

        elif carnival['trim'].str.contains('프레지던트')[i]:
            carnival['upgrade'][i] = '프레지던트' 

        elif carnival['trim'].str.contains('President')[i]:
            carnival['upgrade'][i] = '프레지던트' 

        elif carnival['trim'].str.contains('노블레스')[i]:
            carnival['upgrade'][i] = '노블레스' 

        elif carnival['trim'].str.contains('GX')[i]:
            carnival['upgrade'][i] = 'GX' 

        elif carnival['trim'].str.contains('GLX')[i]:
            carnival['upgrade'][i] = 'GLX' 

        elif carnival['trim'].str.contains('리미티드')[i]:
            carnival['upgrade'][i] = '리미티드' 

        elif carnival['trim'].str.contains('LIMITED')[i]:
            carnival['upgrade'][i] = '리미티드' 

        elif carnival['trim'].str.contains('어린이')[i]:
            carnival['upgrade'][i] = '프레스티지'

        elif carnival['trim'].str.contains('가솔린 9인승 하이리무진')[i]:
            carnival['upgrade'][i] = '시그니처' 

        elif carnival['trim'].str.contains('가솔린 11인승 하이리무진')[i]:
            carnival['upgrade'][i] = '시그니처' 

        elif carnival['trim'].str.contains('이지무브')[i]:
            carnival['upgrade'][i] = 'GLX' 

        elif carnival['trim'].str.contains('9인승 하이리무진')[i] and carnival['type'][i] == '디젤' :
            carnival['upgrade'][i] = '시그니처' 

        elif carnival['trim'].str.contains('7인승 하이리무진')[i] and carnival['type'][i] == '디젤' :
            carnival['upgrade'][i] = '시그니처'

        elif carnival['trim'].str.contains('9인승 하이리무진')[i] and carnival['type'][i] == '가솔린' :
            carnival['upgrade'][i] = '시그니처' 

        elif carnival['trim'].str.contains('11인승 하이리무진')[i] and carnival['type'][i] == '가솔린' :
            carnival['upgrade'][i] = '시그니처'

        elif carnival['trim'].str.contains('트립')[i]:
            carnival['upgrade'][i] = '트립'

        elif carnival['trim'].str.contains('랜드')[i]:
            carnival['upgrade'][i] = '랜드'

        elif carnival['trim'].str.contains('파크')[i]:
            carnival['upgrade'][i] = '파크'

        else :
            carnival['upgrade'][i] = '디럭스'
        
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('세부등급 없음',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('럭셔리',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('디럭스',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('노블레스',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('스페셜',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('프레스티지',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('시그니처',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('프레지던트',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('VIP',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('LIMITED',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('리미티드',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('GX',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('GLX',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('President',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('어린이 보호차',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('이지무브',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('트립',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('랜드',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('파크',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('그 카니발',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('(특장업체)',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('아웃도어',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('프리미엄',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('그 팩',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('기본형',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('최고급형',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].replace('뉴 카니발',''), axis = 1)
    carnival['trim'] = carnival.apply(lambda x: x['trim'].strip(), axis = 1)
    
    sorento1 = df4[df4['info'] == '쏘렌토']
    sorento2 = df4[df4['info'] == '쏘렌토R']
    sorento = pd.concat([sorento1,sorento2])
    
    sorento.reset_index(inplace = True)
    sorento.drop(['index'], axis = 1,inplace = True)
    
    sorento['upgrade'] = ""

    for i in range(0, len(sorento)):

        if sorento['trim'].str.contains('디럭스')[i]:
            sorento['upgrade'][i] = '디럭스'

        elif sorento['trim'].str.contains('럭셔리')[i]:
            sorento['upgrade'][i] = '럭셔리'

        elif sorento['trim'].str.contains('트렌디')[i]:
            sorento['upgrade'][i] = '트렌디'

        elif sorento['trim'].str.contains('프레스티지')[i]:
            sorento['upgrade'][i] = '프레스티지'

        elif sorento['trim'].str.contains('노블레스 스페셜')[i]:
            sorento['upgrade'][i] = '노블레스 스페셜' 

        elif sorento['trim'].str.contains('노블레스')[i]:
            sorento['upgrade'][i] = '노블레스'

        elif sorento['trim'].str.contains('시그니처')[i]:
            sorento['upgrade'][i] = '시그니처' 

        elif sorento['trim'].str.contains('그래비티')[i]:
            sorento['upgrade'][i] = '그래비티' 

        elif sorento['trim'].str.contains('마스터 스페셜')[i]:
            sorento['upgrade'][i] = '마스터 스페셜' 

        elif sorento['trim'].str.contains('마스터')[i]:
            sorento['upgrade'][i] = '마스터' 

        elif sorento['trim'].str.contains('LX')[i]:
            sorento['upgrade'][i] = 'LX' 

        elif sorento['trim'].str.contains('TLX')[i]:
            sorento['upgrade'][i] = 'TLX' 

        elif sorento['trim'].str.contains('TLX 스페셜')[i]:
            sorento['upgrade'][i] = 'TLX 스페셜' 

        elif sorento['trim'].str.contains('리미티드')[i]:
            sorento['upgrade'][i] = '리미티드'

        elif sorento['trim'].str.contains('프리미엄')[i]:
            sorento['upgrade'][i] = '프리미엄' 

        else :
            sorento['upgrade'][i] = '디럭스'
    
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('4WD',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('2WD',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('디젤',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('가솔린',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('리미티드',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('프레스티지',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('노블레스',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('럭셔리',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('TLX',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('프리미엄',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('스페셜',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('최고급형',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('고급형',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('LX',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('마스터',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('시그니처',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].replace('트렌디',''), axis = 1)
    sorento['trim'] = sorento.apply(lambda x: x['trim'].strip(), axis = 1)
    
    #레이
    ray = df4[df4['info'] == '레이']
    ray.reset_index(inplace = True)
    ray.drop(['index'], axis = 1,inplace = True)
    ray['upgrade'] = ""

    for i in range(0, len(ray)):

        if ray['trim'].str.contains('디럭스')[i]:
            ray['upgrade'][i] = '디럭스'

        elif ray['trim'].str.contains('럭셔리')[i]:
            ray['upgrade'][i] = '럭셔리'

        elif ray['trim'].str.contains('트렌디')[i]:
            ray['upgrade'][i] = '트렌디'

        elif ray['trim'].str.contains('프레스티지 스페셜')[i]:
            ray['upgrade'][i] = '프레스티지 스페셜'

        elif ray['trim'].str.contains('프레스티지')[i]:
            ray['upgrade'][i] = '프레스티지' 

        elif ray['trim'].str.contains('스탠다드')[i]:
            ray['upgrade'][i] = '스탠다드' 

        elif ray['trim'].str.contains('시그니처')[i]:
            ray['upgrade'][i] = '시그니처' 

        elif ray['trim'].str.contains('캠핑카')[i]:
            ray['upgrade'][i] = '캠핑카' 

        elif ray['trim'].str.contains('고급형')[i]:
            ray['upgrade'][i] = '고급형' 

        else :
            ray['upgrade'][i] = '스탠다드'
    #K9        
    K9 = df4[df4['info'] == 'K9']
    K9.reset_index(inplace = True)
    K9.drop(['index'], axis = 1,inplace = True)
    K9['upgrade'] = ""

    for i in range(0, len(K9)):

        if K9['trim'].str.contains('5.0 GDI')[i]:
            K9['upgrade'][i] = '퀸텀'

        elif K9['trim'].str.contains('플래티넘 Ⅰ')[i]:
            K9['upgrade'][i] = '플래티넘'

        elif K9['trim'].str.contains('플래티넘 Ⅱ')[i]:
            K9['upgrade'][i] = '플래티넘'

        elif K9['trim'].str.contains('플래티넘 Ⅲ')[i]:
            K9['upgrade'][i] = '플래티넘'

        elif K9['trim'].str.contains('3.8 GDI')[i] and 'AWD' not in  K9['trim'][i]: 
            K9['upgrade'][i] = '플래티넘'

        elif K9['trim'].str.contains('그랜드 플래티넘')[i]:
            K9['upgrade'][i] = '그랜드 플래티넘'

        elif K9['trim'].str.contains('플래티넘')[i]:
            K9['upgrade'][i] = '플래티넘'

        elif K9['trim'].str.contains('베스트 셀렉션Ⅰ')[i]:
            K9['upgrade'][i] = '베스트 셀렉션 1'

        elif K9['trim'].str.contains('베스트 셀렉션Ⅱ')[i]:
            K9['upgrade'][i] = '베스트 셀렉션 2'

        elif K9['trim'].str.contains('마스터즈 Ⅰ')[i]:
            K9['upgrade'][i] = '마스터즈'

        elif K9['trim'].str.contains('마스터즈 Ⅱ')[i]:
            K9['upgrade'][i] = '마스터즈'

        elif K9['trim'].str.contains('마스터즈 Ⅲ')[i]:
            K9['upgrade'][i] = '마스터즈'

        elif K9['trim'].str.contains('그랜드 마스터즈')[i]:
            K9['upgrade'][i] = '그랜드 마스터즈'

        elif K9['trim'].str.contains('프레스티지 스페셜')[i]:
            K9['upgrade'][i] = '프레스티지 스페셜' 

        elif K9['trim'].str.contains('프레스티지')[i]:
            K9['upgrade'][i] = '프레스티지'

        elif K9['trim'].str.contains('이그제큐티브')[i]:
            K9['upgrade'][i] = '이그제큐티브' 

        elif K9['trim'].str.contains('노블레스 스페셜')[i]:
            K9['upgrade'][i] = '노블레스 스페셜' 

        elif K9['trim'].str.contains('노블레스')[i]:
            K9['upgrade'][i] = '노블레스' 

        elif K9['trim'].str.contains('RVIP')[i]:
            K9['upgrade'][i] = 'RVIP' 

        elif K9['trim'].str.contains('VIP')[i]:
            K9['upgrade'][i] = 'VIP'

        else :
            K9['upgrade'][i] = '프레스티지'
        
        #포르테
    forte = df4[df4['info'] == '포르테']
    forte.reset_index(inplace = True)
    forte.drop(['index'], axis = 1,inplace = True)
    forte['upgrade'] = ""

    for i in range(0, len(forte)):

        if forte['trim'].str.contains('프레스티지')[i]:
            forte['upgrade'][i] = '프레스티지'

        elif forte['trim'].str.contains('블랙스페셜')[i]:
            forte['upgrade'][i] = '블랙스페셜'

        elif forte['trim'].str.contains('럭셔리')[i]:
            forte['upgrade'][i] = '럭셔리'

        elif forte['trim'].str.contains('디럭스')[i]:
            forte['upgrade'][i] = '디럭스'

        elif forte['trim'].str.contains('기본형')[i]:
            forte['upgrade'][i] = '기본형'

        elif forte['trim'].str.contains('레드프리미엄')[i]:
            forte['upgrade'][i] = '레드프리미엄'

        elif forte['trim'].str.contains('Si')[i]:
            forte['upgrade'][i] = '기본형'

        elif forte['trim'].str.contains('Si 프리미엄')[i]:
            forte['upgrade'][i] = '블랙'

        elif forte['trim'].str.contains('고급')[i]:
            forte['upgrade'][i] = '고급형'

        else :
            forte['upgrade'][i] = '스탠다드'
            
            
    #모닝
    morning = df4[df4['info']=='모닝']
    morning.reset_index(inplace = True)
    morning.drop(['index'], axis = 1,inplace = True)
    morning['upgrade'] = ""

    for i in range(0, len(morning)):

        if morning['trim'].str.contains('스탠다드')[i]:
            morning['upgrade'][i] = '스탠다드'

        elif morning['trim'].str.contains('스탠다드 마이너스')[i]:
            morning['upgrade'][i] = '스탠다드'

        elif morning['trim'].str.contains('베이직 플러스')[i]:
            morning['upgrade'][i] = '스탠다드'

        elif morning['trim'].str.contains('기본형')[i]:
            morning['upgrade'][i] = '스탠다드'

        elif morning['trim'].str.contains('프레스티지')[i]:
            morning['upgrade'][i] = '프레스티지'

        elif morning['trim'].str.contains('시그니처')[i]:
            morning['upgrade'][i] = '시그니처'

        elif morning['trim'].str.contains('시그니처 엣지-업')[i]:
            morning['upgrade'][i] = '프레스티지'

        elif morning['trim'].str.contains('스마트 스페셜')[i]:
            morning['upgrade'][i] = '스페셜'

        elif morning['trim'].str.contains('디럭스 스페셜')[i]:
            morning['upgrade'][i] = '스페셜'

        elif morning['trim'].str.contains('스페셜')[i]:
            morning['upgrade'][i] = '스페셜'

        elif morning['trim'].str.contains('럭셔리 스포츠')[i]:
            morning['upgrade'][i] = '스포츠'

        elif morning['trim'].str.contains('디럭스')[i]:
            morning['upgrade'][i] = '디럭스'    

        elif morning['trim'].str.contains('럭셔리')[i]:
            morning['upgrade'][i] = '럭셔리'    

        elif morning['trim'].str.contains('트렌디')[i]:
            morning['upgrade'][i] = '트렌디'  

        elif morning['trim'].str.contains('스마트')[i]:
            morning['upgrade'][i] = '스마트'  

        elif morning['trim'].str.contains('RUN')[i]:
            morning['upgrade'][i] = '스포츠' 

        elif morning['trim'].str.contains('블랙프리미엄')[i]:
            morning['upgrade'][i] = '블랙프리미엄' 

        elif morning['trim'].str.contains('고급형')[i]:
            morning['upgrade'][i] = '고급형' 

        elif morning['trim'].str.contains('기본형')[i]:
            morning['upgrade'][i] = '기본형' 

        elif morning['trim'].str.contains('레이디')[i]:
            morning['upgrade'][i] = '레이디' 

        else :
            morning['upgrade'][i] = '스탠다드'
    
    #K8
    K8 = df4[df4['info'] == 'K8']
    K8.reset_index(inplace = True)
    K8.drop(['index'], axis = 1,inplace = True)
    K8['upgrade'] = ""

    for i in range(0, len(K8)):

        if K8['trim'].str.contains('시그니처')[i]:
            K8['upgrade'][i] = '시그니처'

        elif K8['trim'].str.contains('2.5 가솔린')[i]:
            K8['upgrade'][i] = '노블레스'

        elif K8['trim'].str.contains('노블레스')[i]:
            K8['upgrade'][i] = '노블레스'

        elif K8['trim'].str.contains('노블레스 라이트')[i]:
            K8['upgrade'][i] = '노블레스'

        elif K8['trim'].str.contains('플래티넘')[i]:
            K8['upgrade'][i] = '플래티넘'

        elif K8['trim'].str.contains('트렌디')[i]:
            K8['upgrade'][i] = '트렌디'

        elif K8['trim'].str.contains('프레스티지')[i]:
            K8['upgrade'][i] = '프레스티지'

        elif K8['trim'].str.contains('3.5 가솔린')[i]:
            K8['upgrade'][i] = '노블레스'

        elif K8['trim'].str.contains('3.5 LPG')[i]:
            K8['upgrade'][i] = '스탠다드'

        else :
            K8['upgrade'][i] = '스탠다드'
            
    #카렌스
    carens = df4[df4['info']=='카렌스']
    carens.reset_index(inplace = True)
    carens.drop(['index'], axis = 1,inplace = True)
    
    # trim열의 프리미엄 스포츠 여부를 upgrade 열에 추가
    carens['upgrade'] = ""

    for i in range(0, len(carens)):

        if carens['trim'].str.contains('디럭스')[i]:
            carens['upgrade'][i] = '디럭스'

        elif carens['trim'].str.contains('럭셔리')[i]:
            carens['upgrade'][i] = '럭셔리'

        elif carens['trim'].str.contains('트렌디')[i]:
            carens['upgrade'][i] = '트렌디'

        elif carens['trim'].str.contains('프레스티지')[i]:
            carens['upgrade'][i] = '프레스티지'

        elif carens['trim'].str.contains('노블레스')[i]:
            carens['upgrade'][i] = '노블레스'

        elif carens['trim'].str.contains('에코')[i]:
            carens['upgrade'][i] = '에코 다이나믹스'

        elif carens['trim'].str.contains('TLX')[i]:
            carens['upgrade'][i] = 'TLX'

        elif carens['trim'].str.contains('GLX')[i]:
            carens['upgrade'][i] = 'GLX'

        elif carens['trim'].str.contains('LX')[i]:
            carens['upgrade'][i] = 'LX'

        elif carens['trim'].str.contains('EX')[i]:
            carens['upgrade'][i] = 'EX'

        elif carens['trim'].str.contains('GX')[i]:
            carens['upgrade'][i] = 'GX'

        elif carens['trim'].str.contains('프리미')[i]:
            carens['upgrade'][i] = '프리미엄'

        elif carens['trim'].str.contains('리미티드')[i]:
            carens['upgrade'][i] = '리미티드'

        elif carens['trim'].str.contains('골드')[i]:
            carens['upgrade'][i] = '비즈니스'

        elif carens['trim'].str.contains('비즈니스')[i]:
            carens['upgrade'][i] = '비즈니스'

        elif carens['trim'].str.contains('베타')[i]:
            carens['upgrade'][i] = '비즈니스'

        else :
            carens['upgrade'][i] = '스탠다드'
    
    #스팅어
    stingr = df4[df4['info'] == '스팅어']
    stingr.reset_index(inplace = True)
    stingr.drop(['index'], axis = 1,inplace = True)
    
    # trim열의 프리미엄 스포츠 여부를 upgrade 열에 추가
    stingr['upgrade'] = ""

    for i in range(0, len(stingr)):

        if stingr['trim'].str.contains('프라임')[i]:
            stingr['upgrade'][i] = '프라임'

        elif stingr['trim'].str.contains('플래티넘')[i]:
            stingr['upgrade'][i] = '플래티넘'

        elif stingr['trim'].str.contains('마스터즈')[i]:
            stingr['upgrade'][i] = '마스터즈'

        elif stingr['trim'].str.contains('익스트림')[i]:
            stingr['upgrade'][i] = '익스트림 팩'

        elif stingr['trim'].str.contains('드림')[i]:
            stingr['upgrade'][i] = '드림 에디션'

        elif stingr['trim'].str.contains('알칸타라')[i]:
            stingr['upgrade'][i] = '알칸타라 에디션'

        elif stingr['trim'].str.contains('GT')[i]:
            stingr['upgrade'][i] = 'GT'

        elif stingr['trim'].str.contains('2.0 터보')[i]:
            stingr['upgrade'][i] = '프라임'

        elif stingr['trim'].str.contains('2.2 디젤')[i]:
            stingr['upgrade'][i] = '프라임'

        elif stingr['trim'].str.contains('3.3 터보')[i]:
            stingr['upgrade'][i] = '마스터즈'

        else :
            stingr['upgrade'][i] = '플래티넘'
    
    # K3
    K3 = df4[df4['info'] == 'K3']
    K3.reset_index(inplace = True)
    K3.drop(['index'], axis = 1,inplace = True)
    
    # trim열의 프리미엄 스포츠 여부를 upgrade 열에 추가
    K3['upgrade'] = ""

    for i in range(0, len(K3)):

        if K3['trim'].str.contains('디럭스')[i]:
            K3['upgrade'][i] = '디럭스'

        elif K3['trim'].str.contains('트렌디')[i]:
            K3['upgrade'][i] = '트렌디'

        elif K3['trim'].str.contains('스탠다드')[i]:
            K3['upgrade'][i] = '스탠다드'

        elif K3['trim'].str.contains('베이직')[i]:
            K3['upgrade'][i] = '트렌디'

        elif K3['trim'].str.contains('플러스')[i]:
            K3['upgrade'][i] = '럭셔리'

        elif K3['trim'].str.contains('럭셔리')[i]:
            K3['upgrade'][i] = '럭셔리'

        elif K3['trim'].str.contains('프레스티지')[i]:
            K3['upgrade'][i] = '프레스티지'

        elif K3['trim'].str.contains('노블레스')[i]:
            K3['upgrade'][i] = '노블레스'

        elif K3['trim'].str.contains('시그니처')[i]:
            K3['upgrade'][i] = '시그니처'

        elif K3['trim'].str.contains('W 스페셜')[i]:
            K3['upgrade'][i] = 'W 스페셜'

        elif K3['trim'].str.contains('1.6 터보 GT')[i]:
            K3['upgrade'][i] = '트렌디'

        elif K3['trim'].str.contains('1.6')[i]:
            K3['upgrade'][i] = '럭셔리'

        else :
            K3['upgrade'][i] = '스탠다드'
    
    #마스터
    master = df4[df4['info'] == '마스터']
    master.reset_index(inplace = True)
    master.drop(['index'], axis = 1,inplace = True)
    master['upgrade'] = ""

    for i in range(0, len(master)):

        if master['trim'].str.contains('마스터즈')[i]:
            master['upgrade'][i] = '마스터즈'

        elif master['trim'].str.contains('플래티넘')[i]:
            master['upgrade'][i] = '플래티넘'

        else :
            master['upgrade'][i] = '마스터즈'
            
    #오피러스
    opirus = df4[df4['info'] == '오피러스']
    opirus.reset_index(inplace = True)
    opirus.drop(['index'], axis = 1,inplace = True)
    opirus['upgrade'] = ""

    for i in range(0, len(opirus)):

        if opirus['trim'].str.contains('디럭스')[i]:
            opirus['upgrade'][i] = '디럭스'

        elif opirus['trim'].str.contains('럭셔리')[i]:
            opirus['upgrade'][i] = '럭셔리'

        elif opirus['trim'].str.contains('고급형')[i]:
            opirus['upgrade'][i] = '럭셔리'

        elif opirus['trim'].str.contains('프리미엄')[i]:
            opirus['upgrade'][i] = '프리미엄'

        elif opirus['trim'].str.contains('프레스티지')[i]:
            opirus['upgrade'][i] = '프레스티지'

        elif opirus['trim'].str.contains('노블레스')[i]:
            opirus['upgrade'][i] = '노블레스'

        else :
            opirus['upgrade'][i] = '디럭스'
            
    #프라이드
    pride = df4[df4['info'] == '프라이드']
    pride.reset_index(inplace = True)
    pride.drop(['index'], axis = 1,inplace = True)
    
    pride['upgrade'] = ""

    for i in range(0, len(pride)):

        if pride['trim'].str.contains('디럭스')[i]:
            pride['upgrade'][i] = '디럭스'

        elif pride['trim'].str.contains('트렌디')[i]:
            pride['upgrade'][i] = '트렌디'

        elif pride['trim'].str.contains('럭셔리')[i]:
            pride['upgrade'][i] = '럭셔리'

        elif pride['trim'].str.contains('프레스티지')[i]:
            pride['upgrade'][i] = '프레스티지'

        elif pride['trim'].str.contains('프리미엄')[i]:
            pride['upgrade'][i] = '프리미엄'

        elif pride['trim'].str.contains('SLX')[i]:
            pride['upgrade'][i] = '프레스티지'

        elif pride['trim'].str.contains('LX')[i]:
            pride['upgrade'][i] = '럭셔리'

        elif pride['trim'].str.contains('L')[i]:
            pride['upgrade'][i] = '트렌디'

        else :
            pride['upgrade'][i] = '디럭스'
            
    #로체,스토닉,셀토스
    l = df4[df4['info'] == '로체']
    s = df4[df4['info'] == '스토닉']
    sel = df4[df4['info'] == '셀토스']
    
    lss = pd.concat([l,s,sel])
    lss.reset_index(inplace = True)
    lss.drop(['index'], axis = 1,inplace = True)
    
    # trim열의 프리미엄 스포츠 여부를 upgrade 열에 추가
    lss['upgrade'] = ""

    for i in range(0, len(lss)):

        if lss['trim'].str.contains('디럭스')[i]:
            lss['upgrade'][i] = '디럭스'

        elif lss['trim'].str.contains('기본형')[i]:
            lss['upgrade'][i] = '디럭스'

        elif lss['trim'].str.contains('트렌디')[i]:
            lss['upgrade'][i] = '트렌디'

        elif lss['trim'].str.contains('고급형')[i]:
            lss['upgrade'][i] = '트렌디'

        elif lss['trim'].str.contains('럭셔리')[i]:
            lss['upgrade'][i] = '럭셔리'

        elif lss['trim'].str.contains('최고급형')[i]:
            lss['upgrade'][i] = '럭셔리'

        elif lss['trim'].str.contains('프레스티지')[i]:
            lss['upgrade'][i] = '프레스티지'

        elif lss['trim'].str.contains('비즈니스')[i]:
            lss['upgrade'][i] = '프레스티지'

        elif lss['trim'].str.contains('노블레스')[i]:
            lss['upgrade'][i] = '노블레스'

        elif lss['trim'].str.contains('프리미엄')[i]:
            lss['upgrade'][i] = '프리미엄'

        elif lss['trim'].str.contains('시그니처')[i]:
            lss['upgrade'][i] = '시그니처'

        elif lss['trim'].str.contains('그래비티')[i]:
            lss['upgrade'][i] = '그래비티'

        else :
            lss['upgrade'][i] = '디럭스'
    
    #소울
    soul = df4[df4['info'] == '쏘울']
    soul.reset_index(inplace = True)
    soul.drop(['index'], axis = 1,inplace = True)
    
    # trim열의 프리미엄 스포츠 여부를 upgrade 열에 추가
    soul['upgrade'] = ""

    for i in range(0, len(soul)):

        if soul['trim'].str.contains('디럭스')[i]:
            soul['upgrade'][i] = '디럭스'

        elif soul['trim'].str.contains('기본형')[i]:
            soul['upgrade'][i] = '디럭스'

        elif soul['trim'].str.contains('트렌디')[i]:
            soul['upgrade'][i] = '트렌디'

        elif soul['trim'].str.contains('고급형')[i]:
            soul['upgrade'][i] = '트렌디'

        elif soul['trim'].str.contains('럭셔리')[i]:
            soul['upgrade'][i] = '럭셔리'

        elif soul['trim'].str.contains('최고급형')[i]:
            soul['upgrade'][i] = '럭셔리'

        elif soul['trim'].str.contains('프레스티지')[i]:
            soul['upgrade'][i] = '프레스티지'

        elif soul['trim'].str.contains('그린존')[i]:
            soul['upgrade'][i] = '프레스티지'

        elif soul['trim'].str.contains('레드존')[i]:
            soul['upgrade'][i] = '프레스티지'

        elif soul['trim'].str.contains('노블레스')[i]:
            soul['upgrade'][i] = '노블레스'

        elif soul['trim'].str.contains('브라운존')[i]:
            soul['upgrade'][i] = '노블레스'

        elif soul['trim'].str.contains('프리미엄')[i]:
            soul['upgrade'][i] = '프리미엄'

        else :
            soul['upgrade'][i] = '디럭스'
            
    #쎄라토, 니로        
    ss = df4[df4['info'] == '쎄라토']
    n = df4[df4['info'] == '니로']
    op = df4[df4['info'] == '옵티마']
    sno = pd.concat([ss,n,op])
    sno.reset_index(inplace = True)
    sno.drop(['index'], axis = 1,inplace = True)
    
    # trim열의 프리미엄 스포츠 여부를 upgrade 열에 추가
    sno['upgrade'] = ""

    for i in range(0, len(sno)):

        if sno['trim'].str.contains('디럭스')[i]:
            sno['upgrade'][i] = '디럭스'

        elif sno['trim'].str.contains('기본형')[i]:
            sno['upgrade'][i] = '디럭스'

        elif sno['trim'].str.contains('트렌디')[i]:
            sno['upgrade'][i] = '트렌디'

        elif sno['trim'].str.contains('고급형')[i]:
            sno['upgrade'][i] = '트렌디'

        elif sno['trim'].str.contains('럭셔리')[i]:
            sno['upgrade'][i] = '럭셔리'

        elif sno['trim'].str.contains('최고급형')[i]:
            sno['upgrade'][i] = '럭셔리'

        elif sno['trim'].str.contains('프레스티지')[i]:
            sno['upgrade'][i] = '프레스티지'

        elif sno['trim'].str.contains('프리미엄')[i]:
            sno['upgrade'][i] = '프리미엄'

        elif sno['trim'].str.contains('프라임')[i]:
            sno['upgrade'][i] = '프리미엄'

        elif sno['trim'].str.contains('노블레스')[i]:
            sno['upgrade'][i] = '노블레스'

        elif sno['trim'].str.contains('스포츠')[i]:
            sno['upgrade'][i] = '스포츠'

        elif sno['trim'].str.contains('스페셜')[i]:
            sno['upgrade'][i] = '스페셜'

        else :
            sno['upgrade'][i] = '디럭스'
            
    # 봉고
    bo = df4[df4['info'] == '봉고III 트럭 CRDi 카고']
    no = df4[df4['info'] == '더 뉴 봉고III 트럭 CRDi 카고']
    go = df4[df4['info'] == '봉고3']
    bongo = pd.concat([bo,no,go])
    bongo.reset_index(inplace = True)
    bongo.drop(['index'], axis = 1,inplace = True)
    
    for i in range(0, len(bongo)):
        bongo['info'][i] = '봉고3'
    
    bongo['upgrade'] = ""

    for i in range(0, len(bongo)):

        if bongo['trim'].str.contains('GLS')[i]:
            bongo['upgrade'][i] = 'GLS'

        elif bongo['trim'].str.contains('GL')[i]:
            bongo['upgrade'][i] = 'GL'

        elif bongo['trim'].str.contains('L')[i]:
            bongo['upgrade'][i] = 'L'

        else :
            bongo['upgrade'][i] = 'L'
    
    #차량종합
    df5 = pd.concat([K5,K7,mohave,sport,carnival,sorento,ray,K9,forte,morning,K8,carens,stingr,K3,master,opirus,pride,lss,soul,sno,bongo])
    df5.drop(['trim'], axis = 1, inplace = True)
    df5.reset_index(inplace = True)
    df5.drop(['index'], axis = 1,inplace = True)
    df5= df5[['brand','info','upgrade','type','km','year','accident','color','wd','price']]
    df5.columns=['brand','name','trim','type','km','year','accident','color','wd','price']
    df5.to_csv('기아추출.csv',mode='w',header=True,encoding='UTF-8',index=False)
    
    #포드
    df6=df[df.brand.str.contains('포드',case=False)]
    df6['trim'] = df6['trim'].astype('str') 
    df6['trim'] = df6['trim'].astype('str') 
    df6['s'] = np.where(df6['trim'].str.contains('2.3'),'2.3',
                     np.where(df6['trim'].str.contains('3.5'),'3.5',
                              np.where(df6['trim'].str.contains('쿠페'),'쿠페',
                                       np.where(df6['trim'].str.contains('컨버터블'),'컨버터블',
                                                np.where(df6['trim'].str.contains('3.5l'),'3.5',
                                                         np.where(df6['trim'].str.contains('2.0 트렌드'),'2.0 트렌드',
                                                                   np.where(df6['trim'].str.contains('gt 쿠페'),'gt 쿠페',
                                                                        np.where(df6['trim'].str.contains('2.0  에코부스트'),'2.0 에코부스트',
                                                                                 np.where(df6['trim'].str.contains('gt 컨버터블'),'gt 컨버터블',
                                                                                          np.where(df6['trim'].str.contains('3.5 sel'),'3.5 sel',
                                                                                                 np.where(df6['trim'].str.contains('2.0 티타늄'),'2.0 티타늄',
                                                                                                          np.where(df6['trim'].str.contains('5.0l'),'5.0l', ''))))))))))))
    df6['trim'] = df6['trim'].fillna('') + ' '+ df6['s'].fillna('') 
    del df6['s']
    df6= df6[['brand','info','trim','type','km','year','accident','color','wd','price']]
    df6.columns=['brand','name','trim','type','km','year','accident','color','wd','price']
    df6.to_csv('포드추출.csv',mode='w',header=True,encoding='utf-8',index=False)

    
    #미니
    df7=df[df.brand.str.contains('미니',case=False)]
    df7['s'] = np.where(df7['trim'].str.contains('5도어'),'5도어',
                     np.where(df7['trim'].str.contains('파크레인'),'컨트리맨 파크래인',
                              np.where(df7['trim'].str.contains('jcw'),'jcw',
                                       np.where(df7['trim'].str.contains('캠든'),'캠든',
                                                np.where(df7['trim'].str.contains('se'),'se',
                                                    np.where(df7['trim'].str.contains('all4'),'컨트리맨', ''))))))
    
    df7['trim'] = df7['trim'].fillna('') + ' '+ df7['s'].fillna('')  
    del df7['s']
    df7= df7[['brand','info','trim','type','km','year','accident','color','wd','price']]
    df7.columns=['brand','name','trim','type','km','year','accident','color','wd','price']
    df7.to_csv('미니추출.csv',mode='w',header=True,encoding='utf-8',index=False)

    
    #쌍용
    df8=df[df.brand.str.contains('쌍용',case=False)]
    df8['trim'] = df8['trim'].str.replace('2WD', '')
    df8['trim'] = df8['trim'].str.replace('4WD', '')
    df8['trim'] = df8['trim'].str.replace('디젤', '')
    df8['trim'] = df8['trim'].str.replace('4tronic', '')
    df8['trim'] = df8['trim'].str.replace('4tronicvip', '')
    df8['trim'] = df8['trim'].str.replace('4tronic프레스티지', '')
    df8['trim'] = df8['trim'].str.replace('4tronicvvip', '')
    df8['trim'] = df8['trim'].str.replace('세부등급 없음', '')
    df8['trim'] = df8['trim'].str.replace('가솔린', '')
    df8['trim'] = df8['trim'].str.replace('lv5', '')
    df8['trim'] = df8['trim'].str.replace('lv6', '')
    df8['trim'] = df8['trim'].str.replace('ev6', '')
    df8['trim'] = df8['trim'].str.replace('ev5', '')
    df8['trim'] = df8['trim'].str.replace('클럽', '')
    df8['trim'] = df8['trim'].str.replace('파크', '')
    df8['trim'] = df8['trim'].str.replace('cw700 vvip', 'cw700 vip')
    df8['trim'] = df8['trim'].str.replace('스페셜', 'cw700 vip')
    df8['trim'] = df8['trim'].str.replace('2.2 프레스티지 스폐셜', '2.2 프레스티지')
    df8['trim'] = df8['trim'].str.replace('2.2 헤리티지 스폐셜', '2.2 헤리티지')
    df8['trim'] = df8['trim'].str.replace('기어 플러스 Ⅱ', '기어 플러스')
    df8['trim'] = df8['trim'].str.replace('기어 플러스 Ⅰ', '기어 플러스')
    df8['trim'] = df8['trim'].str.replace('기어 플러스Ⅰ', '기어 플러스')
    df8['trim'] = df8['trim'].str.replace('기어 에디션', '기어 플러스')
    df8['trim'] = df8['trim'].str.replace('체어맨 cm500s', '체어맨 500s')
    df8['trim'] = df8['trim'].str.replace('티볼리 티볼리', '티볼리')
    ##########
    df8['trim'] = df8['trim'].str.strip()
    df8['trim'] = df8['trim'].str.lstrip()
    
    df8= df8[['brand','info','trim','type','km','year','accident','color','wd','price']]
    df8.columns=['brand','name','trim','type','km','year','accident','color','wd','price']
    df8=df8[~df8.name.str.contains('베리')]
    df8.to_csv('쌍용추출.csv',mode='w',header=True,encoding='utf-8',index=False)
    
    #랜드로버
    df9=df[df.brand.str.contains('랜드로버',case=False)]
    df9['trim'] = df9['trim'].str.replace('vogue se', 'vogue')
    df9= df9[['brand','info','trim','type','km','year','accident','color','wd','price']]
    df9.columns=['brand','name','trim','type','km','year','accident','color','wd','price']
    df9.to_csv('랜드로버추출.csv',mode='w',header=True,encoding='utf-8',index=False)        
    
    #르노삼성
    df10=df[df.brand.str.contains('르노삼성',case=False)]   
    df10.dropna(axis=0, inplace=True)
    df10['type'] = df10.apply(lambda x: x['type'].strip(), axis = 1)
    df10= df10[['brand','info','trim','type','km','year','accident','color','wd','price']]
    df10.columns=['brand','name','trim','type','km','year','accident','color','wd','price']
    df10.to_csv('르노삼성추출.csv',mode='w',header=True,encoding='utf-8',index=False)

    
    
    #제네시스
    df11=df[df.brand.str.contains('제네시스',case=False)]
    df11['trim']=df11['trim'].str.replace(pat='AWD', repl='')
    df11['trim']=df11['trim'].str.replace(pat='2WD', repl='')
    df11['trim']=df11['trim'].str.replace(pat='4WD', repl='')
    df11['trim']=df11['trim'].str.replace(pat='가솔린', repl='')
    df11['trim']=df11['trim'].str.replace(pat='디젤', repl='')
    df11['trim']=df11['trim'].str.replace(pat='터보', repl='t')
    df11['trim']=df11['trim'].str.replace(pat='2.2D', repl='2.2')
    df11['trim']=df11['trim'].str.replace(pat=' T', repl='t')
    df11['trim']=df11['trim'].str.replace(pat='GDi', repl='')
    df11['trim']=df11['trim'].str.replace(pat='GDI', repl='')
    df11['trim']=df11['trim'].str.replace(pat='-', repl='')
    df11['trim']=df11['trim'].str.replace(pat='Turbo', repl='')
    df11['trim']=df11['trim'].str.replace(pat='  ', repl='')
    df11['trim']=df11['trim'].str.replace(pat='3.3프리미엄 럭셔리', repl='3.3 프리미엄 럭셔리')
    df11['trim']=df11['trim'].str.replace(pat='3.3럭셔리', repl='3.3 럭셔리')
    df11['trim']=df11['trim'].str.replace(pat='3.8럭셔리', repl='3.8 럭셔리')
    df11['trim']=df11['trim'].str.replace(pat='3.8프레스티지', repl='3.8 프레스티지')
    df11['trim']=df11['trim'].str.replace(pat='3.3프레스티지', repl='3.3 프레스티지')
    df11['trim']=df11['trim'].str.strip()
    
    df11.dropna(axis=0, inplace=True)
    df11= df11[['brand','info','trim','type','km','year','accident','color','wd','price']]
    df11.columns=['brand','name','trim','type','km','year','accident','color','wd','price']
    df11.to_csv('제네시스추출.csv',mode='w',header=True,encoding='utf-8',index=False) 
    
    #폭스바겐 
    df12=df[df.brand.str.contains('폭스바겐',case=False)]
    df12['s'] = np.where(df12['trim'].str.contains('TSI'),'TSI',
                         np.where(df12['trim'].str.contains('블루모션'),'블루모션',
                            np.where(df12['trim'].str.contains('TDI'),'TDI','')))
    df12['trim'] = df12['trim'].fillna('') + ' '+ df12['s'].fillna('') 
    del df12['s']
    

    #혹시 nan값이 너무 많이 보이면 위에 info + ts/td/b 확인
    df12.dropna(axis=0, inplace=True)
    df12= df12[['brand','info','trim','type','km','year','accident','color','wd','price']]
    df12.columns=['brand','name','trim','type','km','year','accident','color','wd','price']
    df12.to_csv('폭스바겐추출.csv',mode='w',header=True,encoding='utf-8',index=False) 
    
    #현대
    df13=df[df.brand.str.contains('현대',case=False)]
    df13.dropna(axis=0, inplace=True)
    df13= df13[['brand','info','trim','type','km','year','accident','color','wd','price']]
    df13.columns=['brand','name','trim','type','km','year','accident','color','wd','price']
    df13.to_csv('현대추출.csv',mode='w',header=True,encoding='utf-8',index=False) 
    
    df_f=pd.concat([df1,df2,df3,df5,df6,df7,df8,df9,df10,df11,df12,df13],ignore_index=True,sort=True)
    df_f['wd']=df_f['wd'].str.replace('2WD','1').str.replace('4WD','2').str.replace('AWD','2')
    df_f=df_f[~df_f.trim.str.contains('nan')]
    df_f['km']=df_f['km'].str.replace(',','').str.replace('"', '', regex=True)
    df_f.dropna(axis=0, inplace=True)
    df_f = df_f.groupby('name').filter(lambda x : len(x)>10)
    df_f = df_f.groupby('trim').filter(lambda x : len(x)>10)
    df_f.insert(0, 'id', range(0, 0 + len(df_f)))
    df_f=df_f[['id','brand','name','trim','type','km','year','accident','color','wd','price']]
    df_f.columns=['id','brand','name','trim','type','km','year','accident','color','wd','price']
    df_f.to_csv('추출완성본.csv',mode='w',header=True,encoding='utf-8',index=False) 
    
    
    engine = create_engine("mysql+mysqldb://root:0000@localhost:3306/blog", encoding='utf-8')
    conn = engine.connect()
    
    df_f.to_sql(name='cha', con=engine, if_exists='replace', index=False)
    
    #데이터 집어넣기 전에 mysql에서 테이블 생성 
    

    



    

    
    
    
    



    
    
        
    

    
    


    
    
    



    
    



    


# In[68]:


data()


# In[ ]:





# In[ ]:




