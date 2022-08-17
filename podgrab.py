#-----------------------------------------------------------------------
# Program: podgrab
# Purpose: To snag episodes of podcasts off of the google podcast feed
#    so they can go on an mp3 player
#-----------------------------------------------------------------------

import requests
import lxml.html

#list for podcast feeds
feeds = {'Lord of Spirits': 'https://podcasts.google.com/feed/aHR0cDovL2ZlZWRzLmFuY2llbnRmYWl0aC5jb20vVGhlTG9yZE9mU3Bpcml0cw?sa=X&ved=0CAYQ9sEGahgKEwiQi9Wux5T5AhUAAAAAHQAAAAAQiwM',
        'Online Great Books': 'https://podcasts.google.com/feed/aHR0cDovL2ZlZWRzLmxpYnN5bi5jb20vMTIwNTk1L3Jzcw?sa=X&ved=0CAMQ4aUDahgKEwjoisGQm875AhUAAAAAHQAAAAAQ2Qo',
        'School Sucks': 'https://podcasts.google.com/feed/aHR0cHM6Ly9zY2hvb2xzdWNrcy5wb2RvbWF0aWMuY29tL3JzczIueG1s?sa=X&ved=0CAwQ9sEGahgKEwjoisGQm875AhUAAAAAHQAAAAAQug0'}
try:
    output = open("Podcasts.txt", "w")
except Exception(e):
    print('***\n' + str(e) + '\n***')

for podcast in feeds:
    output.write('\n***' + str(podcast) + '***\n\n')
    # Making a GET request
    r = requests.get(feeds[podcast])
    html_txt = str(r.text)
    html = lxml.html.fromstring(html_txt)

    episodes = {}
    titles = html.cssselect('.e3ZUqe')
    links = html.cssselect('.zlb4lf')
    for title in titles:
        for link in links:
            episodes[title] = link
            
    for episode in episodes:
        clean_title = str(lxml.html.tostring(episode).decode('utf-8').lstrip('<div class="e3ZUqe" role="presentation">').rstrip('</div>'))
        clean_url = str(lxml.html.tostring(episodes[episode]).decode('utf-8').lstrip('<div class="zlb4lf"><div jsname="fvi9Ef" jsmodel="kY0ub" jsdata="Kwyn5e;'))
        dbl_clean_url = clean_url.split(";")
        output.writelines(clean_title)
        output.writelines( ' : ' + str(dbl_clean_url[0]) + '\n')

output.close()