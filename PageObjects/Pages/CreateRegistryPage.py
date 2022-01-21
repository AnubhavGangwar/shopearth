from PageObjects.Utils.CommonMethods import *

CREATE_REGISTRY_PAGE = xpathLocator('//div[text()="1. Create a registry"]')
RING_ICON_BUTTON = xpathLocator('//ul[@class="src-containers-myAccount-components-Bridal-_styles_icons src-containers-myAccount-components-Bridal-_styles_bridalicon-pdp"]//li[1]//*[name()="svg"]')
PROCEED_TO_SET_THE_DATE_BUTTON = cssSelector('[value="PROCEED TO SET THE DATE"]')
PROCEED_BUTTON = cssSelector('[class="src-containers-myAccount-components-Bridal-_styles_arrow-down"]')
SET_THE_DATE_PAGE = xpathLocator('//div[text()="2. SET THE DATE"]')
DATE = cssSelector('input[placeholder="DD/MM/YYYY"]')
PROCEED_TO_FILL_DETAILS_BUTTON = cssSelector('[value="PROCEED TO FILL DETAILS"]')



def createRegistryPage():
    if isElementPresent(CREATE_REGISTRY_PAGE):
        print(str(CREATE_REGISTRY_PAGE) + "Element is Located")
    else:
        raise Exception(str(CREATE_REGISTRY_PAGE) + "element is not located.")


def clickOnRingIconButton():
    if isElementPresent(RING_ICON_BUTTON):
        if isElementPresent(PROCEED_TO_SET_THE_DATE_BUTTON.is_enabled()):
            raise Exception(str(PROCEED_TO_SET_THE_DATE_BUTTON) + "element is not disabled initially.")
        else:
            clickOnTheButton(RING_ICON_BUTTON)
    else:
        raise Exception(str(CREATE_REGISTRY_PAGE) + "element is not located.")


def clickOnProceedToSetDateButton():
    if isElementPresent(PROCEED_TO_SET_THE_DATE_BUTTON.is_enable()):
        clickOnTheButton(PROCEED_TO_SET_THE_DATE_BUTTON)
    else:
        raise Exception(str(PROCEED_TO_SET_THE_DATE_BUTTON) + "element is not in enabled state.")


def enterSetTheDate(date):
    if isElementPresent(SET_THE_DATE_PAGE):
        if isElementPresent(PROCEED_TO_FILL_DETAILS_BUTTON.is_enabled()):
            raise Exception(str(PROCEED_TO_FILL_DETAILS_BUTTON + "element is not disabled initially."))
        else:
            clearTheInputField(DATE)
            enterTheInputValue(date)
    else:
        raise Exception(str(SET_THE_DATE_PAGE) + "element is not located.")


def clikOnProceed


