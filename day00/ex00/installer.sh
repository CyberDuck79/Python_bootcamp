#!/bin/bash

INSTALL_PATH="/goinfre/miniconda3"

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
	which python
	if grep -q "^export PATH=$bin" ~/.zshrc
	then
		echo "export already in .zshrc" > /dev/tty
		echo "use source ~/.zshrc cmd to reload you zsh conf." > /dev/tty
		source ~/.zshrc
	else
		echo "adding export to .zshrc ..." > /dev/tty
		echo "export PATH=$bin:$PATH" >> ~/.zshrc
		echo "use source ~/.zshrc cmd to reload you zsh conf." > /dev/tty
		source ~/.zshrc
	fi
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