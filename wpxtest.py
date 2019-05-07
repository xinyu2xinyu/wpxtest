import time
import code
timeStamp = 1551077515
timeArray = time.localtime(timeStamp)
formatTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print (formatTime)
code.interact(banner = "", local = locals())
