from datetime import date, datetime
from mongoengine import *


class Event(Document):
    eveId=SequenceField()
    eveName=StringField()
    eveDate=DateField()
    eveDepartment=StringField()
    eveParticipants=StringField(required=False)
    eveWinner=StringField(required=False)

    def _str__(self):
        return "Event Information "+str(self.eveId)+" "+self.eveName+" "+str(self.eveDate)+" "+self.eveDepartment+" "+self.eveParticipants+" "+self.eveWinner+"\n"
        
    def initiate(self,nm="",dt=datetime.utcnow(),dept="",part="",win=""):
        self.eveName=nm
        self.eveDate=dt
        self.eveDepartment=dept
        self.eveWinner=win