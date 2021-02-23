echo "
   ______      __  __               _  __
  / ____/_  __/ /_/ /_  ____  ____ | |/ /
 / /   / / / / __/ __ \/ __ \/ __ \|   / 
/ /___/ /_/ / /_/ / / / /_/ / / / /   |  
\____/\__, /\__/_/ /_/\____/_/ /_/_/|_|  
     /____/
	    °•° CythonX Installation Begins •°•
	    °•° Honor CɪᴘʜᴇʀX •°•

"
apt-get update
apt-get upgrade -y
apt-get autoremove --purge
pip3 install -r requirements.txt
python3 -m setup.py
