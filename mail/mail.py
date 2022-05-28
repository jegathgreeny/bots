import ezgmail
import sys, os

# This is the format to send mail.
# mail mail_id subject body attachment
# enclose them in to quotes to send sentences. 


os.chdir(r"C:\Users\jegat\Desktop\py_work\work\bots\mail\jg")

# get the data from sys.argv
to = sys.argv[1]
subject = sys.argv[2]
body = sys.argv[3]

try:
    attachments = [sys.argv[4]]

    # sends the mail
    ezgmail.send(to, subject, body, attachments[0])
    print("mail sent with attachments...")

except:
    print("sending with no attachments")
    ezgmail.send(to, subject, body)

