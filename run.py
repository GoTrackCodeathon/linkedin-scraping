from linkedin import linkedin

API_KEY = '81gwj1xw9ggojq'
API_SECRET = '7x7XpoBx8yfW6CtH'
RETURN_URL = 'http://localhost/linkedin-scraping'

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
    print (authentication.authorization_url)    # open this url on your browser
application = linkedin.LinkedInApplication(authentication)