import os
import time
import re
from multiprocessing.pool import Pool
import requests

def wget_cookie(url):
    data = os.popen('wget -qO- --no-cookies --header "Cookie: PREF=ID=1111111111111111:FF=0:LD=en:TM=1436290443:LM=1436416084:GM=1:V=1:S=OAaQWZel2Z7y4x1p; NID=74=GLwB9lf6lZlA5_McRg8SlHSZ8yX1Kgyfg5Ws_8TxuMzk1PxAPTuo8rlQGSgiZMA-qLf30iwlQAtiz5rlitcVTHMOW7rOv9VvEATdigqequ1R7Vw-K2fDKYDXQx890ZeIr3VGCBpT_Y2qnVwkAQbuTeV96zbPOItcst2Vv65f3cWeL32iKowtBN-5plPXu8ryEhE-Y1mnSdfG9pO16fwPNP_xqMHM6nBVPu-7-Wxhd1Sva4RtZKJ7_mrIljfWbnb8pi3udFecv7HroY2L4N4Gg5npQbkJ789IdLmPy0QmZGpsXDEuq4CAat32c_EdmWSrXO0; SID=DQAAALkBAACNQ2_VECWVHHPvzPw5zeCz4i7sCGrZ-EPJnSstSx_bAHKaUK-sGsJz_NsCJarNpJ6qe-5Ts6fGe5c0FypLc0OKOcBiFEuNziFTPoNDFGVREU5RDBPd0s95-SrwlQyJYkIMbtad44X0QdEf52b9jX4sOFQ088XTCd3D5LBEycjM6Opsekt_ftzt1kp52LeDx8-jjBz4MW-_Z7TDlZaSNxoVy3w4IDFfll7gJf3u75Rc8EA78XTLUXh1DVfIq7oYtwGDQ36tZ6rnWHajS-toXtEDdUma1P5CRXr13OZ5pEwLAT8qGFc3q7GKelHa0l5HcSe6izm7BhoaZq_c4qspMOxfbDBBam3vGMOvqrzKBT6U7mIQuIidZYFWn--SePbFSN_JW3bExOGiwbvlagNX0M9LpU7CxdsbdNlxkcwq0466u-rI-eOnauauJWPvSVUuCIE_RxUsuDCw90lGGfT2wNFR5zBnMzC0VLctZFS-HhXjMkrs3-KxcUDYsRYEX2dbU4YV8uV9yg5JfEuufmMMKQNNqQKB-xBEmFScpVMvso9tmt3I7-0T7bXi9NaYcZ6cD0BZXFHJ7zmRQ_MVI6kXUTXZ; HSID=ATVQjd3hxGbpcRAUF; SSID=AZjLdgea1C8pxyeyc; APISID=soBn4_aazTI4Wywn/ADRCh3F_lHo-hPEXx; SAPISID=vhXD61-cvsSQwADN/A8hDmgS1-sePcS7Rp; _ga=GA1.3.1983500809.1437616179; OGPC=4061155-2:; PLAY_ACTIVE_ACCOUNT=ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=mounarajan@semantics3.com; PLAY_PREFS=CtwDCKrLu9TFChLSAwoCSU4Q8Pn0zZgqGpcDERITFBUWGNQB1QGDAqsC2QPCBMQE4wXlBegF1wbYBt4G3wbdD_APkJWBBpGVgQaSlYEGk5WBBpWVgQaXlYEGpJWBBq2VgQa4lYEGwZWBBsSVgQbFlYEGyJWBBs6VgQbPlYEG0JWBBtSVgQbZlYEG65WBBuyVgQbtlYEG8pWBBviVgQb5lYEGhpaBBoiWgQaMloEGj5aBBpCWgQaeloEGn5aBBqCWgQahloEGppaBBqeWgQaoloEGypeBBu6XgQbvl4EGgZiBBoWYgQa-mIEGiJqBBqObgQatm4EGy5uBBrudgQa8nYEGw52BBsSdgQbFnYEGxp2BBsedgQbdnYEG7J2BBpCegQbon4EG-5-BBoCggQakoIEG9aCBBoShgQaQoYEGwKGBBsuhgQbMoYEGzaGBBu6hgQbxoYEG4qKBBvOigQaxo4EGmqSBBrKkgQbvpIEGhKWBBq-lgQbqpYEGnaaBBsamgQa3p4EGx6eBBo-ogQbNqIEGvKyBBoOugQaZr4EG1q-BBtivgQbjr4EGlbCBBuD8nDEo8Pn0zZgqOiQxYTBmN2Q0Yy1hZDNlLTQ2NTAtYmU3Ny1jYmY1Njk3ZmI2YjQ:S:ANO1ljKOEhExS4ysyg; _gat=1;" %s'% url).read()
    print data

def wget_sepcial(url):
    data = os.popen('wget  -qO- --header="Accept: text/html" --user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0"  %s'% url).read()
    return data

def urlLib(url):
    
    user_agent = 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'
    headers = {'User-Agent': user_agent}
    data = requests.get(url,headers = headers)
    return data.text.encode('utf-8')


