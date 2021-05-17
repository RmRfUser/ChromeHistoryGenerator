import sqlite3
import sys
import requests
from bs4 import BeautifulSoup
import os
import datetime
import random

username = os.getlogin()
con = sqlite3.connect('C:\\Users\\'+username+ '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History')
cur = con.cursor()

def from_chrome_time(timestamp):
    epoch_start = datetime.datetime(1601,1,1)
    delta = datetime.timedelta(microseconds=int(timestamp))
    return(epoch_start + delta)

def to_chrome_time(date):
    epoch_start = datetime.datetime(1601, 1, 1)
    diff = date - epoch_start
    seconds_in_day = 60 * 60 * 24
    return '{:<017d}'.format(diff.days * seconds_in_day + diff.seconds + diff.microseconds)

def randomtime(start, end, n):
    frmt = '%H:%M:%S'
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    td = etime - stime
    return [random.random() * td + stime for _ in range(n)]

def randomdate(start,end,n):
    frmt = '%Y-%m-%d'
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    td = etime - stime
    return [random.random() * td + stime for _ in range(n)]

def get_total_urls():
    res = cur.execute("SELECT id FROM urls ORDER BY id DESC LIMIT 1;")
    rows = cur.fetchall()
    total = rows[0]
    return int(total[0])

def get_title(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    if soup.title:
        return(soup.title.string)
    else:
        return ""

def insert_urls():
    print("Inserting urls...")
    f = open(sys.argv[1],"r")
    url_data = f.read()
    f.close()
    urls = url_data.split("\n")
    del urls[-1]
    url_dict = []
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
    for url in urls:
        try:
            r = requests.get(url,headers=headers)
        except:
            continue
        title =  get_title(r.content)
        if title == "":
            title = url.split("/")
            title = title[2]
            title = title.split(".")
            if title[0] == "www":
                title = title[1]
            else:
                title = title[0]

        cur.execute('insert into urls (url,title,visit_count,typed_count,last_visit_time,hidden) VALUES ("'+url+'","'+title+'", 1,1,13265399616887477,0);')
        con.commit()

insert_urls()
total_urls = get_total_urls()
random_times = randomtime("9:35:47","23:35:47",25000)
random_dates = randomdate("2016-2-2","2021-5-5",25000)
random_dates.sort()

print("Inserting visits...")
for x in range(len(random_dates)):
    year = random_dates[x].year
    month = random_dates[x].month
    day = random_dates[x].day
    hour = random_times[x].hour
    minute = random_times[x].minute
    second = random_times[x].second
    full_date = datetime.datetime(year,month,day,hour,minute,second)
    chrome_time = to_chrome_time(full_date)
    url_id = random.randint(0,total_urls)
    cur.execute('insert into visits (url,visit_time,from_visit,transition,segment_id,visit_duration,incremented_omnibox_typed_score,publicly_routable) VALUES ('+ str(url_id)+','+str(chrome_time)+',0,805306368,0,0,0,1);')
    con.commit()
