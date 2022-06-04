import bge
import aud
from collections import OrderedDict

class Ball(bge.types.KX_PythonComponent):
    # Put your arguments here of the format ("key", default_value).
    # These values are exposed to the UI.
    args = OrderedDict([
    ])

    def start(self, args):
        self.dir_x = -0.1
        self.dir_y = 0.1
        self.count1 = 0
        self.count2 = 0
        
        self.score1 = self.object.scene.objects["score1"] #referenciando o objeto do score 1 (da esquerda)
        self.score2 = self.object.scene.objects["score2"] # minha variavel score2 é igual ao meu objeto score2
        self.text_win = self.object.scene.objects["youwin"] 
        self.text_rejogar = self.object.scene.objects["text_rejogar"]
        
        self.pts1 = 0
        self.pts2 = 0
        
        self.play = True
        
        

    def update(self):
        self.rejogar() # esta fora da flag pois mesmo que o jogo termine deve ser possivel reiniciar
        if self.play:
            self.moveball()
            self.colision()
            self.win()
            self.pts()
            

        
        
    def moveball(self):
        self.object.applyMovement([self.dir_x, self.dir_y, 0])
        
    def colision(self):
        if self.object.collide("player1")[0]:
            self.count1 += 0.0061
            self.dir_x = 0.1
            self.dir_x += self.count1
            self.audio_impacto()
            
            
        elif self.object.collide("player2")[0]:
            self.count2 -= -0.0061
            self.dir_x = -0.1
            self.dir_x -= self.count2
            self.audio_impacto()
            
            
        if self.object.worldPosition.y > 5.34976:
            self.dir_y = -0.083
            self.audio_parede()
            
        elif self.object.worldPosition.y < -5.34976:
            self.dir_y = 0.083
            self.audio_parede()
            
    def pts(self):
        if self.object.worldPosition.x > 10.1454:
            self.pts1 += 1
            self.object.worldPosition.x = 0
            self.object.worldPosition.y = 0
            self.dir_x = -0.1
            self.dir_y = -0.1
            self.score1.text = str(self.pts1)
            self.count1 = 0 # zerando os contadores de acumuladores de velocidade
            self.count2 = 0 # zerando os contadores de acumuladores de velocidade
            if self.pts1 != 3:
                self.audio_pontuacao()
            
        elif self.object.worldPosition.x < -10.1454:
            self.pts2 += 1
            self.object.worldPosition.x = 0
            self.object.worldPosition.y = 0
            self.dir_x = 0.1
            self.dir_y = 0.1
            self.score2.text = str(self.pts2)
            self.count1 = 0 # zerando os contadores de acumuladores de velocidade
            self.count2 = 0 # zerando os contadores de acumuladores de velocidade
            if self.pts2 != 3:
                self.audio_pontuacao()
            
            
    def win(self):
        if self.pts1 == 3 or self.pts2 == 3:
            self.text_win.setVisible(True)
            self.text_rejogar.setVisible(True)
            self.audio_youwin()
            self.play = False
        else:
            self.text_win.setVisible(False)
            self.text_rejogar.setVisible(False)
            
    def rejogar(self):
        key = bge.logic.keyboard.inputs
        
        if key[bge.events.RKEY].active and self.play == False:

            bge.logic.restartGame()        
            
            
    def audio_impacto(self):
        device = aud.device()
        sound = aud.Factory.file(bge.logic.expandPath("//som_batida1.mp3"))
        device.play(sound)
        
    def audio_pontuacao(self):
        device = aud.device()
        sound = aud.Factory.file(bge.logic.expandPath("//som_pontuacao.mp3"))
        device.play(sound)
        
    def audio_parede(self):
        device = aud.device()
        sound = aud.Factory.file(bge.logic.expandPath("//som_boing.mp3"))
        device.play(sound)
        
    def audio_youwin(self):
        device = aud.device()
        sound = aud.Factory.file(bge.logic.expandPath("//som_youwin1.mp3"))
        device.play(sound)
         
        