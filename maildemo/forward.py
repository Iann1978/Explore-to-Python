#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sender as sd
import receiver as rv

if __name__ == '__main__':
    print('forward start')

    receiver = rv.EMailReceiver()
    receiver.login()
    maillist = receiver.receive()

    sender = sd.EMailSender()
    sender.login()
    sender.send(maillist)
