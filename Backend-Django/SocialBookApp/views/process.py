'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet, ViewSet
from SocialBookApp.models.bookmodels import (Book)
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from SocialBookApp.models.usermodels import (App_User)
from SocialBookApp.serializers.serializers import (BookSerializer,App_UserSerializer)
from rest_framework.response import Response
import logging
from django.contrib.auth.models import User
from rest_framework.authtoken.models import (Token)
import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from rest_framework.permissions import AllowAny
<<<<<<< HEAD
<<<<<<< HEAD
import random
import string
=======
from django.core.files.base import ContentFile
import base64
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
=======

>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
import json

logger = logging.getLogger("book.request")

class LoginCheckSet(ModelViewSet):

    queryset = App_User.objects.all()
    serializer_class = App_UserSerializer
    permission_classes = [AllowAny]

    def login(self, request):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                item = App_User.objects.get(username=username)
                logger.info(item.password)

                if (item.active == False):
                    return Response("Account is not activated please check your mail", status=404)

                if (item.password == password):
                    response ={}
                    list = User.objects.get(username=username)
                    auth = Token.objects.get(user=list.id)
                    response['message'] ="User Verification Successful"
                    response['username'] = item.username
                    response['email'] = item.email
                    response['usertype'] = item.usertype
<<<<<<< HEAD
                    response['dp'] = item.dp
=======
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
                    response['app_userid']= item.id
                    tokenJson={}
                    tokenJson["token"] = auth.key
                    response['auth_token'] = tokenJson
                    return Response(response, status=200)

                else:
                    return Response("Username or Password MisMatch", status=404)


            except App_User.DoesNotExist:
                return Response("Username does not Exist. Please Register", status=404)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)


<<<<<<< HEAD
    def change_pass(self, request):
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            try:
                item = App_User.objects.get(username=username.lower())
                if (item.active == False):
                    return Response("Account is not activated please check your mail", status=404)
                if (item.email == email):
                    return Response("verified", status=200)
                else:
                    return Response("not available", status=404)
            except App_User.DoesNotExist:
                return Response("Username does not Exist. Please Register", status=404)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)

    def generate_pass(self, request):
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            
            item = App_User.objects.get(username=username.lower())
            letters = string.ascii_letters
            passwd = ''.join(random.choice(letters) for i in range(10))
            item.password = passwd
            item.save()
            smtpsenderforpass(passwd, item.email)
            return Response("Check Mail For Pass", status=200)
                                 
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)


def smtpsenderforpass(data,email):
    smtphost = 'smtp.gmail.com'
    smtpport = 587
    smtpuser = 'indbookstagram@gmail.com'
    smtppasswd = 'bookserver12345@'
    smtpfromaddr = 'noreply@bookstagram.com'
    smtptoaddr = email
    smtptype = 'html'
    smtpsubject = "Temporary Password Mail From Bookstagram"
    mail_content = data
    try:
        if smtptype == "text":
            logger.info("Sending Text Email")
        else:
            logger.info("Sending HTML Email")
            emailtemp = """\
                     <html>
                     <head>
                     <style>
                     table, th, td {
                     border: 2.5px solid #7b887c;
                     border-collapse: collapse;
                     color: black;
                     }
                     td
                     {
                     background-color: #eee;
                     }
                     td:hover {background-color:#949494;}
                     </style>
                     <meta name="viewport" content="width=device-width, initial-scale=1">
                     <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
                     </head>
                     <body> 
                        <br><br>
                           Hello Bookstagramer,<br>
                                <p>          Use the temporary password to login. Please do <b>Update password after loging in</b></p>  
                                      <br>  <br>      

                                          <h3><b>Tempprary Password:</b></h3>         
                                          <table>
                                            <tr>  
                                                <td>
                                                    <i><b>password</b></i>
                                                        </td>
                                                            <td>
                                                                <i>""" + mail_content + """</i>
                                                                    </td>
                                                                      </tr>
                                                                         </table> 
                                                                         <br>  <br> <br>  <br> 

                                                                           <i>Thanks and Regards,<br>
                                                                             Mail Bot,<br>
                                                                               Bookstagram.</i>
                                                                               </body>
                                                                               </html>
                                                                                                       """
            SMTPCON(smtphost, smtpport, smtpuser, smtppasswd, smtpfromaddr, smtptoaddr, smtptype, smtpsubject,
                                        emailtemp).SendHtmlEmail()


    except Exception as e:
        logger.info(e)
=======
@api_view(['POST'])
@permission_classes((AllowAny, ))
def create_Dp(request):
    try:
        image_data = "image/png:base64,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"
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(image_data), name='temp.' + ext)
        return Response(data, status=200)


        # return Response(serializer.errors, status=200)
    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)
