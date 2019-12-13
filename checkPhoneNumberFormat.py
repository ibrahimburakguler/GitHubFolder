from psdi.server import MXServer
from psdi.mbo import Mbo, MboSet, MboRemote, MboSetRemote
from java.util.regex import Pattern, Matcher
from java.lang import System
from psdi.app.workorder import WO,WORemote,WOSet,WOSetRemote
from psdi.mbo import MboConstants


def setError(assetattrid, group, key):
	global params,errorkey, errorgroup
	params = [assetattrid]
	errorkey=key
	errorgroup=group

phoneNumber = mbo.getMboValue("PHONE").getString()


if  phoneNumber != None and phoneNumber != '':
    phoneNumberPattern = '^(?:0?5[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9])$'
    pattern = Pattern.compile(phoneNumberPattern);
    matcher = pattern.matcher(phoneNumber);
    if(matcher.find()):
	    a = 1
    else:
        setError(phoneNumber,"mygroup","phoneNumberCheck")