import unittest

from behave import *
from selenium import webdriver
from locators.locators import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'the user search for EZ-Link\'s Portal')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.get("http://10.2.5.36:33000/login")


@when(u'he enter login credentials')
def step_impl(context):
    context.driver.find_element_by_name("username").send_keys("zivwang")
    context.driver.find_element_by_name("password").send_keys("Passw0rd2!")
    context.driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()

@then(u'he should be able to access View All Top Up Requests page')
def step_impl(context):
    context.driver.find_element_by_xpath(utilityTopUp_xpath).click()
    context.driver.find_element_by_xpath(viewTopUpRequest_xpath).click()


@given(u'the user click the filter results for the job order number of new card')
def step_impl(context):
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqNewCard)
    time.sleep(5)
    context.driver.find_element_by_xpath(filter_result_xpath).click()


@when(u'he check top-up information')
def step_impl(context):
    context.driver.find_element_by_xpath(rejectnc_button_xpath).click()


@when(u'reject the request with valid reason')
def step_impl(context):
    context.driver.find_element_by_xpath(rejectncReason_xpath).send_keys("Invalid Request")


@then(u'result will show success message')
def step_impl(context):
    expected_response = "Record successfully rejected!"
    context.driver.find_element_by_xpath(reject1_button_xpath).click()
    context.driver.find_element_by_xpath(reject1_button_xpath).click()
    response = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]").text
    assert response == expected_response, "Invalid response, Expected response is %s" % expected_response



@then(u'status will show "Returned" when user search for the job order number of new card entered in the filter textbox')
def step_impl(context):
    expected_status = "Returned"
    context.driver.find_element_by_xpath(viewTopUpRequest_xpath).click()
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqNewCard)
    time.sleep(5)
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "invalid status, Expected status is %s" %expected_status
    context.driver.close()


@given(u'the user click the filter results for the job order number of existing card')
def step_impl(context):
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqExistCard)
    time.sleep(5)
    context.driver.find_element_by_xpath(filter_result_xpath).click()


@when(u'he check top-up request information')
def step_impl(context):
    context.driver.find_element_by_xpath(rejectec_button_xpath).click()
    # expected_jobOrder = jobReqNewCard
    # card_quantity = "6"
    # total_amt = 6.00
    # job_order = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/b[1]").text
    # no_of_cards = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[5]/div[2]/b[1]").text
    # topup_amt = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[2]/b[1]").text
    # assert job_order == expected_jobOrder, "Incorrect job order number, expected job order number is %s" %expected_jobOrder
    # assert no_of_cards == card_quantity, "Incorrect number of cards, expected number of cards is %s" %card_quantity
    # assert float(topup_amt) == total_amt, "Incorrect topup amount, expected topup amount is %s" %total_amt


@when(u'reject the request with proper reason')
def step_impl(context):
    context.driver.find_element_by_xpath(rejectec_button_xpath).send_keys("Invalid Request")


@then(u'submission will be successful')
def step_impl(context):
    expected_response = "Record successfully rejected!"
    context.driver.find_element_by_xpath(reject1_button_xpath).click()
    context.driver.find_element_by_xpath(reject1_button_xpath).click()
    response = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]").text
    assert response == expected_response, "Invalid response, Expected response is %s" % expected_response



@then(u'status will show "Returned" when user search for the job order number of existing card entered in the filter textbox')
def step_impl(context):
    expected_status = "Returned"
    context.driver.find_element_by_xpath(viewTopUpRequest_xpath).click()
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqExistCard)
    time.sleep(5)
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "invalid status, Expected status is %s" %expected_status
    context.driver.close()
