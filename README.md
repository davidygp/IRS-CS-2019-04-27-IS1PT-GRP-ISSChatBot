# IRS-CS-2019-04-27-IS1PT-GRP-ISSChatBot

# SECTION 1 : PROJECT TITLE                                                                      
### ISSChatBot NUS Stanley



# SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
ISS website is informative but unstructured, like all website experiences. Additionally we see that there is no sitemap to assist user navigation.

Our Chatbot is created to provide a human language conversational interface for contextual, and targeted access. 

We started the chatbot design keeping user centricity in mind. Identifying the use categories and their information knowledge expectations from a bot was key.

While the chatbot is designed for english only, we have considered different phrases, utterances and incomplete phrases to train the intents.

For easy information access we have considered slack and Google Assistant.

We have tried to create a dynamic system and hence automated scraping and associated database refresh is ensured.

Intents are central to the user interaction. We designed user journeys based on user interaction, and preserved the user conversation context between dialogue /conversation turns. Similar matching intents were “resolved” through prioritization. Additionally to “course correct” the user, fallback intents were designed with sufficient aids and trials to bring the user back to successful resolution of the queries.

In our opinion, today’s chat bot addresses user category: prospective student well. For the chatbot to truly serve the needs of current students, faculty, and collaborations e.g. research, recruiters, etc. we will need the bot to “crawl” and ingest relevant datasets. Per guidance from course instructors, we restricted ourselves to publicly available information. 

The roadmap of our chatbot has to consider following aspects: serving all user categories for ISS, omni-channel (facebook integration, Building BOT into ISS website), authentication (to prevent Denial of Service/DoS), and authentication based personalized interaction.


# SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name | Student ID (MTech Applicable)| Work Items (Who Did What) |
| :---: | :---: | :---: |
| David Yam  | A0195315A | Business idea generation, web scraping, heroku integration, backend logic and project report |
| Li Duo | A0195364W | Business idea generation, web scraping, project video and project report |
| Ajay Vikram Singh | A0020986B | Business idea generation and project report |
| Rahul Jalan | A0195299H | Business idea generation, frontend intent classification & training and project report |

# SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO
[![Watch the video](https://user-images.githubusercontent.com/31118924/58703342-f0593c80-83da-11e9-9501-a6253367b3cc.png)](https://www.youtube.com/watch?v=vBZqKLAhY3U&feature=youtu.be)


# SECTION 5 : USER GUIDE
[ 1 ] To converse with NUS Stanley via Slack

Subscribe to workspace "mtech2019pt"

Search for "stanleyisschatbot2" under Direct Messages.

Start chatting with NUS Stanley ChatBot.

[ 2 ] To converse with NUS Stanley via Google Assistant

Speak to any of the project groupmates, permission must be given to your google account.

Use the invocation statement "Talk to NUS Stanley" to invoke the application.

Start chatting with NUS Stanley ChatBot.

[ 3 ] To download the code and run it locally. (not suggested)

$ git clone https://github.com/davidygp/IRS-CS-2019-04-27-IS1PT-GRP-ISSChatBot

$ cd ./IRS-CS-2019-04-27-IS1PT-GRP-ISSChatBot

$ pip install Flask requests numpy pandas

(Download and use a tunneler such as ngrok. https://ngrok.com/download)
(Unzip the ChatBot and import it into your DialogFlow account.)
(Setup the tunnel by the command $ngrok http 5000.)
(Copy paste the http url into the fulfillment tab of the ChatBot in DialogFlow.)

$ python app.py

(Start chatting with NUS Stanley ChatBot)

# SECTION 6 : PROJECT REPORT / PAPER
<Github File Link>  https://github.com/davidygp/IRS-CS-2019-04-27-IS1PT-GRP-ISSChatBot/blob/master/ProjectReport/report.pdf

Recommended Sections for Project Report / Paper:
+ Executive Summary
+ Introduction
+ Objective
+ Scoping
+ Functionality
+ Solution
+ Critical Analysis
+ References

# SECTION 7 : MISCELLANEOUS
Questions.xlsx
+ Original questions (not all were developed)

How to make changes to Heroku.docx
+ Contains instructions on how to push code up to Heroku

ISS-CS-DaLiRaAj.zip
+ Export of DialogFlow ChatBot
