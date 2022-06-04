import bge
import aud
from collections import OrderedDict

class Seta(bge.types.KX_PythonComponent):
    # Put your arguments here of the format ("key", default_value).
    # These values are exposed to the UI.
    args = OrderedDict([
    ])

    def start(self, args):
        pass

    def update(self):
        key = bge.logic.keyboard.inputs
        
        if key[bge.events.WKEY].activated:
            self.object.worldPosition.y = -1
            self.audio_menu()
            
        elif key[bge.events.SKEY].activated:
            self.object.worldPosition.y = -2 
            self.audio_menu()
        
        
        if key[bge.events.ENTERKEY].activated:
            if self.object.worldPosition.y == -1:
                self.object.scene.replace("Game") 
                self.audio_menu()
            elif self.object.worldPosition.y == -2:
                self.object.scene.end() 
                self.audio_menu()
                
        
    
    def audio_menu(self):
        device = aud.device()
        sound = aud.Factory.file(bge.logic.expandPath("//som_click2.mp3"))
        device.play(sound)