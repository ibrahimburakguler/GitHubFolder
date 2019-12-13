from psdi.mbo import Mbo,MboRemote,MboSet,MboSetRemote,DBShortcut,SqlFormat
from psdi.security import UserInfo,ConnectionKey
from psdi.server import MXServer,DBManager
from java.lang import System
from psdi.mbo import Mbo, MboRemote, MboSet, MboSetRemote
from psdi.app.asset import Asset, AssetRemote, AssetSet, AssetSetRemote
from psdi.app.workorder import WO,WORemote,WOSet,WOSetRemote
from psdi.app.location import Location,LocationRemote,LocationSet,LocationSetRemote
from java.lang import System
from java.util import Date
from psdi.mbo import MboConstants
from java.util import Calendar
from psdi.mbo import Mbo,MboRemote,MboSet,MboSetRemote,DBShortcut,SqlFormat
from psdi.security import UserInfo,ConnectionKey
from psdi.server import MXServer,DBManager
from java.lang import System
import time


def calculateTheTotalWorkingTimeInMilliseconds():
    try:

        mxServer = MXServer.getMXServer()
        userInfo = mxServer.getSystemUserInfo()
        username = str(userInfo.getUserName())
        conKey = mxServer.getSystemUserInfo().getConnectionKey()
        currentUser=mxServer.getUserInfo(user) 
        dbs = DBShortcut()
        dbs.connect(conKey)
        reportedby = mbo.getString('REPORTEDBY')
        timediffer=''
		
        if reportedby != None and reportedby != '':            
            query = "select PERSON.FIRSTNAME from person where PERSON.PERSONID= " + "'" + str(reportedby) + "' fetch first row only"
            rs = dbs.executeQuery(query)
            if rs.next():


                FIRSTNAME = rs.getString(1)
                       
            query2 = "select PERSON.HIREDATE from person where PERSON.PERSONID= " + "'" + str(reportedby) + "' fetch first row only"
            rs2 = dbs.executeQuery(query2)
            if rs2.next():

                HIREDATE = rs2.getDate(1)
            
                        
            dateNow = MXServer.getMXServer().getDate()

            timediffer = dateNow.getTime()- HIREDATE.getTime()



    except Exception , e:
        mbo.setValue("MX_IMZA",str(e),11L)
        dbs.rollBack()
    finally:
        dbs.close()
        return timediffer




def calulateTheDays():
    diff = calculateTheTotalWorkingTimeInMilliseconds()
    remainDetails = ''
    
    MILLISECONDS_HOUR = 3600000
            
    MILLISECONDS_MINUTE = 60000

    MILLISECOND_DAY = MILLISECONDS_HOUR * 24

    MILLISECOND_YEAR = (MILLISECOND_DAY * 365) + (5 * MILLISECONDS_HOUR) + (48 * MILLISECONDS_MINUTE)
            
    years = 0 
    days = 0
    hours = 0
    minutes = 0

    years = long(diff) / MILLISECOND_YEAR
    days = (long(diff) / MILLISECOND_DAY) - (long(years) * 365)
    hours = (long(diff) / MILLISECONDS_HOUR) - (long(days) * 24) - (long(years) * 365 * 24)
    minutes = (long(diff) / MILLISECONDS_MINUTE) - (long(years) * 365 * 24 * 60) - (long(days)*24*60) - (long(hours) * 60)

    remainDetails = 'Total Service Time : ' ,str(years) + ':' + str (days) + ':' + str(hours) + ':' + str(minutes)


    return  remainDetails 



status = mbo.getMboValue("STATUS").getString()
person = mbo.getMboSet("REPORTEDBY").getMbo(0)
x = person.getString('PRIMARYCALNUM')
if status == 'WAPPR':
    if not mbo.getMboSet("WORKTYPE").isEmpty():
        worktype = mbo.getString("WORKTYPE")
        if worktype == 'EM':
            mbo.setValue('MX_TEST', str(calulateTheDays()), 2L)
            mbo.setValue('MX_IMZA', str(x) , 2L)	
