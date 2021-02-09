from behave import *
from selenium import webdriver
from locators.locators import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'the user access EZ-Link\'s Portal')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.get("http://10.2.5.36:33000/login")


@when(u'he enter login information')
def step_impl(context):
    context.driver.find_element_by_name("username").send_keys("zivwang")
    context.driver.find_element_by_name("password").send_keys("Passw0rd2!")
    context.driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()


@then(u'he should be able to login to Utility Top Up navigation menu')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@id='wrapper']/div/ul/li[8]/a").click()


@given(u'the user click on create top up (new card) request navigation menu')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'create top up request (new card)')]").click()


@when(u'he enter job order number and top up amount in the request page')
def step_impl(context):
    context.driver.find_element_by_xpath(jobOrder_xpath).send_keys(jobReqNewCard)
    element = WebDriverWait(context.driver, 2).until(
        EC.presence_of_element_located((By.XPATH, excelButton_xpath))
    )
    element.send_keys(excpath)
    context.driver.find_element_by_xpath(topup_textbox_xpath).send_keys("1")


@when(u'check the total top-up amount')
def step_impl(context):
    expected_price = 6.00
    context.driver.find_element_by_xpath(calculateAmount_xpath).click()
    subTotalAmt = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[4]/div[1]").text
    totalCalAmt = context.driver.find_element_by_xpath("//label[contains(text(),'Total Amount: $6.00')]").text.replace('Total amount: $', '')
    assert float(subTotalAmt) == float(totalCalAmt.split('$')[1]) == expected_price, "Price mismatch! Expected price is %s, subtotal is %s, total price is %s" % (expected_price, subTotalAmt, totalCalAmt)


@then(u'the successful submission response is displayed once request is submitted for new card')
def step_impl(context):
    context.driver.find_element_by_xpath(buttonSubmit_xpath).click()
    time.sleep(5)
    expected_result = "Successfully submitted"
    result = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/label[1]").text
    assert result == expected_result, "Incorrect result. Expected result should be %s" % expected_result
    context.driver.find_element_by_xpath(viewTopUpRequest_xpath).click()


@then(u'status should display "Pending" once he key in the new card job order number in the View Top Up Request page')
def step_impl(context):
    expected_status = "Pending"
    context.driver.find_element_by_xpath("//input[@id='filterInput']").send_keys(jobReqNewCard)
    time.sleep(5)
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "Incorrect status, Expected status is %s" % expected_status
    time.sleep(5)
    context.driver.close()


@given(u'the user click on create top up (existing card) request navigation menu')
def step_impl(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'Create top up request (existing card)')]").click()


@when(u'he enter job order number in the request page')
def step_impl(context):
    context.driver.find_element_by_xpath(jobOrder_xpath).send_keys(jobReqExistCard)
    element = WebDriverWait(context.driver, 2).until(
        EC.presence_of_element_located((By.XPATH, excelButton1_xpath))
    )
    element.send_keys(excpath1)


@when(u'check the total topup amount')
def step_impl(context):
    expected_price = 4.00
    context.driver.find_element_by_xpath(calculateAmount1_xpath).click()
    subTotalAmt = context.driver.find_element_by_xpath("//*[@id='table']/tbody/tr/td[5]/div").text
    totalCalAmt = context.driver.find_element_by_xpath("//*[@id='wrapper']/div[3]/div/div/div[5]/div[2]/label").text.replace('Total amount: $', '')
    assert float(subTotalAmt) == float(totalCalAmt.split('$')[1]) == expected_price, "Price mismatch! Expected price is %s, subtotal is %s, total price is %s" % (expected_price, subTotalAmt, totalCalAmt)


@then(u'the successful submission response is displayed once request is submitted for existing card')
def step_impl(context):
    context.driver.find_element_by_xpath(buttonSubmit1_xpath).click()
    time.sleep(5)
    expected_result = "Successfully submitted"
    result = context.driver.find_element_by_xpath("//body[1]/div[1]/div[3]/div[1]/div[1]/div[6]/label[1]").text
    assert result == expected_result, "Incorrect result. Expected result should be %s" % expected_result
    context.driver.find_element_by_xpath(viewTopUpRequest_xpath).click()


@then(u'status should display "Pending" once he key in the existing card job order number in the View Top Up Request '
      u'page>')
def step_impl(context):
    expected_status = "Pending"
    context.driver.find_element_by_xpath("//input[@id='filterInput']").send_keys(jobReqExistCard)
    time.sleep(5)
    status = context.driver.find_element_by_xpath(verifyStatus_xpath).text
    assert status == expected_status, "Incorrect status, Expected status is %s" % expected_status
    time.sleep(5)
    context.driver.close()

