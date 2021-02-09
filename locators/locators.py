# Paths for new card
jobOrder_xpath = "//body/div[@id='wrapper']/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]"
excelButton_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/input[1]"
topup_textbox_xpath = "//input[@id='input-live']"
calculateAmount_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]/button[1]"
buttonSubmit_xpath = "//body/div[@id='wrapper']/div[3]/div[1]/div[1]/div[4]/div[3]/button[1]"
excpath = r"C:\Users\lukegoh\Desktop\Python Projects\AutomationTesting\excel\ABT0475EC Card Init Detailed Rpt Test 01 - v13_74.xlsx"
excsheetName = 'ABT0475EC Card Initialization D'
jobReqNewCard = "appNC05"
JobReqNewCard1 = "cancel8"
verifyStatus_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]"

# Paths for existing card
jobOrder_xpath = "//body/div[@id='wrapper']/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]"
excelButton1_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/ul[1]/div[1]/li[1]/input[1]"
calculateAmount1_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[1]/button[1]"
buttonSubmit1_xpath = "//body/div[@id='wrapper']/div[3]/div[1]/div[1]/div[5]/div[3]/button[1]"
excpath1 = r"C:\Users\lukegoh\Desktop\Python Projects\AutomationTesting\excel\Card Profile Top-up w topup valueTest 03_34.xlsx"
excsheetName1 = 'data123'
jobReqExistCard = "appEC05"
verifyStatus_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]"

#Paths for View Request
viewTopUpRequest_xpath = "//a[contains(text(),'View all topup request')]"
filter_textbox_xpath = "//input[@id='filterInput']"
filter_result_xpath = "//table[@id='table']/tbody/tr/td[2]"
approve_button_xpath = "/html/body/div/div[3]/div/div/div[3]/button[1]"
approveConfirmation_xpath = "/html/body/div/div[3]/div/div/div[3]/button[1]"
rejectec_button_xpath = "//button[contains(text(),'Reject')]"
rejectnc_button_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[3]/button[2]"
reject1_button_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[3]/button[1]"
rejectReason_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/textarea[1]"
rejectncReason_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[2]/textarea[1]"
approveVoidReq_button_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[3]/button[1]"
approveVoidReqConfirm_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[3]/button[1]"
before_xpath = "//table[@id='table']/tbody/tr["
after_xpath = "]/td[2]/div[1]"
verifyStatus_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]"

#Paths for Void Request
filter_textbox_xpath = "//input[@id='filterInput']"
filter_result_xpath = "//tbody/tr[1]/td[2]"
approve_button_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[3]/button[1]"
approveConfirmation_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[3]/button[1]"
cancelRequest_button_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[4]/button[1]"
cancelRequest_reason_xpath = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
submitReason_xpath = "//button[contains(text(),'Submit')]"
submitReasonConfirmation_xpath = "//body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]"
closeReason_xpath = "/html/body/div[2]/div[1]/div/div/header/button"
verifyStatus_xpath = "//body[1]/div[1]/div[3]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/div[1]"

#Sub-menu paths
utilityTopUp_xpath = "//div[@id='wrapper']/div/ul/li[8]/a"
reqNewCard_xpath = "//a[contains(text(),'create top up request (new card)')]"
reqExistingCard_xpath = "//a[contains(text(),'Create top up request (existing card)')]"
viewTopUpRequest_xpath = "//a[contains(text(),'View all topup request')]"
viewVoidRequest_xpath = "//body[1]/div[1]/div[1]/div[1]/ul[1]/li[5]/a[1]"

