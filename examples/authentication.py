from linkedin.linkedin import (LinkedInAuthentication, LinkedInApplication,
                               PERMISSIONS)


if __name__ == '__main__':
    API_KEY = '81gwj1xw9ggojq'
    API_SECRET = '7x7XpoBx8yfW6CtH'
    RETURN_URL = 'http://localhost/linkedin-scraping'
    authentication = LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL,
                                            PERMISSIONS.enums.values())
    print authentication.authorization_url
    application = LinkedInApplication(authentication)
