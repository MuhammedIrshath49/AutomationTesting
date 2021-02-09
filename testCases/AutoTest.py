import unittest
import HtmlTestRunner
from selenium import webdriver
import pytest
import allure
import sys
import time

sys.path.append("C:\Users\lukegoh\Desktop\Python Projects\SoftwareAutomationTesting")
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import Homepage
from newCard.NewCard import NewCard
from existingCard.ExistingCard import ExistingCard
from viewRequest.viewRequest import ViewRequest
from viewVoidRequest.viewVoidRequest import ViewVoidRequest


class AutoTest(unittest.TestCase):
    baseURL = "http://10.2.5.36:33000/login"
    username = "zivwang"
    password = "Passw0rd2!"
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @unittest.skip("Not testing Existing Card at the moment")
    def test_existingcard(self):
        lp = LoginPage(self.driver)
        hp = Homepage(self.driver)
        ep = ExistingCard(self.driver)
        vp = ViewRequest(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        hp.clickutil()
        hp.clickreqExistingCard()
        ep.createReqExistingCard(expected_price=4.00)
        hp.clickviewRequest()
        # vp.approveReqExistingCard(expected_status="Topup_Completed")
        vp.rejectReqExistingCard(expected_status="Returned")

    @unittest.skip("not testing for new card")
    def test_newcard(self):
        lp = LoginPage(self.driver)
        hp = Homepage(self.driver)
        np = NewCard(self.driver)
        vp = ViewRequest(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        hp.clickutil()
        hp.clickreqNewCard()
        np.createReqNewCard(expected_price=6.00)
        hp.clickviewRequest()
        # vp.approveReqNewCard(expected_status="Topup_Completed")
        vp.rejectReqNewCard(expected_status="Returned")

    # @unittest.skip("Not testing creating request for new card and voiding it")
    def test_voidnewcard(self):  # This is scenario 1- to create request for new card in tandem with voiding request
        lp = LoginPage(self.driver)
        hp = Homepage(self.driver)
        np = NewCard(self.driver)
        vp = ViewRequest(self.driver)
        vvp = ViewVoidRequest(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        hp.clickutil()
        hp.clickreqNewCard()
        np.createReqNewCard(expected_price=6.00)
        hp.clickviewRequest()
        vp.approveReqNewCard(expected_status="Topup_Completed")
        vp.createVoidReq()
        hp.clickutil()
        hp.clickviewVoidRequest()
        vvp.approveVoidReq(expected_status1="void_topup_incomplete", expected_status2="Voided")
        # vvp.rejectVoidReq(expected_status3="Cancelled")

    @unittest.skip("Not testing view request")
    def test_viewRequest(self):  # To view top up requests
        lp = LoginPage(self.driver)
        hp = Homepage(self.driver)
        vp = ViewRequest(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        hp.clickutil()
        hp.clickviewRequest()
        vp.viewTopUpRequest(rownum=10)

    @unittest.skip("Not testing view void request")
    def test_viewVoidRequest(self):  # To view void top up requests(only applicable to new card)
        lp = LoginPage(self.driver)
        hp = Homepage(self.driver)
        vvp = ViewVoidRequest(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        hp.clickutil()
        hp.clickviewVoidRequest()
        vvp.viewVoidRequest()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")

if __name__ == '__main__':
       unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
       output='C:/Users/lukegoh/Desktop/Python Projects/SoftwareAutomationTesting/reports'))
