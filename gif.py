import requests
import json
from random import randint
import os

def GetListOfSubstrings(stringSubject,string1,string2):
    MyList = []
    intstart=0
    strlength=len(stringSubject)
    continueloop = 1

    while(intstart < strlength and continueloop == 1):
        intindex1=stringSubject.find(string1,intstart)
        if(intindex1 != -1): #The substring was found, lets proceed
            intindex1 = intindex1+len(string1)
            intindex2 = stringSubject.find(string2,intindex1)
            if(intindex2 != -1):
                subsequence=stringSubject[intindex1:intindex2]
                MyList.append(subsequence)
                intstart=intindex2+len(string2)
            else:
                continueloop=0
        else:
            continueloop=0
    return MyList

def get_size(the_path):
    """Get size of a directory tree or a file in bytes."""
    path_size = 0
    for path, directories, files in os.walk(the_path):
        for filename in files:
            path_size += os.lstat(os.path.join(path, filename)).st_size
        for directory in directories:
            path_size += os.lstat(os.path.join(path, directory)).st_size
    path_size += os.path.getsize(the_path)
    return path_size

def gif_download(search_term,lmt,apikey):
	gifs=[]

	# load the user's anonymous ID from cookies or some other disk storage
	# anon_id = <from db/cookies>

	# ELSE - first time user, grab and store their the anonymous ID
	r = requests.get("https://api.tenor.com/v1/anonid?key=%s" % apikey)

	if r.status_code == 200:
	    anon_id = json.loads(r.content)["anon_id"]
	    # store in db/cookies for re-use later
	else:
	    anon_id = ""

	#Size
	size="basic"

	# get a random GIF
	r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&anon_id=%s&media_filter=%s" % (search_term, apikey, lmt, anon_id,size))

	if r.status_code == 200:
	    # load the GIFs using the urls for the smaller GIF sizes
	    top_8gifs = json.loads(r.content)

	else:
	    top_8gifs = None

	a=str(top_8gifs)

	i=0

	gifs = GetListOfSubstrings(a,"'gif': {'url': '","',")

	while True:

		imagen = requests.get(gifs[randint(0, lmt-1)]).content

		with open('gif_BOT.gif', 'wb') as handler:
			handler.write(imagen)

		if get_size('gif_BOT.gif') < 3072*1000:
			break