def youtube_again(url,url1):
    f2 = open('main-urls.txt','a')
    f3 = open('main-urls1.txt','a')
    url = re.sub(r"[\s\n]*","",url)
    #url = re.sub(r'\&','\&',url)
    print url
    data = urlLib(url)
    data = str(data)

    if re.search(r'(?mis)channelId\"\:\s\"([^\"]*)\"',data):
        links = re.findall(r'(?mis)channelId\"\:\s\"([^\"]*)\"',data)
        for link in links:
            if re.search(r'^htt',link):
                f2.write(link+"\n")
                print (link+"\n")
            elif re.search(r'\w',link):
                link = re.sub(r'^','http://youtube.com/channel/',link)
                link = re.sub(r'(.*?channel\/.*)',r'\1/about',link)
                link = re.sub(r'amp\;',r'',link)
                f2.write(link+"\n")
                print (link+"\n")
                #data_extract(link)

        if re.search(r'(?mis)videoId\"\:\s\"([^\"]*)\"',data):
            links = re.findall(r'(?mis)videoId\"\:\s\"([^\"]*)\"',data)
            for link in links:
                if re.search(r'^htt',link):
                    f3.write(link+"\n")
                    print (link+"\n")
                elif re.search(r'\w',link):
                    link = re.sub(r'^','https://www.youtube.com/watch\?v=',link)
              
                    link = re.sub(r'amp\;',r'',link)
                    f3.write(link+"\n")
                    print (link+"\n")
                    #deatilsExtract(link)
        if re.search(r'(?mis)&pageToken=\w+',url1):
            url1 = re.sub(r'&publishedAfter=[^\&]*','',url1)
            url1 = re.sub(r'&pageToken=\w+',r'',url1)
        if re.search(r'(?mis)nextPageToken\"\:\s\"([^\"]*)\"',data):
            links = re.findall(r'(?mis)nextPageToken\"\:\s\"([^\"]*)\"',data)[0]
            url1 = re.sub(r'&publishedAfter=[^\&]*','',url1)
            url1 = url1+"&pageToken={0}".format(links)
            print (url1)
            links_extract1(url1)

def links_extract1(url):
    f2 = open('main-urls.txt','a')
    f3 = open('main-urls1.txt','a')
    url = re.sub(r"[\s\n]*","",url)
    #url = re.sub(r'\&','\&',url)
    print url
    data = urlLib(url)
    data = str(data)

    if re.search(r'(?mis)channelId\"\:\s\"([^\"]*)\"',data):
        links = re.findall(r'(?mis)channelId\"\:\s\"([^\"]*)\"',data)
        for link in links:
            if re.search(r'^htt',link):
                f2.write(link+"\n")
                print (link+"\n")
            elif re.search(r'\w',link):
                link = re.sub(r'^','http://youtube.com/channel/',link)
                link = re.sub(r'(.*?channel\/.*)',r'\1/about',link)
                link = re.sub(r'amp\;',r'',link)
                f2.write(link+"\n")
                print (link+"\n")
                #data_extract(link)

        if re.search(r'(?mis)videoId\"\:\s\"([^\"]*)\"',data):
            links = re.findall(r'(?mis)videoId\"\:\s\"([^\"]*)\"',data)
            for link in links:
                if re.search(r'^htt',link):
                    f3.write(link+"\n")
                    print (link+"\n")
                elif re.search(r'\w',link):
                    link = re.sub(r'^','https://www.youtube.com/watch\?v=',link)
              
                    link = re.sub(r'amp\;',r'',link)
                    f3.write(link+"\n")
                    print (link+"\n")
                    #deatilsExtract(link)
        if re.search(r'(?mis)&pageToken=\w+',url):
            url = re.sub(r'&publishedAfter=[^\&]*','',url)
            url = re.sub(r'&pageToken=\w+',r'',url)
        if re.search(r'(?mis)nextPageToken\"\:\s\"([^\"]*)\"',data):
            links = re.findall(r'(?mis)nextPageToken\"\:\s\"([^\"]*)\"',data)[0]
            url = re.sub(r'&publishedAfter=[^\&]*','',url)
            url = url+"&pageToken={0}".format(links)
            print (url)
            links_extract1(url)


       
    

def links_extract(url):
    f2 = open('main-urls.txt','a')
    f3 = open('main-urls1.txt','a')
    url = re.sub(r"[\s\n]*","",url)
    #url = re.sub(r'\&','\&',url)
    print url
    data = urlLib(url)
    data = str(data)

    if re.search(r'(?mis)channelId\"\:\s\"([^\"]*)\"',data):
        links = re.findall(r'(?mis)channelId\"\:\s\"([^\"]*)\"',data)
        for link in links:
            if re.search(r'^htt',link):
                f2.write(link+"\n")
                print (link+"\n")
            elif re.search(r'\w',link):
                link = re.sub(r'^','http://youtube.com/channel/',link)
                link = re.sub(r'(.*?channel\/.*)',r'\1/about',link)
                link = re.sub(r'amp\;',r'',link)
                f2.write(link+"\n")
                print (link+"\n")
                #data_extract(link)

        if re.search(r'(?mis)videoId\"\:\s\"([^\"]*)\"',data):
            links = re.findall(r'(?mis)videoId\"\:\s\"([^\"]*)\"',data)
            for link in links:
                if re.search(r'^htt',link):
                    f3.write(link+"\n")
                    print (link+"\n")
                elif re.search(r'\w',link):
                    link = re.sub(r'^','https://www.youtube.com/watch\?v=',link)
              
                    link = re.sub(r'amp\;',r'',link)
                    f3.write(link+"\n")
                    print (link+"\n")
                    #deatilsExtract(link)

        if re.search(r'(?mis)publishedAt\"\:\s\"([^\"]*)T[^\"]*\"',data):
            links = re.findall(r'(?mis)publishedAt\"\:\s\"([^\"]*)T[^\"]*\"',data)
            for link in links:
                url_li = "https://www.googleapis.com/youtube/v3/search?part=snippet&publishedBefore={0}T00%3A00%3A00Z&type=video&key=AIzaSyAnimLnprBHU5BVrd_61ynch4x5gPzrsPA".format(link)
                youtube_again(url_li,url)
                
        if re.search(r'(?mis)&pageToken=\w+',url):
            url = re.sub(r'&publishedAfter=[^\&]*','',url)
            url = re.sub(r'&pageToken=\w+',r'',url)
        if re.search(r'(?mis)nextPageToken\"\:\s\"([^\"]*)\"',data):
            links = re.findall(r'(?mis)nextPageToken\"\:\s\"([^\"]*)\"',data)[0]
            url = re.sub(r'&publishedAfter=[^\&]*','',url)
            url = url+"&pageToken={0}".format(links)
            print (url)
            links_extract(url)


