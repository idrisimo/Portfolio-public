''' This program will indicate the best time to post, based on either top 500 posts of all time.'''
from pprint import pprint
import praw
import pandas as pd
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials


def reddit_auth(): # connects to reddit
        reddit = praw.Reddit(client_id= "client_id",
                             client_secret= "client_secret",
                             user_agent= "Ruser_agent")
        return reddit

def reddit_data(reddit, subreddit_name):
    subData = {}
    subreddit = reddit.subreddit(subreddit_name)
    count = 0
    for submission in subreddit.top('all', limit=300):
        time_created = datetime.fromtimestamp(submission.created_utc)
        day_of_week = time_created.weekday()
        time_of_day = time_created.strftime('%H:%M')
        time_of_day = pd.Timestamp(time_of_day).round('60min').to_pydatetime().strftime('%H')
        subData.setdefault(submission.id, {"Day of week": day_of_week, "Time of day": time_of_day})
        count += 1
    subFrame = pd.DataFrame(subData).T
    subArray = [[0 for j in range(24)] for i in range(7)]
    for index, row in subFrame.iterrows():
        dow = row['Day of week']
        tod = int(row['Time of day'])
        subArray[dow][tod] += 1
    return subArray

def subreddit_logo(reddit, subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    logo = subreddit.icon_img
    return logo
