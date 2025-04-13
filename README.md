# Plex Scripts
A place for my Plex scripts to fix annoyances and the like

Loving the work I do? buy me a coffee https://buymeacoffee.com/musicmovearr

# Script - Plex Merge Albums
This script will connect to your Plex Server, gather all the artists, loop through each Artist to gather it's Album's and find the duplicates by name (case insensitive)

It will use the merge API, the same you would use in the browser but of course, with this script it's completely automated saving you a lot of time/hassle doing it by hand

# Usage on ArchLinux
yay -S  python python-plexapi
git clone https://github.com/MusicMoveArr/PlexScripts.git
cd PlexScripts

Update the script before using it with your URL/Token
python3 plex_merge_albums.py

# Usage on Debian (Ubuntu, Linux Mint etc) (Not tested)
sudo apt update
sudo apt install python3 python3-pip
pip install plexapi
git clone https://github.com/MusicMoveArr/PlexScripts.git
cd PlexScripts

Update the script before using it with your URL/Token
python3 plex_merge_albums.py


