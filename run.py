from linkedin import linkedin

API_KEY = '81gwj1xw9ggojq'
API_SECRET = '7x7XpoBx8yfW6CtH'
RETURN_URL = 'http://localhost/linkedin-scraping'

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
# Optionally one can send custom "state" value that will be returned from OAuth server
# It can be used to track your user state or something else (it's up to you)
# Be aware that this value is sent to OAuth server AS IS - make sure to encode or hash it
#authorization.state = 'your_encoded_message'
print (authentication.authorization_url)    # open this url on your browser
application = linkedin.LinkedInApplication(authentication)