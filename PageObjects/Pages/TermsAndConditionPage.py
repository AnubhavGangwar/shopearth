from PageObjects.Pages.LogInPopUp import uniqueEmailGenerator
from PageObjects.Utils.CommonMethods import *

ACCOUNT_BUTTON = xpathLocator('(//div[@class="src-components-dropdown-baseDropdownMenu-_styles_label"])[2]')
LOGIN_BUTTON = xpathLocator('//li[text()="Login"]')
EMAIL = xpathLocator('(//input[@type="text"])[3]')


def clickOnAccountButton():
    clickOnTheButton(ACCOUNT_BUTTON)


def clickOnLoginButton():
    clickOnTheButton(LOGIN_BUTTON)


def inputEmail():
    clearTheInputField(EMAIL)
    enterTheInputValue(EMAIL, uniqueEmailGenerator())





