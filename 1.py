'''
Find subdomain in a domain using regex. Test https://blog.microsoft.com/test.html (blog), https://www.blog.microsoft.com/test/test (blog is the answer - www is not considered), https://www.microsoft.com (no subdomain) 
'''
import re

url = input('URL to get subdomain name: ')
result = re.findall('^((http|https)(\:\/\/))?(www\.)?(\w+\.)?\w+\.\w+(\/.+)?$', url)

print(result)
if result:
	print('Subdomain is: ', result[0][4][:-1])
else:
	print('No subdomain')
