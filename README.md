# IRS-CS-2019-04-27-IS1PT-GRP-ISSChatBot

$ git clone https://github.com/davidygp/IRS-CS-2019-04-27-IS1PT-GRP-ISSChatBot

$ cd ./IRS-CS-2019-04-27-IS1PT-GRP-ISSChatBot/SystemCode

$ conda activate ./venv/ISSChatBot-venv

# SECTION 1 : PROJECT TITLE                                                                      
### MRCard Recommender System
<img width="812" alt="welcome" src="https://user-images.githubusercontent.com/48171290/54080819-80836a80-4333-11e9-9f1d-7f21123d454f.png">

# SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
With the income of working adults in singapore steadily rising over the years, many people are gaining access to credit cards, especially young working adults. The majority of adults nowadays own at least one or more credit cards, with many others planning to start using credit cards as well. Banks have also been actively coming up with more credit cards and trying and to get consumers to take them up. 

There can be many advantages in having a credit card. One advantage is that credit card users can earn benefits in terms of rebates, air miles, and rewards. This is usually the main draw for people to use credit cards. However, not every card is suitable for everyone. Each card has its own requirements and rates, and whether the user can earn the benefits from the card largely depends on their lifestyle and spending habits. With many credit cards available from the banks in Singapore, it can be a time-consuming task to pick up a suitable credit card, and many people simply get cards where their potential benefits are not maximised. 

As a group of 5 young working professionals, we felt that this was a very relevant issue. Hence, we came up with the idea of designing a recommendation system to recommend the most suitable credit card or saving account based on the applicant's personal background, spending habits and personal preferences.

For this project, we first set out to perform knowledge acquisition by interviewing a subject matter expert, and also conducting a survey. To build the system, we decided to utilise the Django web framework, for its ease of integration with the front-end user interface (done with HTML), and the back-end rules engine (PyKnow) that we used to perform rule-based reasoning.

Our team learned a lot in the process of working on this project. We got the chance to apply techniques (like knowledge acquisition and rule-based reasoning) that we learned in our lectures and workshops in a viable business application scenario, and also picked up technical skills which would surely prove useful in the future course of our work.

# SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name | Student ID (MTech Applicable)| Work Items (Who Did What) | Email (Optional) |
| :---: | :---: | :---: | :---: |
| LI DUO  | A0195364W | Business idea generation, domain expert interview, reward rules implementation, project video and project report | e0384995@u.nus.edu |
| LIM CHONG SENG HERMANN | A0195392U | Business idea generation, project report and testing execution | e0385023@u.nus.edu |
| LU JIAHAO | A0091835Y | Business idea generation, UI design, domain expert interview, data clean, project report integration and testing execution | e0384293@u.nus.edu |
| YAM GUI PENG DAVID | A0195315A | Business idea generation, overall rules implementation, database and backend logic, overall integration and project report | e0384946@u.nus.edu |
| ZHAO YAZHI | A0195305E | Business idea generation, cashback rules implementation, survey result analysis, fuzzy logic implementation and project report | e0384936@u.nus.edu |

# SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO
# SECTION 1 : PROJECT TITLE                                                                      
### MRCard Recommender System
<img width="812" alt="welcome" src="https://user-images.githubusercontent.com/48171290/54080819-80836a80-4333-11e9-9f1d-7f21123d454f.png">

# SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
With the income of working adults in singapore steadily rising over the years, many people are gaining access to credit cards, especially young working adults. The majority of adults nowadays own at least one or more credit cards, with many others planning to start using credit cards as well. Banks have also been actively coming up with more credit cards and trying and to get consumers to take them up. 

There can be many advantages in having a credit card. One advantage is that credit card users can earn benefits in terms of rebates, air miles, and rewards. This is usually the main draw for people to use credit cards. However, not every card is suitable for everyone. Each card has its own requirements and rates, and whether the user can earn the benefits from the card largely depends on their lifestyle and spending habits. With many credit cards available from the banks in Singapore, it can be a time-consuming task to pick up a suitable credit card, and many people simply get cards where their potential benefits are not maximised. 

