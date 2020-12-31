'''
Write a python program which will take email as parameter and determine the pattern. 
Email can come as 
FIRST DOT LAST = "first.last@", 
LAST DOT FIRST = "last.first@", 
FIRST UNDERSCORE LAST = "first_last@", 
LAST UNDERSCORE FIRST = "last_first@", 
FIRST CHAR LAST = "first(1)last@", 
LAST CHAR FIRST = "last(1)first@", 

COMMON_EMAIL = "?" 

You can use NameDataset ((https://github.com/philipperemy/name-dataset) which tells us if the name is first name and last name. 

IMPORTANT NOTE: 
* Tested with Python 3.9 64 bit on Windows, with names_dataset installed using "pip install names_dataset".
'''

import re
from names_dataset import NameDataset

def get_email_pattern(email):
	email_username = email.split('@')[0]  # get first (left) part of email address

	print('email_username ', email_username)
	pattern = ''

	# split it to 3 parts (ideally)
	result = re.split('(\.|_|\([A-Za-z0-9]+\))', email_username) 

	
	if len(result) < 3:
		pattern = 'COMMON_EMAIL'
	else:
		p1 = result[0]
		mid = result[1]
		p2 = result[2]


		if mid == '.':  # since only can be looked up, I didn't use a dictionary
			seperator = 'DOT'
		elif mid == '_':
			seperator = 'UNDERSCORE'
		else:
			seperator = 'CHAR'
		
		nds = NameDataset()

		'''
			There are few names that found in both firstnames and lastnames. e.g. basha, syed
			So, for basha_syed and syed_basha, first condition is always evaluated to True.
		'''
		if nds.search_first_name(p1) and nds.search_last_name(p2):
			pattern = 'FIRST%sLAST'%seperator
		elif nds.search_last_name(p1) and nds.search_first_name(p2):
			pattern = 'LAST%sFIRST'%seperator
		else:
			pattern = 'COMMON_EMAIL'
	
	return pattern

email = input('Enter email: ')
pattern = get_email_pattern(email)
print('Pattern: ', pattern)