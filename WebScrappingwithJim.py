###
from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())
    
    
###
from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    # content = html_file.read()
    
    soup = BeautifulSoup(html_file, 'lxml')
    print(soup.prettify())
    
###
from bs4 import BeautifulSoup
with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('h5') # note here if u use just find method it give only one if use findall then it give all
    print(tags)
    

###
from bs4 import BeautifulSoup
html_file = open("home.html", 'r')
soup = BeautifulSoup(html_file, 'lxml')
print(soup.prettify()) #Note if not give prettify a bracket it will not give output in seriol manner

###
from bs4 import BeautifulSoup
html_file = open("home.html", 'r')
soup = BeautifulSoup(html_file, 'lxml')
tags = soup.find_all('div')
print(tags)

###
from bs4 import BeautifulSoup
with open("home.html", 'r') as html_file :
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags:
        print(course.text)
'''
Python for beginners
Python Web Development 
Python Machine Learning
'''

###
from bs4 import BeautifulSoup
with open("home.html", 'r') as html_file :
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        print(course)
        
###
from bs4 import BeautifulSoup
with open("home.html", 'r') as html_file :
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        print(course.h5)
'''
<h5 class="card-title">Python for beginners</h5>
<h5 class="card-title">Python Web Development</h5> 
<h5 class="card-title">Python Machine Learning</h5>
'''

