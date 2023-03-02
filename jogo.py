import threading as th
import tkinter as tk
import objetos

class Janela(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


app = Janela("Jogo")
app.geometry("700x700+300+0")

fundo = tk.PhotoImage(file = "sky.gif")

titulo = tk.Label(app, text = "Knife escape", font = ("Verdana", 30))
titulo.pack()

canvas = tk.Canvas(app, width = 600, height = 600, bg = "white")
canvas.pack()
canvas.focus_set()
id_fundo = canvas.create_image(300, 300, image = fundo)

bola = objetos.Ball(canvas, app)

morrer = th.Thread(target = bola.perder)
morrer.daemon = True
morrer.start()

pontos = th.Thread(target = bola.aumentar_pontuacao)
pontos.daemon = True
pontos.start()

canvas.bind("<Right>", bola.mover_direita)
canvas.bind("<Left>", bola.mover_esquerda)

faca = objetos.Faca(canvas)

criar_facas = th.Thread(target = faca.criar_faca)
criar_facas.daemon = True
criar_facas.start()
cair_facas = th.Thread(target = faca.cair)
cair_facas.daemon = True
cair_facas.start()

app.mainloop()
