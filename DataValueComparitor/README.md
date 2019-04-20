# Data Value Comparitor

This repository contains a script to compare one set of values from another.  
This project is intended to be an easy way to practice coding while requiring little to no knowledge of programming.
Check the [README.md](README.md) file for more information.

## Getting Started

Just clone/download the files and any dependencies for your project then run the script using the bash command
$ python36 DataValueComparitor.py
If the message ***Initial Setup Still Required*** appears then you must still modify the code.

In order to properly modify the code, you must first update it to suit your needs. Below is an example of a modified script:
_________________________________________________________________________________
# Example: Verifying Checksum Signitures
_________________________________________________________________________________
 1. Most downloads come with a .txt file containing the MD/SHA Checksums.
 Begin by viewing the .txt file to begin properly verifying your files.

 2. Checksum your intended file, in this case the file is named:
 UnverifiedInstallation.sh

 3. Update DataValueComparitor.py's (a =) to state the warning message below.
 
 4. Update your i and !i to match your checksum values.

 5. Save and exit nano using CTRL + x
 
 6. Run the script:
 $ python36 DataValueComparitor.py
 If the message ***WARNING...*** appears then you have successfully modified the script.
 _________________________________________________________________________________
 Perform these commands in your shell prompt to run the script.
 
 $ nano SHA256CHECKSUM.txt
 d64923b036585b9043ee96b8127c3337498be69f1a196681e0d9dbbc34ee5c2d

 $ sha256sum UnverifiedInstallation.sh
 3c4289fa42b328f0d19557b2cf9dc5647fcf450f72196715f46ee5104826348a

 $ nano DataValueComparitor.py
 a = """
 ***WARNING UNVERIFIED SIGNITURE***
 Your provided signitures provided do not match.  In order to
 properly ensure your computer's safety, it is vital to only
 download and install software from a reliable source.
 """
 i="3c4289fa42b328f0d19557b2cf9dc5647fcf450f72196715f46ee5104826348a"
 if(i!="d64923b036585b9043ee96b8127c3337498be69f1a196681e0d9dbbc34ee5c2d"):
      print(a)
 else:
      print("Acceptable Signiture")

 $ python36 Comparison.py

 ***WARNING UNVERIFIED SIGNITURE***
 Your provided signitures provided do not match.  In order to
 properly ensure your computer's safety, it is vital to only
 download and install software from a reliable source.
_________________________________________________________________________________

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

1. Currently the script is intended as a beginner project but with enough contributions the comparitor can be used just about
anywhere.
2. Currently the script requires adjustments based on its specific needs, at the moment there are no plans to develop
the script to allow for bash commands.
3. Currently there is no real time verification.
4. Unknown issues.

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
