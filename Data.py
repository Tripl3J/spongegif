import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds=ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client=gspread.authorize(creds)

sheet=client.open('SpongeBOT').sheet1


def Get_data():	

	class data:
		def __init__(self):
			#TWITTER KEYS
			self.ck=ck				#consumer_key
			self.cs=cs  			#consumer_secret
			self.at=at 				#access_token
			self.ats=ats 			#access_token_secret

			#TENOR KEY
			self.tk=tk 				#apikey

			#TWEET DATA
			self.id_ment=id_ment	#id of mention
			self.base=base			#base_search

	#TWITTER KEYS
	data.ck=sheet.cell(2,2).value
	data.cs=sheet.cell(3,2).value
	data.at=sheet.cell(4,2).value
	data.ats=sheet.cell(5,2).value

	#TENOR KEY
	data.tk=sheet.cell(8,2).value

	#TWEET DATA
	data.id_ment=sheet.cell(11,2).value
	data.base=sheet.cell(12,2).value

	return data

def Update_id(new_id):
	sheet.update_cell(11,2,new_id)