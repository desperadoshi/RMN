#!/usr/bin/python3.5
from urllib.request import urlopen
import re
from random import choice
from requests import post
#  connect to a URL
site_url = "http://desperadoshi.github.io/notes/site/index.html"
website = urlopen(site_url)
#  read html code
html = website.read()
_html_str = html.decode("utf-8")

#############################
# 
#############################
#  
def log(in_url):
    print(in_url+" is added to Pocket.")

def get_url(in_group_name, in_pattern):
    #  use re.findall to get all the links
    links = re.findall(in_pattern, _html_str)
    #  select random one
    link = choice(links)
    link_base = "http://desperadoshi.github.io/notes/site/"
    url = link_base + link
    return url
#  add to Pocket
def add_to_pocket(in_url):
    consumer_key = '66977-53ed346d5d8f7842346319ec'
    access_token = '47cae2c3-59fa-9d64-78eb-8851b8'
    result = post('https://getpocket.com/v3/add', data={'url': in_url, 'consumer_key': consumer_key, 'access_token': access_token})
    if(result.status_code == 200):
        log(in_url)
    else:
        print(in_url+" is NOT added to Pocket.")

def execute_once():
    #  for Technical Notes
    group_list = ["cfd", "computer_science", "fluid_dynamics", "math", "misc", "programming", "tools"]
    group_name = choice(group_list)
    pattern = group_name+'/[\w\d+.]+\.html'
    url = get_url(group_name, pattern)
    add_to_pocket(url)
    #  for This American Life
    group_name = "thisamericanlife"
    pattern = group_name+'/\d+\.html'
    url = get_url(group_name, pattern)
    add_to_pocket(url)

#  from time import sleep
#  while(True):
    #  sleep_time = 3600*24
    #  sleep(sleep_time)
from datetime import date
wday = date.today().isoweekday()
if(wday == 1):
    execute_once()

