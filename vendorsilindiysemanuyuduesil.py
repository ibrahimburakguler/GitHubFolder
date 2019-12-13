from psdi.mbo import Mbo,MboRemote,MboSet,MboSetRemote
from psdi.server import MXServer
from java.lang import System



vendorValue = mbo.getString('VENDOR')

if(vendorValue == None or vendorValue == '' ):
	
	mbo.setValueNull("MANUFACTURER", 11L)
	mbo.setValue("SERIALNUM","Turn It Off",11L)