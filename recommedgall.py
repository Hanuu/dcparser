from bs4 import BeautifulSoup
import requests
import datetime
import re


def get_dccontent(articlenumber):
    url="http://gall.dcinside.com/board/view/?id=bitcoins&no="+articlenumber+"&page=1&exception_mode=recommend"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Mactinosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0"
    }
    r = requests.get(url, headers=headers)
    html=r.text
    soup=BeautifulSoup(str(html),"lxml")
    result_text=str(soup.find_all(class_="s_write"))

    result_text = re.sub('[a-zA-Z]', '', result_text)
    result_text = re.sub('[\{\}\[\]\/?,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]', '', result_text)
    return result_text

def get_dchtml():
    url="http://gall.dcinside.com/board/lists/?id=bitcoins&page=1&exception_mode=recommend"

    # 페이지 이름
    # payload = {"id": "bitcoins","page":"1"}
    # 디씨인사이드는 현재 파이썬을 이용한 파싱을 막고있다.
    headers={
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent":"Mozilla/5.0 (Mactinosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0"
    }
    r=requests.get(url,headers=headers)
    return r.text

if __name__=="__main__":

    raw_html=get_dchtml()

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

    # string = str(articletime[6])

    datetoday= str(datetime.date.today()).split("-")



    for i in range(0,len(articlenumbers)):
        # dc_ip=articlewriters[i].get("ip")
        # dc_user=articlewriters[i].get("user_name")
        dc_num=str(articlenumbers[i].get_text())
        dc_title=articletitles[i].get_text()
        string=str(articletime[i])
        dc_time=string[26:45]

        dc_date = []
        dc_date.append(dc_time[0:4])
        dc_date.append(dc_time[5:7])
        dc_date.append(dc_time[8:10])

        if dc_date == datetoday:
            # print(dc_ip)
            # print(dc_user)
            print(dc_num)
            print(dc_title)
            print(dc_time)
            print(dc_date)
            print(get_dccontent(dc_num))
            print("---------------------")
