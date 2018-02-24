from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome(executable_path='../../drivers/chromedriver.exe')

def after_all(context):
    context.driver.quit()