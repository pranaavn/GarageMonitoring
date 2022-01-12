from flask import Flask, request, send_from_directory
import threading
from prometheus_client import start_http_server, Gauge, start_http_server
import time
import statistics



"""
----------GLOBAL VARIABLES----------
"""

instructionCode=''

globalData=1

tempDataPoints = []

garageOpen = False

ardStatus = 0



"""
---------------THREADS---------------
"""



"""
WEBSERVER THREAD 1
"""

class webserverThread(threading.Thread):
    def __init__(self, threadID, threadName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName

    def run(self):
        webservice()

def webservice():
    print('starting webserverThread'+'\n')
    app1 = Flask(__name__, static_url_path='/static')

    @app1.route("/device", methods=['GET', 'POST'])
    def device():
        global instructionCode
        global globalData
        global tempDataPoints
        global ardStatus

        ardStatus = 1

        numVals = 0
        if request.method == 'POST':
            data = request.data.decode('ascii')
            print("Data from Sensor is: "+data)
            data = data[39:42]
            globalData = float(data)
            print ('globalData: '+str(globalData))
            print("Distance Value is: "+data)
            tempDataPoints.append(int(data))
            for item in tempDataPoints:
                numVals+=1
            print(numVals)

            if (numVals>=30):
                del tempDataPoints[0]

        return (instructionCode)

    #@app1.route("/firmwareupdate", methods=['GET', 'POST'])
    @app1.route("/firmwareupdate", methods=['GET', 'POST'])
    def firmwareupdate():
        print('Returning bin file to client')
        #return app.send_static_file('GarageDoor.ino.generic.bin')
        return send_from_directory('/home/pranaavn','GarageDoor.ino.generic.bin')

    app1.run(host='0.0.0.0', port = 80, threaded = True, debug = False)



"""
INSTRUCTION THREAD 2
"""

class instructionThread(threading.Thread):
    def __init__(self, threadID, threadName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName

    def run(self):
        instructionThreadLoop()


def instructionThreadLoop():
    global instructionCode
    print('starting instructionThread'+'\n')
    while True:
        instructionCode=input()
        print("Instruction Code has been change to: "+instructionCode)



"""
GARAGE LOGIC THREAD 3
"""

class garageLogicThread(threading.Thread):
    def __init__(self, threadID, threadName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName

    def run(self):
        garageLogic()


def garageLogic():
    global garageOpen
    print('starting garageLogicThread'+'\n')
    while True:
        if len(tempDataPoints) > 10:
            if statistics.mean(tempDataPoints[-2:]) < 62:
                garageOpen = True
            elif statistics.mean(tempDataPoints[-2:]) > 68:
                garageOpen = False



"""
STATUS CHECK THREAD 4
"""

class statusCheckThread(threading.Thread):
    def __init__(self, threadID, threadName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName

    def run(self):
        statusCheck()


def statusCheck():
    print('starting statusCheckThread'+'\n')
    while True:
        if ardStatus == 1:
            ardStatustatus = 0
            time.sleep(20)



"""
EXPOSE DATA THREAD 5
"""

class exposeDataThread(threading.Thread):
    def __init__(self, threadID, threadName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName

    def run(self):
        exposeData()

def exposeData():
    global globalData
    print('starting exposeDataThread')
    proxData = Gauge('ProximityData', 'Description of gauge')
    proxData.set_to_current_time()

    proxData.set(globalData)

    gStat = Gauge('GarageStatus', 'Description of gauge')
    gStat.set_to_current_time()

    gStat.set(globalData)

    flaskStat = Gauge('ArduinoStatus', 'Description of gauge')
    flaskStat.set_to_current_time()

    flaskStat.set(0)

    start_http_server(9091)
    while True:
        proxData.set(globalData)
        if (garageOpen == False):
            gStat.set(0)
        elif (garageOpen == True):
            gStat.set(1)
        flaskStat.set(ardStatus)
        time.sleep(10)

def exposeDataTemp():
    print('starting exposeDataTemp'+'\n')
    app2 = Flask(__name__, static_url_path='/static')

    @app2.route('/metrics', methods=['GET', 'POST'])
    def metrics():
        #return json.loads('{"GarageStatus":[{"status":"5"}]}')
        #return '{"GarageStatus":[{"status":"5"}]}'
        return 'metric_name ["{" label_name "=" `"` label_value `"` { "," label_name "=" `"` label_value `"` } [ "," ] "}"] value [ timestamp ]'

    print('running dbApp')
    app2.run(host='0.0.0.0', port=9091, threaded=True, debug=False)

"""
----------THREAD INITIALIZATION----------
"""

thread1 = webserverThread(1, 'webServerThread')
thread1.start()

thread2 = instructionThread(2, 'instructionThread')
thread2.start()

thread3 = garageLogicThread(3, 'garageLogicThread')
thread3.start()

thread4 = statusCheckThread(4, 'statusCheckThread')
thread4.start()

thread5 = exposeDataThread(5, 'exposeDataThread')
thread5.start()



