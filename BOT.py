import tweepy
import gif
from datetime import time
import Data
from datetime import datetime

#Getting all data from files
data=Data.Get_data()

#Important data keys from twiter
consumer_key=data.ck
consumer_secret=data.cs
access_token=data.at
access_token_secret=data.ats
#----------------------------------------------------------------

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Base to search gifs of that
base_search='spongebob'

id_res=data.id_ment

while True:

	ment=api.search('@SpongeBOT_Gifs',rpp=1,since_id=id_res)

	#The program needs to wait until twitter lets tweet again
	api.wait_on_rate_limit=True

	

	#Only works if there is at least one mention
	if len(ment)>0:

		#Using this I get which gif user are searching
		w=ment[0].text.partition(' ')
		word_search=w[2]
		Data.Update_id(str(ment[0].id))
		id_res=ment[0].id

		print(id_res)
		print(ment[0].text,"\n")

		if datetime.now()==time(20,48,0):
			gif.gif_download(data.base,20,data.tk)
			api.update_with_media('gif_BOT.gif',status='🎉😍DAILY GIFS!!😍🎉')
			print('Dayly printed')

		#Getting the gif
		gif.gif_download(data.base+' '+word_search,20,data.tk)

		#Tweet the response
		api.update_with_media('gif_BOT.gif',status='@'+ment[0].user.screen_name,in_reply_to_status_id=ment[0].id)
