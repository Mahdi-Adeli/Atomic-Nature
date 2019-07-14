import sys
from beadfinder import Beadfinder
from blob import Blob
from picture import Picture


def beadtracker(min_pixels, tau, delta, file1, file2):
    pic1 = Picture(file1)
    pic2 = Picture(file2)

    blobs1 = Beadfinder(pic1, tau)
    blobs2 = Beadfinder(pic2, tau)


    beads1 = blobs1.getBeads(min_pixels)
    beads2 = blobs2.getBeads(min_pixels)


    found = []


    conected_beads = [0]*len(beads2)

    for i in range(len(beads1)):

        temp = [20000, beads2[0]]

        for j in range(len(beads2)):
            if conected_beads[j] == 0:
                distance = beads1[i].distanceTo(beads2[j])
                if distance <= delta and distance < temp[0]:
                    temp = [distance, j]
        if temp[0] != 20000:
            found.append(temp[0])
            conected_beads[temp[1]] = 1

    return found



def index(i):
    if i < 10:
        index = "00" + str(i)
    elif i < 100:
        index = "0" + str(i)
    else:
        index = str(i)
    return index


def __main__():
    min_pixels = int(sys.argv[1])
    tau = int(sys.argv[2])
    delta = float(sys.argv[3])
    folder = sys.argv[4][0:6]

    for i in range(200 - 1):
        index1 = index(i)
        index2 = index(i + 1)

        filename1 = folder + "frame00" + index1 + ".jpg"
        filename2 = folder + "frame00" + index2 + ".jpg"

        results = beadtracker(min_pixels, tau, delta, filename1, filename2)

        for result in results:
            print("%0.4f" % (result))


if __name__ == "__main__":
    __main__()