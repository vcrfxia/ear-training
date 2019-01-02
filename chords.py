import random
import sys

from mingus.midi import fluidsynth as fs
from mingus.containers import Bar
import mingus.core.chords as chords

from utils import learn, quiz, make_ascending


CHORD_NAMES = ['major', 'minor', 'diminished', 'augmented', 'suspended']
CHORD_FUNCS = [chords.major_triad, chords.minor_triad, chords.diminished_triad, chords.augmented_triad, chords.suspended_fourth_triad]

def get_bar_from_triad(triad):
	assert len(triad) == 3
	triad = make_ascending(triad)
	# print triad

	b = Bar()
	for n in triad:
		b.place_notes(n, 4)  ## add quarter note
	b.place_notes(triad, 4)
	return b

def learn_chords(play_func):
	learn(CHORD_NAMES, play_func)

def quiz_chords(play_func):
	quiz(CHORD_NAMES, play_func)


if __name__ == '__main__':
	fs.init('GeneralUser GS 1.471/GeneralUser GS v1.471.sf2')

	def play_chord(choice, key):
		fs.play_Bar(get_bar_from_triad(CHORD_FUNCS[choice](key)))

	if len(sys.argv) > 1:
		if sys.argv[1] == 'learn':
			learn_chords(play_chord)
		elif sys.argv[1] == 'quiz':
			quiz_chords(play_chord)
		else:
			print "First arg should be 'learn' or 'quiz'."
	else:
		quiz_chords(play_chord)