>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1


def smtpsender(data,id):


    smtphost = 'smtp.gmail.com'
    smtpport = 587
    smtpuser = 'indbookstagram@gmail.com'
    smtppasswd = 'bookserver12345@'
    smtpfromaddr = 'noreply@bookstagram.com'
    smtptoaddr = data["email"]
    smtptype = 'html'
    smtpsubject = "Verification Mail From Bookstagram"

    first = data["first_name"]
    last = data["last_name"]
    username = data["username"]
    country = data["country"]
    contact = data["contact"]
    
    mail_content = "http://40.80.95.65/store/activate_user/?pk="+ str(id) + ""
    url = '<a href="'+mail_content+'">Activate</a>'
    try:
        if smtptype == "text":
            logger.info("Sending Text Email")
<<<<<<< HEAD
            
=======

>>>>>>> 456a87408c67465ab5351b43cc5e09ea0589d8d1
        else:
            logger.info("Sending HTML Email")
            emailtemp = """\
                        <html>
<head>
<style>
table, th, td {
border: 2.5px solid #7b887c;
border-collapse: collapse;
color: black;
}
td
{
background-color: #eee;
}
td:hover {background-color:#949494;}
</style>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body> 
   <br><br>
   Hello Bookstagramer,<br>
     <p>          Please check the following Details and click the link below to activate your Bookstagram Account</p>  
     <h2><b>Bookstagramer Information:</b></h2>         
<table>
  <tr>  
    <td>
    <i><b>User Name</b></i>
    </td>
    <td>
    <i>"""+username+"""</i>
    </td>
  </tr>
  </table>
  <br><br>
    <h3><b>Activate Bookstagram:</b></h3>         
<table>
  <tr>  
    <td>
    <i><b>Activation Link</b></i>
    </td>
    <td>
    <i>"""+url+"""</i>
    </td>
  </tr>
   </table> 
<br>  <br> <br>  <br> 
 
  <i>Thanks and Regards,<br>
  Mail Bot,<br>
  Bookstagram.</i>
</body>
</html>
                        """
            SMTPCON(smtphost, smtpport, smtpuser, smtppasswd, smtpfromaddr, smtptoaddr, smtptype, smtpsubject,emailtemp).SendHtmlEmail()
    except Exception as e:
        logger.info(e)


class SMTPCON(object):

    def __init__(self, smtphost, smtpport, smtpuser, smtppasswd, smtpfromaddr, smtptoaddr, emailtype, subject, content):
        self.smtphost = smtphost
        self.smtpport = smtpport
        self.smtpuser = smtpuser
        self.smtppasswd = smtppasswd
        self.smtpfromaddr = smtpfromaddr
        self.smtptoaddr = smtptoaddr
        self.emailtype = emailtype
        self.subject = subject
        self.content = content
        print(self.smtphost)

    def SendTextEmail(self):

        print("entering here")
        # Contructing a Email Message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.smtpfromaddr
        msg['To'] = self.smtptoaddr


        # Attaching the Content of email

        body = MIMEText(self.content, 'plain')

        # Attaching the body of email

        msg.attach(body)
        logger.info("in py")

        # Connection to SMTP Server
        con = smtplib.SMTP(self.smtphost, self.smtpport)
        if self.smtpuser == '':
            con.sendmail(self.smtpfromaddr, [self.smtptoaddr, self.cc], msg.as_string())
        else:
            logger.info("hi")
            logger.info(con.login(self.smtpuser, self.smtppasswd))
            logger.info(con.sendmail(self.smtpfromaddr, [self.smtptoaddr, self.cc], msg.as_string()))
            logger.info("JI")
        return ("Already Sent")

    def SendHtmlEmail(self):
        # Contructing a Email Message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.smtpfromaddr
        msg['To'] = self.smtptoaddr


        # Attaching the Content of email

        body = MIMEText(self.content, 'html')

        # Attaching the body of email

        msg.attach(body)

        # Connection to SMTP Server
        logger.info("in py")
        con = smtplib.SMTP(self.smtphost, self.smtpport)

<<<<<<< HEAD
        con.info(con.starttls())
        if self.smtpuser == '':
            con.sendmail(self.smtpfromaddr, [self.smtptoaddr], msg.as_string())
        else:
            logger.info(con.login(self.smtpuser, self.smtppasswd))
            logger.info(con.sendmail(self.smtpfromaddr, [self.smtptoaddr], msg.as_string()))
=======


