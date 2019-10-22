# -- coding: utf-8 --

def shakehand():
  rest()
  i01.startedGesture()
  ##move arm and hand
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(1.0, 1.0)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(39,70)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,55,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",50,50,40,20,20,90)
  i01.moveTorso(95,95,90)
  sleep(3)
   ##optional, detect if there is a human ( waiting finger sensor, we use ultrasonic distance as test )
  if ultraSonicSensorActivated:
    distance=200
    timeout=0
    timeoutGetCloser=0
    while (not distance or distance > 80): 
      timeout+=1
      timeoutGetCloser+=1
      distance=i01.getUltrasonicSensorDistance()
      print distance
      if timeout > 20:
        chatBot.getResponse("SYSTEM_SHAKE_HAND_NOHUMAN")
        sleep(2)
        shakehandFinish()
        break  
      sleep(0.5)
      # ask GET CLOSER
      if timeoutGetCloser> 10:
        chatBot.getResponse("SYSTEM_SHAKE_HAND_GET_CLOSER")
        timeoutGetCloser=0
        sleep(2)  
      sleep(1)
    # great, human detected
    if distance<=80:shakehandAnimation()
  else:
    sleep(3)
    shakehandAnimation()

def shakehandAnimation():  
  ##set hand up
  i01.setHandVelocity("left", 22.0, 22.0, 22.0, 22.0, 22.0, -1)
  i01.setHandVelocity("right", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(-1, -1)
  i01.setTorsoVelocity(31.0, 13.0, -1)
  i01.moveHead(90,90)
  i01.moveArm("left",5,84,16,15)
  i01.moveArm("right",6,73,60,16)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveTorso(95,95,90)
  i01.moveHand("right",80,70,70,50,50,77)
  i01.moveHand("right",50,50,40,20,20,90)
  sleep(3)
  if rightHandSensorActivated:
    #global rightHandSensorPin
    global rightThumbSensorPin
    global rightIndexSensorPin
    global rightMajeureSensorPin
    global rightRingFingerSensorPin
    global rightPinkySensorPin
    ##close the hand
    i01.setHandVelocity("left", 22.0, 22.0, 22.0, 22.0, 22.0, -1)
    i01.setHandVelocity("right", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
    i01.setArmVelocity("right", 31.0, 43.0, 59, 43.0)
    i01.setArmVelocity("left", 31.0, 43.0, 31.0, 43.0)
    i01.setHeadVelocity(-1, -1)
    i01.setTorsoVelocity(31.0, 13.0, -1)
    i01.moveHead(39,70)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,60,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveTorso(95,95,90)
    
    #sleep(1.5) # Very important
    # ok we start a threaded loop ( I use a timer for that )
    # because python "while" loop may stuck other threads like "pin publishers"
    # thread will reajust fingers every Xms since the gesture is not finished ( we can change it )

    sensorTimer.startClock(True)
  
    # TODO : create a sub function and launch this bottom from the timer thread
    # IF a finger detect something ( if rightThumbSensorPin>1 or rightIndexSensorPin ... )
    sleep(3)
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
    i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
    i01.setHeadVelocity(31.0, 31.0)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(70,53)
    sleep(0.5)
    i01.moveHead(39,70)
    sleep(0.5)
    i01.moveHead(70,53)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,48,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveTorso(95,95,90)
    sleep(1.5) 
    ##shake hand up
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
    i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
    i01.setHeadVelocity(43.0, 43.0)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(80,53)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,60,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveTorso(95,95,90)
    sleep(1)
    chatBot.getResponse("SYSTEM_SHAKE_HAND")
    ##shake hand down
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
    i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
    i01.setHeadVelocity(43.0, 43.0)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(80,88)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,48,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveTorso(95,95,90)
    sleep(1.5)
    ##shake hand up
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
    i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
    i01.setHeadVelocity(43.0, 43.0)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(80,53)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,60,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveTorso(95,95,90)
    sleep(1)
    ##shake hand down
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
    i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
    i01.setHeadVelocity(43.0, 43.0)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(80,88)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,48,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveTorso(95,95,90)
    sleep(1.5)
    ##shake hand up
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
    i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
    i01.setHeadVelocity(43.0, 43.0)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(80,53)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,60,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveTorso(95,95,90)
    sleep(1)
    ## release hand 

    sensorTimer.stopClock()
    
    i01.setHandVelocity("left", 22.0, 22.0, 22.0, 22.0, 22.0, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("right", 59, 59, 59, 43.0)
    i01.setArmVelocity("left", 31.0, 43.0, 59, 43.0)
    i01.setHeadVelocity(-1, -1)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(39,70)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,45,16)
    i01.moveHand("left",50,50,40,20,20,77)
    i01.moveHand("right",0,0,0,0,0,90)
    i01.moveTorso(95,95,90)
    sleep(1)
    shakehandFinish()

  else:
    ## No Hand Sensor
    ##close the hand
    i01.setHandVelocity("left", 22.0, 22.0, 22.0, 22.0, 22.0, -1)
    i01.setHandVelocity("right", 43.0, 43.0, 43.0, 43.0, 43.0, -1)
    i01.setArmVelocity("right", 31.0, 43.0, 59, 43.0)
    i01.setArmVelocity("left", 31.0, 43.0, 31.0, 43.0)
    i01.setHeadVelocity(-1, -1)
    i01.setTorsoVelocity(31.0, 13.0, -1)
    i01.moveHead(39,70)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,60,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveHand("right",180,125,135,145,168,77)
    i01.moveTorso(95,95,90)
    sleep(3)
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
    i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
    i01.setHeadVelocity(31.0, 31.0)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(70,53)
    sleep(0.5)
    i01.moveHead(39,70)
    sleep(0.5)
    i01.moveHead(70,53)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,48,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveHand("right",180,125,135,145,168,77)
    i01.moveTorso(95,95,90)
    sleep(1.5)
    ##shake hand up
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
    i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
    i01.setHeadVelocity(43.0, 43.0)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(80,53)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,60,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveTorso(95,95,90)
    sleep(1)
    chatBot.getResponse("SYSTEM_SHAKE_HAND")
    ##shake hand down
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
    i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
    i01.setHeadVelocity(43.0, 43.0)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(80,88)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,48,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveTorso(95,95,90)
    sleep(1.5)
    ##shake hand up
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
    i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
    i01.setHeadVelocity(43.0, 43.0)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(80,53)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,60,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveTorso(95,95,90)
    sleep(1)
    ##shake hand down
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
    i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
    i01.setHeadVelocity(43.0, 43.0)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(80,88)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,48,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveTorso(95,95,90)
    sleep(1.5)
    ##shake hand up
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
    i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
    i01.setHeadVelocity(43.0, 43.0)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(80,53)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,60,16)
    i01.moveHand("left",50,50,40,20,20,90)
    i01.moveTorso(95,95,90)
    sleep(1)
    ## release hand  
    i01.setHandVelocity("left", 22.0, 22.0, 22.0, 22.0, 22.0, -1)
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
    i01.setArmVelocity("right", 59, 59, 59, 43.0)
    i01.setArmVelocity("left", 31.0, 43.0, 59, 43.0)
    i01.setHeadVelocity(-1, -1)
    i01.setTorsoVelocity(22.0, 13.0, -1)
    i01.moveHead(39,70)
    i01.moveArm("left",5,84,16,15)
    i01.moveArm("right",6,73,45,16)
    i01.moveHand("left",50,50,40,20,20,77)
    i01.moveHand("right",20,30,30,20,20,90)
    i01.moveTorso(95,95,90)
    sleep(1)
    shakehandFinish()

def shakehandFinish():
  sleep(0.5)
  #rightHandSensorPin = 0
  i01.finishedGesture()
  rest()
  relax()
