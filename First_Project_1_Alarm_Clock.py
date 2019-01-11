"""First Project 1 Alarm Clock

Steps:
a) prompts user in command line to input time
b) saves time so that alarm will go off at this time
c) starts to play Youtube video in browser at time
d) convert to text file with URLs of different alarm videos"""

from datetime import datetime
import pafy
import vlc
url = "https://www.youtube.com/watch?v=iNpXCzaWW1s"
video = pafy.new(url)
best = video.getbest()
media = vlc.MediaPlayer(best.url)

now = datetime.now()
set_off_time = raw_input("What time do you want the alarm to go off? (hh:mm) ")

"""def alarm_clock(set_off_time):
	if str(set_off_time) == "%02d:%02d" % (now.hour, now.minute):
		media.play()
	else:
		print "Alarm has been set and will go off at the selected time. "
"""
while str(set_off_time) == "%02d:%02d" % (now.hour, now.minute):
	media.play()
	set_off_time = False

