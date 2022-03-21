from bs4 import BeautifulSoup
import requests
import time

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=' ).text

soup= BeautifulSoup(html_text , 'lxml')
jobs=soup.find_all('li' , class_ = 'clearfix job-bx wht-shd-bx')

print("Put some skills that you are unfamiliar with")
unfamiliar_skill = input ()
print("******** Filtered result is : ********* ")

def finding_jobs () :
    for index , job in enumerate(jobs) :
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date :
            company_name=job.find('h3' , class_ = 'joblist-comp-name').text.replace(' ' , '')
            skills=job.find ('span' , class_= 'srp-skills').text.replace(' ' ,'')
            more_info = job.find('header').h2.a['href']
            if unfamiliar_skill not in skills :
                with open (f'posts/Result_Sample.txt' , 'a' ) as f :

                    f.write(f'company Name : {company_name.strip()} \n')
                    f.write(f'Required Skills : {skills.strip()} \n')
                    f.write(f'Published date : {published_date.strip()} \n')
                    f.write(f'More info : {more_info} \n')
                    f.write('******************************* \n')
    print(f' file saved ')



if __name__ == '__main__' :
    while True :
        finding_jobs()
        time_wait = 2 #in minutes
        print(f' Waiting {time_wait} minutes ')
        time.sleep(time_wait*60)