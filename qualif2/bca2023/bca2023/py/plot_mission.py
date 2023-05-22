import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# The log file can be opened on Excel as csv file
# The separator is a comma
# The 18 columns are defined as :
#  1 : Simulator time (unit s)
#  2 : Left command (unit pwm : 10 bits [0 1023])
#  3 : Right command (unit pwm : 10 bits [0 1023])
#  4 : X coordinate of the robot (unit m)
#  5 : Y coordinate of the robot (unit m)
#  6 : Z coordinate of the robot (unit m)
#  7 : Distance measured by front sonar (unit m)
#  8 : Distance measured by left sonar (unit m)
#  9 : Distance measured by back (rear) sonar (unit m)
# 10 : Distance measured by right sonar (unit m)
# 11 : Number of ticks counted by left odometer (signed integer 32 bits)
# 12 : Number of ticks counted by right odometer (signed integer 32 bits)
# 13 : X component of measured magnetic field (signed integer 32 bits)
# 14 : Y component of measured magnetic field (signed integer 32 bits)
# 15 : Reflectivity of left line sensor (float betwwen 0.0 and 1.0)
# 16 : Reflectivity of middle line sensor (float betwwen 0.0 and 1.0)
# 17 : Reflectivity of right line sensor (float betwwen 0.0 and 1.0)
# 18 : Battery level (float betwwen 0.0 and 1.0)


# to cope with french coma instead of US/UK decimal point
def cvt_float(st):
    try:
        v = float(st)
    except:
        v = float(st.replace(',', '.'))
    return v

vx=[]
vy=[]
vt=[]

vsonf=[]
vsonl=[]
vsonr=[]
vbat=[]

vcmdl=[]
vcmdr=[]

it = 0
icmdl = 1
icmdr = 2
ix = 3
iy = 4
isonf = 6
isonl = 7
isonr = 9
ibat = 17

nmax = -200
n = 0

logfile = "../../../vrep/define-track-with-remote-api/challenges/qualif3/A/rob1a.log"
try:
    logfile = sys.argv[1]
except:
    pass

if not os.path.exists (logfile):
    print (logfile, "has not been found exit ...")
    exit()

flog = open (logfile,"r")
st = flog.readline()
while True:
    st = flog.readline()
    if len(st) == 0:
        break
    v = st[0:-1].split(";")
    timsim=cvt_float(v[it])
    vt.append(timsim)
    vx.append(cvt_float(v[ix]))
    vy.append(cvt_float(v[iy]))
    vsonf.append(cvt_float(v[isonf]))
    vsonl.append(cvt_float(v[isonl]))
    vsonr.append(cvt_float(v[isonr]))
    vbat.append(cvt_float(v[ibat]))
    n = n+1
    if n == nmax:
        break    
flog.close()

print (len(vx)," track points")

vx = np.asarray(vx)
vy = np.asarray(vy)
vt =  np.asarray(vt)

plt.figure(1)
plt.xlim([-0.5+np.round(np.min(vx)*2.0)/2.0, 0.5+np.round(np.max(vx)*2)/2.0])
plt.ylim([-0.5+np.round(np.min(vy)*2.0)/2.0, 0.5+np.round(np.max(vy)*2)/2.0])
plt.plot(vx,vy)
plt.plot(vx,vy,'*b')
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("robot track (duration = %ds)"%(int(round(np.max(vt)))))
plt.savefig('robot_log_track.png')

plt.figure(2)
plt.plot (vt,vsonf,'*b')
plt.xlabel("t (s)")
plt.ylabel("front sonar (m)")
plt.title("front sonar")
plt.savefig('robot_log_front.png')

plt.figure(3)
plt.plot (vt,vsonl,'*b')
plt.xlabel("t (s)")
plt.ylabel("left sonar (m)")
plt.title("left sonar")
plt.savefig('robot_log_left.png')

plt.figure(4)
plt.plot (vt,vsonr,'*b')
plt.xlabel("t (s)")
plt.ylabel("right sonar (m)")
plt.title("right sonar")
plt.savefig('robot_log_right.png')

plt.figure(5)
plt.plot (vt,vbat,'*b')
plt.xlabel("t (s)")
plt.ylabel("battery level (%)")
plt.title("battery level")
plt.savefig('robot_log_battery.png')

plt.show()
