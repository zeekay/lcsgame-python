import os, struct

def load_graphic(fn):
    """Load ascii art from cpc file"""
    with open(os.path.join('..', 'art', fn), 'rb') as f:
        picnum, dimx, dimy = struct.unpack('iii', f.read(4*3))
        return [[[[struct.unpack('BBBB', f.read(4))] for y in xrange(dimy)] for x in xrange(dimx)] for p in xrange(picnum)]
