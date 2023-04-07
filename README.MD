# Objective

Python hook on RunSignUp's (RSU) API

# How to use

	1. Clone repo to your destination
	2. `pip install -r requirements.txt`
	3. Set up the following environment variables in `.env`
		- EMAIL: Your RSU email address
		- PASSWORD: Your RSU email address
		- RSU_USER_ID: The user_id of interest
		- RSU_CLUB_ID: The club_id of interest
		- RSU_PROTECTED_API_SIG: Read To Do
		- TMP_KEY: Will be auto populated by code
		- TMP_SECRET: Will be auto populated by code

# To Do

	- Login authentication through OAuth 1.0 authentication.
	- Get RSU Protected API Signature
	- Further investigate Club API functions
