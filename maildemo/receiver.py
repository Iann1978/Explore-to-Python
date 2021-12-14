#!/usr/bin/python
# -*- coding: UTF-8 -*-

import imaplib, email, os
from email.parser import BytesParser, Parser


# 解析邮件内容
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, decode=True)


# search('FROM','abc@outlook.com',conn)  根据输入的条件查找特定的邮件
def search(key, value, conn):
    result, data = conn.search(None, key, '"()"'.format(value))
    return data


# 获取附件
def get_attachements(msg):
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        filename = part.get_filename()

        if bool(filename):
            filepath = os.path.join(attachementdir, filename)
            with open(filepath, 'wb') as f:
                f.write(part.get_payload(decode=True))


class EMailReceiver:
    def __init__(self):
        self.imapserver = 'imap.fzcx.xyz'
        self.emailuser = "me1@fzcx.xyz"
        self.emailpasswd = "12345678"

    def login(self):
        self.conn = imaplib.IMAP4_SSL(self.imapserver)
        self.conn.login(self.emailuser, self.emailpasswd)

    def logout(self):
        self.conn.logout()

    def receive(self):
        l = self.conn.list()  # 列出邮箱中所有的列表，如：收件箱、垃圾箱、草稿箱。。。

        s = self.conn.select('INBOX')  # 选择收件箱（默认）
        result, dataid = self.conn.search(None, 'ALL')

        mailidlist = dataid[0].split()  # 转成标准列表,获得所有邮件的ID
        # type, data = conn.fetch(mailidlist[0], '(RFC822)')

        maillist = []
        for id in mailidlist:
            result, data = self.conn.fetch(id, '(RFC822)')  # 通过邮件id获取邮件
            e = email.message_from_bytes(data[0][1])
            from email.policy import default
            msg = BytesParser(policy=default).parsebytes(data[0][1])
            maillist.append(e)
            subject = email.header.make_header(email.header.decode_header(e['SUBJECT']))
            mail_from = email.header.make_header(email.header.decode_header(e['From']))
            print("邮件的subject是:%s" % subject)
            print("邮件的发件人是:%s" % mail_from)
            body = str(get_body(e), encoding='gb2312')  # utf-8 gb2312 GB18030解析中文日文英文
            print("邮件内容是:%s" % body)

        return maillist

if __name__ == '__main__':
    receiver = EMailReceiver()
    receiver.login()
    maillist = receiver.receive()


#
#
# attachementdir = r"d:\a"  # 附件存放的位置
#
# conn = imaplib.IMAP4_SSL(imapserver)
# conn.login(emailuser, emailpasswd)
#
#
#
#
#
#
#
# #result, dataid = conn.uid('search', None, "ALL")
# result, dataid = conn.search(None, 'ALL')
#
# mailidlist = dataid[0].split()  # 转成标准列表,获得所有邮件的ID
# # type, data = conn.fetch(mailidlist[0], '(RFC822)')
#
# for id in mailidlist:
#     result, data = conn.fetch(id, '(RFC822)')  # 通过邮件id获取邮件
#     e = email.message_from_bytes(data[0][1])
#     subject = email.header.make_header(email.header.decode_header(e['SUBJECT']))
#     mail_from = email.header.make_header(email.header.decode_header(e['From']))
#     print("邮件的subject是%s" % subject)
#     print("邮件的发件人是%s" % mail_from)
#     body = str(get_body(e), encoding='gb2312')  # utf-8 gb2312 GB18030解析中文日文英文
#     print("邮件内容是%s" % body)
#
# conn.logout()