#!/usr/bin/python

"""
ShouldHaveBot

@author:	Stefan New - http://www.stefannew.com
@date:		September 11th, 2014
@version:	1.0

"""

import datetime
import praw
import time

from dev import *

user_agent = ("Should Have Bot 1.0")
r = praw.Reddit(user_agent = user_agent)
r.login('ShouldHaveBot', USER_PASSWORD)

already_checked = []

while True:
	all_comments = r.get_comments('all')

	for comment in all_comments:
		if comment.id not in already_checked:
			if "should of" in comment.body.lower():
				comment.reply("I think you meant *should have*.")
				print "[" + datetime.datetime.now().strftime("%I:%M%p") + "] Replied to comment " + comment.id
			already_checked.append(comment.id)
	time.sleep(60)
