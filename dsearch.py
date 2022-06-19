import requests
import subprocess
import shlex
from head import header

def length(value,i):
	print(value[i])
	if len(value[(i)] > v
	
	

header()

albums = [];tracklist=[];a=0
search = input('Search Artist: ')

header()
artist = requests.get('http://api.deezer.com/search/artist/', params={'q':search.replace(" ","+")}).json()
page = str(artist['data'][0]['tracklist']).replace('limit=50','limit=150')

tracks = requests.get(page).json()
while a < len(tracks['data']):
	albums.append(tracks['data'][a]['album']['title'])
	tracklist.append(tracks['data'][a]['album']['tracklist'])
	a +=1
	if a == len(tracks['data']):
		a = 0; break



#while a < len(albums):
	#print (str(a)+" - "+albums[a]+"   				|    ", end='');print(str(a+1)+" - "+albums[a])
	#a +=2

option=input("\nAlbum Number: ")
header()
albumTracks=requests.get(tracklist[option]).json()
while a < len(albumTracks['data']):
	print(str(a)+" - "+albumTracks['data'][a]['title'])
	a +=1
	
