#!/bin/bash

################################################################################
##   PrimeRange - Python 3.6                                                  ##
##   May 2019 BeatleJuice - BeatleJuicePack                                   ##
##   https://beatlejuicepack.com/                                             ##
##   https://github.com/BeatleJuicePack                                       ##
################################################################################
##   This program is free software: you can redistribute it and/or modify     ##
##   it under the terms of the GNU General Public License as published by     ##
##   the Free Software Foundation, either version 3 of the License, or        ##
##   (at your option) any later version.                                      ##
##                                                                            ##
##   This program is distributed in the hope that it will be useful,          ##
##   but WITHOUT ANY WARRANTY; without even the implied warranty of           ##
##   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            ##
##   GNU General Public License for more details.                             ##
##                                                                            ##
##   You should have received a copy of the GNU General Public License        ##
##   along with this program.  If not, see <https://www.gnu.org/licenses/>.   ##
################################################################################

import time

n = int(input("Find the prime numbers to what value? "))

start = time.time()
print("Initializing timer... ")

p = 2
for p in range(2, n+1):
    for i in range(2,p):
        if p % i ==0:
            break
    else:
        print(p),

end = time.time()
print(end - start)
print("   seconds")
print("Done!")
