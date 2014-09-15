#!/usr/bin/python

'''
ShouldHaveBot

@author:    Stefan New - http://www.stefannew.com
@date:      September 14th, 2014
@version:   1.1

'''

import datetime
import praw
import time
import re

from settings import *


class ShouldHaveBot(object):
    def __init__(self, username, password, user_agent, interval):
        self.username = username
        self.password = password
        self.instance = praw.Reddit(user_agent=user_agent)
        self.interval = interval

    def log(self, date, now, cid):
        string = '[' + date + ' ' + now + ']' + ' - Replied to comment ' + cid

        with open('log.txt', 'a+') as f:
            f.write(string + '\n')
        print(string)

    def login(self):
        self.instance.login(self.username, self.password)

    def run(self):
        already_checked = []

        while True:
            all_comments = self.instance.get_comments('all')
            regex = ur'\bshould of\b'

            date = time.strftime('%d/%m/%Y')
            now = datetime.datetime.now().strftime('%I:%M%p')

            for comment in all_comments:
                if comment.id not in already_checked:
                    if re.search(regex, comment.body.lower()):
                        comment.reply('I think you meant *should have*.')
                        self.log(date, now, comment.id)
                    already_checked.append(comment.id)

            time.sleep(self.interval)

bot = ShouldHaveBot('ShouldHaveBot', PASSWORD, 'ShouldHaveBot 1.1', 60)
bot.login()
bot.run()
