#!/bin/bash

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

function dvc(){
    python36 ~/.dvcCore/dvcCore.py
}

mkdir ~/.dvcCore/;
cp ~/Downloads/dvc/dvcCore.py ~/.dvcCore/
cp ~/Downloads/dvc/.dvcsc.sh ~/.dvcCore/
cp ~/Downloads/dvc/uninstall.sh ~/.dvcCore
cp ~/Downloads/dvc/textSum.py ~/.dvcCore

read -p "Would you like to add shortcut to your desktop? [Y,n]? " input
case ${input:0:1} in
    y|Y )
	chmod +x ~/Downloads/dvc/dvcCore.sh
	cp ~/Downloads/dvc/dvcCore.sh ~/Desktop
    ;;
    n|N|* )
    ;;
esac

echo 'source ~/.dvcCore/.dvcsc.sh' >> ~/.bashrc;
reset
source ~/.dvcCore/.dvcsc.sh
reset

read -p "Would you like to run the program after the installation is complete? [Y/n]? " input
case ${input:0:1} in
    y|Y )
        python36 ~/.dvcCore/dvcCore.py
	echo "Installation Complete!" & echo "You can begin verifying your files by using the bash shortcut 'dvc'." & echo " "
    ;;
    n|N|* )
        echo "Installation Complete!" & echo "You can begin verifying your files by using the bash shortcut 'dvc'." & echo " "
    ;;
esac

echo "Please consider contributing at: https://github.com/BeatleJuicePack"
