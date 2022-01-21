from PageObjects.Utils.CommonMethods import *
from PageObjects.Utils.TestData import TestData

VERIFY_EMAIL = xpathLocator('//div[text()="Verify Email"]')
ENTER_OTP = cssSelector('[name="otp"]')


def verifyEmailPopUP():
    if isElementPresent(VERIFY_EMAIL):
        isElementPresent(ENTER_OTP)
        print(str(VERIFY_EMAIL) + "element is located.")
    else:
        print(str(VERIFY_EMAIL) + "element is not located.")


def enterEmailVerificationOtp(otp):
    if isElementPresent(ENTER_OTP):
        clearTheInputField(ENTER_OTP)
        enterTheInputValue(ENTER_OTP, otp)
    else:
        print(str(VERIFY_EMAIL) + "element is not located.")
