from PageObjects.Utils.CommonMethods import *

ENTER_EMAIL = cssSelector('[name="identifier"]')
SIGNIN_PAGE = cssSelector('[class="kHn9Lb"]')
ENTER_PASSWORD = cssSelector('[name="password"]')
NEXT_BUTTON = xpathLocator('(//div[@class="VfPpkd-RLmnJb"])[1]')
NEXT_BUTTON_2 = xpathLocator('(//span[@class="VfPpkd-vQzf8d"])[1]')


def enterGoogleEmail(email):
    if isElementPresent(SIGNIN_PAGE):
        if isElementPresent(ENTER_EMAIL):
            clearTheInputField(ENTER_EMAIL)
            enterTheInputValue(ENTER_EMAIL, email)
        else:
            print(str(ENTER_EMAIL) + "element is not located.")
    else:
        print(str(SIGNIN_PAGE) + "element is not located.")


def enterGooglePassword(password):
    if isElementPresent(SIGNIN_PAGE):
        if isElementPresent(ENTER_PASSWORD):
            clearTheInputField(ENTER_PASSWORD)
            enterTheInputValue(ENTER_PASSWORD, password)
        else:
            print(str(ENTER_PASSWORD) + "element is not located.")
    else:
        print(str(SIGNIN_PAGE) + "element is not located.")


def clickOnNextButton():
    if isElementPresent(NEXT_BUTTON):
        clickOnTheButton(NEXT_BUTTON)
    else:
        print(str(NEXT_BUTTON) + "element is not located.")


def clickOnNextButton2():
    if isElementPresent(NEXT_BUTTON_2):
        clickOnTheButton(NEXT_BUTTON_2)
    else:
        print(str(NEXT_BUTTON_2) + "element is not located.")







