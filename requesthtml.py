import requests
import json

def jsonParse(str):
    print("Parsing the json...")
    result = json.loads(str)
    try:
        var = result['data']['version']
        print('The server is working well')        
        print('The current app server version is',var)        
    except ValueError:
        print('We can not parse the string.')
    
def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")


try:
    response = requests.get('https://mobileapps-as.hutchisonports.com/resources_hpt/server/status', timeout=10)
    jsonParse(response.text)
except requests.exceptions.RequestException as e:
    print('The server doesn''t answer...')
    print('Sending Email to administrator...')
    send_email('evanchansky@gmail.com','emanrules','edc220@lehigh.edu','server error','The mobile server might be down, please check')
    print(e)



