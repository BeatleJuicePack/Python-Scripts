# Data Value Comparitor Core

This repository contains a script to compare one set of values from another.  
This project is intended to be an easy way to practice coding while requiring little to no knowledge of programming.
Check the [README.md](README.md) file for more information.

## Getting Started

Just clone/download the files and any dependencies for your project then run the script using the bash command
$ python36 dvcCore.py

In order to properly modify the code, you must first update it to suit your needs. Below is an example of a modified script:

### Example: Verifying Checksum Signatures

 1. Download "TestFile.txt" and "TestFile.sh", both of which can be found on
 my github repository: 
 https://github.com/BeatleJuicePack/Python-Scripts/tree/master/DataValueComparitor/DataValueComparitorCore 
 2. Install Python 3.6 and run the following command:
 $ python36 dvcCore.py

 3. Update the script by adjusting your filename/path in the strings:
 sig & ver & vergpgs & vergpga & vergpgf
 
 4. Save and repeat as needed.

 python36 dvcCore.py

DataValueComparitorv2 - April 2019
#BeatleJuice - BeatleJuicePack
#https://beatlejuicepack.com/
#https://github.com/BeatleJuicePack

Files: 
~/Downloads/TestFile.txt
~/Downloads/TestFile.sh
~/Downloads/TestFilePGPPublicKey.py.sig
~/Downloads/TestFilePGPPublicKey.py.asc
~/Downloads/TestFilePGPPublicKey.py

MD5sum: ~/Downloads/TestFile.sh
ff1caab2eefe13cd4cd82da3400bdd35

SHA1Sum: ~/Downloads/TestFile.sh
d99c49861579d424442e63c5f885181bf49c3f57

SHA224sum: ~/Downloads/TestFile.sh
89125fa4362562663b5231a2f7d9c3dd78ab3f9a4c4ea4266d74e703

SHA256sum: ~/Downloads/TestFile.sh
cf1868bcaa2e490b186fb3984e64d2aeea24f4c5b361c480bdff07f4a53cc885

SHA384sum: ~/Downloads/TestFile.sh
abfc6695cd67baba21a6418530e6bfdfc6072e86c90f9f529f28d2b7d708d8d8d7fa8302ed46511b#12ec194c9b6f2bcd

SHA512sum: ~/Downloads/TestFile.sh
824748200fe007c6a079f4fbacc1cc376cad4da93072956482fd017c6db26d13cb12e48e2eb374f4#c6be6b653bd95c5340faf88f5c52a18df1ec31e6daf47b4

~/Downloads/TestFilePGPPublicKey.py.asc
gpg: Signature made Mon 22 Apr 2019 11:59:31 AM PDT using RSA key ID 0B55EEFF
gpg: Good signature from "BeatleJuice <porkinghog9@yahoo.com>"

~/Downloads/TestFilePGPPublicKey.py.sig
gpg: Signature made Mon 22 Apr 2019 11:55:15 AM PDT using RSA key ID 0B55EEFF
gpg: Good signature from "BeatleJuice <porkinghog9@yahoo.com>"

Verified Values for: ~/Downloads/TestFile.txt
MD5:ff1caab2eefe13cd4cd82da3400bdd35
SHA1:
SHA224:
SHA256:cf1868bcaa2e490b186fb3984e64d2aeea24f4c5b361c480bdff07f4a53cc885
SHA384:
SHA512:

MD5 Verified: YES
SHA1 Verified: No
SHA224 Verified: No
SHA256 Verified: YES
SHA384 Verified: No
SHA512 Verified: No

Task Complete!

### Prerequisites

In order to run any Python based scripts you must first have installed Python as well as any dependencies for your project.
You can download Python many various ways:
1. Python's website: https://www.python.org/
2. Repository: Most if not all linux distros have a repository containing python that can be accessed using the below
example commands (more information can be found by accessing the manual/help page for your operating system):
For Debian/GNU Linux: $ sudo apt-get install python36
RedHat: $ sudo yum install python36

Occasionally scripts may require dependencies; the easiest way to properly install them is by:
1. Searching github repositories and clone/download the appropriate .zip for your project.  This can be done in a web browser
or thru the "git clone ssh://git@github.com/[username]/[repository-name].git	" command.  Once downloaded, import the library
and restart your IDE.

### Example installation

1. Download python into an easily accesible directory
2. Install as needed
3. Import any libraries/dependencies for your project (most if not all projects will state this in the first few lines)
4. Clone the files from the repository.
5. Upload the code to your Device (Laptop, Raspberry Pi, Desktop, etc.).
6. Contribute to further developments.
7. Repeat as needed!

## Issues

1. Unknown issues.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/BeatleJuicePack/47204bcc706e0e0c9e11d80e267f3d29) for details on our
code of conduct, and the process for submitting pull requests to us.

## Authors

* **BeatleJuice** - *Initial Work* - [BeatleJuicePack](https://github.com/BeatleJuicePack)
See also the list of [contributors](https://github.com/BeatleJuicePack/Arduino-Projects/contributors)

## License

This project is licensed under the GNU General Public License Version 3 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements

* A big thanks to any and all contributors, no matter how big or small the contribution it all helps.
