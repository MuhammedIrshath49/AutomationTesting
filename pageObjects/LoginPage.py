class LoginPage:

    textbox_username_name="username"
    textbox_password_name="password"
    button_login_xpath="//button[contains(text(),'Login')]"


    def __init__(self,driver):
        self.driver=driver


    def setUsername(self,username):
        self.driver.find_element_by_name(self.textbox_username_name).send_keys(username)


    def setPassword(self, password):
        self.driver.find_element_by_name(self.textbox_password_name).send_keys(password)


    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()