def get_data():
    f2 = open('main-urls.txt','r')

    nprocs = 50 # nprocs is the number of processes to run
    ParsePool = Pool(nprocs)
    #ParsePool.map(btl_test,url)
    ParsedURLS = ParsePool.map(data_extract,f2)

def get_urls1():
    f2 = open('main-urls.txt1','r')

    nprocs = 50 # nprocs is the number of processes to run
    ParsePool = Pool(nprocs)
    #ParsePool.map(btl_test,url)
    ParsedURLS = ParsePool.map(deatilsExtract,f2)

def data_extract(url):
    f1 = open('presonal_urls.txt','a')
    f2 = open('facebook_urls.txt','a')
    f3 = open('crawled_email1','a')
    url = re.sub(r"[\s\n]*","",url)
    url = re.sub(r'\&','\&',url)
    data = wget_sepcial(url)
    data = str(data)

    if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
        email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
        if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
            email = re.sub(r'(.*)\/',r"\1",email)
            f3.write(email+"\n")
                                            #f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
            print (email)                           

    if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
        email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
        for mail in email:
            if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
                mail = re.sub(r'(.*)\/',r"\1",mail)
                f3.write(mail+"\n")
                                    #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                print (mail)
    if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
        must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
        for mail in must:
            if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
                mail = re.sub(r'(.*)\/',r"\1",mail)
                f3.write(mail+"\n")
                                    #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                print (mail)

    if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
        ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
        ear = re.sub(r'(.*)\/',r"\1",ear)
        f3.write(ear+"\n")
                            #f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
        print (ear)

    if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
        ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
        for mail in ear:
            if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
                mail = re.sub(r'(.*)\/',r"\1",mail)
                f3.write(mail+"\n")
                                    #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                print (mail) 

    if re.search(r'(?mis)<a\shref\=\"([^\"]*\.com)\"\srel\=\"me.*?title\=\"[^\"]*\"',data):
        email = re.findall(r'(?mis)<a\shref\=\"([^\"]*\.com)\"\srel\=\"me.*?title\=\"[^\"]*\"',data)[0]
        print (email)
        f1.write(email)
        crawl_fb_again(email) 

    if re.search(r'(?mis)<a\shref\=\"([^\"]*)\"\srel\=\"me.*?title\=\"[^\"]*\"',data):
        email = re.findall(r'(?mis)<a\shref\=\"([^\"]*)\"\srel\=\"me.*?title\=\"[^\"]*\"',data)[0]
        print (email)
        f1.write(email)
        crawl_fb_again(email) 

    if re.search(r'(?mis)<a\shref\=\"([^\"]*)\"\srel\=\"me\snofollow\"[^\"]*\"[^\"]*\"\stitle\=\"[^\"]*Facebook\"',data):
        email = re.findall(r'(?mis)<a\shref\=\"([^\"]*)\"\srel\=\"me\snofollow\"[^\"]*\"[^\"]*\"\stitle\=\"[^\"]*Facebook\"',data)[0]
        print (email) 
        f2.write(email)
        crawl_fb_onceagain(email)


def dedup_one():
    with open('crawled_email1') as result:
        uniqlines = set(result.readlines())
        with open('crawled_email1', 'w') as rmdup:
            rmdup.writelines(set(uniqlines))

