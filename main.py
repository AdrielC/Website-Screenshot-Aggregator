import time
import sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.PhantomJS(executable_path='/Volumes/🅱️/Macbook Desktop 2/Giant/ScreenshotProject/phantomjs') # PATH to installation of PhantomJS
weburl = 'http://hodgkinhub.com/'
wait = 1

### Viewport definitions
iPhone4s = (320, 480)
iPhone5 = (320, 568)
iPhone6 = (375, 667)
iPhone6Plus = (414, 736)
iPad2 = (1024, 768)
SamsungGalaxy = (360, 640)
Macbook13 = (1440, 900)
iMac27 = (2560, 1440)

### Select Viewports
viewports = (Macbook13, iPhone6Plus, iMac27, iPhone4s)
viewports = list(viewports)

class Screenshot():
    def __init__(self, viewport):
        driver.set_window_size(viewport[0], viewport[1])
        driver.get(weburl)

    def capture(self, weburl, output_file):
        driver.save_screenshot(output_file)

for idx, viewport in enumerate(viewports):
    time.sleep(wait)
    s = Screenshot(viewport)
    s.capture(weburl, 'screenshot1%s %s.png' % (idx, viewport))
    sbtn = driver.find_element_by_css_selector('.relapsed a')
    sbtn.click()
    time.sleep(wait)
    s.capture(weburl, 'screenshot2%s %s.png' % (idx, viewport))
