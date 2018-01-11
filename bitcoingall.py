from bs4 import BeautifulSoup
import requests
import csv
import datetime
import time
import random

def get_html(pagenumber):
    url="http://gall.dcinside.com/board/lists/?id=bitcoins&page="+str(pagenumber)
    # 디씨인사이드는 현재 파이썬을 이용한 파싱을 막고있다.
    headers={
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent":"Mozilla/5.0 (Mactinosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0"
    }
    r=requests.get(url,headers=headers)
    return r.text

def getpage(pagenumber):

    raw_html=get_html(pagenumber)

    soup=BeautifulSoup(str(raw_html),"lxml")
    tr_data = soup.find_all("tr",class_="tb")

    # print(dt1)

    # 게시글번호
    soup=BeautifulSoup(str(tr_data),"lxml")
    articlenumbers=soup.find_all("td",class_="t_notice")

    #게시글 제목
    soup = BeautifulSoup(str(tr_data), "lxml")
    articletitles = soup.find_all("td", class_="t_subject")

    # 게시글 작성자 + ip
    soup = BeautifulSoup(str(tr_data), "lxml")
    articlewriters = soup.find_all("td", class_="t_writer")

    soup = BeautifulSoup(str(tr_data),"lxml")
    articletime = soup.find_all("td",class_="t_date")

    soup=BeautifulSoup(str(tr_data),"lxml")
    viewAndHit=soup.find_all("td",class_="t_hits")

    hits=[]
    views=[]
    for i in range(len(viewAndHit)):
        if i%2==0:
            views.append(viewAndHit[i].get_text())
        else:
            hits.append(viewAndHit[i].get_text())

    dc_num=[]
    dc_title=[]
    dc_time=[]
    dc_hits=[]
    dc_views=[]
    for i in range(0,len(articlenumbers)):
        # dc_ip=articlewriters[i].get("ip")
        # dc_user=articlewriters[i].get("user_name")
        if articlenumbers[i].get_text()=="공지":
            pass
        else:
            dc_num.append(articlenumbers[i].get_text())
            dc_title.append(articletitles[i].get_text())
            string=str(articletime[i])
            dc_time.append(string[26:45])
            dc_hits.append(hits[i])
            dc_views.append(views[i])

    # for i in range(len(dc_num)):
    #     # print(dc_ip)
    #     # print(dc_user)
    #     print(dc_num[i])
    #     # print(dc_title[i])
    #     # print(dc_time[i])
    #     print(dc_hits[i])
    #     print(dc_views[i])
    #     print("---------------------")
    return dc_num,dc_title,dc_views,dc_hits,dc_time

# print(getpage(1))
todaydate=str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
totalpage=100000
startpage=9798
page=startpage
with open(todaydate+"_"+str(startpage)+"_"+str(totalpage)+"p.csv","w",newline="",encoding='utf8') as csvfile:
    spamwriter=csv.writer(csvfile,delimiter=" ",quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while(page<totalpage):
        page+=1
        print(page)
        if page%50==0:
            print(page, datetime.datetime.now())
        try:
            spamwriter.writerow(getpage(page),)
        except requests.exceptions.ConnectionError:
            print("connection error at page",page,datetime.datetime.now())
            page-=1
            time.sleep(1)


