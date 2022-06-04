import bge
from collections import OrderedDict

class Player2(bge.types.KX_PythonComponent):
    # Put your arguments here of the format ("key", default_value).
    # These values are exposed to the UI.
    args = OrderedDict([
    ])

    def start(self, args):
        pass

    def update(self):
        self.movimento()
        self.object.worldPosition.x = 8.13884
    
    def movimento(self):
        key = bge.logic.keyboard.inputs
        
        if key[bge.events.OKEY].active:
            if self.object.worldPosition.y > 5.34976:
                pass
            else:
                self.object.applyMovement([0, 0.13, 0]) # se refere ao objeto deste script
        elif key[bge.events.KKEY].active:
            if self.object.worldPosition.y < -5.34976:
                pass
            else:
                self.object.applyMovement([0, -0.13, 0])
