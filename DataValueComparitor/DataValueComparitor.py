################################################################################
##   Data Value Comparitor - Python36                                         ##
##   April 2019 BeatleJuice - BeatleJuicePack                                 ##
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
#
# Example: Verifying Checksum Signitures
#
################################################################################
#
# 1. Most downloads come with a .txt file containing the MD/SHA Checksums.
# Begin by viewing the .txt file to begin properly verifying your files.
#
# 2. Checksum your intended file, in this case the file is named:
# UnverifiedInstallation.sh
#
# 3. Update Comparison.py's (a =) to state the warning message below.
# 
# 4. Update your i and !i to match your checksum values.
#
# 5. Save and exit nano using CTRL + x
#
################################################################################
#
# nano SHA256CHECKSUM.txt
# d64923b036585b9043ee96b8127c3337498be69f1a196681e0d9dbbc34ee5c2d
#
# sha256sum UnverifiedInstallation.sh
# 3c4289fa42b328f0d19557b2cf9dc5647fcf450f72196715f46ee5104826348a
#
# nano Comparison.py
# a = """
# ***WARNING UNVERIFIED SIGNITURE***
# Your provided signitures provided do not match.  In order to
# properly ensure your computer's safety, it is vital to only
# download and install software from a reliable source.
# """
# i="3c4289fa42b328f0d19557b2cf9dc5647fcf450f72196715f46ee5104826348a"
# if(i!="d64923b036585b9043ee96b8127c3337498be69f1a196681e0d9dbbc34ee5c2d"):
#      print(a)
# else:
#      print("Acceptable Signiture")
#
# python36 Comparison.py
#
# ***WARNING UNVERIFIED SIGNITURE***
# Your provided signitures provided do not match.  In order to
# properly ensure your computer's safety, it is vital to only
# download and install software from a reliable source.
#
################################################################################

a = """
***Initial Setup Still Required***
"""

i="3c4289fa42b328f0d19557b2cf9dc5647fcf450f72196715f46ee5104826348a"
if(i!="d64923b036585b9043ee96b8127c3337498be69f1a196681e0d9dbbc34ee5c2d"):
    print(a)
else:
    print("Acceptable Signiture")
