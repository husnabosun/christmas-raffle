# christmas-raffle
Christmas Raffle is a Django app that allows you to organize a gift exchange raffle with your family or friends for the new year.
You upload an excel file includes the names and emails of participants, and they receive an email informing them whom they should buy a gift for!
It has a very user friendly interface and of course  you can customize it if you wish.


![Homepage]( https://i.imgur.com/vYoiqiE.png=300x200)


![Homepage]( https://i.imgur.com/8ldAHb0.png)
### REQUIREMENTS
 - python 3.6 or higher 
- redis
### RUNNING THE CODE
**1-** first, clone the github repository:
```bash 
git clone https://github.com/husnabosun/christmas-raffle.git
cd christmas-raffle
```
**2-** Create a virtual environment. Depending on the IDE you are using, you might not need to set this up manually.
```bash 
python -m venv .venv source .venv/bin/activate
````
**3-** create you own .env file
You need to create a .env file which includes some private settings
```bash 
copy .env.example .env
```
In the .env file, add your secret key, email host, and email password in the following format. I strongly  recommended to use an app specific password by enabling your email account has two-factor authentication . The email accounts own password might cause issues sometimes.
```bash 
SECRET_KEY=secretkey # You can generate this using a random secret key generator
EMAIL_HOST_USER=email_address 
EMAIL_HOST_PASSWORD=email_app_password
```

**5-** install the required libraries
```python
pip install -r requirements.txt
```
**6-** run the migrations
```python
python manage.py migrate
```
**7-** create a superuser by following the prompts to create the superuser and access the django admin panel. You can follow the tasks via on admin panel (You can access the admin panel via this link:http://127.0.0.1:8000/admin.)
```python 
python manage.py createsuperuser
```
**8-** open Ubuntu panel and start redis
```bash 
sudo systemctl start redis-server
```
To check the server is running properly you can run this command
```bash 
sudo systemctl status redis-server
```
if you see an output which indicates active/running it means that the server has been started successully
**9-** run celery worker
Return to the project directory and start the celery worker in the terminal by this command
```python
celery -A christmas_raffle worker -l info --pool=solo
```
**10-** finally you can access the application through the link which appears on the terminal after running this code.
```python
python manage.py runserver
```
## UPLOADING FILES
Your excel file format should be in the format below

![excel]( https://i.imgur.com/n3lig67.png)

## AND THAT’S IT. HAVE FUN !
