from plexapi.server import PlexServer
from collections import defaultdict
from urllib.parse import quote
import requests

# ==== CONFIGURATION ====
PLEX_URL = 'PLEX_URL_HERE'       # Replace it with your "https://plex...:32400"
PLEX_TOKEN = 'YOUR_PLEX_TOKEN'   # Replace with your Plex token
MUSIC_LIBRARY_NAME = 'Music'     # Your Plex music library name

# ==== CONNECT TO PLEX ====
plex = PlexServer(PLEX_URL, PLEX_TOKEN)
music_library = plex.library.section(MUSIC_LIBRARY_NAME)

print("🔍 Gathering artists...")
artists = music_library.search(libtype='artist')

print(f"🎶 Found {len(artists)} artists. Processing...")

def album_merge(primary_album, other_albums, plex_url, plex_token):
    try:
        primary_id = str(primary_album.ratingKey)
        other_ids = ",".join(str(album.ratingKey) for album in other_albums)

        merge_url = f"{plex_url}/library/metadata/{primary_id}/merge?ids={quote(other_ids)}&X-Plex-Token={plex_token}"

        response = requests.put(merge_url, verify=False)

        if response.status_code == 200:
            print(f"  ✅ API merge successful for: {primary_album.title}")
        else:
            print(f"  ❌ merge failed: HTTP {response.status_code} - {response.text}")

    except Exception as e:
        print(f"  ❌ Exception during raw merge: {e}")

for artist in artists:
    try:
        artist_name = artist.title.strip().lower()
        print(f"\n🎤 Processing artist: {artist.title}")

        # Fetch all albums for the artist
        albums = artist.albums()
        album_map = defaultdict(list)

        for album in albums:
            title = album.title.strip().lower()
            album_map[title].append(album)

        # Process potential duplicates
        for title, album_group in album_map.items():
            if len(album_group) > 1:
                print(f"  🔁 Found {len(album_group)} duplicates of album '{title}'")
                
                print("  ⬇️  Albums to merge:")
                for a in album_group:
                    print(f"    - {a.title} | key: {a.key}")

                # Attempt merge using PlexAPI
                album_merge(album_group[0], album_group[1:], PLEX_URL, PLEX_TOKEN)

    except Exception as artist_err:
        print(f"⚠️ Error processing artist '{artist.title}': {artist_err}")
