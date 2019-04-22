################################################################################
##   Data Value Comparitorv2 - Python 3.6                                     ##
##   April 2019 BeatleJuice - BeatleJuicePack                                 ##
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
#
# Example: Verifying Checksum Signatures
#
################################################################################
#
# 1. Download "TestFile.txt" and "TestFile.sh", both of which can be found on
# my github repository: 
# https://github.com/BeatleJuicePack/Python-Scripts/tree/master/DataValueComparitor.
# 
# 2. Install Python 3.6 and run the following command:
# $ python36 dvcv2.py
#
# 3. Update the script by adjusting your filename/path in the strings:
# sig & ver
# 
# 4. Save and repeat as needed.
#
################################################################################
#
# git https://github.com/BeatleJuicePack/Python-Scripts/tree/master/DataValueComparitor/TestFile.txt.
# git https://github.com/BeatleJuicePack/Python-Scripts/tree/master/DataValueComparitor/TestFile.sh.
#
# python36 dvcv2.py
#
# Files Checked: 
# ~/Downloads/TestFile.txt
# ~/Downloads/TestFile.sh
#
# SHA1Sum: ~/Downloads/TestFile.sh
# d99c49861579d424442e63c5f885181bf49c3f57
#
# SHA224sum: ~/Downloads/TestFile.sh
# 89125fa4362562663b5231a2f7d9c3dd78ab3f9a4c4ea4266d74e703
#
# SHA256sum: ~/Downloads/TestFile.sh
# cf1868bcaa2e490b186fb3984e64d2aeea24f4c5b361c480bdff07f4a53cc885
#
# SHA384sum: ~/Downloads/TestFile.sh
# abfc6695cd67baba21a6418530e6bfdfc6072e86c90f9f529f28d2b7d708d8d8d7fa8302ed46511b12ec194c9b6f2bcd
#
# SHA512sum: ~/Downloads/TestFile.sh
# 824748200fe007c6a079f4fbacc1cc376cad4da93072956482fd017c6db26d13cb12e48e2eb374f4c6be6b653bd95c5340faf88f5c52a18df1ec31e6daf947b4
#
# MD5sum: ~/Downloads/TestFile.sh
# ff1caab2eefe13cd4cd82da3400bdd35
#
#
# Verified Values for: ~/Downloads/TestFile.txt
# SHA1Sum:
# SHA224Sum:
# SHA256Sum:cf1868bcaa2e490b186fb3984e64d2aeea24f4c5b361c480bdff07f4a53cc885
# SHA384Sum:
# SHA512Sum:
# MD5Sum:ff1caab2eefe13cd4cd82da3400bdd35
#
# Unverified: SHA1
# Unverified: SHA224
# Verified: SHA256
# Unverified: SHA384
# Unverified: SHA512
# Verified: MD5
#
################################################################################

# Import your dependencies
import os
import subprocess

# *Optional* Clears the terminal screen
os.system("reset")

# Define the path to your files
sig = fileSignature = "~/Downloads/TestFile.txt"
ver = fileToBeVerified = "~/Downloads/TestFile.sh"

# Strings for Checksum
md5 = ("md5sum" + " " + ver)
s1 = ("sha1sum" + " " + ver)
s224 = ("sha224sum" + " " + ver)
s256 = ("sha256sum" + " " + ver)
s384 = ("sha384sum" + " " + ver)
s512 = ("sha512sum" + " " + ver)

# Obtains a string from the checksum output
md5out = subprocess.getoutput(md5)
s1out = subprocess.getoutput(s1)
s224out = subprocess.getoutput(s224)
s256out = subprocess.getoutput(s256)
s384out = subprocess.getoutput(s384)
s512out = subprocess.getoutput(s512)

# Obtains the hash value
md5split = md5out.split()[0]
s1split = s1out.split()[0]
s224split = s224out.split()[0]
s256split = s256out.split()[0]
s384split = s384out.split()[0]
s512split = s512out.split()[0]

# Defines how the output will be printed
md5print = ("MD5sum: " + ver + "\n" + md5split + "\n")
s1print = ("\n" + "SHA1Sum: " + ver + "\n" + s1split + "\n")
s224print = ("\n" + "SHA224sum: " + ver + "\n" + s224split + "\n")
s256print = ("\n" + "SHA256sum: " + ver + "\n" + s256split + "\n")
s384print = ("\n" + "SHA384sum: " + ver + "\n" + s384split + "\n")
s512print = ("\n" + "SHA512sum: " + ver + "\n" + s512split + "\n")

b = "--------------------------------------------------------------------------------"

# Prints the files checked and their checksum values
print(b + "DataValueComparitorv2 - April 2019" + "\r")
print("BeatleJuice - BeatleJuicePack")
print("https://beatlejuicepack.com/")
print("https://github.com/BeatleJuicePack")
print(b + "Files: " + "\n" + sig + "\n" + ver + "\n" + b)
print(md5print + s1print + s224print + s256print + s384print + s512print + b)

# Uses grep to search the signatures within the file
md5grep = subprocess.getoutput("grep" + " " + md5split + " " + sig)
s1grep = subprocess.getoutput("grep" + " " + s1split + " " + sig)
s224grep = subprocess.getoutput("grep" + " " + s224split + " " + sig)
s256grep = subprocess.getoutput("grep" + " " + s256split + " " + sig)
s384grep = subprocess.getoutput("grep" + " " + s384split + " " + sig)
s512grep = subprocess.getoutput("grep" + " " + s512split + " " + sig)

# Prints only the verified values for your given files
print("Verified Values for: " + sig + "\n" + "MD5:" + md5grep + "\n" + "SHA1:" + s1grep + "\n" + "SHA224:" + s224grep + "\n" + "SHA256:" + s256grep + "\n" + "SHA384:" + s384grep + "\n" + "SHA512:" + s512grep + "\n" + b)

# Prints a YES or a No as to whether or not the values have been verified
if not md5grep:
    print("MD5 Verified: No")
else:
    print("MD5 Verified: YES")

if not s1grep:
    print("SHA1 Verified: No")
else:
    print("SHA1 Verified: YES")

if not s224grep:
    print("SHA224 Verified: No")
else:
    print("SHA224 Verified: YES")

if not s256grep:
    print("SHA256 Verified: No")
else:
    print("SHA256 Verified: YES")

if not s384grep:
    print("SHA384 Verified: No")
else:
    print("SHA384 Verified: YES")

if not s512grep:
    print("SHA512 Verified: No")
else:
    print("SHA512 Verified: YES")

print(b)
print("Task Complete!")
