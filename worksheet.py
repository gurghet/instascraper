from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os, time, json

options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
options.add_argument('headless')
caps = DesiredCapabilities.CHROME
caps['loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(executable_path="./chromedriver", options=options, desired_capabilities=caps)
driver.get('https://www.instagram.com/')
driver.add_cookie({'name': 'sessionid', 'value': os.environ['INSTAGRAM_SESSION_ID'], 'secure': True})
driver.get('https://www.instagram.com/suh_pig/')
trialCounter = 0
while len(driver.find_elements_by_css_selector('a[href="/p/BomgHhkg_wV/"]')) == 0:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    trialCounter += 1
    print(trialCounter)
browser_log = driver.get_log('performance')
# driver.close()
with open('/tmp/data.json', 'w') as file:
    file.write(json.dumps(browser_log))
driver.close()

# cat data.json | jq '.[] | .message | fromjson.message | select(.method == "Network.requestWillBeSent") | .params.request.url' | grep after
# prendo __a=1 e gli altri e ottengo altrettanti json
# estraggo gli array di edge e li unisco
# prendo i like di ognuno e li salvo