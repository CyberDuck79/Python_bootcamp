#!/bin/bash

INSTALL_PATH="/goinfre/$USER/miniconda3"

function get_choice()
{
	local choice

	echo "Download and reinstall 64-bit Miniconda?" > /dev/tty
	echo -n "[yes|no]> " > /dev/tty
	read choice
	while [[ "$choice" != "yes" && "$choice" != "no" ]]; do
		echo "(╬ Ò﹏Ó) -- I asked yes or no ! idiot !" > /dev/tty
		echo "Download and reinstall 64-bit Miniconda?" > /dev/tty
		echo -n "[yes|no]> " > /dev/tty
		read choice
	done
	echo "$choice"
}

function install()
{
	local script="Miniconda3-latest-MacOSX-x86_64.sh"
	local url="http://repo.continuum.io/miniconda/$script"
	local bin="$INSTALL_PATH/bin"

	echo "Download 64-bit Miniconda." > /dev/tty
	curl -LO $url
	echo "Install 64-bit Miniconda in $INSTALL_PATH." > /dev/tty
	sh $script -b -p $INSTALL_PATH > /dev/null
	echo "Python has been installed." > /dev/tty
	echo -n "run export PATH=$bin:\$PATH command"
	echo " to change the default python interpreter path."
	rm $script
}

if [ -d "$INSTALL_PATH" ]; then
	CHOICE=$(get_choice)
	if [ $CHOICE == "yes" ]; then
		rm -rf $INSTALL_PATH
		echo "python has been removed."
		install
	else
		echo "exit."
		exit
	fi
else
	install
fi