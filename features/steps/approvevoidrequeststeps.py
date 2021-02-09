from behave import *
from selenium import webdriver
from locators.locators import *
import time


@given(u'the user search for job order number in filter textbox')
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
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqNewCard)
    time.sleep(5)


@when(u'he click the filter result')
def step_impl(context):
    context.driver.find_element_by_xpath(filter_result_xpath).click()


@when(u'submit void request')
def step_impl(context):
    context.driver.find_element_by_xpath(approveVoidReq_button_xpath).click()
    context.driver.find_element_by_xpath(approveConfirmation_xpath).click()


@then(u'successful submission response should be displayed on the page')
def step_impl(context):
    expected_status = "Successfully submitted"
    status = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[6]/label[1]").text
    assert status == expected_status, "Invalid status, expected status is %s" % expected_status


@then(u'status should display "Pending" in void request page')
def step_impl(context):
    context.driver.find_element_by_xpath(viewVoidRequest_xpath).click()
    expected_status = "Pending"
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "Invalid status,expected status is %s" %expected_status


@given(u'the user search for job order number in filter textbox in void request page')
def step_impl(context):
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqNewCard)
    time.sleep(5)
    context.driver.find_element_by_xpath(verifyStatus_xpath).click()


@when(u'check the request information(top-up amount, job order number and number of cards)')
def step_impl(context):
   # job_Order = jobReqNewCard
   # card_quantity = "6"
    total_amt = 6
    subtotal = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]").text
  #  job_order = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/label[2]/b[1]").text
  #  no_of_cards = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]").text
    topup_amt = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[2]/label[1]").text.replace('Total amount: $', '')
   # assert job_order == job_Order, "Incorrect job order number, expected job order number is %s" % job_order
   # assert card_quantity == no_of_cards, "Incorrect number of cards, expected number of cards is %s" % no_of_cards
    assert total_amt == int(topup_amt.split('$')[1]) == int(subtotal), "Price mismatch! Expected price is %s, total price is %s, subtotal is %s" % (total_amt, topup_amt, subtotal)


@then(u'result should display successful submission response')
def step_impl(context):
   context.driver.find_element_by_xpath(approve_button_xpath).click()
   context.driver.find_element_by_xpath(approveConfirmation_xpath).click()
   expected_result = "Successfully submitted"
   result = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[6]/label[1]").text
   assert result == expected_result, "Invalid result. Expected result is %s" %expected_result


@then(u'the filtered result for job order number entered in the filter textbox should have status "Approved"')
def step_impl(context):
    context.driver.find_element_by_xpath(viewVoidRequest_xpath).click()
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqNewCard)
    time.sleep(5)
    expected_status = "Approved"
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "Incorrect status. Expected status is %s" % expected_status


@then(u'status display "void_topup_incomplete" in the view void request page')
def step_impl(context):
    time.sleep(20)
    context.driver.refresh()
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqNewCard)
    time.sleep(5)
    expected_status = "void_topup_incomplete"
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "Incorrect status. Expected status is %s" % expected_status
    time.sleep(5)

@then(u'status also display "Voided" in view all request webpage')
def step_impl(context):
    context.driver.find_element_by_xpath(utilityTopUp_xpath).click()
    context.driver.find_element_by_xpath(viewTopUpRequest_xpath).click()
    context.driver.find_element_by_xpath(filter_textbox_xpath).send_keys(jobReqNewCard)
    time.sleep(5)
    expected_status = "Voided"
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "Incorrect status. Expected status is %s" % expected_status
    time.sleep(5)
    context.driver.close()

