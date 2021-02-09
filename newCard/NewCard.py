import openpyxl
from pageObjects.HomePage import Homepage
import time


class NewCard:
    jobOrder_xpath = "//body/div[@id='wrapper']/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]"
    excelButton_xpath = "//input[@id='img']"
    topup_textbox_xpath = "//input[@id='input-live']"
    calculateAmount_xpath = "//body/div[@id='wrapper']/div[3]/div[1]/div[1]/div[4]/div[1]/button[1]"
    buttonSubmit_xpath = "//body/div[@id='wrapper']/div[3]/div[1]/div[1]/div[4]/div[3]/button[1]"
    excpath = r"C:\Users\lukegoh\Desktop\Python Projects\SoftwareAutomationTesting\newCard\ABT0475EC Card Init Detailed Rpt Test 01 - v13_58.xlsx"
    excsheetName = 'ABT0475EC Card Initialization D'
    jobReqNewCard = "testnc126"
    verifyStatus_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]"
    rownum = 9

    def __init__(self, driver):
        self.driver = driver

    def createReqNewCard(self, expected_price):
        self.driver.find_element_by_xpath(self.jobOrder_xpath).send_keys(self.jobReqNewCard)
        self.driver.find_element_by_xpath(self.excelButton_xpath).send_keys(self.excpath)
        self.driver.find_element_by_xpath(self.topup_textbox_xpath).send_keys("1")
        self.driver.find_element_by_xpath(self.calculateAmount_xpath).click()
        subTotalAmt = self.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]").text
        totalCalAmt = self.driver.find_element_by_xpath("//label[contains(text(),'Total Amount: $6.00')]").text.replace('Total amount: $', '')
        assert float(subTotalAmt) == float(totalCalAmt.split('$')[1]) == expected_price, "Price mismatch! Expected price is %s, subtotal is %s, total price is %s" % (
            expected_price, subTotalAmt, totalCalAmt)
        self.driver.find_element_by_xpath(self.buttonSubmit_xpath).click()
        time.sleep(8)

    def enterJobOrder(self):
        self.driver.find_element_by_xpath(self.jobOrder_xpath).send_keys(self.jobReqNewCard)

    def clickExcel(self):
        self.driver.find_element_by_xpath(self.excelButton_xpath).send_keys(self.excpath)

    def enterTopUpAmt(self):
        self.driver.find_element_by_xpath(self.topup_textbox_xpath).send_keys("1")

    def clickCalulateButton(self):
        self.driver.find_element_by_xpath(self.calculateAmount_xpath).click()

    def checkTopUpInfo(self):
        expected_price=6.00
        subTotalAmt = self.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]").text
        totalCalAmt = self.driver.find_element_by_xpath("//label[contains(text(),'Total Amount: $6.00')]").text.replace('Total amount: $', '')
        assert float(subTotalAmt) == float(totalCalAmt.split('$')[1]) == expected_price, "Price mismatch! Expected price is %s, subtotal is %s, total price is %s" % (
            expected_price, subTotalAmt, totalCalAmt)

    def submitRequest(self):
        self.driver.find_element_by_xpath(self.buttonSubmit_xpath).click()
        time.sleep(8)
        expected_result = "Successfully submitted"
        result = self.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/label[1]").text
        assert result == expected_result, "Incorrect result. Expected result should be %s" % expected_result

    def checkStatus(self):
        hp = Homepage(self.driver)
        expected_status = "Pending"
        hp.clickviewRequest()
        self.driver.find_element_by_xpath("//input[@id='filterInput']").send_keys(self.jobReqNewCard)
        time.sleep(5)
        status = self.driver.find_element_by_xpath(self.verifyStatus_xpath).text
        assert status == expected_status, "Incorrect status, Expected status is %s" %expected_status







    # def deleteRow(self):
    #    workbook = openpyxl.load_workbook(self.excpath)
    #    sheet = workbook.get_sheet_by_name(self.excsheetName)
    #    sheet.delete_rows(self.rownum, 1)
    #    workbook.save(self.excpath)
