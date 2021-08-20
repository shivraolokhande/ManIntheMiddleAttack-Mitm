import smtplib
def send():
    Sender_Email = ""
    Reciever_Email = ""
    #Password = input('Enter your email account password: ')
    Subject = "Your System has been ARP SPOOFED"
    Body = "Hi Suchith,\nSomething happening in your system please check it "
    Message = f'Subject: {Subject}\n\n{Body}'
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(Sender_Email, '<Enter password>')
        smtp.sendmail(Sender_Email, Reciever_Email, Message)
