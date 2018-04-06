# slonimsky scales generator

from music21 import *
import sys
import itertools

def calc_pos(pos,nl):
    newpos = pos + nl
    if(newpos >= 1.):
        newpos = 0.
    
    return newpos
    
def make_slonim(oct,division,stuff_n,start_note):

    # Show arg info
    print("oct      = %d" % oct)
    print("division = %d" % division)
    print("stuff_n  = %d" % stuff_n)

    nl=0.25 # use 16th notes
    totaloct = oct * 12
    unit = int(totaloct / division) # semitones of one unit
    print("semitones of one unit = %d" % unit)
    
    # Check whether unit is appropriate
    if unit <= stuff_n:
        print("Error: Division too much or too many notes")
        quit()
    
    stuff_notes=[x for x in range(1,unit)] 
    print("stuff notes = ",stuff_notes)
    comb = [el for el in itertools.combinations(stuff_notes,stuff_n)]
    print("combination of unit elements = ",comb)
    
    tc = clef.TrebleClef()
    strm = stream.Part()
    meas = stream.Measure()
    meas.append(tc)
    
    #for each combination
    for el in comb:
        pos = 0.
        curpitch = start_note
        noteList = []
        
        for i in range(0,division):
            nt = note.Note(curpitch,quarterLength = nl)
            nt.color = '#ff0000'
            noteList.append(nt)
            pos = calc_pos(pos,nl)
            
            for offset in el:
                nt = note.Note(curpitch + offset,quarterLength = nl)
                noteList.append(nt)
                pos = calc_pos(pos,nl)
            curpitch += unit
            
        nt = note.Note(start_note + totaloct,quarterLength = nl)
        nt.color = '#ff0000'
        noteList.append(nt)
        pos = calc_pos(pos,nl)
        
        if pos != 0.:
            noteList.append(note.Rest(quarterLength = (1. - pos)))
                
        meas.append(noteList)
        meas.rightBarline = bar.Barline('double')
        strm.append(meas)
        meas = stream.Measure()
        
    caption = 'Equal Division of ' + str(oct) + ' Octave(s) into ' + str(division) + ' Parts \nInterpolation of ' + str(stuff_n) + ' Note(s): Root ' + (note.Note(start_note)).name
    s = stream.Score()
    s.insert(0, metadata.Metadata())
    s.metadata.title = caption
    s.insert(0, strm)
    #s.show('musicxml')
    s.show('lily.png')
    

if __name__ == "__main__":

    argvs = sys.argv
    argc = len(argvs)

    if (argc != 5):
        print ("Usage: python slonim_gen.py [total octaves] [division] [number of interpolation notes] [midi note of start]")
        quit()
        
    oct = int(argvs[1])
    division = int(argvs[2])
    stuff_n = int(argvs[3])
    start_note = int(argvs[4])
    
    if((oct * 12) % division):
        print ("Error: octave % division != 0")
        quit()

    make_slonim(oct,division,stuff_n,start_note)
    
