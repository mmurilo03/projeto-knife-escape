import threading as th
import tkinter as tk
from random import choice

class Ball:

    def __init__(self, canvas, janela):
        self.janela = janela
        self.canvas = canvas
        self.pontuacao = 0
        self.vivo = True
        self.imagem = tk.PhotoImage(file ="bola.gif")
        self.id = canvas.create_oval([280, 520, 320, 560], fill = "cyan", tag = "ball")
        self.id_bola = canvas.create_image(300, 540, image = self.imagem)
        self.chao = canvas.create_rectangle([0,560,600,600], fill = "green")

    def mover_direita(self, *args):
        posicao = self.canvas.coords(self.id)
        posicao_imagem = self.canvas.coords(self.id_bola)
        if 593 in posicao:
            pass
        else:
            self.canvas.move(self.id, 7, 0)
            self.canvas.move(self.id_bola, 7, 0)

    def mover_esquerda(self, *args):
        posicao = self.canvas.coords(self.id)
        posicao_imagem = self.canvas.coords(self.id_bola)
        if 7 in posicao:
            pass
        else:
            self.canvas.move(self.id, -7, 0)
            self.canvas.move(self.id_bola, -7, 0)


    def perder(self, *args):
        try:
            while self.vivo:
                posicao = self.canvas.coords(self.id)
                tag_faca = self.canvas.find_withtag("faca")
                tag_ball = self.canvas.find_overlapping(*self.canvas.coords(self.id))
                for item in tag_ball:
                    if item in tag_faca:
                        pontos = self.pontuacao
                        self.vivo = False
                        pontuacao_final = tk.Label(self.janela, text = "Pontuação final: "+str(pontos), font = ("Verdana", 20))
                        self.canvas.delete(item)
                        self.canvas.delete(self.id)
                        self.canvas.delete(self.id_bola)

                        pontuacao_final.pack()
                        #print(pontos)
        except:
            pass

        
    
    def aumentar_pontuacao(self, *args):
        try:
            while self.vivo:
                tag_faca = self.canvas.find_withtag("faca")
                zona = self.canvas.find_overlapping(*self.canvas.coords(self.chao))
                for item in zona:
                    if item in tag_faca:
                        self.canvas.delete(item)
                        self.pontuacao += 1
        except:
            pass

class Faca:

    def __init__(self, canvas):
        self.canvas = canvas
        self.tempo_de_criacao = 1.3
        #self.id = canvas.create_polygon([0,0,0,100,20,90,40,40,20,40,20,0,0,0], tag = "faca")

    def criar_faca(self, *args):
        try:
            local_de_inicio = choice(range(550))
            posicao = [10, 10, 10, 65, 20, 48, 25, 30, 18, 30, 20, 10, 18, 9, 11, 9, 10, 10]
            for num in range(18):
                if num % 2 == 0:
                    posicao[num] += local_de_inicio

            faca = self.canvas.create_polygon(*posicao, tag = "faca")
            if self.tempo_de_criacao > 0.4:
                self.tempo_de_criacao -= 0.008

            if self.tempo_de_criacao < 1.0 and self.tempo_de_criacao > 0.75:
                local_de_inicio = choice(range(550))
                posicao = [10, 10, 10, 65, 20, 48, 25, 30, 18, 30, 20, 10, 18, 9, 11, 9, 10, 10]
                for num in range(18):
                    if num % 2 == 0:
                        posicao[num] += local_de_inicio

                faca = self.canvas.create_polygon(*posicao, tag = "faca")

            elif self.tempo_de_criacao < 0.75:
                local_de_inicio = choice(range(550))
                posicao = [10, 10, 10, 65, 20, 48, 25, 30, 18, 30, 20, 10, 18, 9, 11, 9, 10, 10]
                for num in range(18):
                    if num % 2 == 0:
                        posicao[num] += local_de_inicio

                faca = self.canvas.create_polygon(*posicao, tag = "faca")
                local_de_inicio = choice(range(550))
                posicao = [10, 10, 10, 65, 20, 48, 25, 30, 18, 30, 20, 10, 18, 9, 11, 9, 10, 10]
                for num in range(18):
                    if num % 2 == 0:
                        posicao[num] += local_de_inicio

                faca = self.canvas.create_polygon(*posicao, tag = "faca")

            if self.canvas:
                th.Timer(self.tempo_de_criacao, self.criar_faca).start()
        except:
            pass

    def cair(self, *args):
        try:
            while True:
                self.canvas.move("faca", 0, 20)
                self.canvas.update()
                self.canvas.after(100)
        except:
            pass
