import random
import sys

from mingus.midi import fluidsynth as fs
from mingus.containers import Bar
import mingus.core.intervals as intervals

from utils import learn, quiz, make_ascending


INTERVAL_NAMES = ['major third', 'minor third', 'major fifth', 'major seventh', 'minor seventh']
INTERVAL_FUNCS = [intervals.major_third, intervals.minor_third, intervals.major_fifth, intervals.major_seventh, intervals.minor_seventh]

def get_bar_from_interval(interval):
	assert len(interval) == 2
	interval = make_ascending(interval)
	# print interval

	b = Bar()
	for n in interval:
		b.place_notes(n, 4)
	b.place_notes(interval, 2)
	return b

def learn_intervals(play_func):
	learn(INTERVAL_NAMES, play_func)

def quiz_intervals(play_func):
	quiz(INTERVAL_NAMES, play_func)


if __name__ == '__main__':
	fs.init('GeneralUser GS 1.471/GeneralUser GS v1.471.sf2')

	def play_interval(choice, key):
		fs.play_Bar(get_bar_from_interval([key, INTERVAL_FUNCS[choice](key)]))

	if len(sys.argv) > 1:
		if sys.argv[1] == 'learn':
			learn_intervals(play_interval)
		elif sys.argv[1] == 'quiz':
			quiz_intervals(play_interval)
		else:
			print "First arg should be 'learn' or 'quiz'."
	else:
		quiz_intervals(play_interval)