def crawl_fb_onceagain(url):
        #f1 = open('facebook_crawled_urls','r+')
    f2 = open('facebook_crawled_again','a')
    f3 = open('crawled_email1','a')
    f4 = open('crawled_email_ugly','a')
    f5 = open('facebook-crawled_email_ids_report.json','a')
    if re.search(r'^htt',url):
        lin = re.sub(r"\s*","",url)
        #print (lin)
        try:
            data = wget_sepcial(lin) 
            data = str(data)
                #print (data)

            if re.search(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data):
                email = re.findall(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data)
                for fb in email:
                    url = re.sub(r'\?.*','',fb)
                    if re.search(r'^htt',url):
                        fb_cac = re.sub(r'\?.*','',fb)
                        fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
                        fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
                        f2.write(fb_cac+"\n")
                        print (fb_cac)
                        time.sleep(sleep)
                        if re.search(r'^htt',fb_cac):
                            #print (lin)
                            first = "/info?tab=page_info"
                            second = "/about?section=contact-info"
                            url = fb_cac+first   
                            print (url)  
                            try:                                                                                             
                                data = wget_sepcial(url)
                                    
                                data = str(data)
                                if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
                                    link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
                                    for mail in link:
                                        mail = re.sub(r'\&\#064\;','@',mail)
                                        f4.write(mail+"\n")
                                        fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
                                        for smail in fmail:

                                            f3.write(smail+"\n")
                                            f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
                                            print (smail)
                            except Exception: 
                                pass    

                                    #else:
                                     #   url = fb_cac+second  
                                      #  print (url)
                                       # try:                                                                                               
                                        #    output.wget_sepcial(url)
                                         #   data = self.data 
                                          #  data = str(data)
                                           # if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
                                            #    link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
                                             #   for mail in link:
                                              #      mail = re.sub(r'\&\#064\;','@',mail)
                                               #     f4.write(mail+"\n")
                                                #    fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
                                                 #   for smail in fmail:

                                                  #      f3.write(smail+"\n")
                                                   #     f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
                                                    #    print (smail)
                                        #except Exception: 
                                         #   pass    

            else: 
                print ("not found")
                f5.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")
        except Exception: 
            pass

def crawl_fb_again(url):
        #f1 = open('facebook_crawled_urls','r+')
    f2 = open('facebook_crawled_again','a')
    f3 = open('crawled_email1','a')
    f4 = open('crawled_email_ugly','a')
    f5 = open('facebook-crawled_email_ids_report.json','a')
    if re.search(r'^\w',url):
        lin = re.sub(r"\s*","",url)
            #print (lin)
        try:
            url_lin = re.sub(r'(.*?\/)',r"\1",lin)
            print (url_lin)
            data = wget_sepcial(lin)
                
            data = str(data)
                #print (data)
                #print (data)

            if re.search(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data):
                email = re.findall(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data)
                for fb in email:
                    url = re.sub(r'\?.*','',fb)
                    if re.search(r'^htt',url):
                        fb_cac = re.sub(r'\?.*','',fb)
                        fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
                        fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
                        f2.write(fb_cac+"\n")
                        print (fb_cac)
                        
                        if re.search(r'^\w',fb_cac):
                            try:                                                                                             
                                data = wget_sepcial(url)
                                     
                                data = str(data)
                                    #print (data)
                                if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                                    email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
                                    if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
                                        email = re.sub(r'(.*)\/',r"\1",email)
                                        f3.write(email+"\n")
                                            #f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
                                        print (email)

                                if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                                    email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
                                    for mail in email:
                                        if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
                                            mail = re.sub(r'(.*)\/',r"\1",mail)
                                            f3.write(mail+"\n")
                                    #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                                            print (mail)
                                if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                                    must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
                                    for mail in must:
                                        if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
                                            mail = re.sub(r'(.*)\/',r"\1",mail)
                                            f3.write(mail+"\n")
                                    #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                                            print (mail)

                                if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
                                    ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
                                    ear = re.sub(r'(.*)\/',r"\1",ear)
                                    f3.write(ear+"\n")
                            #f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
                                    print (ear)

                                if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
                                    ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
                                    for mail in ear:
                                        if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
                                            mail = re.sub(r'(.*)\/',r"\1",mail)
                                            f3.write(mail+"\n")
                                #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                                            print (mail)

                                if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
                                    ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)
                                    if re.search(r'(?ms)^\/',ear[0]):
                                        ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
                                        print (ear)
                                        link_again11(ear,sleep)
                                if re.search(r'(?mis)^.*',ear[0]):
                                        ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
                                        print (ear)
                                        link_again11(ear,sleep)

                                if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
                                    ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)
                                    if re.search(r'(?mis)^\/',ear[0]):
                                        ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
                                        print (ear)
                                        link_again11(ear,sleep)
                                    if re.search(r'(?mis)^.*',ear[0]):
                                        ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
                                        print (ear)
                                        link_again11(ear,sleep)
                                    
                                    print (ear[0])
                                    link_again11(ear[0],sleep)

                                if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
                                    ear = re.findall(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)
                                    if re.search(r'(?ms)^\/',ear[0]):
                                        ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
                                        print (ear)
                                        link_again11(ear,sleep)
                                    if re.search(r'(?mis)^.*',ear[0]):
                                        ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
                                        print (ear)
                                        link_again11(ear,sleep)
                                    
                                    print (ear)
                                    link_again11(ear[0],sleep)

                                if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
                                    ear = re.findall(r'(?msi)<a.*?href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)
                                    if re.search(r'(?mis)^\/',ear[0]):
                                        ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
                                        print (ear)
                                        link_again11(ear,sleep)
                                    if re.search(r'(?mis)^.*',ear[0]):
                                        ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
                                        print (ear)
                                        link_again11(ear,sleep)
                                        
                                    print (ear[0])
                                    link_again11(ear[0],sleep)

                            except Exception: 
                                pass    

                                    #else:
                                     #   url = fb_cac+second  
                                      #  print (url)
                                       # try:                                                                                               
                                        #    output.wget_sepcial(url)
                                         #   data = self.data 
                                          #  data = str(data)
                                           # if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
                                            #    link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
                                             #   for mail in link:
                                              #      mail = re.sub(r'\&\#064\;','@',mail)
                                               #     f4.write(mail+"\n")
                                                #    fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
                                                 #   for smail in fmail:

                                                  #      f3.write(smail+"\n")
                                                   #     f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
                                                    #    print (smail)
                                        #except Exception: 
                                         #   pass    

            else: 
                print ("not found")
                f5.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")
        except Exception: 
            pass  

        

    if re.search(r'^\w',url):
        lin = re.sub(r"\s*","",url)
        print (lin)
        try:
            url_lin = re.sub(r'(.*?\/)',r"\1",lin)
                #print (url_lin)
            data = wget_sepcial(lin)
            data = str(data) 
                
            if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
                if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
                    email = re.sub(r'(.*)\/',r"\1",email)
                    f3.write(email+"\n")
                                            #f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
                    print (email)

            if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
                for mail in email:
                    if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
                        mail = re.sub(r'(.*)\/',r"\1",mail)
                        f3.write(mail+"\n")
                                    #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                        print (mail)
            if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
                for mail in must:
                    if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
                        mail = re.sub(r'(.*)\/',r"\1",mail)
                        f3.write(mail+"\n")
                                    #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                        print (mail)

            if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
                ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
                ear = re.sub(r'(.*)\/',r"\1",ear)
                f3.write(ear+"\n")
                            #f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
                print (ear)

            if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
                ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
                for mail in ear:
                    if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
                        mail = re.sub(r'(.*)\/',r"\1",mail)
                        f3.write(mail+"\n")

            if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
                print ("yes")
                ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)
            #print (ear)
                if re.search(r'(?ms)^\/',ear[0]):
                    ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
                    print (ear)
                    link_again11(ear,sleep)
                if re.search(r'(?mis)^.*',ear[0]):
                    ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
                    print (ear)
                    link_again11(ear,sleep)
                    
                print (ear)
                link_again11(ear[0],sleep)

            if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
                ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)
                if re.search(r'(?ms)^\/',ear[0]):
                    ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
                    print (ear)
                    link_again11(ear,sleep)
                if re.search(r'(?mis)^.*',ear[0]):
                    ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
                    print (ear)
                    link_again11(ear,sleep)
                
                print (ear)
                link_again11(ear[0],sleep)

            if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
                print ("yes")
                ear = re.findall(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)
                #print (ear)
                if re.search(r'(?ms)^\/',ear[0]):
                    ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
                    print (ear)
                    link_again11(ear,sleep)
                if re.search(r'(?mis)^.*',ear[0]):
                    ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
                    print (ear)
                    link_again11(ear,sleep)
                
                print (ear)
                link_again11(ear[0],sleep)

            if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
                ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)
                if re.search(r'(?ms)^\/',ear[0]):
                    ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
                    print (ear)
                    link_again11(ear,sleep)
                if re.search(r'(?mis)^.*',ear[0]):
                    ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
                    print (ear)
                    link_again11(ear,sleep)
                    
                print (ear)
                link_again11(ear[0],sleep)

        except Exception: 
            pass  

        

