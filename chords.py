import random
import sys

from mingus.midi import fluidsynth as fs
from mingus.containers import Bar
import mingus.core.chords as chords

from utils import learn, quiz, make_ascending

SEVENTH_CHORD_FLAG = '-s'

TRIAD_NAMES = ['major', 'minor', 'diminished', 'augmented', 'suspended']
TRIAD_FUNCS = [chords.major_triad, chords.minor_triad, chords.diminished_triad, chords.augmented_triad, chords.suspended_fourth_triad]

SEVENTH_CHORD_NAMES = ['major', 'minor', 'diminished', 'minor-major', 'dominant', 'dominant flat-five (french augmented sixth)', 'augmented']
SEVENTH_CHORD_FUNCS = [chords.major_seventh, chords.minor_seventh, chords.diminished_seventh, chords.minor_major_seventh, chords.dominant_seventh, chords.dominant_flat_five, chords.augmented_minor_seventh]

def get_bar_from_chord(chord):
	chord = make_ascending(chord)
	# print chord

	b = Bar(meter=(len(chord) + 1, 4))
	for n in chord:
		b.place_notes(n, 4)  ## add quarter note
	b.place_notes(chord, 4)
	return b

def learn_chords(chord_names, play_func):
	learn(chord_names, play_func)

def quiz_chords(chord_names, play_func):
	quiz(chord_names, play_func)

def usage():
	print "Usage: python chords.py [-s] [learn|quiz]"

if __name__ == '__main__':
	fs.init('GeneralUser GS 1.471/GeneralUser GS v1.471.sf2')

	def play_triad(choice, key):
		fs.play_Bar(get_bar_from_chord(TRIAD_FUNCS[choice](key)))

	def play_seventh_chord(choice, key):
		fs.play_Bar(get_bar_from_chord(SEVENTH_CHORD_FUNCS[choice](key)))

	if SEVENTH_CHORD_FLAG in sys.argv:
		chord_names = SEVENTH_CHORD_NAMES
		play_func = play_seventh_chord
		sys.argv.remove(SEVENTH_CHORD_FLAG)
	else:
		chord_names = TRIAD_NAMES
		play_func = play_triad

	if len(sys.argv) <= 1:
		quiz_chords(chord_names, play_func)
	elif len(sys.argv) == 2:
		if sys.argv[1] == 'learn':
			learn_chords(chord_names, play_func)
		elif sys.argv[1] == 'quiz':
			quiz_chords(chord_names, play_func)
		else:
			usage()
	else:
		usage()
