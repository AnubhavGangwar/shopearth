from PageObjects.Utils.CommonMethods import *

MY_PROFILE = cssSelector('[class="src-containers-myAccount-components-_styles_form-heading"]')
MY_ACCOUNT = cssSelector('[class="src-containers-myAccount-_styles_heading src-styles-_global_vertical-middle"]')
GOOD_EARTH_REGISTRY_TAB = cssSelector('[class="src-containers-myAccount-_styles_bridalleftsec src-containers-myAccount-_styles_bridalplus"]')
CREATE_REGISTRY = xpathLocator('//a[text()="Create a Registry"]')
GOOD_EARTH_REGISTRY_POLICY = xpathLocator('//a[text()="Good Earth Registry Policy"]')


def verifyGoodEarthRegistryTab():
    if isElementPresent(MY_PROFILE):
        print(str(MY_PROFILE) + "element is located.")
        if isElementPresent(MY_ACCOUNT):
            isElementPresent(GOOD_EARTH_REGISTRY_TAB)
        else:
            raise Exception(str(GOOD_EARTH_REGISTRY_TAB) + "element is not located.")
    else:
        print(str(MY_PROFILE) + "element is not located.")


def clickOnGoodEarthRegistryTabAndVerify():
    if isElementPresent(GOOD_EARTH_REGISTRY_TAB):
        clickOnTheButton(GOOD_EARTH_REGISTRY_TAB)
        if isElementPresent(CREATE_REGISTRY):
            isElementPresent(GOOD_EARTH_REGISTRY_POLICY)
        else:
            print(str(CREATE_REGISTRY) + "element is not located." and str(GOOD_EARTH_REGISTRY_POLICY) + "element is not located.")
    else:
        print(str(GOOD_EARTH_REGISTRY_TAB) + "element is not located.")


def clickOnCreateRegistryTab():
    if isElementPresent(CREATE_REGISTRY):
        clickOnTheButton(CREATE_REGISTRY)
    else:
        print(str(CREATE_REGISTRY) + "element is not located.")


def clickOnGoodEarthRegistryPolicy():
    if isElementPresent(GOOD_EARTH_REGISTRY_POLICY):
        clickOnTheButton(GOOD_EARTH_REGISTRY_POLICY)
    else:
        print(str(GOOD_EARTH_REGISTRY_POLICY) + "element is not located.")

