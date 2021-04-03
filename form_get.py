from flask import Flask 
from flask import request 
 
def login():
	if request.method == 'GET': 
		first_name = request.form['firstname'] 
		last_name = request.form['lastname'] 
		country = request.form['country']

		subject = request.form['subject']

		print(first_name, last_name, country, subject)
		# code that uses the data you've got 
		# in our case, checking if the user exists 
		# and logs them in, if not redirect to sign up 
	else: 
		print('SRY')