from selenium import webdriver
import sys
import io

#
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf - 8')
options = webdriver.ChromeOptions()
# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 
#self.options.add_argument("--headless")
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
#options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"]) 

#options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.63 MQQBrowser/8.9 Mobile Safari/537.36')
options.add_experimental_option("detach", True)

# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 
driver = webdriver.Chrome(options=options) 

# Send the request 
driver.get("https://www.urbtix.hk")