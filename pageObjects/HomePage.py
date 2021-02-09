from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Homepage:
    utilityTopUp_xpath = "//div[@id='wrapper']/div/ul/li[8]/a"
    reqNewCard_xpath = "//a[contains(text(),'create top up request (new card)')]"
    reqExistingCard_xpath = "//a[contains(text(),'Create top up request (existing card)')]"
    viewTopUpRequest_xpath = "//a[contains(text(),'View all topup request')]"
    viewVoidRequest_xpath = "//body[1]/div[1]/div[1]/div[1]/ul[1]/li[5]/a[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickutil(self):
        self.driver.find_element_by_xpath(self.utilityTopUp_xpath).click()

    def clickreqNewCard(self):
        self.driver.find_element_by_xpath(self.reqNewCard_xpath).click()

    def clickreqExistingCard(self):
        self.driver.find_element_by_xpath(self.reqExistingCard_xpath).click()

    def clickviewRequest(self):
        self.driver.find_element_by_xpath(self.viewTopUpRequest_xpath).click()

    def clickviewVoidRequest(self):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.viewVoidRequest_xpath)))
        element.click()