As a group of 5 young working professionals, we felt that this was a very relevant issue. Hence, we came up with the idea of designing a recommendation system to recommend the most suitable credit card or saving account based on the applicant's personal background, spending habits and personal preferences.

For this project, we first set out to perform knowledge acquisition by interviewing a subject matter expert, and also conducting a survey. To build the system, we decided to utilise the Django web framework, for its ease of integration with the front-end user interface (done with HTML), and the back-end rules engine (PyKnow) that we used to perform rule-based reasoning.

Our team learned a lot in the process of working on this project. We got the chance to apply techniques (like knowledge acquisition and rule-based reasoning) that we learned in our lectures and workshops in a viable business application scenario, and also picked up technical skills which would surely prove useful in the future course of our work.

# SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name | Student ID (MTech Applicable)| Work Items (Who Did What) | Email (Optional) |
| :---: | :---: | :---: | :---: |
| LI DUO  | A0195364W | Business idea generation, domain expert interview, reward rules implementation, project video and project report | e0384995@u.nus.edu |
| LIM CHONG SENG HERMANN | A0195392U | Business idea generation, project report and testing execution | e0385023@u.nus.edu |
| LU JIAHAO | A0091835Y | Business idea generation, UI design, domain expert interview, data clean, project report integration and testing execution | e0384293@u.nus.edu |
| YAM GUI PENG DAVID | A0195315A | Business idea generation, overall rules implementation, database and backend logic, overall integration and project report | e0384946@u.nus.edu |
| ZHAO YAZHI | A0195305E | Business idea generation, cashback rules implementation, survey result analysis, fuzzy logic implementation and project report | e0384936@u.nus.edu |

# SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO
[![Watch the video](https://user-images.githubusercontent.com/48171290/54084381-cad40e00-436a-11e9-8c73-83abc096a3f2.PNG)](https://www.youtube.com/watch?v=vu1eQ-0R4e8&feature=youtu.be)


# SECTION 5 : USER GUIDE
[ 1 ] To run the system in any machine with anaconda 3 installed

$ git clone https://github.com/davidygp/IRS-MR-2019-01-19-IS1PT-GRP-MRCard

$ cd ./IRS-MR-2019-01-19-IS1PT-GRP-MRCard/SystemCode

$ source activate ./venv/MRCard-env

(MRCard-env) $ python manage.py runserver

Go to URL using web browser http://127.0.0.1:8000/

$ (MRCard-env) $ source deactivate

[ 2 ] To run the system in other/local machine: Install additional necessary libraries. This application works in python 3 only.

$ pip install anaconda 3 

$ git clone https://github.com/davidygp/IRS-MR-2019-01-19-IS1PT-GRP-MRCard

$ cd ./IRS-MR-2019-01-19-IS1PT-GRP-MRCard/SystemCode

$ source activate ./venv/MRCard-env

(MRCard-env) $ python manage.py runserver

Go to URL using web browser http://127.0.0.1:8000/

$ (MRCard-env) $ source deactivate

# SECTION 6 : PROJECT REPORT / PAPER
<Github File Link>  https://github.com/davidygp/IRS-MR-2019-01-19-IS1PT-GRP-MRCard/tree/master/ProjectReport/Report.pdf

Recommended Sections for Project Report / Paper:
+ Executive Summary / Paper Abstract
+ Business Problem Background
+ Project Objectives & Success Measurements
+ Project Solution
+ Project Performance & Validation
+ Project Conclusions: Findings & Recommendation
+ References

# SECTION 7 : MISCELLANEOUS
MRCard Survey Result.xlsx
+ Results of survey
+ Insights derived, which helped on features selection that are subsequently used in our system

Interview with Hu Juan.mps
+ Audio of the interview process with domain expert

Card Data - Bank Card Data (Cleaned_v2).csv
+ Data that used in the backend 

Data Fields - Sheet1.csv
+ Variables that used in the backend and rules
