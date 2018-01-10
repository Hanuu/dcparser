from bs4 import BeautifulSoup
import requests
import csv
import datetime

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

    dc_num=[]
    dc_title=[]
    dc_time=[]
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


        # print(dc_ip)
        # print(dc_user)
        # print(dc_num)
        # print(dc_title)
        # print(dc_time)
        # print("---------------------")

    return dc_num,dc_title,dc_time

# print(getpage(1))
todaydate=str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
totalpage=100

with open(todaydate+"_"+str(totalpage)+"p_.csv","w",newline="",encoding='utf8') as csvfile:
    spamwriter=csv.writer(csvfile,delimiter=" ",quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(1,totalpage+1):
        spamwriter.writerow(getpage(i),)