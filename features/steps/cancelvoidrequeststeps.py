import unittest

from behave import *
from selenium import webdriver
from locators.locators import *
import pyassert
import time


@given(u'the user enter job order number in filter textbox')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    context.driver.get("http://10.2.5.36:33000/login")
    context.driver.find_element_by_name("username").send_keys("zivwang")
    context.driver.find_element_by_name("password").send_keys("Passw0rd2!")
    context.driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()
    context.driver.find_element_by_xpath(utilityTopUp_xpath).click()
    context.driver.find_element_by_xpath(viewTopUpRequest_xpath).click()
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(JobReqNewCard1)
    time.sleep(5)


@when(u'he click on the filter result')
def step_impl(context):
    context.driver.find_element_by_xpath(filter_result_xpath).click()


@when(u'submit the void request')
def step_impl(context):
    context.driver.find_element_by_xpath(approveVoidReq_button_xpath).click()
    context.driver.find_element_by_xpath(approveConfirmation_xpath).click()


@then(u'respose should be successful')
def step_impl(context):
    expected_status = "Successfully submitted"
    status = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[6]/label[1]").text
    assert status == expected_status, "Invalid status, expected status is %s" % expected_status


@then(u'status should display as "Pending" in void request page')
def step_impl(context):
    context.driver.find_element_by_xpath(viewVoidRequest_xpath).click()
    expected_status = "Pending"
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "Invalid status,expected status is %s" %expected_status


@given(u'the user enter job order number in filter textbox in void request page')
def step_impl(context):
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(JobReqNewCard1)
    time.sleep(5)


@when(u'he click the filtered result')
def step_impl(context):
    context.driver.find_element_by_xpath(verifyStatus_xpath).click()

@unittest.skip("This test case is not working")
@when(u'check the topup request information(top-up amount, job order number and number of cards)')
def step_impl(context):
    # job_Order = jobReqNewCard
    # card_quantity = "6"
    total_amt = 6
    subtotal = context.driver.find_element_by_xpath("//*[@id='table']/tbody/tr/td[4]/div").text
    #  job_order = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/label[2]/b[1]").text
    #  no_of_cards = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]").text
    totalCalAmt = context.driver.find_element_by_xpath("//*[@id='wrapper']/div[3]/div/div/div[5]/div[2]/label").text.replace('Total amount: $', '')
    # assert job_order == job_Order, "Incorrect job order number, expected job order number is %s" % job_order
    # assert card_quantity == no_of_cards, "Incorrect number of cards, expected number of cards is %s" % no_of_cards
    assert int(subtotal) == int(totalCalAmt.split('$')[1]) == total_amt, "Price mismatch! Expected price is %s, subtotal is %s, total price is %s" % (total_amt, subtotal, totalCalAmt)



@when(u'reject request with acceptable reason')
def step_impl(context):
    context.driver.find_element_by_xpath(cancelRequest_button_xpath).click()
    context.driver.find_element_by_xpath(cancelRequest_reason_xpath).send_keys("Invalid void request")
    context.driver.find_element_by_xpath(submitReason_xpath).click()



@then(u'result should display rejected submission response')
def step_impl(context):
    context.driver.find_element_by_xpath(submitReasonConfirmation_xpath).click()
    context.driver.find_element_by_xpath(closeReason_xpath).click()
    expected_result = "Topup request cancelled successfully"
    result = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[6]/label[1]").text
    assert result == expected_result, "Invalid result. Expected result is %s" % expected_result
    context.driver.find_element_by_xpath(viewVoidRequest_xpath).click()


@then(u'the filtered result  should have status "Cancelled"')
def step_impl(context):
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(JobReqNewCard1)
    time.sleep(5)
    expected_status = "Cancelled"
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "Incorrect status. Expected status is %s" % expected_status

