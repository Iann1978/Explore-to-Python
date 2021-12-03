#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class EMailSender:
    def __init__(self):
        self.mail_host = "smtp.fzcx.xyz"  # 设置服务器
        self.mail_user = "me1@fzcx.xyz"  # 用户名
        self.mail_pass = "12345678"  # 口令
        self.sender = 'me1@fzcx.xyz'
        self.receivers = ['me@fzcx.xyz']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    def login(self):
        try:
            self.smtpObj = smtplib.SMTP()
            self.smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            self.smtpObj.login(self.mail_user, self.mail_pass)
            # self.smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            print
            "邮件发送成功"
        except smtplib.SMTPException:
            print( "Error: 无法发送邮件")


    def send(self, maillist):
        message = MIMEText('Python 邮件发送测试... 来自Iann的自动化邮件发送程序', 'plain', 'utf-8')
        message['From'] = Header("菜鸟教程", 'utf-8')
        message['To'] = Header("测试", 'utf-8')

        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            self.smtpObj.sendmail(self.sender, self.receivers, message.as_string())

        except smtplib.SMTPException:
            print
            "Error: 无法发送邮件"





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
