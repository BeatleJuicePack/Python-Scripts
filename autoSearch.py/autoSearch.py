#!/bin/bash

################################################################################
##   AutoSearch - Python 3.6                                                  ##
##   August 2019 BeatleJuice - BeatleJuicePack                                ##
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

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
    
from random import *

x = randint(1,3)*10
y = randint(1,3)*10
z = randint(2,20)
  
# to search 
query = input("Enter Your Search: ")
  
for j in search(query, tld="com", num=x, stop=y, pause=z): 
    print(j) 
