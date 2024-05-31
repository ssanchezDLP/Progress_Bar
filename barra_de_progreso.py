# ------------------------------------------------------------
# Manera 1  ||||||||||||||||||||||||||||||||||||||||||||||||| 
#------------------------------------------------------------

# from tqdm.auto import tqdm

# for i in tqdm(range(100001)):
#     #aquí tendría que estar tu código pero (no sé como enlazarlo)


# ------------------------------------------------------------
# Manera 2  ||||||||||||||||||||||||||||||||||||||||||||||||| 
#------------------------------------------------------------

from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 10
    download = 0
    speed = 0.05
    while(download<GB):
        time.sleep(0.05)
        bar['value']+= (speed/GB) * 100
        download += speed
        porcentaje.set(str(int(download/GB)*100)+"%")
        texto.set(str(download)+"/"+str(GB)+" GB completado/s")
        window.update_idletasks()


window= Tk()

porcentaje= StringVar()
texto= StringVar()


bar= Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

textoLabel= Label(window, textvariable=porcentaje).pack()

comLabel= Label(window, textvariable=texto).pack()

boton= Button(window, text="Descargar", command=start).pack()

window.mainloop
