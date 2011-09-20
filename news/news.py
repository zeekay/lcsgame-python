import os, struct

def load_cbc(fn):
    """Load ascii art from cpc file"""
    with open(fn, 'rb') as f:
        picnum, dimx, dimy = struct.unpack('iii', f.read(4*3))
        return [[[[struct.unpack('BBBB', f.read(4))] for y in xrange(dimy)] for x in xrange(dimx)] for p in xrange(picnum)]

def loadgraphics():
    """Loads graphical resources"""
    return (load_cbc(os.path.join('art', fn)) for fn in ('largecap.cpc', 'newstops.cpc', 'newspic.cpc'))

