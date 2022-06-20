import requests
import subprocess
import shlex
from selenium import webdriver
from head import header
from funcs import longest, spaces, takinOurJobs

header()

albums=[]; tracklist=[]; previews=[];a=0
		
search = input('\nSearch Artist: ')	
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

print('Search Returned '+str(len(albums))+' albums. \n')

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

option=input("\n\nAlbum Number: ")
albumTracks=requests.get(tracklist[int(option)-1]).json()

header()
print("ALBUM : "+tracks['data'][int(option)-1]['album']['title']);print("-"*80);a=0
while a < len(albumTracks['data']):
	print(str(a+1)+" - "+albumTracks['data'][a]['title'])
	previews.append(albumTracks['data'][a]['preview'])
	a +=1

previewIndex = input("\nChoose a 30sec preview: ")
browser = webdriver.Chrome()
browser.set_window_size(100,100);browser.get(previews[int(previewIndex)-1])

print("\nEnjoy.\n")
