# Importing Module Requests
import requests

# Setting up a Session object
session = requests.session()
session.proxies = {}

# Real IP
RealIP = session.get('http://httpbin.org/ip')
print("Real IP:", RealIP.text)

# Adding Proxies
session.proxies['http'] = 'socks5h://127.0.0.1:9150'
session.proxies['https'] = 'socks5h://127.0.0.1:9150'

# To view Changed IP address
ChangedIP = session.get("http://httpbin.org/ip")
print("Changed IP:", ChangedIP.text)

# Dark Web Request- Request that is possible only in Tor Browser not in normal Browser
r = session.get('https://www.facebookcorewwwi.onion/')
print(r.headers)

"""Well they (Who are 'they' here?) know we are using python script with version too."""
user_agent = session.get('https://httpbin.org/user-agent')
print("User:", user_agent.text)

"""Well! Let's change user """
headers = {'User-agent': 'CatLanguage/7.1.1 PCS'}  # Well there is no CatLanguage :-)
new_user_agent = session.get('https://httpbin.org/user-agent', headers=headers)
print("Changed User: ", new_user_agent.text)

"""Using Session object means we have cookies.. Let's set a new cookie with the value 'RAW'"""
session.get('http://httpbin.org/cookies/set/sessioncookie/RAW')

# Let's check our new cookie
cookies = session.get('http://httpbin.org/cookies')
print("Cookies: ", cookies.text)


