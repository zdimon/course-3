
class MonitorT(object):
    def update(self):
        print 'Monitor temperature'

class MonitorH(object):
    def update(self):
        print 'Monitor humidity'


class Data(object):

    monitors = []

    ''''
    def __init__(self):
        self.mt = MonitorT()
        self.mh = MonitorH()
    '''    
       
    def addMonitor(self,monitor):
        self.monitors.append(monitor)
    
    def delMonitor(self,monitor): 
        pass   
    
    temp = 0
    humidity = 100
    def change(self, **kwargs):
        print 'Changing...'
        for m in self.monitors:
            m.update()

        
        
#######################################
import pdb; pdb.set_trace()
data = Data()
monitorT = MonitorT()
data.addMonitor(monitorT)
data.change()


        
        
        
        
        
