import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com',587)

# start TLS for security
s.starttls()

# Authentication
s.login("sazcmrece56@gmail.com","ubuntu123$cmru")

# message to be sent 
message ="Message_you_need_to_send"

# sending the mail
s.sendmail("sazcmrece56@gmail.com","saraht060786@gmail.com",message)
print("message has been sent")

# terminating the session
s.quit()