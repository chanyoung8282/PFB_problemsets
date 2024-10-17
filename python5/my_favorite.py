#!/usr/bin/env python3
favorite = {'book':'Perfume', 'song' : 'Back Down', 'tree' : 'Cedar'}
fav_thing = 'book'
print(fav_thing)
print(favorite[fav_thing])
fav_tree = 'tree'
print(favorite[fav_tree])
favorite['organism'] = 'cat'
print(favorite['organism'])
print(favorite)

for key in favorite:
	print(key, favorite[key])

books = input("what's your favorite book: ")
print(books)
songs = input("what's your favorite song: ")
print(songs)
tree = input("what's your favorite tree: ")
print(tree)
organisms = input("what's yout favorite organism: ")
print(organisms)

favorite['book'] = books
favorite['song'] = songs
favorite['tree'] = tree
favorite['organism'] = organisms
print(favorite)
