#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.header import Header
import email

# 解析邮件内容
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, decode=True)
class EMailSender:
    def __init__(self):
        print("EMailSender.__init__")
        self.mail_host = "smtp.fzcx.xyz"  # 设置服务器
        self.mail_user = "me1@fzcx.xyz"  # 用户名
        self.mail_pass = "12345678"  # 口令
        # self.sender = 'me1@fzcx.xyz'
        self.receivers = ['me@fzcx.xyz']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    def login(self):
        try:
            self.smtpObj = smtplib.SMTP()
            self.smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            self.smtpObj.login(self.mail_user, self.mail_pass)
            # self.smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            print
            "登录成功"
        except smtplib.SMTPException:
            print( "Error: 无法发送邮件")


    def send(self, maillist):

        for e in maillist:
            subject = email.header.make_header(email.header.decode_header(e['SUBJECT']))
            mail_from = email.header.make_header(email.header.decode_header(e['From']))
            print("邮件的subject是:%s" % subject)
            print("邮件的发件人是:%s" % mail_from)
            body = str(get_body(e), encoding='gb2312')  # utf-8 gb2312 GB18030解析中文日文英文
            print("邮件内容是:%s" % body)

            # try:
            #     message = MIMEText(body, 'plain', 'utf-8')
            #     message['From'] = self.mail_user
            #     message['To'] = self.receivers[0]
            #     message['Subject'] = subject
            #
            #     self.smtpObj.sendmail(self.mail_user, self.receivers, message.as_string())

            try:
                # message = e
                message = EmailMessage()
                message['From'] = self.mail_user
                message['To'] = self.receivers[0]
                message['Subject'] = 'aaa'
                # message.set_payload(e.get_payload(0))
                # bo = e.get_content()
                message.set_content(body)
                # message.set_content(get_body(e))

                self.smtpObj.send_message(message, self.mail_user, self.receivers[0])

            except smtplib.SMTPException:
                print ("Error: 无法发送邮件")
        # message = MIMEText('Python 邮件发送测试... 来自Iann的自动化邮件发送程序', 'plain', 'utf-8')
        # message['From'] = Header("菜鸟教程", 'utf-8')
        # message['To'] = Header("测试", 'utf-8')
        #
        # subject = 'Python SMTP 邮件测试'
        # message['Subject'] = Header(subject, 'utf-8')
        # try:
        #     self.smtpObj.sendmail(self.sender, self.receivers, message.as_string())
        #
        # except smtplib.SMTPException:
        #     print
        #     "Error: 无法发送邮件"





# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
#     smtpObj.login(mail_user, mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print
#     "邮件发送成功"
# except smtplib.SMTPException:
#     print
#     "Error: 无法发送邮件"

if __name__ == '__main__':
    sender = EMailSender()
    sender.login()
    sender.send(None)
