import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


CLIENT_ID = 'a4cef65041d04fe1a6b05d464d464d15'
CLIENT_SECRET = '70ae8a9c07844be5ae31bd7b2496a183'
REDIRECT_URL = 'http://localhost:8888/callback'
SCOPE = 'playlist-modify-public'

# Getting top 100 songs of a particular date
date = input('What year you want to travel? Type date in this format YYYY-MM-DD: ')
url = f'https://www.billboard.com/charts/hot-100/{date}/'
response = requests.get(url)
billboard = response.text
soup = BeautifulSoup(billboard, 'html.parser')
# songs_list = [song.text for song in soup.select('li ul li h3')]
songs_list = [
    "Tum Hi Ho",
    "Pehli Nazar Mein",
    "Raabta",
    "Jeene Laga Hoon",
    "Tera Ban Jaunga",
    "Bekhayali",
    "Mere Rashke Qamar",
    "Tujh Mein Rab Dikhta Hai",
    "Tera Hone Laga Hoon",
    "Janam Janam",
    "Dil Diyan Gallan",
    "Hawa Banke",
    "Tera Yaar Hoon Main",
    "Galliyan",
    "Samjhawan",
    "Tum Mile",
    "Hasi Ban Gaye",
    "Kabira",
    "Naino Ne Baandhi",
    "Zaalima",
    "Channa Mereya",
    "Gerua",
    "Pee Loon",
    "Kun Faya Kun",
    "Sun Saathiya",
    "Pal Pal Dil Ke Paas",
    "Jeene Ke Hain Chaar Din",
    "Gallan Goodiyaan",
    "Dilliwali Girlfriend",
    "Kala Chashma",
    "High Rated Gabru",
    "Suit Suit",
    "Lamborghini",
    "Kya Baat Ay",
    "Naah",
    "Coca Cola",
    "Laung Laachi",
    "Patola",
    "Ishare Tere",
    "Tareefan",
    "Lahore",
    "Qismat",
    "Laal Ghagra",
    "Ghoomar",
    "Nachde Ne Saare",
    "Bom Diggy Diggy",
    "Tamma Tamma Again",
    "Kar Gayi Chull",
    "Akh Lad Jaave",
    "O Saki Saki",
    "Genda Phool",
    "Dilbar",
    "Pachtaoge",
    "Ve Maahi",
    "Jab Tak",
    "Kehte Hain Khuda Ne",
    "Saari Raat",
    "Despacito (Punjabi Mix)",
    "Soch Na Sake",
    "Mann Bharrya",
    "Ik Vaari Aa",
    "Aaj Se Teri",
    "Enna Sona",
    "Ishq Mubarak",
    "Tere Sang Yaara",
    "Sunn Raha Hai",
    "Aaj Phir Tumpe",
    "Sanam Re",
    "Saware",
    "Lo Safar",
    "Khairiyat",
    "Thodi Jagah",
    "Kaise Hua",
    "Mere Sohneya",
    "Duniyaa",
    "Photo",
    "Coka",
    "Laare",
    "Aankh Marey",
    "Sauda Khara Khara",
    "Morni Banke",
    "Dil Chori",
    "Aankhon Se Batana",
    "Baaki Baatein Peene Baad",
    "Baby Doll",
    "Lovely",
    "Kamariya",
    "Hookah Bar",
    "Subha Hone Na De",
    "Badtameez Dil",
    "Balam Pichkari",
    "Besharmi Ki Height",
    "Chittiyaan Kalaiyaan",
    "Sooraj Dooba Hai",
    "Let’s Nacho",
    "Nashe Si Chadh Gayi",
    "Kala Doreya",
    "Phir Bhi Tumko Chaahunga",
    "Dheere Dheere Se",
    "Tum Jo Aaye",
    "Hamari Adhuri Kahani",
    "Muskurane",
    "Main Rang Sharbaton Ka",
    "Duaa",
    "Sunn Raha Hai (Female)",
    "Zehnaseeb",
    "Mast Magan",
    "Sooiyan",
    "Laal Ishq",
    "Hasi",
    "Kabhi Jo Baadal Barse",
    "Manwa Laage",
    "Bolna",
    "Sab Tera",
    "Vaaste",
    "Kaun Tujhe",
    "Sanam Teri Kasam",
    "Rabba",
    "Dil Cheez Tujhe Dedi",
    "Lut Gaye",
    "Saibo",
    "Tu Hi Yaar Mera",
    "Dil Na Jaaneya",
    "Dil Hi Toh Hai",
    "Zinda",
    "Agar Tum Saath Ho",
    "Hawayein",
    "Khuda Jaane",
    "Tum Se Hi",
    "Mere Haath Mein",
    "Kaise Mujhe Tum Mil Gayi",
    "Ae Dil Hai Mushkil",
    "Tere Liye",
    "Proper Patola",
    "Makhna",
    "Milegi Milegi",
    "Bom Diggy",
    "O Saathi",
    "Gali Gali",
    "Saudagar Sauda",
    "Tamma Tamma",
    "Zingaat",
    "Odhani",
    "Dhoom Dhadakka"
]


# Adding songs into the playlist
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope=SCOPE))


user_id = sp.me()['id']
playlist_name = f'{date} Top 100 songs'
playlist_description = f'This playlist contains top 100 songs of {date}'

playlist = sp.user_playlist_create(user=user_id,
                                   name=playlist_name,
                                   description=playlist_description,
                                   public=True)

playlist_id = playlist['id']
print(f'Playlist {playlist_name} has been created successfully')
print(f'Playlist ID: {playlist_id}')

for song in songs_list:
    track_name = song
    results = sp.search(q=track_name, limit=1)
    song = results['tracks']['items'][0]
    song_uri = song['uri']
    sp.playlist_add_items(playlist_id=playlist_id, items=[song_uri])
    print('Song Added successfully')

