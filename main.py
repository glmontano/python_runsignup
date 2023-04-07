import requests
import json
import os

from dotenv import find_dotenv, load_dotenv, set_key

dotenv_file = find_dotenv()
load_dotenv(dotenv_file, override=True)

JSON_INDENT_NUM = 2

RSL_URLS = {'URL_LOGIN': 'https://runsignup.com/rest/login',
			'URL_USER_PRE': 'https://runsignup.com/rest/user/',
			'URL_CLUB_PRE': 'https://runsignup.com/rest/club/'}


class RunSignUpAPI:

	def __init__(self):
		self.output_format = 'json'
		self.tmp_key = os.environ['TMP_KEY']
		self.tmp_secret = os.environ['TMP_SECRET'],
		self.rsu_protected_api_sig = os.environ['RSU_PROTECTED_API_SIG']
		self.email = os.environ['EMAIL'],
		self.password = os.environ['PASSWORD'],
		self.user_id = os.environ['RSU_USER_ID']
		self.club_id = os.environ['RSU_CLUB_ID']
		
	def login(self):

		params = {
			'format': self.output_format,
			'supports_nb': 'F',
			'email' : self.email,
			'password': self.password
		}

		res = requests.post(RSL_URLS['URL_LOGIN'], data=params)
		print(f'{res.url}\n{res.text}')
		res = json.loads(res.text)
		print(json.dumps(res, indent=JSON_INDENT_NUM))
		for e in ['tmp_key', 'tmp_secret']: set_key(dotenv_file, e.upper(), res[e])
		


	def get_user_information(self):

		params = {
			'format': self.output_format,
			'tmp_key': self.tmp_key,
			'tmp_secret': self.tmp_secret,
		}

		res = requests.get(f'{RSL_URLS["URL_USER_PRE"]}{self.user_id}', params=params)
		print(f'{res.url}\n{res.status_code}')
		res = json.loads(res.text)
		print(json.dumps(res, indent=JSON_INDENT_NUM))


	def get_club_information(self):

		params = {
			'format': self.output_format,
			'tmp_key': self.tmp_key,
			'tmp_secret': self.tmp_secret,
		}

		res = requests.get(f'{RSL_URLS["URL_CLUB_PRE"]}{self.club_id}', params=params)
		print(f'{res.url}\n{res.text}')
		res = json.loads(res.text)
		print(json.dumps(res, indent=JSON_INDENT_NUM))



	def get_club_members(self):

		params = {
			'format': self.output_format,
			'tmp_key': self.tmp_key,
			'tmp_secret': self.tmp_secret,
		}

		res = requests.get(f'{RSL_URLS["URL_CLUB_PRE"]}{self.club_id}/members', params=params)
		print(f'{res.url}\n{res.text}')
		res = json.loads(res.text)
		print(json.dumps(res, indent=JSON_INDENT_NUM))

foo = RunSignUpAPI()
foo.get_user_information()