def link_again11(url):
    f2 = open('facebook_crawled_again','a')
    f3 = open('crawled_email1','a')
    f4 = open('crawled_email_ugly','a')
    f5 = open('facebook-crawled_email_ids_report.json','a')
    f6 = open('contact-links','a')

    if re.search(r'^\w',url):
        lin = re.sub(r"\s*","",url)
        try:
            data = wget_sepcial(lin) 
            data = str(data) 
            if re.search(r'(?mis)\"textarea',data):
                print ("This is contact")
                f6.write(lin+"\n")
            if re.search(r'(?mis)form\"',data):
                print ("This is contact")
                f6.write(lin+"\n")
            if re.search(r'(?mis)\"form',data):
                print ("This is contact")
                f6.write(lin+"\n")
            if re.search(r'(?mis)\"submit',data):
                print ("This is contact")
                f6.write(lin+"\n")
        except Exception: 
            pass  

                                            #f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")

    if re.search(r'^\w',url):
        lin = re.sub(r"\s*","",url)
        print (lin)
        try:
            data = wget_sepcial(lin)
            data = str(data) 

            if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
                if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
                    email = re.sub(r'(.*)\/',r"\1",email)
                    f3.write(email+"\n")
                                            #f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
                    print (email)

            if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
                for mail in email:
                    if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
                        mail = re.sub(r'(.*)\/',r"\1",mail)
                        f3.write(mail+"\n")
                                    #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                        print (mail)
            if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
                for mail in must:
                    if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
                        mail = re.sub(r'(.*)\/',r"\1",mail)
                        f3.write(mail+"\n")
                                    #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                        print (mail)

            if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
                ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
                ear = re.sub(r'(.*)\/',r"\1",ear)
                f3.write(ear+"\n")
                            #f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
                print (ear)

            if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
                ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
                for mail in ear:
                    if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
                        mail = re.sub(r'(.*)\/',r"\1",mail)
                        f3.write(mail+"\n")

        except Exception: 
            pass  
        

