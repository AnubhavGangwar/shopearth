from PageObjects.Utils.CommonMethods import *

WEDDING = cssSelector('.src-containers-myAccount-components-Bridal-_styles_active')
PROCEED_BUTTON = cssSelector('[value="PROCEED TO SET THE DATE"]')
ENTER_DATE = cssSelector('[placeholder="DD/MM/YYYY"]')
PROCEED_TO_FILL_DETAILS_BUTTON = cssSelector('[value="PROCEED TO FILL DETAILS"]')
REGISTRANTS_NAME = cssSelector('[name="registrantName"]')
CO_REGISTRANT_NAME = cssSelector('[name="coRegistrantName"]')
REGISTRY_NAME = cssSelector('[name="registryName"]')
PROCEED_TO_FILL_ADDRESS_FORM = cssSelector('[value="Proceed to add shipping details"]')


def clickOnWeddingButton():
    if isElementPresent(WEDDING):
        clickOnTheButton(WEDDING)
    else:
        print(str(WEDDING) + "element is not located.")


def clickOnProceedToStartButton():
    if isElementPresent(PROCEED_BUTTON):
        clickOnTheButton(PROCEED_BUTTON)
    else:
        print(str(PROCEED_BUTTON) + "element is not located.")


def passTheDate():
    if isElementPresent(ENTER_DATE):
        passPresentDate(ENTER_DATE)
    else:
        print(str(ENTER_DATE) + "element is not located.")


def clickOnProceedToFillDetails():
    if isElementPresent(PROCEED_TO_FILL_DETAILS_BUTTON):
        clickOnTheButton(PROCEED_TO_FILL_DETAILS_BUTTON)
    else:
        print(str(PROCEED_TO_FILL_DETAILS_BUTTON) + "element is not located.")


def inputTheRegistrantsName(name):
    if isElementPresent(REGISTRANTS_NAME):
        enterTheInputValue(REGISTRANTS_NAME, name)
    else:
        print(str(REGISTRANTS_NAME) + "element is not located.")


def inputCoRegistrantName(co_regName):
    if isElementPresent(CO_REGISTRANT_NAME):
        enterTheInputValue(CO_REGISTRANT_NAME, co_regName)
    else:
        print(str(CO_REGISTRANT_NAME) + "element is not located.")


def clickOnProceedToFillAddressForm():
    if isElementPresent(PROCEED_TO_FILL_ADDRESS_FORM):
        clickOnTheButton(PROCEED_TO_FILL_ADDRESS_FORM)
    else:
        print(str(PROCEED_TO_FILL_ADDRESS_FORM) + "element is not located.")
