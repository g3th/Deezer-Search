import requests
import subprocess
import shlex
from head import header
from funcs import longest, spaces, takinOurJobs

header()

albums=[]; tracklist=[]; a=0
		
search = 'Herbie Hancock' #input('Search Artist: ');header()	
header()

artist = requests.get('http://api.deezer.com/search/artist/', params={'q':search.replace(" ","+")}).json()
page = str(artist['data'][0]['tracklist']).replace('limit=50','limit=150')
tracks = requests.get(page).json()

while a < len(tracks['data']):
	trackRequest = tracks['data'][a]['album']['title']
	trackRequest = takinOurJobs(trackRequest)
	if len(trackRequest) > 30:
		albums.append(trackRequest.replace(trackRequest[28:],'..'))	
	else:	
		albums.append(trackRequest)
	tracklist.append(tracks['data'][a]['album']['tracklist'])
	a +=1
	if a == len(tracks['data']):
		a = 0; break

albums = list(dict.fromkeys(albums))
tracklist = list(dict.fromkeys(tracklist))

print('Search Returned '+str(len(albums)+1)+' albums, duplicate entries were omitted.\n')
print(longest(albums))

while a != len(albums):
	try:
		if a < 10:
			print (' '+str(a+1)+" - "+albums[a]+" "*spaces(albums,a)+"| ",end='')
			print(''+str(a+2)+" - "+albums[a+1])
		else:
			print (str(a+1)+" - "+albums[a]+" "*spaces(albums,a)+"| ",end='')
			print(str(a+2)+" - "+albums[a+1])
		a +=2
	except IndexError:
		a = 0
		break


option=input("\nAlbum Number: ")
albumTracks=requests.get(tracklist[int(option)]).json()
header()

print("ALBUM : "+tracks['data'][int(option)]['album']['title']);print("-"*65)
while a < len(albumTracks['data']):
	print(str(a)+" - "+albumTracks['data'][a]['title'])
	a +=1
print("\n")
