from PageObjects.Utils.CommonMethods import *


FIRST_NAME = cssSelector('[name="firstName"]')
LAST_NAME = cssSelector('[name="lastName"]')
PIN_CODE = cssSelector('[placeholder="Pin/Zip Code"]')
SELECT_COUNTRY = cssSelector('[name="country"]')
COUNTRY = cssSelector('[value="India"]')
# SELECT_STATE = cssSelector('')
# STATE = cssSelector('')
ADDRESS_LINE = cssSelector('[placeholder="Address Line 1"]')
CITY = cssSelector('[name="city"]')
CONTACT_NUMBER = cssSelector('[name="phoneNumber"]')
SAVE_ADDRESS_BUTTON = cssSelector('[value="Save Address"]')


def inputFirstName(fName):
    if isElementPresent(FIRST_NAME):
        enterTheInputValue(FIRST_NAME, fName)
    else:
        print(str(FIRST_NAME) + "element is not located.")


def inputLastName(lName):
    if isElementPresent(LAST_NAME):
        enterTheInputValue(LAST_NAME, lName)
    else:
        print(str(LAST_NAME) + "element is not located.")


def inputPinCode(pin):
    if isElementPresent(PIN_CODE):
        enterTheInputValue(PIN_CODE, pin)
    else:
        print(str(PIN_CODE) + "element is not located.")


def selectCountryFromDropDown():
    if isElementPresent(SELECT_COUNTRY):
        clickOnTheButton(SELECT_COUNTRY)
        if isElementPresent(COUNTRY):
            clickOnTheButton(COUNTRY)
        else:
            print(str(COUNTRY) + "element is not located.")
    else:
        print(str(SELECT_COUNTRY) + "element is not located.")


# def selectStateFromDropDown():
#     clickOnTheButton(SELECT_STATE)
#     clickOnTheButton(STATE)


def inputAddressLine(address):
    if isElementPresent(ADDRESS_LINE):
        enterTheInputValue(ADDRESS_LINE, address)
    else:
        print(str(ADDRESS_LINE) + "element is not located.")


def inputCity(city):
    if isElementPresent(CITY):
        enterTheInputValue(CITY, city)
    else:
        print(str(CITY) + "element is not located.")


def inputContactDetails(contactNumber):
    if isElementPresent(CONTACT_NUMBER):
        enterTheInputValue(CONTACT_NUMBER, contactNumber)
    else:
        print(str(CONTACT_NUMBER) + "element is not located.")


def clickOnSaveAddressButton():
    if isElementPresent(SAVE_ADDRESS_BUTTON):
        clickOnTheButton(SAVE_ADDRESS_BUTTON)
    else:
        print(str(SAVE_ADDRESS_BUTTON) + "element is not located.")
