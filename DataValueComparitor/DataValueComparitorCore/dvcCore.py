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
# 1. Download all the TestFiles and PGPkeys, all of which can be found on my github repository: 
# https://github.com/BeatleJuicePack/Python-Scripts/tree/master/DataValueComparitor/DataValueComparitorCore
# 2. Install Python 3.6 and run the following command:
# $ python36 dvcCore.py
#
# 3. Update the script by adjusting your filename/path in the strings:
# sig & ver & vergpgs & vergpga & vergpgf
# 
# 4. Save and repeat as needed.
#
################################################################################
#
# python36 dvcCore.py
#
#--------------------------------------------------------------------------------DataValueComparitorv2 - April 2019
#BeatleJuice - BeatleJuicePack
#https://beatlejuicepack.com/
#https://github.com/BeatleJuicePack
#--------------------------------------------------------------------------------#Files: 
#~/Downloads/TestFile.txt
#~/Downloads/TestFile.sh
#~/Downloads/TestFilePGPPublicKey.py.sig
#~/Downloads/TestFilePGPPublicKey.py.asc
#~/Downloads/TestFilePGPPublicKey.py
#--------------------------------------------------------------------------------
#MD5sum: ~/Downloads/TestFile.sh
#ff1caab2eefe13cd4cd82da3400bdd35
#
#SHA1Sum: ~/Downloads/TestFile.sh
#d99c49861579d424442e63c5f885181bf49c3f57
#
#SHA224sum: ~/Downloads/TestFile.sh
#89125fa4362562663b5231a2f7d9c3dd78ab3f9a4c4ea4266d74e703
#
#SHA256sum: ~/Downloads/TestFile.sh
#cf1868bcaa2e490b186fb3984e64d2aeea24f4c5b361c480bdff07f4a53cc885
#
#SHA384sum: ~/Downloads/TestFile.sh
#abfc6695cd67baba21a6418530e6bfdfc6072e86c90f9f529f28d2b7d708d8d8d7fa8302ed46511b#12ec194c9b6f2bcd
#
#SHA512sum: ~/Downloads/TestFile.sh
#824748200fe007c6a079f4fbacc1cc376cad4da93072956482fd017c6db26d13cb12e48e2eb374f4#c6be6b653bd95c5340faf88f5c52a18df1ec31e6daf947b4
#--------------------------------------------------------------------------------
#~/Downloads/TestFilePGPPublicKey.py.asc
#gpg: Signature made Mon 22 Apr 2019 11:59:31 AM PDT using RSA key ID 0B55EEFF
#gpg: Good signature from "BeatleJuice <porkinghog9@yahoo.com>"
#
#~/Downloads/TestFilePGPPublicKey.py.sig
#gpg: Signature made Mon 22 Apr 2019 11:55:15 AM PDT using RSA key ID 0B55EEFF
#gpg: Good signature from "BeatleJuice <porkinghog9@yahoo.com>"
#--------------------------------------------------------------------------------
#Verified Values for: ~/Downloads/TestFile.txt
#MD5:ff1caab2eefe13cd4cd82da3400bdd35
#SHA1:
#SHA224:
#SHA256:cf1868bcaa2e490b186fb3984e64d2aeea24f4c5b361c480bdff07f4a53cc885
#SHA384:
#SHA512:
#--------------------------------------------------------------------------------
#MD5 Verified: YES
#SHA1 Verified: No
#SHA224 Verified: No
#SHA256 Verified: YES
#SHA384 Verified: No
#SHA512 Verified: No
#--------------------------------------------------------------------------------
#Task Complete!
################################################################################

# Import your dependencies
import os
import subprocess
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# *Optional* Clears the terminal screen
os.system("reset")

# Define the path to your files using a GUI
# *Optional* Specifies the files types by adding the below comment to the sig string
#,filetypes = [("Text Files: ", "*.txt"), ("Signature Files:", "*.sig")])
sig = askopenfilename(initialdir = "~/Downloads/", title = "Select SHA/MD Hash file: (example : dvcCore_checksums.txt)")
ver = askopenfilename(initialdir = "~/Downloads/", title = "Select a file to be verified: (example: dvcCore.py)")
vergpgs = askopenfilename(initialdir = "~/Downloads/", title = "Select GPG signature: (example: dvcCore.py.sig)")
vergpga = askopenfilename(initialdir = "~/Downloads/", title = "Select GPG ASCI signature: (example: dvcCore.py.asc)")
vergpgf = ver
# *Optional* Specify the file to be GPG and SHA/MD verified
#vergpgf = askopenfilename(initialdir = "~/Downloads/", title = "Select file to be GPG verified: (fileName.ext)")

# *Optional* Specify your files directly by adjusting the code below
#sig = fileSignature = "~/Downloads/TestFile.txt"
#ver = fileToBeVerified = "~/Downloads/TestFile.sh"
#vergpgs = "~/Downloads/TestFilePGPPublicKey.py.sig"
#vergpga = "~/Downloads/TestFilePGPPublicKey.py.asc"
#vergpgf = "~/Downloads/TestFilePGPPublicKey.py"

# Strings for Checksum
verf = (" " + ver)
md5 = ("md5sum" + verf)
s1 = ("sha1sum" + verf)
s224 = ("sha224sum" + verf)
s256 = ("sha256sum" + verf)
s384 = ("sha384sum" + verf)
s512 = ("sha512sum" + verf)

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

# Defines the gpg process
vergpgaa = (vergpga + " " + vergpgf)
vergpgss = (vergpgs + " " + vergpgf)
gpgver = ("gpg" + " " + "--verify" + " ")

a = "-"
b = a*80

# Prints the files checked and their checksum values
print(b + "DataValueComparitorv2 - April 2019" + "\r")
print("BeatleJuice - BeatleJuicePack")
print("https://beatlejuicepack.com/")
print("https://github.com/BeatleJuicePack")
print(b + "Files: " + "\n" + sig + "\n" + ver + "\n" + vergpgs + "\n" + vergpga  + "\n" + b)
sumpr = (md5print + s1print + s224print + s256print + s384print + s512print)
print(sumpr + b)

# Creates a copy of the checksum hashes for your file
#with open(f"{ver}_checksum.txt", "w") as text_file:
#    print(f"{sumpr}", file=text_file)

# Performs gpg import and verification for specified files
gpgkeyva = subprocess.getoutput(gpgver + vergpgaa)
print(vergpga + "\n" + gpgkeyva + "\n")
gpgkeyvs = subprocess.getoutput(gpgver + vergpgss)
print(vergpgs + "\n" + gpgkeyvs)
print(b)

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
