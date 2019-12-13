from psdi.mbo import Mbo, MboRemote, MboSet, MboSetRemote
from psdi.app.asset import Asset, AssetRemote, AssetSet, AssetSetRemote
from psdi.server import MXServer
from psdi.mbo import Mbo,MboRemote,MboSet,MboSetRemote
from psdi.app.workorder import WO,WORemote,WOSet,WOSetRemote
from psdi.app.location import Location,LocationRemote,LocationSet,LocationSetRemote
from java.lang import System
from java.util import Date
from psdi.mbo import MboConstants



def locationTypeCheck():
	isLabor = False
	if(not mbo.getMboSet("LOCATION").isEmpty()):
		if(mbo.getMboSet("LOCATION").getMbo(0).getString('TYPE') == 'BPM3100'):
			isLabor = True
	
	return isLabor


def isTwoDays():

    isLate = False
    dates = mbo.getDate("ActFinish")
    datef = mbo.getDate("SchedFinish")
   
    if(datef != None and dates != None):

        MILLISECONDS_HOUR = 3600000
        
        MILLISECONDS_MINUTE = 60000

        MILLISECOND_DAY = MILLISECONDS_HOUR * 24
        
        twodays = MILLISECOND_DAY * 2

        days=0
        hours = 0
        minutes = 0

        schedFinish = mbo.getDate('SchedFinish')
        actFinish = mbo.getDate('ActFinish')
        diff = abs(schedFinish.getTime() - actFinish.getTime())

        if schedFinish.getTime() < actFinish.getTime()  and diff > twodays:
            isLate = True


    return isLate


def remainTimePrint():
    remainDetails = ''
    
    datef = mbo.getDate("SchedFinish")
    if(datef != None):
        MILLISECONDS_HOUR = 3600000
            
        MILLISECONDS_MINUTE = 60000

        MILLISECOND_DAY = MILLISECONDS_HOUR * 24
            
        
        days=0
        hours = 0
        minutes = 0

        schedFinish = mbo.getDate('SchedFinish')
        actFinish = mbo.getDate('ActFinish')
        diff = schedFinish.getTime() - actFinish.getTime()

        days = long(diff) / MILLISECOND_DAY
        hours = (long(diff) / MILLISECONDS_HOUR) - (long(days) * 24)
        minutes = (long(diff) / MILLISECONDS_MINUTE) - (long(days)*24*60) - (long(hours) * 60)


        if schedFinish.getTime() - actFinish.getTime() >= 0 :

            remainDetails = 'Remaining Time : ' + str (days) + ':' + str(hours) + ':' + str(minutes)


    return  remainDetails 



status = mbo.getMboValue("STATUS").getString()

if status =='COMP' and locationTypeCheck :


    lateError = ''

    if isTwoDays():
        lateError = ' Late !'
    



    type = mbo.getMboSet("LOCATION").getMbo(0).getString('LOCATION') 
    mbo.setValue('MX_IMZA', remainTimePrint() + " Location type is " + type + lateError , 11L)

    

    if(not mbo.getMboSet("ASSET").isEmpty()):
        newStatus = "LIMITEDUSE" 
        asset = mbo.getMboSet("ASSET").getMbo(0)
        LOCATION = mbo.getMboSet("LOCATION").getMbo(0)
        assetStatus = asset.getString("STATUS")
        changeby = asset.getString("CHANGEBY")
        newStatusLocation = "ACTIVE" 

        newchangeby = 'automationscript'
        description = asset.getString("DESCRIPTION")
        if(assetStatus == 'ACTIVE' or assetStatus == 'OPERATING' ):
            asset.changeStatus(newStatus, MXServer.getMXServer().getDate(), None, 2L)
            mbo.setValue("ASSET.CHANGEBY", description , 11L)
            mbo.setValue("LOCATION.DESCRIPTION", "ibg" , 11L)
            mbo.setValue("LOCATION.SERVICEADDRESSCODE", "chill be adam" , 11L)
            LOCATION.changeStatus(newStatusLocation, MXServer.getMXServer().getDate(), None, 2L)



