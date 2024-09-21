import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'sahithyabadri@gmail.com'
email_passwd = 'hnmj hvri dfjj icbv'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='gmaheswaranmca@gmail.com', msg="Sent from my IDE. Hehe")
connection.close()
print('Mail sent successfully')