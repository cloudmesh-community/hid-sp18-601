import connexion
import six

from swagger_server import util

from flask import request

def sub_post():  # noqa: E501
    """sub_post

    creates subscriber with name sub_name # noqa: E501


    :rtype: None
    """
    #getting the input
    subscriberData = raw_input(
        "Enter the subscriber name and email separated by a comma:")
    subscriberList = open('./subscriberList.txt','r+')
    if subscriberDataSplitEmail not in subscriberList:
        subscriberList.write(subscriberData)
        subscriberList.write('\n')
    else:
        print('Subscriber already present')
