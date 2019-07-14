import sys
import stdio
import stdarray
import luminance
from blob import Blob
from picture import Picture


class Beadfinder:
# This class for identifiyng picture blobs and then find bead in the pic
 

    def __init__(self, pic, tau):

        self._blobs = []
# create 2D booleans picture
        condition = stdarray.create2D(pic.width(), pic.height(), False)

        for i in range(pic.width()):
            for j in range(pic.height()):
                blob = Blob()
                self._blobfinder(pic, tau, i, j, condition, blob)
                if blob.mass() > 0:
                    self._blobs += [blob]

    def _blobfinder(self, pic, tau, i, j, condition, blob):

        if i >= pic.width() or j >= pic.height() or i < 0 or j < 0 :
            return
        if condition[i][j] == True  or luminance.check_luminance(pic.get(i, j)) < tau:
            return

        condition[i][j] = True

        blob.add(i, j)

        self._blobfinder(pic, tau, i+1, j, condition, blob)
        self._blobfinder(pic, tau, i-1, j, condition, blob)
        self._blobfinder(pic, tau, i, j+1, condition, blob)
        self._blobfinder(pic, tau, i, j-1, condition, blob)

    def getBeads(self, min_pixel):

        Blob = []
        for i in self._blobs:
            if i.mass() >= min_pixel:
                Blob += [i]
        return Blob

def _main():
    min_pixel = int(sys.argv[1])
    tau = float(sys.argv[2])
    pic = Picture(sys.argv[3])
    bf = Beadfinder(pic, tau)
    beads = bf.getBeads(min_pixel)
    stdio.writeln(str(len(beads)) + ' Beads:')
    for i in beads:
        stdio.writeln(str(i))


if __name__ == '__main__':
    _main()
