from curses import wrapper
import inspect
import locale
from random import randrange
from random import randint
import time
from time import sleep
import math
import argparse

locale.setlocale(locale.LC_ALL, '')

#parse arguments
parser = argparse.ArgumentParser(description='scrolling-marque - Scrolling Marque in Terminal ')
parser.add_argument('message',nargs=1,
               help='what is the message for the scrolling marque')
parser.add_argument('--bounce', dest='bounce', action='store_true',
               help='should the scrolling marque bounce')

parser.add_argument('--faster', dest='faster', action='store_true',
               help='the effect is fast')
parser.add_argument('--slower', dest='slower', action='store_true',
               help='the effect is slow')
parser.add_argument('--vertical', dest='vertical', action='store_true',
               help='additionally move vertical')

args = parser.parse_args()

interval = 0.040
if args.faster:
    interval = 0.030
elif args.slower:
    interval = 0.050    

#print(args)

def main(stdscr):
    # Clear screen
    stdscr.clear()
    #stdscr.addstr(0, 0, 'this is a string {},{}'.format(stdscr.getmaxyx()[0],stdscr.getmaxyx()[1]))
    ##time interval 30fps 0.03

    tupple1 = (0,randrange(stdscr.getmaxyx()[1]),0)
    dots = (tupple1,)
    timeac = 0
    now1=time.time()
    startt = now1
    #interval=0.033
    acc = 9.8 #m/s^2
    whgt=2205

    ## variable
    bounce = args.bounce
    bounced = True #bounce state
    msg = args.message[0]
    
    ticks = 1
    blockLenth = len(msg)
    sW = stdscr.getmaxyx()[1] - 1 #reduce width by 1 to stop potential bug
    sH = stdscr.getmaxyx()[0]

    x = randint(0, sW)
    y = randint(0, sH)
    


    stdscr.addstr(y,x, '{}'.format(msg))
    stdscr.refresh()

    while(True):
        time2=time.time()
        sleepm = interval-(time2-now1)
        stdscr.addstr(0,0,'sleeping {}'.format(sleepm))
        #sleep(0.1)
        sleep(sleepm)
        now1=time.time()

        if args.vertical:
            y+=1
            y=y%sH            
        else:
            x+=1
            x=x%sW

        stdscr.clear()

        #bounce?
        if(bounce):
            if(not(bounced)):
                x-=2            
            if((len(msg)+x)>sW):
                bounced = False
                stdscr.addstr(y,x, '{}'.format(msg))
            elif(x<0):
                bounced = True
                x+=2
                stdscr.addstr(y,x, '{}'.format(msg))
            else:
                stdscr.addstr(y,x, '{}'.format(msg))
        else:
            if((len(msg)+x)>sW):
                  l1 = (len(msg)+x)%sW
                  stdscr.addstr(y,0, '{}'.format(msg[(l1*-1):]))
                  stdscr.addstr(y,x, '{}'.format(msg[l1:]))
            else:
                stdscr.addstr(y,x, '{}'.format(msg))                       

        stdscr.refresh()
        
    stdscr.getkey()
  
wrapper(main)
