DIR="$(pwd)/venv"
if [ -d "$DIR" ] 
then 
	venv/bin/python spyker.py "$@" 1>/dev/null 2>&1
else
	echo 'Build first by typing "make"'
fi
