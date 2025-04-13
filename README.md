# Plex Scripts
A place for my Plex scripts to fix annoyances and the like

Loving the work I do? buy me a coffee https://buymeacoffee.com/musicmovearr

# Script - Plex Merge Albums
This script will connect to your Plex Server, gather all the artists, loop through each Artist to gather it's Album's and find the duplicates by name (case insensitive)

It will use the merge API, the same you would use in the browser but of course, with this script it's completely automated saving you a lot of time/hassle doing it by hand

## Example output:
```
🎤 Processing artist: Death Ss

🎤 Processing artist: Death Valley Girls

🎤 Processing artist: Deathbrain

🎤 Processing artist: Deathday

🎤 Processing artist: Deathsiege

🎤 Processing artist: Deathstars
  🔁 Found 3 duplicates of album 'decade of debauchery'
  ⬇  Albums to merge:
    - Decade of debauchery | key: /library/metadata/3349841
    - Decade of Debauchery | key: /library/metadata/3093459
    - Decade of Debauchery | key: /library/metadata/3339958
  ✅ API merge successful for: Decade of debauchery
  🔁 Found 2 duplicates of album 'night electric night (platinum edition)'
  ⬇  Albums to merge:
    - Night Electric Night (Platinum Edition) | key: /library/metadata/3093468
    - Night Electric Night (Platinum Edition) | key: /library/metadata/3339966
  ✅ API merge successful for: Night Electric Night (Platinum Edition)
  🔁 Found 2 duplicates of album 'the perfect cult'
  ⬇  Albums to merge:
    - The Perfect Cult | key: /library/metadata/3093426
    - The Perfect Cult | key: /library/metadata/3339984
  ✅ API merge successful for: The Perfect Cult
  🔁 Found 2 duplicates of album 'synthetic generation'
  ⬇  Albums to merge:
    - Synthetic Generation | key: /library/metadata/3093566
    - Synthetic Generation | key: /library/metadata/3345752
  ✅ API merge successful for: Synthetic Generation

🎤 Processing artist: Deaundre

🎤 Processing artist: DeBarge
  🔁 Found 2 duplicates of album 'time will reveal: the complete motown albums'
  ⬇  Albums to merge:
    - Time Will Reveal: the Complete Motown Albums | key: /library/metadata/2667225
    - Time Will Reveal: The Complete Motown Albums | key: /library/metadata/2667223
  ✅ API merge successful for: Time Will Reveal: the Complete Motown Albums

🎤 Processing artist: Debauchery

🎤 Processing artist: Debbie Deb

```

# Usage on ArchLinux
```
yay -S  python python-plexapi
git clone https://github.com/MusicMoveArr/PlexScripts.git
cd PlexScripts
```
Update the script before using it with your URL/Token

```
python3 plex_merge_albums.py
```

# Usage on Debian (Ubuntu, Linux Mint etc) (Not tested)
```
sudo apt update
sudo apt install python3 python3-pip
pip install plexapi
git clone https://github.com/MusicMoveArr/PlexScripts.git
cd PlexScripts
```
Update the script before using it with your URL/Token
```
python3 plex_merge_albums.py
```


