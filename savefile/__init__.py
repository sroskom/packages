#for use with a kivy app

from kivy.app import App
from kivy.storage.jsonstore import JsonStore
import os

class SaveFile:
    def __init__(self,
            game = 'game',
            file_ext = '.json',
            directory = '.',
            local = True,
            *args, **kwargs):
        
        if not local:
            user_data_dir = App.get_running_app().user_data_dir
            directory = os.path.join(user_data_dir,directory)
        self.completePath = os.path.join(directory,
                game + file_ext)
        
    def load(self, *args, **kwargs):
        self.store = JsonStore(self.completePath)
        if self.store.count() < 1:
            return False
        else:
            return True

    def set(self,key,value,topKey='p1'):
        self.store[topKey] = {key:value}

    def get(self,key,topKey='p1'):
        return self.store[topKey][key]
