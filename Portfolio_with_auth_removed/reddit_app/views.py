from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .PortfolioProjectScripts import TimeToPostReddit as ttp



def timetopost_view(request):
    time = [num for num in range(0, 24)]
    context = {'time': time}
    return render(request, 'time_to_post_reddit.html', context)
    '''reddit = ttp.reddit_auth()
    if request.method == 'POST':
        subname_request = request.POST
        subname = subname_request['SubNameInput']
        request.session.save()
    else:
        subname = 'redditdev'
    subarray = ttp.reddit_data(reddit, subname)
    sublogo = ttp.subreddit_logo(reddit, subname)

    context = {'subarray': subarray, 'time': time, 'subname': subname, 'sublogo': sublogo}
    return render(request, 'time_to_post_reddit.html', context)'''

@api_view(['POST', 'GET'])
def collect_reddit_data(request):
    reddit = ttp.reddit_auth()

    subname_request = request.data
    subname = subname_request['subRedditName']
    request.session.save()

    collect_reddit_data.subarray = ttp.reddit_data(reddit, subname)
    collect_reddit_data.sublogo = ttp.subreddit_logo(reddit, subname)
    return Response()

@api_view(['POST', 'GET'])
def show_reddit_data(request):
    subreddit_array = collect_reddit_data.subarray
    subreddit_icon = collect_reddit_data.sublogo
    Json_Item = {"subreddit_array": subreddit_array, "subreddit_icon": subreddit_icon}
    return Response(Json_Item)