def smtpsender(data,id):


    smtphost = 'smtp.gmail.com'
    smtpport = 587
    smtpuser = 'indbookstagram@gmail.com'
    smtppasswd = 'bookserver12345@'
    smtpfromaddr = 'noreply@bookstagram.com'
    smtptoaddr = data["email"]
    smtptype = 'html'
    smtpsubject = "Verification Mail From Bookstagram"

    first = data["first_name"]
    last = data["last_name"]
    username = data["username"]
    country = data["country"]
    contact = data["contact"]
    
    mail_content = "http://40.80.95.65/store/activate_user/?pk="+ str(id) + ""
    url = '<a href="'+mail_content+'">Activate</a>'
    try:
        if smtptype == "text":
            logger.info("Sending Text Email")
            
        else:
            logger.info("Sending HTML Email")
            emailtemp = """\
                        <html>
<head>
<style>
table, th, td {
border: 2.5px solid #7b887c;
border-collapse: collapse;
color: black;
}
td
{
background-color: #eee;
}
td:hover {background-color:#949494;}
</style>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body> 
   <br><br>
   Hello Bookstagramer,<br>
     <p>          Please check the following Details and click the link below to activate your Bookstagram Account</p>  
     <h2><b>Bookstagramer Information:</b></h2>         
<table>
  <tr>  
    <td>
    <i><b>First Name</b></i>
    </td>
    <td>
    <i>"""+first+"""</i>
    </td>
  </tr>
  <tr>  
    <td>
    <i><b>Last Name</b></i>
    </td>
    <td>
    <i>"""+last+"""</i>
    </td>
  </tr>
  <tr>  
    <td>
    <i><b>User Name</b></i>
    </td>
    <td>
    <i>"""+username+"""</i>
    </td>
  </tr>
  <tr>  
    <td>
    <i><b>Country</b></i>
    </td>
    <td>
    <i>"""+country+"""</i>
    </td>
  </tr>
  <tr>  
    <td>
    <i><b>contact</b></i>
    </td>
    <td>
    <i>"""+contact+"""</i>
    </td>
  </tr>
 
  </table>
  <br><br>
    <h3><b>Activate Bookstagram:</b></h3>         
<table>
  <tr>  
    <td>
    <i><b>Activation Link</b></i>
    </td>
    <td>
    <i>"""+url+"""</i>
    </td>
  </tr>
   </table> 
<br>  <br> <br>  <br> 
 
  <i>Thanks and Regards,<br>
  Mail Bot,<br>
  Bookstagram.</i>
</body>
</html>
                        """
            SMTPCON(smtphost, smtpport, smtpuser, smtppasswd, smtpfromaddr, smtptoaddr, smtptype, smtpsubject,emailtemp).SendHtmlEmail()
    except Exception as e:
        logger.info(e)


class SMTPCON(object):

    def __init__(self, smtphost, smtpport, smtpuser, smtppasswd, smtpfromaddr, smtptoaddr, emailtype, subject, content):
        self.smtphost = smtphost
        self.smtpport = smtpport
        self.smtpuser = smtpuser
        self.smtppasswd = smtppasswd
        self.smtpfromaddr = smtpfromaddr
        self.smtptoaddr = smtptoaddr
        self.emailtype = emailtype
        self.subject = subject
        self.content = content
        print(self.smtphost)

    def SendTextEmail(self):

        print("entering here")
        # Contructing a Email Message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.smtpfromaddr
        msg['To'] = self.smtptoaddr


        # Attaching the Content of email

        body = MIMEText(self.content, 'plain')

        # Attaching the body of email

        msg.attach(body)
        logger.info("in py")

        # Connection to SMTP Server
        con = smtplib.SMTP(self.smtphost, self.smtpport)
        if self.smtpuser == '':
            con.sendmail(self.smtpfromaddr, [self.smtptoaddr, self.cc], msg.as_string())
        else:
            con.login(self.smtpuser, self.smtppasswd)
            con.sendmail(self.smtpfromaddr, [self.smtptoaddr, self.cc], msg.as_string())
        return ("Already Sent")

    def SendHtmlEmail(self):
        # Contructing a Email Message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.smtpfromaddr
        msg['To'] = self.smtptoaddr


        # Attaching the Content of email

        body = MIMEText(self.content, 'html')

        # Attaching the body of email

        msg.attach(body)

        # Connection to SMTP Server
        logger.info("in py")
        con = smtplib.SMTP(self.smtphost, self.smtpport)
        logger.info(con.starttls())
        if self.smtpuser == '':
            con.sendmail(self.smtpfromaddr, [self.smtptoaddr], msg.as_string())
        else:
            con.login(self.smtpuser, self.smtppasswd)
            con.sendmail(self.smtpfromaddr, [self.smtptoaddr], msg.as_string())
>>>>>>> 3a6ac2f4a60c403b47d2a717b96898550240b765
        con.close()
