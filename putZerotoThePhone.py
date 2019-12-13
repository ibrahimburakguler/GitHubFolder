from psdi.server import MXServer
from psdi.mbo import Mbo, MboSet, MboRemote, MboSetRemote
from java.util.regex import Pattern, Matcher
from java.lang import System
from psdi.app.workorder import WO,WORemote,WOSet,WOSetRemote
from psdi.mbo import MboConstants


phoneNumber = mbo.getMboValue("PHONE").getString()


if  phoneNumber != None and phoneNumber != '':
    if phoneNumber[0] == '5' and len(phoneNumber) == 10:

        newPhoneNumber = '0' + str(phoneNumber)
    else:
        newPhoneNumber = phoneNumber
        
    mbo.setValue('PHONE', newPhoneNumber, 2L)
