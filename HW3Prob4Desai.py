import re 

myLinks = ''' my name is 
Ishaan Desai
I am a computer engineer

at northeastern university

and I 
live in Boston

http://www.domain_name.edu 
https://www.domain_name.extension 
http://domain_name.co.uk 
https://domain_name.extension
http://domain_name.extension 
https://dom@!n_name.extension
http://do.extension 
https://domain_name.extension

im originally from andover
hope i get a good grade
'''


findingURL = re.compile(r'https?://w?w?w?\.?[^_]\w{2,}[^_]\.\w+\.?\w+\w')
findingMatch = findingURL.findall(myLinks)
for match in findingMatch:
        print("URL: ")
        print(match)