import random
from PageObjects.Utils.CommonMethods import *
from PageObjects.Utils.TestData import TestData

ENTER_EMAIL = xpathLocator('(//input[@type="text"])[3]')
CONTINUE_BUTTON = cssSelector('[value="continue"]')
FIRST_NAME = cssSelector('[name="firstName"]')
LAST_NAME = cssSelector('[name="lastName"]')
GENDER = cssSelector('[name="gender"]')
MALE_GENDER = cssSelector('[value="Male"]')
DATE_OF_BIRTH = cssSelector('[name="dateOfBirth"]')
COUNTRY = cssSelector('[name="country"]')
INDIA_COUNTRY = cssSelector('[value="India"]')
STATE = cssSelector('[name="state"]')
SELECT_STATE = cssSelector('[value="Uttar Pradesh"]')
PHONE_NUMBER = cssSelector('[name="phone"]')
PASSWORD = cssSelector('[name="password1"]')
CONFIRM_PASSWORD = cssSelector('[name="password2"]')
AGREE_TERMS = xpathLocator('//label[text() = "I agree to the "]')
# AGREE_TERMS = ".src-components-signin-_styles_subscribe>label'),':before'"
AGREE_RECEIVE_EMAILS = cssSelector('label[for="subscrib"]')
ENTER_EXISTING_PASSWORD = xpathLocator('//input[@type="password"]')
GOOGLE_BUTTON1 = cssSelector('div.src-styles-_global_voffset3:nth-of-type(2) img.src-components-signin-socialLogin-_styles_social-login')


def uniqueEmailGenerator():
    value = random.randint(1, 100)
    email = TestData.USERNAME + "+" + str(value) + "@gmail.com"
    print(email)
    return email


def enterTheStoredEmail():
    if isElementPresent(ENTER_EMAIL):
        clearTheInputField(ENTER_EMAIL)
        enterTheInputValue(ENTER_EMAIL, uniqueEmailGenerator())
    else:
        print(str(ENTER_EMAIL) + "element is not located.")


def generateRandomMobileNumber():
    number = "9291" + str(random.randint(123334, 999999))
    return number


def enterTheStoredPhoneNumber():
    if isElementPresent(PHONE_NUMBER):
        enterTheInputValue(PHONE_NUMBER, generateRandomMobileNumber())
    else:
        print(str(PHONE_NUMBER) + "element is not located.")


def clickOnContinueButton():
    if isElementPresent(CONTINUE_BUTTON):
        clickOnTheButton(CONTINUE_BUTTON)
    else:
        print(str(CONTINUE_BUTTON) + "element is not located.")


def inputFirstName(fName):
    if isElementPresent(FIRST_NAME):
        clearTheInputField(FIRST_NAME)
        enterTheInputValue(FIRST_NAME, fName)
    else:
        print(str(FIRST_NAME) + "element is not located.")


def inputLastName(lName):
    if isElementPresent(lName):
        clearTheInputField(LAST_NAME)
        enterTheInputValue(LAST_NAME, lName)
    else:
        print(str(LAST_NAME) + "element is not located.")


def selectGender():
    if isElementPresent(GENDER):
        clickOnTheButton(GENDER)
        if isElementPresent(MALE_GENDER):
            clickOnTheButton(MALE_GENDER)
        else:
            print(str(MALE_GENDER) + "element is not Located")
    else:
        print(str(GENDER) + "element is not located")


def inputDateOfBirth(DOB):
    if isElementPresent(DATE_OF_BIRTH):
        clearTheInputField(DATE_OF_BIRTH)
        enterTheInputValue(DATE_OF_BIRTH, DOB)
    else:
        print(str(DATE_OF_BIRTH) + "element is not located")


def selectIndiaCountry():
    if isElementPresent(COUNTRY):
        clickOnTheButton(COUNTRY)
        if isElementPresent(INDIA_COUNTRY):
            clickOnTheButton(INDIA_COUNTRY)
        else:
            print(str(INDIA_COUNTRY) + "element is not Located")
    else:
        print(str(INDIA_COUNTRY) + "element is not located")


def selectStateName():
    if isElementPresent(STATE):
        clickOnTheButton(STATE)
        if isElementPresent(SELECT_STATE):
            clickOnTheButton(SELECT_STATE)
        else:
            print(str(SELECT_STATE) + "element is not Located")
    else:
        print(str(STATE) + "element is not located")


def inputMobileNumber():
    if isElementPresent(PHONE_NUMBER):
        clearTheInputField(PHONE_NUMBER)
        enterTheInputValue(PHONE_NUMBER, enterTheStoredPhoneNumber())
    else:
        print(str(PHONE_NUMBER) + "element is not located.")


def inputPassword(password):
    if isElementPresent(PASSWORD):
        clearTheInputField(PASSWORD)
        enterTheInputValue(PASSWORD, password)
    else:
        print(str(PASSWORD) + "element is not located.")


def inputConfirmPassword(confPassword):
    if isElementPresent(CONFIRM_PASSWORD):
        clearTheInputField(CONFIRM_PASSWORD)
        enterTheInputValue(CONFIRM_PASSWORD, confPassword)
    else:
        print(str(CONFIRM_PASSWORD) + "element is not located.")


def agreeTerms():
    # javaScriptExecutorClick(AGREE_TERMS)

    clickOnTheButton(CONFIRM_PASSWORD)
    useTabKeys()
    useSpaceKeys()
    useSpaceKeys()
    # clickOnTheButton(AGREE_TERMS)
    # clickByUsingEnterKey(AGREE_TERMS)


def agreeReceiveEmail():
    if isElementPresent(AGREE_RECEIVE_EMAILS):
        clickOnTheButton(AGREE_RECEIVE_EMAILS)
    else:
        print(str(AGREE_RECEIVE_EMAILS) + "element is not located.")


def clickOnContinueButtonAgain():
    if isElementPresent(CONTINUE_BUTTON):
        clickOnTheButton(CONTINUE_BUTTON)
        expectedAssertion()
    else:
        print(str(CONTINUE_BUTTON) + "element is not located.")


def switchBackToDefaultWindow():
    time.sleep(20)
    closeNewBrowserTab()


def expectedAssertion():
    if isElementPresent('[alt="goodearth-logo"]'):
        isElementPresent('[alt="goodearth-logo"]')
    else:
        closeBrowser()


def enterExistingEmailAccount(existgEmail):
    if isElementPresent(ENTER_EMAIL):
        clearTheInputField(ENTER_EMAIL)
        enterTheInputValue(ENTER_EMAIL, existgEmail)
    else:
        print(str(ENTER_EMAIL) + "element is not located.")


def inputExistingPassword(existgPassword):
    if isElementPresent(ENTER_EXISTING_PASSWORD):
        clearTheInputField(ENTER_EXISTING_PASSWORD)
        enterTheInputValue(ENTER_EXISTING_PASSWORD, existgPassword)
    else:
        print(str(ENTER_EXISTING_PASSWORD) + "element is not located.")


def clickOnGoogleLogin():
    if isElementPresent(GOOGLE_BUTTON1):
        clickOnTheButton(GOOGLE_BUTTON1)
    else:
        print(str(GOOGLE_BUTTON1) + "element is not located.")

