'''
Created on Oct 2, 2010

@author: Andrew Toshiaki Nakayama Kurauchi
'''
class LOGGER:
    def startLog(self):
        self.LOG = open("dStar.log", "w")
    
    def endLog(self):    
        self.LOG.close()
        
    def log(self, info):
        self.LOG.write(str(info)+"\n")