def deatilsExtract(url):

    f3 = open('crawled_email1','a')
    f4 = open('final_data.csv','at')
    url = re.sub(r'(?mis)[\s\n]*','',url)
    url = re.sub(r'\&','\&',url)
    #url = re.sub(r'\?','\?',url)
    #url = re.sub(r'\;','\;',url)
    print url
    time.sleep(1)
    data = wget_sepcial(url)
    data = str(data)

    if re.search(r'(?mis)dev\-link\"\shref\=\"mailto\:([^\"]*)\"',data):
        email = re.findall(r'(?mis)dev\-link\"\shref\=\"mailto\:([^\"]*)\"',data)[0]
        print email
        f3.write(email+"\n")
        f4.write("{0},{1},{2}".format(url,url,email)+"\n")
    elif re.search(r'(?mis)dev\-link\"\shref\=\"mailto\:[^\"]*\"[^>]*>([^<]*)<',data):
        email = re.findall(r'(?mis)dev\-link\"\shref\=\"mailto\:([^\"]*)\"',data)[0]
        email = re.sub(r'(?mis)Email','',email)
        email = re.sub(r'(?mis)[\s\n]*','',email)
        print email
        f3.write(email+"\n")
        f4.write("{0},{1},{2}".format(url,url,email)+"\n")

    if re.search(r'(?mis)yt-uix-redirect-link">([^<]*)<\/a>',data):
        visit_site1 = re.findall(r'(?mis)yt-uix-redirect-link">([^<]*)<\/a>',data)
        for visit_site in visit_site1:
            print visit_site
            crawl_fb_again_again(visit_site,url)


    if re.search(r'(?mis)yt-uix-redirect-link">[^<]*<\/a><br\s\/><a\shref\=\"([^\"]*)\"',data):
        visit_site1 = re.findall(r'(?mis)yt-uix-redirect-link">[^<]*<\/a><br\s\/><a\shref\=\"([^\"]*)\"',data)
        for visit_site in visit_site1:
            print visit_site
            crawl_fb_again_again(visit_site,url)

