from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome(executable_path='../tools/chromedriver.exe')

def after_all(context):
    context.driver.quit()