import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
a = [24, 25, 8, 7, 12, 16, 20, 21]

def lightUp(ledNumber, period):
    p = a[ledNumber]
    GPIO.setup(p, GPIO.OUT)
    GPIO.output(p, 1)
    time.sleep(period)
    GPIO.output(p, 0)
    GPIO.cleanup(p)

def blink(ledNumber, blinkCount, blinkPeriod):
    while blinkCount > 0:
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)
        blinkCount -= 1

def runningLight(count, period):
    for i in range(0, count):
        for j in range(0, 8):
            lightUp(j, period)

def runningDark(count, period):
    for i in a:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, 1)
    while count > 0:
        for j in a:
            GPIO.output(j, 0)
            time.sleep(period)
            GPIO.output(j, 1)
        count -= 1
    for k in a:
        GPIO.cleanup(k)

def decToBinList(decNumber):
    X = []
    for i in range(0, 8):
        remind = decNumber
        remind = remind >> 1
        remind = remind << 1
        c = remind & decNumber
        if c == decNumber:
            X.append(0)
        else:
            X.append(1)
        decNumber = decNumber >> 1
    X.reverse()
    return X

def lightNumber(number):
    newD = decToBinList(number)
    newD.reverse()
    count = 0
    for i in a:
        GPIO.setup(i, GPIO.OUT)
        p = newD[count]
        GPIO.output(i, p)
        count += 1
    time.sleep(1)
    for j in a:
        GPIO.output(j, 0)
        GPIO.cleanup(j)

def runningPattern(pattern, direction):
    result = pattern
    lightNumber(pattern)
    count = 8
    while count > 0:
        X = decToBinList(result)
        if direction == 1:
            reminder = X[7]
            result <<= 1 
        else:
            reminder = X[0]
            result >>= 1
        result = result | reminder
        lightNumber(result)
        count -= 1

lightNumber(127)