def crawl_fb_again_again(url1,url):
        #f1 = open('facebook_crawled_urls','r+')
    sleep = 1
    main_url = url
    f2 = open('facebook_crawled_again','a')
    f3 = open('crawled_email1','a')
    f4 = open('crawled_email_ugly','a')
    f5 = open('facebook-crawled1_email_ids_report.json','a')
    f6 = open('final_data.csv','at')
    if re.search(r'^htt',url1):
        lin = re.sub(r'(?mis)[\s\n]*','',url1)
        lin = re.sub(r'\&','\&',lin)
        #lin = re.sub(r'\?','\?',lin)
        #lin = re.sub(r'\;','\;',lin)
        print (lin)
        try:
            data = wget_sepcial(lin)
            data = data 
            data = str(data)

            if re.search(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data):
                print "pause"
                email = re.findall(r'(?ms)og\:url\"\scontent\=\"([^\"]*)\"',data)
                for fb in email:
                    url2 = re.sub(r'\?.*','',fb)
                    if re.search(r'^htt',url2):
                        fb_cac = re.sub(r'\?.*','',fb)
                        fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
                        fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
                        f2.write(fb_cac+"\n")
                        print (fb_cac)
                        time.sleep(sleep)
                        if re.search(r'^htt',fb_cac):
                            #print (lin)
                            first = "/info?tab=page_info"
                            second = "/about?section=contact-info"
                            url2 = fb_cac+first   
                            print (url2)  
                            try:                                                                                             
                                data = wget_sepcial(url2)
                                data = data 
                                data = str(data)
                                if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
                                    link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
                                    for mail in link:
                                        mail = re.sub(r'\&\#064\;','@',mail)
                                        f4.write(mail+"\n")
                                        fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
                                        for smail in fmail:

                                            f3.write(smail+"\n")
                                            f6.write("{0},{1},{2}".format(url,url1,smail+"\n"))
                                            f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
                                            print (smail)
                            except Exception: 
                                pass    

            if re.search(r'(?mis)303"\shref\=\"([^\"]*)\"',data):
                email = re.findall(r'(?mis)303"\shref\=\"([^\"]*)\"',data)
                for fb in email:
                    url2 = re.sub(r'\?.*','',fb)
                    if re.search(r'^htt',url2):
                        fb_cac = re.sub(r'\?.*','',fb)
                        fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
                        fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
                        fb_cac = re.sub(r'([^\?]*)\?.*',r'\1',fb_cac)
                        fb_cac = re.sub(r'(.*?\.com\/[^\/]*)\/.*',r'\1',fb_cac)
                        f2.write(fb_cac+"\n")
                        print (fb_cac)
                        time.sleep(sleep)
                        if re.search(r'^htt',fb_cac):
                                #print (lin)
                            first = "/info?tab=page_info"
                            second = "/about?section=contact-info"
                            url2 = fb_cac+first   
                            print (url2)  
                            try:                                                                                             
                                data = wget_sepcial(url2)
                                data = data 
                                data = str(data)
                                if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
                                    link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
                                    for mail in link:
                                        mail = re.sub(r'\&\#064\;','@',mail)
                                        f4.write(mail+"\n")
                                        fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
                                        for smail in fmail:
                                            f3.write(smail+"\n")
                                            f6.write("{0},{1},{2}\n".format(url,url1,smail)+"\n")
                                            f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
                                            print (smail)
                            except Exception: 
                                pass

                        if re.search(r'^htt',fb_cac):
                                #print (lin)
                            first = "/info?tab=page_info"
                            second = "/about?section=contact-info"
                            url2 = fb_cac+second 
                            print (url2)  
                            try:                                                                                             
                                data = wget_sepcial(url2)
                                data = data 
                                data = str(data)
                                if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
                                    link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
                                    for mail in link:
                                        mail = re.sub(r'\&\#064\;','@',mail)
                                        f4.write(mail+"\n")
                                        fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
                                        for smail in fmail:
                                            f3.write(smail+"\n")
                                            f6.write("{0},{1},{2}\n".format(url,url1,smail)+"\n")
                                            f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
                                            print (smail)
                            except Exception: 
                                pass

            if re.search(r'(?mis)a\sclass\=\"\_8\_2\"\shref\=\"([^\"]*)',data):
                email = re.findall(r'(?mis)a\sclass\=\"\_8\_2\"\shref\=\"([^\"]*)',data)
                for fb in email:
                    url2 = re.sub(r'\?.*','',fb)
                    if re.search(r'^htt',url2):
                        fb_cac = re.sub(r'\?.*','',fb)
                        fb_cac = re.sub(r'.*sharer\.php$','',fb_cac)
                        fb_cac = re.sub(r'.*\/2008\/fbml$','',fb_cac)
                        f2.write(fb_cac+"\n")
                        print (fb_cac)
                        time.sleep(sleep)
                        if re.search(r'^htt',fb_cac):
                                #print (lin)
                            first = "/info?tab=page_info"
                            second = "/about?section=contact-info"
                            url2 = fb_cac+first   
                            print (url2)  
                            try:                                                                                             
                                data = wget_sepcial(url2)
                                data = data 
                                data = str(data)
                                if re.search(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data):
                                    link = re.findall(r'(?ms)class\=\"\_50f4\"\>([^\<]*\&\#064\;.*?[^<]*)<\/div>',data)
                                    for mail in link:
                                        mail = re.sub(r'\&\#064\;','@',mail)
                                        f4.write(mail+"\n")
                                        fmail = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',mail)
                                        for smail in fmail:
                                            f3.write(smail+"\n")
                                            f6.write("{0},{1},{2}\n".format(url,url1,smail)+"\n")
                                            f5.write("{\""+lin+"\" => \""+smail+"\"}"+"\n")
                                            print (smail)
                            except Exception: 
                                pass


            else: 
                print ("not found")
                f5.write("{\""+lin+"\" => \""+"not found"+"\"}"+"\n")
        except Exception: 
            pass


    if re.search(r'^\w',url1):
        lin = re.sub(r'(?mis)[\s\n]*','',url1)
        lin = re.sub(r'\&','\&',lin)
        #lin = re.sub(r'\?','\?',lin)
        #lin = re.sub(r'\;','\;',lin)
        try:
            url_lin = re.sub(r'(.*?\/)',r"\1",lin)
            print (url_lin)
            data = wget_sepcial(url_lin)
            data = data 
            data = str(data) 
                
            if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
                if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
                    email = re.sub(r'(.*)\/',r"\1",email)
                    f3.write(email+"\n")
                    f6.write("{0},{1},{2}".format(url,url1,email)+"\n")
                                            #f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
                    print (email)

            if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
                for mail in email:
                    if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
                        mail = re.sub(r'(.*)\/',r"\1",mail)
                        f3.write(mail+"\n")
                        f6.write("{0},{1},{2}".format(url,url1,mail)+"\n")
                                #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                        print (mail)
            if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
                for mail in must:
                    if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
                        mail = re.sub(r'(.*)\/',r"\1",mail)
                        f3.write(mail+"\n")
                        f6.write("{0},{1},{2}".format(url,url1,mail)+"\n")
                                #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                        print (mail)

            if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
                ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
                ear = re.sub(r'(.*)\/',r"\1",ear)
                f3.write(ear+"\n")
                f6.write("{0},{1},{2}".format(url,url1,mail)+"\n")
                        #f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
                print (ear)

            if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
                ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
                for mail in ear:
                    if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
                        mail = re.sub(r'(.*)\/',r"\1",mail)
                        f3.write(mail+"\n")
                        f6.write("{0},{1},{2}".format(url,url1,mail)+"\n")

            if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
                ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)
                #print (ear)
                if re.search(r'(?ms)^\/',ear[0]):
                    ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
                    print (ear)
                    link_again(ear,sleep)
                if re.search(r'(?mis)^.*',ear[0]):
                    ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
                    print (ear)
                    link_again(ear,sleep,main_url)
                
                    print (ear)
                    link_again(ear[0],sleep,main_url)

            if re.search(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
                ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)
                if re.search(r'(?ms)^\/',ear[0]):
                    ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
                    print (ear)
                    link_again(ear,sleep,main_url)
                if re.search(r'(?mis)^.*',ear[0]):
                    ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
                    print (ear)
                    link_again(ear,sleep,main_url)
                    
                print (ear)
                link_again(ear[0],sleep,main_url)

            if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data):
                ear = re.findall(r'(?msi)<a.*?href\=\"([^\"]*[\/]*contact.*?[^\"]*)\"',data)[0]
                #print (ear)
                #if re.search(r'(?ms)^\/',ear[0]):
                
                print (ear)
                link_again(ear,sleep,main_url)
                #if re.search(r'(?mis)^.*',ear[0]):
                #   ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
                #   print (ear)
                #   link_again(ear,sleep,main_url)
                

            if re.search(r'(?msi)<a.*?href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data):
                ear = re.findall(r'(?msi)<a\s*href\=\"([^\"]*[\/]*about.*?[^\"]*)\"',data)[0]
                #if re.search(r'(?ms)^\/',ear[0]):
                #ear = re.sub(r'(.*)\/',r"%s\1"%url_lin,ear[0])
                print (ear)
                link_again(ear,sleep,main_url)
                #if re.search(r'(?mis)^.*',ear[0]):
                #   ear = re.sub(r'(.*)',r"%s/\1"%url_lin,ear[0])
                #   print (ear)
                #   link_again(ear,sleep,main_url)
                    
                #print (ear)
                #link_again(ear[0],sleep,main_url)

        except Exception: 
            pass  

def link_again(url,sleep,main_url):
        f2 = open('facebook_crawled_again','a')
        f3 = open('crawled_email1','a')
        f4 = open('crawled_email_ugly','a')
        f5 = open('facebook-crawled_email_ids_report.json','a')
        f6 = open('contact-links','a')
        f7 = open('final_data.csv','at')
                                            #f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")

        if re.search(r'^\w',url):
            lin = re.sub(r"\s*","",url)
            print (lin)
            try:
                data = wget_sepcial(lin)
                data = str(data) 

                if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                    email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)[0]
                    if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',email):
                        email = re.sub(r'(.*)\/',r"\1",email)
                        f3.write(email+"\n")
                        f7.write("{0},{1},{2}".format(main_url,url,mail)+"\n")              #f4.write("{\""+lin+"\" => \""+email+"\"}"+"\n")
                        print (email)

                if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                    email = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
                    for mail in email:
                        if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
                            mail = re.sub(r'(.*)\/',r"\1",mail)
                            f3.write(mail+"\n")
                            f7.write("{0},{1},{2}".format(main_url,url,mail)+"\n")  
                                    #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                            print (mail)
                if re.search(r'(?ms)mailto\:([^\"]*)\"',data):
                    must = re.findall(r'(?ms)mailto\:([^\"]*)\"',data)
                    for mail in must:
                        if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*)',mail):
                            mail = re.sub(r'(.*)\/',r"\1",mail)
                            f3.write(mail+"\n")
                            f7.write("{0},{1},{2}".format(main_url,url,mail)+"\n")  
                                    #f4.write("{\""+lin+"\" => \""+mail+"\"}"+"\n")
                            print (mail)

                if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+]*))',data):
                    ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)[0]
                    ear = re.sub(r'(.*)\/',r"\1",ear)
                    f3.write(ear+"\n")
                    f7.write("{0},{1},{2}".format(main_url,url,mail)+"\n")  
                            #f4.write("{\""+lin+"\" => \""+ear+"\"}"+"\n")
                    print (ear)

                if re.search(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\-\_\+]*))',data):
                    ear = re.findall(r'(?ms)([\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\_\-\+]*))',data)
                    for mail in ear:
                        if re.search(r'(?ms)[\w\_\-\.\+]+@[\w\-\_\+]+[\.]+\w+(?:[\w\.\+\_\-]*)',mail):
                            mail = re.sub(r'(.*)\/',r"\1",mail)
                            f3.write(mail+"\n")
                            f7.write("{0},{1},{2}".format(main_url,url,mail)+"\n")  

            except Exception: 
                pass  

        
