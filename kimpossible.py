################################
################################
import urllib.request
import smtplib
import time

################################
################################

# CONFIG
KIMSUFI_ID = "1804sk12"
KIMSUFI_DESC      = "KS-1"
KIMSUFI_EMAIL_FROM  = "*@tld.net"
KIMSUFI_EMAIL_TO     = "*@*"
KIMSUFI_EMAIL_USER  = "*"
KIMSUFI_EMAIL_PASS = "*"
KIMSUFI_SMTP_SERVER = "mail.riseup.net:587"

# CODE
def kimPOSSIBLE():
    rawPageContent = urllib.request.urlopen("https://www.kimsufi.com/us/en/servers.xml").read()
    rawPageContent = str(rawPageContent)
    id = rawPageContent.find(KIMSUFI_ID)
    row = rawPageContent[id:]
    id = row.find("</tr>")
    row = row[:id]
    searchText = "Currently being replenished"
    id = row.find(searchText)
    return id != -1

def fknSENDIT():
    msg = "From: KIMPOSSIBLE <"+KIMSUFI_EMAIL_FROM+">\r\n"+\
        "To: "+KIMSUFI_EMAIL_TO+"\r\n"+\
        "Subject: [KIMSUFI] "+KIMSUFI_DESC+" is available\r\n"+\
        "\r\n"+\
        "[kimPOSSIBLE]"+KIMSUFI_DESC+" is now ["+time.ctime()+"] available!\r\n"+\
        "https://www.kimsufi.com/en/\r\n"
    server = smtplib.SMTP(KIMSUFI_SMTP_SERVER)
    server.starttls()
    server.login(KIMSUFI_EMAIL_USER,KIMSUFI_EMAIL_PASS)
    server.sendmail(KIMSUFI_EMAIL_FROM, KIMSUFI_EMAIL_TO, msg)
    server.quit()

while True:
    if kimPOSSIBLE():
        print(time.ctime() + " [kimPOSSIBLE] -- "+KIMSUFI_DESC+" not available")
        zzz = 5 #5secs
    else:
        print(time.ctime() + " [kimPOSSIBLE] -- "+KIMSUFI_DESC+" GET IT FGT full fkn SEND")
        fknSENDIT()
        zzz = 5*60
    time.sleep(zzz)
