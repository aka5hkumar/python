#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0
#
# Simple demo of of the LSM303 accelerometer & magnetometer library.
# Will print the accelerometer & magnetometer X, Y, Z axis values every half
# second.
# Author: Tony DiCola
# License: Public Domain

#Modified Akash Kumar
import os
from gps import *
from time import *
import time
import threading
import csv
import Adafruit_LSM303

gpsd = None #setting the global variable
lsm303 = Adafruit_LSM303.LSM303()
# os.system('clear') #clear the terminal (optional)

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    # with open('gpsData.csv', 'wb') as f:    #
    #     writer = csv.writer(f)    #
    #     csv=['Latitude', 'Longitude', 'Time', 'Altitude', 'Speed', 'Climb']    #
    #     writer.writerows(csv)]
    i=0
    titles=['Acceleration X','Acceleration Y','Acceleration Z','Magnetism X','Magnetism Y','Magnetism Z','Latitude','Longitude','Altitude','Speed','Climb']
    #Units=
    csvFile=[]
    csvFile.append(titles)
    while True:
      #It may take a second or two to get good data
      #print gpsd.fix.latitude,', ',gpsd.fix.longitude,'  Time: ',gpsd.utc
      os.system('clear')
      print ('----------------------------------------')
      print('Accelerometer readings')
      print ('----------------------------------------')

      accel, mag = lsm303.read()
      accel_x, accel_y, accel_z = accel
      mag_x, mag_z, mag_y = mag

      print('Accel X={0},\nAccel Y={1},\nAccel Z={2},\nMag X={3},\nMag Y={4},\nMag Z={5}'
      .format(accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))

      print
      print ('GPS reading')
      print ('----------------------------------------')
      print('Latitude={0},\nLongitude={1},\nTime={2},\neps={3},\nepx={4},\nepv={5},\nept={6},\nSpeed (m/s)={7},\nClimb={8},\nTrack={9},\nMode={10}'
      .format(gpsd.fix.latitude, gpsd.fix.longitude, gpsd.fix.time, gpsd.fix.altitude, gpsd.fix.eps, gpsd.fix.epx, gpsd.fix.epv, gpsd.fix.ept, gpsd.fix.speed, gpsd.fix.climb, gpsd.fix.track, gpsd.fix.mode))
      #Assigns Temp variables to appease the csv gods
      tempLat=(gpsd.fix.latitude)
      tempLong=(gpsd.fix.longitude)
      tempAlt=(gpsd.fix.altitude)
      tempSpd=(gpsd.fix.speed)
      tempClb=(gpsd.fix.climb)
      #Writes to a temp array
      csvFile.append([accel_x,accel_y,accel_z,mag_x,mag_y,mag_z,tempLat,tempLong,tempAlt,tempSpd,tempClb])

      i+=1
      print ('----------------------------------------')
      print('Clock (1/2 a second)')
      print(i)
      print ('----------------------------------------')

      time.sleep(.5)

      if (i==1200):
          print('export csv')
     #pops matrix into a csv function
          with open('gpsData.csv', 'wb') as f1:
             writer = csv.writer(f1)
             writer.writerows(csvFile)
             gpsp.running = False
             gpsp.join() # wait for the thread to finish what it's doing
             break
       #records

  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