def dedupUrls():
    with open('cat_links.txt') as result:
        uniqlines = set(result.readlines())
        with open('cat_links1.txt', 'w') as rmdup:
            rmdup.writelines(set(uniqlines))

def dedupUrls1():
    with open('main_links.txt') as result:
        uniqlines = set(result.readlines())
        with open('main_links1.txt', 'w') as rmdup:
            rmdup.writelines(set(uniqlines))

def dedupUrls2():
    with open('app_links.txt') as result:
        uniqlines = set(result.readlines())
        with open('app_links1.txt', 'a') as rmdup:
            rmdup.writelines(set(uniqlines))

def dedupUrls4():
    with open('app_links1.txt') as result:
        uniqlines = set(result.readlines())
        with open('app_links1.txt', 'a') as rmdup:
            rmdup.writelines(set(uniqlines))


def dedupUrls3():
    with open('final_data.csv') as result:
        uniqlines = set(result.readlines())
        with open('final_data1.csv', 'w') as rmdup:
            rmdup.writelines(set(uniqlines))





#extractUrls("https://play.google.com/store/apps")
#dedupUrls()

#assigneCategory()
#dedupUrls1()
#extracctMainurls()
#deatilsExtract("https://play.google.com/store/apps/details?id=com.tocaboca.tocakitchen2")
#urlsDeatilsExtract("https://play.google.com/store/apps/details?id=com.issess.flashplayerpro")
#get_urls1()
#dedupUrls2()
#dedupUrls4()
#get_data()
#dedupUrls3()
links_extract("https://www.googleapis.com/youtube/v3/search?part=snippet&publishedAfter=2014-12-28T00%3A00%3A00Z&type=video&key=AIzaSyAnimLnprBHU5BVrd_61ynch4x5gPzrsPA")
#get_data()
    
