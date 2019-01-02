import random

from mingus.midi import fluidsynth as fs
from mingus.containers import Note, NoteContainer
import mingus.core.chords as chords

from utils import *


def play_notes(fs):
	key = random_key()
	print key

	# fs.play_Note(Note('C-5'))
	# fs.play_NoteContainer(NoteContainer(chords.major_triad(key)))
	# fs.play_Bar(get_bar_from_triad(chords.major_triad(key)))

	fs.play_Note(Note('Cb-4'))   ## this is B-3, not B-4
	fs.play_Note(Note('B-3'))

	# print(_make_ascending(chords.major_triad(key)))
	a = raw_input('hello?')

def scratch():
	import mingus.core.notes as notes
	print notes.reduce_accidentals('B#')  ## output is 'C'

	print notes.remove_redundant_accidentals('C###############')
	print notes.diminish('C##############')

if __name__ == '__main__':
	fs.init('GeneralUser GS 1.471/GeneralUser GS v1.471.sf2')

	# play_notes(fs)
	scratch()
