from newCard.NewCard import NewCard
from pageObjects.HomePage import Homepage
from viewRequest.viewRequest import ViewRequest
import time


class ViewVoidRequest:
    filter_textbox_xpath = "//input[@id='filterInput']"
    filter_result_xpath = "//tbody/tr[1]/td[2]"
    approve_button_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[3]/button[1]"
    approveConfirmation_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[3]/button[1]"
    cancelRequest_button_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[4]/button[1]"
    cancelRequest_reason_xpath = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    submitReason_xpath = "//button[contains(text(),'Submit')]"
    submitReasonConfirmation_xpath = "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]"
    closeReason_xpath = "(//button[@type='button'])[7]"
    verifyStatus_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]"

    def __init__(self, driver):
        self.driver = driver

    def approveVoidReq(self, expected_status1, expected_status2):
        hp = Homepage(self.driver)
        np = NewCard(self.driver)
        vp = ViewRequest(self.driver)
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.filter_result_xpath).click()
        self.driver.find_element_by_xpath(self.approve_button_xpath).click()
        self.driver.find_element_by_xpath(self.approveConfirmation_xpath).click()
        time.sleep(5)
        hp.clickviewVoidRequest()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(5)
        self.driver.refresh()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(5)
        status = self.driver.find_element_by_xpath(np.verifyStatus_xpath).text
        assert status == expected_status1, "Status mismatch! Expected status is %s" % expected_status1
        hp.clickutil()
        hp.clickviewRequest()
        self.driver.find_element_by_xpath(vp.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(5)
        status = self.driver.find_element_by_xpath(np.verifyStatus_xpath).text
        assert status == expected_status2, "Status mismatch! Expected status is %s" % expected_status2



    def rejectVoidReq(self, expected_status3):
        hp = Homepage(self.driver)
        np = NewCard(self.driver)
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.filter_result_xpath).click()
        self.driver.find_element_by_xpath(self.cancelRequest_button_xpath).click()
        self.driver.find_element_by_xpath(self.cancelRequest_reason_xpath).send_keys(
            "Top Up Request is valid for Top Up")
        self.driver.find_element_by_xpath(self.submitReason_xpath).click()
        self.driver.find_element_by_xpath(self.submitReasonConfirmation_xpath).click()
        self.driver.find_element_by_xpath(self.closeReason_xpath).click()
        hp.clickviewVoidRequest()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(5)
        status = self.driver.find_element_by_xpath(np.verifyStatus_xpath).text
        assert status == expected_status3, "Status mismatch! Expected status is %s" % expected_status3

    def viewVoidRequest(self):
        np = NewCard(self.driver)
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.filter_result_xpath).click()
        self.driver.find_element_by_xpath(self.approve_button_xpath).click()
        self.driver.find_element_by_xpath(self.approveConfirmation_xpath).click()
        self.driver.find_element_by_xpath(self.cancelRequest_button_xpath).click()
        self.driver.find_element_by_xpath(self.cancelRequest_reason_xpath).send_keys("Request is valid for top up")
        self.driver.find_element_by_xpath(self.submitReason_xpath).click()