###
from bs4 import BeautifulSoup
with open("home.html", 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml') # if you contain here space near lxml(" ") you get errors (bs4.FeatureNotFound)
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a
        
        print(course_name)
        print(course_price)
"""
Python for beginners
<a class="btn btn-primary" href="#">Start for 20$</a> 
Python Web Development
<a class="btn btn-primary" href="#">Start for 50$</a> 
Python Machine Learning
<a class="btn btn-primary" href="#">Start for 100$</a>
"""

###
from bs4 import BeautifulSoup
with open("home.html", 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml') # if you contain here space near lxml(" ") you get errors (bs4.FeatureNotFound)
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text
        
        print(course_name)
        print(course_price)
"""
Python for beginners
Start for 20$
Python Web Development 
Start for 50$
Python Machine Learning
Start for 100$
"""

###
from bs4 import BeautifulSoup
with open("home.html", 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml') # if you contain here space near lxml(" ") you get errors (bs4.FeatureNotFound)
    course_cards = soup.find_all('div', class_='card') # u've to write underscore bcz its built in functions in python and beutifullsoup understand it
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        
        print(course_name)
        print(course_price)

"""
Python for beginners
20$
Python Web Development 
50$
Python Machine Learning
100$
"""

###
from bs4 import BeautifulSoup
with open('home.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content,'lxml')
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        course_name = course.h5
        course_price = course.a
        print(course_name)
        print(course_price)
"""
<h5 class="card-title">Python for beginners</h5>
<a class="btn btn-primary" href="#">Start for 20$</a> 
<h5 class="card-title">Python Web Development</h5>    
<a class="btn btn-primary" href="#">Start for 50$</a> 
<h5 class="card-title">Python Machine Learning</h5>   
<a class="btn btn-primary" href="#">Start for 100$</a>
"""

###
from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_name_tags =soup.find_all('h5')
    for course in course_name_tags:
        print(course.text)
"""
Python for beginners
Python Web Development 
Python Machine Learning
"""
    
###
from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_name_tags =soup.find_all('h5')
    print(course_name_tags.text())
'''xxxxx wrong no attributes'''

###
from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_name_tags =soup.find_all('h5')
    print(course_name_tags.text)

'''xxxxx wrong no attributes'''
"""
>>> AttributeError: ResultSet object has no attribute 'text'.
>>> You're probably treating a list of elements like a single element.
>>> Did you call find_all() when you meant to call find()?
"""

###
from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_name_tags =soup.find('h5')
    print(course_name_tags.text())
'''    print(course_name_tags.text())
TypeError: 'str' object is not callable'''


###
from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_name_tags =soup.find('h5')
    print(course_name_tags.text)
"""
>>> Python for beginners
"""
    
###
from bs4 import BeautifulSoup
with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div')


###
from bs4 import BeautifulSoup
with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')
'''
Python for beginners costs 20$
Python Web Development costs 50$  
Python Machine Learning costs 100$
'''

##############################################
################# Scrapping real worlds site
###
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
print(job)
"""
PS C:\VsCode> python -u "c:\VsCode\BeutifullSoup\tempCodeRunnerFile.py"
<li class="clearfix job-bx wht-shd-bx">
<header class="clearfix">
<!--
-->
<!-- -->
<h2>
<a href="https://www.timesjobs.com/job-detail/python-surya-informatics-solutions-pvt-ltd-chennai-0-to-3-yrs-jobid-UVlLes58wutzpSvf__PLUS__uAgZw==&amp;source=srp" onclick="logViewUSBT('view','65799390','python  ,  web technologies  ,  linux  ,  mobile  ,  mysql  ,  angularjs  ,  javascript','Chennai','0 - 3','IT Software : Software Products &amp; Services','1' )" target="_blank">
<strong class="blkclor">Python</strong></a> </h2>
<h3 class="joblist-comp-name">
    Surya Informatics Solutions Pvt. Ltd.

    </h3>
</header>
<ul class="top-jd-dtl clearfix">
<li><i class="material-icons">card_travel</i>0 - 3 yrs</li>
<li>
<i class="material-icons">location_on</i>
<span title="Chennai">Chennai</span>
</li>
</ul>
<ul class="list-job-dtl clearfix">
<li>
<label>Job Description:</label>
POSITION: Python Developer ELIGIBILITY: FRESHERS Your RoleUnderstand requirements and participate in project road map discussions in order to design ,  estimate ,  and deliver... <a href="https://www.timesjobs.com/job-detail/python-surya-informatics-solutions-pvt-ltd-chennai-0-to-3-yrs-jobid-UVlLes58wutzpSvf__PLUS__uAgZw==&amp;source=srp" target="_blank">More Details</a>
</li>
<li>
<label>KeySkills:</label>
<span class="srp-skills">
<strong class="blkclor">python</strong>  ,  web technologies  ,  linux  ,  mobile  ,  mysql  ,  angularjs  ,  javascript

      </span> </li>
<!--
            <li>
              <i class="material-icons">location_on</i>
              Chennai
              </li>
-->
</ul>
<div class="list-job-bt clearfix">
<div class="list-action">
<div class="applied-dtl clearfix" id="showPostApplyData_65799390">
<a class="waves-effect waves-light btn" href="javascript:callExtJobApply('65799390','adId=UVlLes58wutzpSvf__PLUS__uAgZw==&amp;compName=Career Progress Consultants','TJPFSRP');" onclick="trackClickEvent('View_AND_Apply_SRP','from_srp_externalJobs');logViewUSBT('apply','65799390','python  ,  web technologies  ,  linux  ,  mobile  ,  mysql  ,  angularjs  ,  javascript','Chennai','0 - 3','IT Software : Software Products 
&amp; Services','1')">Apply</a>
<span class="jobs-status clearfix">
<!--
       <i class="material-icons trnding-up" title="Recently posted job, Recruiter is actively looking for candidates">check_circle</i>      

-->
</span>
<span class="sim-posted">
<span>Posted 5 days ago</span>
</span>
</div>
</div>
</div>
</li>
"""

###
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = job.find('h3',class_ = 'joblist-comp-name')
print(company_name)
'''
<h3 class="joblist-comp-name">
    Surya Informatics Solutions Pvt. Ltd.
    
    </h3>
'''


###
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = job.find('h3',class_ = 'joblist-comp-name')
print(company_name.text)
'''
Surya Informatics Solutions Pvt. Ltd.

'''

###
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = job.find('h3',class_ = 'joblist-comp-name')
print(company_name.text.replace(' ',''))
# >>> SuryaInformaticsSolutionsPvt.Ltd.



###
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = jobs.find('h3', class_ = 'joblist-comp-name' ).text.replace(' ','')
skills = jobs.find('span', class_ = 'srp-skills').text.replace(' ','')
print(skills)
# >>> python,webtechnologies,linux,mobile,mysql,angularjs,javascript


###
from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = jobs.find('h3', class_ = 'joblist-comp-name' ).text.replace(' ','')
skills = jobs.find('span', class_ = 'srp-skills').text.replace(' ','')
print(jobs)
print(company_name)
print(skills)
"""

"""

###
from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = jobs.find('h3', class_ = 'joblist-comp-name' ).text.replace(' ','')
skills = jobs.find('span', class_ = 'srp-skills').text.replace(' ','')
print(f'''
company Name: {company_name}
Required skills: {skills}
''')

'''
>>> company Name: 
>>> SuryaInformaticsSolutionsPvt.Ltd.


>>> Required skills: 
>>> python,webtechnologies,linux,mobile,mysql,angularjs,javascript
'''

###
from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = jobs.find('h3', class_ = 'joblist-comp-name' ).text.replace(' ','')
skills = jobs.find('span', class_ = 'srp-skills').text.replace(' ','')
print(f'''
company Name: {company_name}
Required skills: {skills}''')

"""
company Name:
SuryaInformaticsSolutionsPvt.Ltd.


Required skills:
python,webtechnologies,linux,mobile,mysql,angularjs,javascript
"""



###
from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = jobs.find('h3', class_ = 'joblist-comp-name' ).text.replace(' ','')
skills = jobs.find('span', class_ = 'srp-skills').text.replace(' ','')
published_date = jobs.find('span', class_ = 'sim-posted').text
print(f'''
company Name: {company_name}
Required skills: {skills}
Published_date: {published_date}
''')

'''
company Name: 
SuryaInformaticsSolutionsPvt.Ltd.


Required skills: 
python,webtechnologies,linux,mobile,mysql,angularjs,javascript


Published_date: 
Posted 5 days ago

'''




###
from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_ = 'joblist-comp-name' ).text.replace(' ','')
skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
published_date = job.find('span', class_ = 'sim-posted').span.text # bcz we want text of tag(span)
print(f'''
company Name: {company_name}
Required skills: {skills}
Published_date: {published_date}
''')


"""
company Name: 
SuryaInformaticsSolutionsPvt.Ltd.


Required skills: 
python,webtechnologies,linux,mobile,mysql,angularjs,javascript


Published_date: Posted 5 days ago
"""




###
from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:  
    company_name = job.find('h3', class_ = 'joblist-comp-name' ).text.replace(' ','')
    skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
    published_date = job.find('span', class_ = 'sim-posted').span.text # bcz we want text of tag(span)
    print(f''' 
        \t* Company Name: {company_name.strip()} 
        \t* Required skills: {skills.strip()}
        ''')
    
    print( )
    
"""
                * Company Name: SuryaInformaticsSolutionsPvt.Ltd. 
                * Required skills: python,webtechnologies,linux,mobile,mysql,angularjs,javascript
.
.
.
                * Company Name: creativethoughtsinformaticsindore
                * Required skills: python,django,restapi,html5,javascript
"""


            
###
from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs: 
    published_date = job.find('span', class_ = 'sim-posted').span.text # bcz we want text of tag(span)
    if "few" in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name' ).text.replace(' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
        print(f"Company Name: {company_name.strip()}") # .strip() lagane means we call this method .strip()
        print(f"Skills: {skills.strip()}")
        
        print( )  

"""
Company Name: PolarisConsulting&ServicesLtd
Skills: python,django,apache,devops
.
.
.
.
Company Name: PerfiosSoftware
Skills: python,java,scala
"""


#######################################################
#######################################################
#############  Important concept - (more_info = job.header.h2.a)
from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs: 
    published_date = job.find('span', class_ = 'sim-posted').span.text # bcz we want text of tag(span)
    if "few" in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name' ).text.replace(' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
        
        more_info = job.header.h2.a  ####### Notable   
        print(f"Company Name: {company_name.strip()}") # .strip() lagane means we call this method .strip()
        print(f"Skills: {skills.strip()}")
        print(f'More Info : {more_info}')
        print( ) 
        
"""
Company Name: PolarisConsulting&ServicesLtd
Skills: python,django,apache,devops
More Info : <a href="https://www.timesjobs.com/job-detail/python-devops-polaris-consulting-services-ltd-bengaluru-bangalore-0-to-3-yrs-jobid-ksmR1q1a555zpSvf__PLUS__uAgZw==&amp;source=srp" onclick="logViewUSBT('view','69167469','python  ,  django  ,  apache  ,  devops','Bengaluru / Bangalore','0 - 3','IT Software : Software Products &amp; Services','6' )" target="_blank">
<strong class="blkclor">Python</strong> Devops</a>
.
.
.
.
Company Name: PerfiosSoftware
Skills: python,java,scala
More Info : <a href="https://www.timesjobs.com/job-detail/python-developer-perfios-software-bengaluru-bangalore-5-to-8-yrs-jobid-5GGtzEeKMXxzpSvf__PLUS__uAgZw==&amp;source=srp" onclick="logViewUSBT('view','69029965','python  ,  java  ,  scala','Bengaluru / Bangalore','5 - 8','IT 
Software : Software Products &amp; Services','19' )" target="_blank">
<strong class="blkclor">Python</strong> Developer</a>

"""
        
        
#########################################################
#######################################
from bs4 import BeautifulSoup
import requests
print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print('Filtering out{unfamiliar_skill}')
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs: 
    published_date = job.find('span', class_ = 'sim-posted').span.text # bcz we want text of tag(span)
    if "few" in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name' ).text.replace(' ','')
        skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
        more_info = job.header.h2.a  ####### Notable   
        if unfamiliar_skill not in skills:
            print(f"Company Name: {company_name.strip()}") # .strip() lagane means we call this method .strip()
            print(f"Required Skills: {skills.strip()}")
            print(f'More Info : {more_info}')
            
            
            print(' ') 


################################################
#################### 
from bs4 import BeautifulSoup
import requests
import time
print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print('Filtering out: {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs: 
        published_date = job.find('span', class_ = 'sim-posted').span.text # bcz we want text of tag(span)
        if "few" in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name' ).text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a  ####### Notable   
            if unfamiliar_skill not in skills:
                print(f"Company Name: {company_name.strip()}") # .strip() lagane means we call this method .strip()
                print(f"Required Skills: {skills.strip()}")
                print(f'More Info : {more_info}')
                
                print(' ') 
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting for {time_wait} seconds....')
        time.sleep(time_wait)


################################################
#################### Stored data in created files
from bs4 import BeautifulSoup
import requests
import time
print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print('Filtering out: {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs): 
        published_date = job.find('span', class_ = 'sim-posted').span.text # bcz we want text of tag(span)
        if "few" in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name' ).text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a  ####### Notable   
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}") # .strip() lagane means we call this method .strip()
                    f.write(f"Required Skills: {skills.strip()}")
                    f.write(f'More Info : {more_info}')
                
                print(f'file saved: {index}')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting for {time_wait} seconds....')
        time.sleep(time_wait)


################################################
#################### Stored data in created files
from bs4 import BeautifulSoup
import requests
import time
print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print('Filtering out: {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs): 
        published_date = job.find('span', class_ = 'sim-posted').span.text # bcz we want text of tag(span)
        if "few" in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name' ).text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a  ####### Notable   
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n") # .strip() lagane means we call this method .strip()
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f'More Info : {more_info}')
                
                print(f'file saved: {index}')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting for {time_wait} seconds....')
        time.sleep(time_wait)



###################################
####### white house example
# YouTube Link:

# Let's obtain the links from the following website:
# https://www.whitehouse.gov/briefings-statements/

# One of the things this website consists of is records of presidential
# briefings and statements.

# Goal: Extract all of the links on the page that point to the 
# briefings and statements.

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for h2_tag in soup.find_all('h2'):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])

print(urls)