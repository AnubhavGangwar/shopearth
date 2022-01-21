from PageObjects.Utils.CommonMethods import *


EMAIL = cssSelector('#EmailInput')
PASSWORD = cssSelector('[id="inputPassword1"]')
SUBMIT_BUTTON = cssSelector('button[type="submit"]')


def setUserEmail(email):
    if isElementPresent(EMAIL):
        clearTheInputField(EMAIL)
        enterTheInputValue(EMAIL, email)
    else:
        print(str(EMAIL) + "is not present on Screen.")


def setUserPassword(password):
    if isElementPresent(PASSWORD):
        clearTheInputField(PASSWORD)
        enterTheInputValue(PASSWORD, password)
    else:
        print(str(PASSWORD) + "is not found on Screen.")


def clickOnSubmitButton():
    if isElementPresent(SUBMIT_BUTTON):
        clickOnTheButton(SUBMIT_BUTTON)
    else:
        allure.attach()
        print(str(SUBMIT_BUTTON) + "is not found on the Screen.")
