import math
import stdio

# This module data in the displacements-run_1.txt 

def main():
    n = 0
    var = 0.00
    while not stdio.isEmpty():
        a = stdio.readFloat() * (0.175 * (10 ** -6))
        var += a * a
        n += 1
    var = var / (2 * n)
    eta = 9.135 * 10 ** -4
    rho = 0.5 * 10 ** -6
    T = 297.0
    R = 8.31457
    k = 6 * math.pi * var * eta * rho / T
    N_A = R / k
    stdio.writef('Boltzman = %e\nAvogadro = %e\n', k, N_A)

if __name__ == '__main__':
    main()