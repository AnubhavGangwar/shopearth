from PageObjects.Utils.CommonMethods import *

ACCOUNT_BUTTON = cssSelector('.src-styles-_iconFonts_icon.src-styles-_iconFonts_icon_profile.src-components-header-_styles_icon-style')
LOGIN_BUTTON = cssSelector('div.src-components-header-_styles_header-container li:nth-child(6)')


def clickOnAccountButton():
    if isElementPresent(ACCOUNT_BUTTON):
        clickOnTheButton(ACCOUNT_BUTTON)
    else:
        print(str(ACCOUNT_BUTTON) + "element is not located.")


def clickOnLoginButton():
    if isElementPresent(LOGIN_BUTTON):
        clickOnTheButton(LOGIN_BUTTON)
    else:
        print(str(LOGIN_BUTTON) + "element is not located.")

