from existingCard.ExistingCard import ExistingCard
from newCard.NewCard import NewCard
from pageObjects.HomePage import Homepage
import time


class ViewRequest:
    filter_textbox_xpath = "//input[@id='filterInput']"
    filter_result_xpath = "//table[@id='table']/tbody/tr/td[2]"
    approve_button_xpath = "//button[contains(text(),'Approve')]"
    approveConfirmation_xpath = "//button[contains(text(),'Click again to confirm submit!')]"
    rejectec_button_xpath = "//button[contains(text(),'Reject')]"
    rejectnc_button_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[3]/button[2]"
    reject1_button_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[3]/button[1]"
    rejectReason_xpath = "//textarea[@id='textarea-reason']"
    rejectncReason_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/textarea[1]"
    approveVoidReq_button_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[3]/button[1]"
    approveVoidReqConfirm_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[3]/button[1]"
    verifyStatus_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]"

    def __init__(self, driver):
        self.driver = driver

    def approveReqExistingCard(self, expected_status):
        ep = ExistingCard(self.driver)
        hp = Homepage(self.driver)
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(ep.jobReqExistCard)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.filter_result_xpath).click()
        time.sleep(5)
        # To approve request for existing card
        self.driver.find_element_by_xpath(self.approve_button_xpath).click()
        self.driver.find_element_by_xpath(self.approveConfirmation_xpath).click()
        hp.clickviewRequest()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(ep.jobReqExistCard)
        time.sleep(25)
        self.driver.refresh()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(ep.jobReqExistCard)
        time.sleep(5)
        status = self.driver.find_element_by_xpath(ep.verifyStatus_xpath).text
        assert status == expected_status, "Status mismatch! Expected status is %s" % expected_status

    def rejectReqExistingCard(self, expected_status):
        ep = ExistingCard(self.driver)
        hp = Homepage(self.driver)
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(ep.jobReqExistCard)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.filter_result_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.rejectec_button_xpath).click()
        self.driver.find_element_by_xpath(self.rejectReason_xpath).send_keys("Invalid request")
        self.driver.find_element_by_xpath(self.reject1_button_xpath).click()
        self.driver.find_element_by_xpath(self.reject1_button_xpath).click()
        time.sleep(5)
        hp.clickviewRequest()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(ep.jobReqExistCard)
        time.sleep(25)
        self.driver.refresh()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(ep.jobReqExistCard)
        time.sleep(5)
        status = self.driver.find_element_by_xpath(ep.verifyStatus_xpath).text
        assert status == expected_status, "Status mismatch! Expected status is %s" % expected_status

    def approveReqNewCard(self, expected_status):
        np = NewCard(self.driver)
        hp = Homepage(self.driver)
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.filter_result_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.approve_button_xpath).click()
        self.driver.find_element_by_xpath(self.approveConfirmation_xpath).click()
        hp.clickviewRequest()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(25)
        self.driver.refresh()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(5)
        status = self.driver.find_element_by_xpath(np.verifyStatus_xpath).text
        assert status == expected_status, "Status mismatch! Expected status is %s" % expected_status

    def rejectReqNewCard(self, expected_status):
        np = NewCard(self.driver)
        hp = Homepage(self.driver)
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.filter_result_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.rejectnc_button_xpath).click()
        self.driver.find_element_by_xpath(self.rejectncReason_xpath).send_keys("Invalid Excel File used")
        self.driver.find_element_by_xpath(self.reject1_button_xpath).click()
        self.driver.find_element_by_xpath(self.reject1_button_xpath).click()
        hp.clickviewRequest()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(25)
        self.driver.refresh()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(5)
        status = self.driver.find_element_by_xpath(np.verifyStatus_xpath).text
        assert status == expected_status, "Status mismatch! Expected status is %s" % expected_status

    def createVoidReq(self):
        self.driver.find_element_by_xpath(self.filter_result_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.approveVoidReq_button_xpath).click()
        self.driver.find_element_by_xpath(self.approveVoidReqConfirm_xpath).click()
        time.sleep(5)

    def viewTopUpRequest(self, rownum):
        np = NewCard(self.driver)
        ep = ExistingCard(self.driver)
        hp = Homepage(self.driver)
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(ep.jobReqExistCard)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.filter_result_xpath).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(self.approve_button_xpath).click()
        self.driver.find_element_by_xpath(self.approveConfirmation_xpath).click()
        time.sleep(5)
        hp.clickviewRequest()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(ep.jobReqExistCard)
        time.sleep(20)
        self.driver.refresh()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(ep.jobReqExistCard)

    # This is POM Section. Hence there's a need to distinguish upper chunk and lower chunk

    def searchJobOrder(self):
        ep = ExistingCard(self.driver)
        np = NewCard(self.driver)
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(ep.jobReqExistCard)
        time.sleep(5)

    def clickFilterResult(self):
        self.driver.find_element_by_xpath(self.filter_result_xpath).click()

    def checkStatus(self):
        status = self.driver.find_element_by_xpath(self.verifyStatus_xpath).text
        assert status == "Pending", "Incorrect Status, Expected status is Pending"

    def checkRequestInfo(self):
        ep = ExistingCard(self.driver)
        np = NewCard(self.driver)
        expected_jobOrder = np.jobReqNewCard
        card_quantity = "6"
        total_amt = 6.00
        job_order = self.driver.find_element_by_xpath(
            "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/b[1]").text
        no_of_cards = self.driver.find_element_by_xpath(
            "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[5]/div[2]/b[1]").text
        topup_amt = self.driver.find_element_by_xpath(
            "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[2]/b[1]").text
        assert job_order == expected_jobOrder, "Incorrect job order number, expected job order number is %s" % expected_jobOrder
        assert no_of_cards == card_quantity, "Incorrect number of cards, expected number of cards is %s" % card_quantity
        assert float(topup_amt) == total_amt, "Incorrect topup amount, expected topup amount is %s" % total_amt

    def approveRequest(self):
        self.driver.find_element_by_xpath(self.approve_button_xpath).click()
        self.driver.find_element_by_xpath(self.approveConfirmation_xpath).click()
        expected_result = "Record successfully approved!"
        result = self.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/label[1]").text
        result == expected_result, "Invalid Result. Expected result is %s" % expected_result

    def rejectRequest(self):
        self.driver.find_element_by_xpath(self.rejectec_button_xpath).click()
        self.driver.find_element_by_xpath(self.rejectReason_xpath).send_keys("Invalid request")
        self.driver.find_element_by_xpath(self.reject1_button_xpath).click()
        self.driver.find_element_by_xpath(self.reject1_button_xpath).click()

    def recheckApprovedStatusNewCard(self):
        hp = Homepage(self.driver)
        ep = ExistingCard(self.driver)
        np = NewCard(self.driver)
        expected_status = "Approved"
        hp.clickviewRequest()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(5)
        status = self.driver.find_element_by_xpath(self.verifyStatus_xpath).text
        assert status == expected_status, "Incorrect status, Expected status is %s" % expected_status

    def recheckApprovedStatusExistingCard(self):
        hp = Homepage(self.driver)
        ExistingCard(self.driver)
        np = NewCard(self.driver)
        expected_status = "Approved"
        hp.clickviewRequest()
        self.driver.find_element_by_xpath(self.filter_textbox_xpath).send_keys(np.jobReqNewCard)
        time.sleep(5)
        status = self.driver.find_element_by_xpath(self.verifyStatus_xpath).text
        assert status == expected_status, "Incorrect status, Expected status is %s" % expected_status
