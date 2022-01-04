import pygame

#The asset manager allows using store assets by their names
#You can access assets by name or by index
#Calling assets by name may be useful for visual novels or when a lot of assets exit and you can't remember the index location

#ToDo:
#pygame doesn't allow loading music. This is to save room it is played form source.
#Add Music Store name in assets
#Test

class Asset_Manager:
    def __init__(self):
        self.assets = []
        self.images = {}
        self.videos = {}
        self.music = {}
        self.sounds = {}
        return
    #images
    def load_image(self,name,file_name):
        self.assets.append((pygame.image.load("assets/" + file_name).convert_alpha()))
        index = len(self.assets)-1
        self.images[name]=index
        return index

    def get_image(self,name):
        r = self.images.get(name)
        if r:
            return self.assets[r]
        print("Image: " + name + "doesn't exist")
        return 

    def image_index(self,name):
        return self.images.get(name)    #will return Null if doesn't exist. Address out of range issue will usually occur

    def remove_image(self,name):
        self.assets.pop(self.images.get(name))
        self.images.pop(name)
        return
    #movies
    def load_movie(self,name,file_name):
        self.assets.append((pygame.movie.Movie("assets/"+ file_name)))
        index = len(self.assets)-1
        self.videos[name]=index
        return index

    def get_movie(self,name):
        r = self.videos.get(name)
        if r:
            return self.assets[r]
        print("Movie: " + name + "doesn't exist")
        return

    def movie_index(self,name):
        return self.videos.get(name)    #will return Null if doesn't exist. Address out of range issue will usually occur

    def remove_movie(self,name):
        self.assets.pop(self.videos.get(name))
        self.videos.pop(name)
        return
    #sounds
    def load_sound(self,name,file_name):
        self.assets.append(pygame.mixer.Sound("assets/" + file_name))
        index = len(self.assets)-1
        self.sounds[name]=index
        return index

    def get_sound(self,name):
        r = self.sounds.get(name)
        if r:
            return self.assets[r]
        print("Sound: " + name + "doesn't exist")
        return

    def sound_index(self,name):
        return self.sounds.get(name)    #will return Null if doesn't exist. Address out of range issue will usually occur

    def remove_sound(self,name):
        self.assets.pop(self.sounds.get(name))
        self.sounds.pop(name)
        return

    #pygame doesn't load music into an object just memory
    #So all that can be stored is the file name
    #That can be stored directly in the dictionary and doesn't need the asset array
    #


    