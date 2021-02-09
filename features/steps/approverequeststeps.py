from behave import *
from selenium import webdriver
import unittest
from locators.locators import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'the user browse EZ-Link\'s Portal')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.get("http://10.2.5.36:33000/login")


@when(u'he enter username and password')
def step_impl(context):
    context.driver.find_element_by_name("username").send_keys("zivwang")
    context.driver.find_element_by_name("password").send_keys("Passw0rd2!")
    context.driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()


@then(u'he should be able to login to View All Top Up Requests page')
def step_impl(context):
    context.driver.find_element_by_xpath(utilityTopUp_xpath).click()
    context.driver.find_element_by_xpath(viewTopUpRequest_xpath).click()


@given(u'the user click the filter results for the job order number of new card entered in filter textbox')
def step_impl(context):
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqNewCard)
    time.sleep(5)
    context.driver.find_element_by_xpath(filter_result_xpath).click()

@when(u'he check the job order number, number of cards and top-up amount')
def step_impl(context):
    element = WebDriverWait(context.driver, 2).until(
        EC.presence_of_element_located((By.XPATH, approve_button_xpath))
    )
    element.click()
    context.driver.find_element_by_xpath(approveConfirmation_xpath).click()
   # expected_jobOrder = jobReqNewCard
   # job_order = context.driver.find_element_by_xpath(
   #     "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/b[1]").text
   # no_of_cards = context.driver.find_element_by_xpath(
   #     "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[5]/div[2]/b[1]").text
   # topup_amt = context.driver.find_element_by_xpath(
   #     "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[2]/b[1]").text
   # try:
#    assert job_order == expected_jobOrder.text
   # except AssertionError:
   #     print("Incorrect job order number, expected job order number is %s" % expected_jobOrder)
   # try:
   #     assert no_of_cards == "6"
  #  except AssertionError:
   #     print("Incorrect number of cards, expected number of cards is %s" % no_of_cards)
   # try:
   #     assert topup_amt == "6.00"
   # except AssertionError:
   #     print("Incorrect topup amount, expected topup amount is %s" % topup_amt)
   


@then(u'the successful submission response is displayed once request is submitted')
def step_impl(context):
    expected_result = "Record successfully approved!"
    result = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]").text
    assert result == expected_result, "Invalid result. Expected result is %s" % expected_result
    context.driver.find_element_by_xpath(viewTopUpRequest_xpath).click()


@then(
    u'status will show "Approved" when user search for the job order number of new card entered in the filter textbox')
def step_impl(context):
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqNewCard)
    time.sleep(5)
    expected_status = "Approved"
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "Incorrect status. Expected status is %s" % expected_status


@then(u'eventually status will show "Topup_Completed" upon reloading the page')
def step_impl(context):
    time.sleep(20)
    context.driver.refresh()
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqNewCard)
    time.sleep(5)
    expected_status = "Topup_Completed"
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "Incorrect status, Expected status is %s" % expected_status
    time.sleep(5)
    context.driver.close()


@given(u'the user click the filter results for the job order number of existing card entered in filter textbox')
def step_impl(context):
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqExistCard)
    time.sleep(5)
    context.driver.find_element_by_xpath(filter_result_xpath).click()


@when(u'he check request info of existing card')
def step_impl(context):
    context.driver.find_element_by_xpath(approve_button_xpath).click()
    context.driver.find_element_by_xpath(approveConfirmation_xpath).click()
   # expected_jobOrder = jobReqExistCard
   # job_order = context.driver.find_element_by_xpath(
   #     "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/b[1]").text
   # no_of_cards = context.driver.find_element_by_xpath(
   #     "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[5]/div[2]/b[1]").text
   # topup_amt = context.driver.find_element_by_xpath(
    #    "//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[2]/b[1]").text
   # try:
   #     assert job_order == expected_jobOrder.text
   # except AssertionError:
   #     print("Incorrect job order number, expected job order number is %s" % expected_jobOrder)
   # try:
   #     assert no_of_cards == "4"
   # except AssertionError:
   #     print("Incorrect number of cards, expected number of cards is %s" % no_of_cards)
   # try:
   #     assert topup_amt == "4.00"
   # except AssertionError:
    #    print("Incorrect topup amount, expected topup amount is %s" % topup_amt)


@then(u'the successful response is displayed once request is submitted')
def step_impl(context):
    expected_result = "Record successfully approved!"
    result = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]").text
    assert result == expected_result, "Invalid result. Expected result is %s" % expected_result


@then(
    u'status will show "Approved" when user search for the job order number of existing card entered in the filter textbox')
def step_impl(context):
    context.driver.find_element_by_xpath(viewTopUpRequest_xpath).click()
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqExistCard)
    time.sleep(5)
    expected_status = "Approved"
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "Incorrect status. Expected status is %s" % expected_status


@then(u'eventually status will display "Topup_Completed"')
def step_impl(context):
    time.sleep(20)
    context.driver.refresh()
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqExistCard)
    time.sleep(5)
    expected_status = "Topup_Completed"
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "Incorrect status, Expected status is %s" % expected_status
    time.sleep(5)
    context.driver.close()
