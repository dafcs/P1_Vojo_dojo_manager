# P1_gym_manager

This README.md relates to the Project 1 titled 'gym_manager'.

# ### SETUP ### #

Note: Every command needs Enter to be pressed in order to run.

**Installation necessary software(MAC)**

psycopg2 - https://pypi.org/project/psycopg2/

python - https://docs.python-guide.org/starting/install3/osx/

flask - https://phoenixnap.com/kb/install-flask


**Open the terminal**
1. Open the Spotlight Search (cmd + space bar)
2. Type "Terminal"
3. Press enter

**Creating a folder**
The terminal should start in ~ which is the home path.

4. Create a folder by pasting:
mkdir project_daniel_dimoes

You can change the name as you see fit (e.g. mkdir foldername)

**Navigate to the folder**
Now you will need to step in to that folder
5. Navigate to the folder by pasting:
cd project_daniel_dimoes
The ~ should now be showing 'project_daniel_dimoes'

**Setting up the GIT repository**
Once in the folder, create a GIT repository.
6. Initiate the Git repository by pasting:
git init

The 'project_daniel_dimoes' should now have git:(main) in front of it.

**Accessing the files**
Still in the same folder
7. Pull (or access) the files by pasting:
git clone git@github.com:dafcs/P1_gym_manager.git

**Creating the database**
8. Create the database by pasting:
    createdb gym_manager
This can be done from any point

**Generate the necessary tables**

9. Once the database has been created, generate the respective tables by pasting:
psql -d gym_manager -f db/gym_manager.sql

note: this needs to be ran from the parent folder of db (or the folder in which db is in), if this is not 'project_daniel_simoes' then follow below steps:

While in the folder project_daniel_simoes start by pasting:
ls

this should provide a list of all the items inside the folder project_daniel_simoes

if there is a folder inside that one you will need to navigate to that folder, you can do this by writing cd foldername.
e.g. if the folder is called 'P1_gym_manager' you would write cd P1_gym_manager

**Running flask**
In order to run flask paste in to terminal:
flask run

# Troubleshooting 

Useful navigation commands:

**Finding the currect path**
pwd 
(this will print working directory)

**Returning to ~ (home directory)**
cd ~
cd
(this will change directory to home)

**listing all items in a folder**
ls

**navigating to the correct folder**
cd foldername
(this will change directory to the one specified)

database/table visualisation:
postico
# ### FOLDERS & FILES ### #

*README.md*

*.flaskenv*
contains the base settings for running flask

*app.py*
contains the base settings for returning a web page

*console.py*
manual database manipulation

*run_tests.py*
file used to run unittest

*utest*
testing grounds for python classes

*models*
contains the python classes
gym_class.py
gym_member.py
gym_room.py

*db*
database related files, used to manipulate tables and run sql, contains:
gym_manager.sql
run_sql.py

*controllers*
responsible for receiving http requests and responding with html templates, contains:
controller.py

*repositories*
files that contain sql functions related to respective tables, contains:
gym_class_controller.py
gym_member_controller.py
gym_room_controller.py

*templates*
used to store html(jinja) templates which will structure the view, contains:


*static*
used for holding css files, which will influence the view look, contains:
style.css

# ### References ### #

MarkDown guide - for the README file
https://www.markdownguide.org/basic-syntax/

psycopg2 installation - for the README file
https://pypi.org/project/psycopg2/

python installation - for the README file
https://docs.python-guide.org/starting/install3/osx/

flask - for the README file
https://phoenixnap.com/kb/install-flask

Week_2_day_3 - unittest set up
https://github.com/codeclan/e64_classnotes/blob/main/week_02/day_3/testing/coffee_shop_testing/testing.md

week_4_day_5 - file/table set up
https://github.com/codeclan/e64_classnotes/tree/main/week_04/day_4/01_many_to_many_quest_advisor/quest_advisor_end

create table data types
https://www.w3schools.com/sql/sql_dates.asp#:~:text=SQL%20Server%20comes%20with%20the,%2DDD%20HH%3AMI%3ASS

https://www.w3schools.com/sql/sql_dates.asp#:~:text=SQL%20Server%20comes%20with%20the,%2DDD%20HH%3AMI%3ASS

