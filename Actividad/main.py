import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle    
import matplotlib.animation as manimation
from skimage.io import imread
from skimage import transform
import matplotlib

fondo = imread("parque.jpg")
fondo = transform.rescale(image=fondo,scale=0.1,channel_axis=2)

tubo = imread("torre.png")

gondola = imread("gondola.png")

v_i = 0
y_i = 300
GRAVEDAD = 9.81
masa = 500
ultimaI = 0

t_i = 0
t_f = 300
n = 1000
h = (t_f - t_i) / n

calcularK = lambda masa,gravedad,velocidad : (masa*gravedad)/velocidad


t = np.arange(t_i,t_f+h,h)
altura = np.zeros((n+1))
velocidad = np.zeros((n+1))
aceleracion = np.zeros((n+1))


altura[0] = y_i
velocidad[0] = v_i
aceleracion[0] = 0

for i in range(n-1):
    k1 = h*velocidad[i]
    l1 = h*-GRAVEDAD

    k2 = h*(velocidad[i]+l1/2)
    l2 = h*-GRAVEDAD

    k3=h*(velocidad[i]+l2/2)
    l3=h*-GRAVEDAD

    k4=h*(velocidad[i]+l3)
    l4=h*-GRAVEDAD

    altura[i+1]=altura[i]+(k1+2*k2+2*k3+k4)/6
    velocidad[i+1]= velocidad[i]+(l1+2*l2+2*l3+l4)/6
    aceleracion[i+1] = -9.81

    if altura[i+1] <= 180:
        ultimaI = i
        break




k = -1000

f2 = lambda k,velocidad,masa,gravedad: (k*velocidad/masa)-gravedad

for i in range(ultimaI,n-1):
    k1=h*velocidad[i]
    l1=h*f2(k,velocidad[i],masa,GRAVEDAD)

    k2=h*(velocidad[i]+l1/2)
    l2=h*f2(k,velocidad[i]+l1/2,masa,GRAVEDAD)

    k3=h*(velocidad[i]+l2/2)
    l3=h*f2(k,velocidad[i]+l2/2,masa,GRAVEDAD)

    k4=h*(velocidad[i]+l3)
    l4=h*f2(k,velocidad[i]+l3,masa,GRAVEDAD)

    altura[i+1] = altura[i]+(k1+2*k2+2*k3+k4)/6
    velocidad[i+1]= velocidad[i]+(l1+2*l2+2*l3+l4)/6
    aceleracion[i+1] = f2(k,velocidad[i+1],masa,GRAVEDAD)

    if altura[i+1] <= 80:
        ultimaI = i
        break

k = -3500

f2 = lambda k,velocidad,masa,gravedad : (k*velocidad/masa)-gravedad


for i in range(ultimaI,n-1):
    k1=h*velocidad[i]
    l1=h*f2(k,velocidad[i],masa,GRAVEDAD)

    k2=h*(velocidad[i]+l1/2)
    l2=h*f2(k,velocidad[i]+l1/2,masa,GRAVEDAD)

    k3=h*(velocidad[i]+l2/2)
    l3=h*f2(k,velocidad[i]+l2/2,masa,GRAVEDAD)

    k4=h*(velocidad[i]+l3)
    l4=h*f2(k,velocidad[i]+l3,masa,GRAVEDAD)

    altura[i+1]=altura[i]+(k1+2*k2+2*k3+k4)/6
    velocidad[i+1]= velocidad[i]+(l1+2*l2+2*l3+l4)/6
    aceleracion[i+1] = f2(k,velocidad[i+1],masa,GRAVEDAD)

    if altura[i+1] < 50:
        break

altura = altura[:np.where(altura[1:] <= 50)[0][0]]
velocidad = velocidad[:altura.shape[0]]
aceleracion = aceleracion[:altura.shape[0]]

t = t[:altura.shape[0]]

limiteDerecha = 2.4

fig,ax = plt.subplots()


configuracionesPlots = {
    "simulacion.mp4":{
        "xlabel":"Metros",
        "ylabel":"Metros",
        "title":"Simulación de góndola",
        "xlim":(0,600),
        "ylim":(0,350),
        "grid":False,
        "Datos":altura
    },

    "velocidad.mp4":{
        "xlabel":"Tiempo (segundos)",
        "ylabel":"Velocidad (m/s)",
        "title":"Velocidad vs. tiempo",
        "xlim":(0,t[-1]),
        "ylim":(min(velocidad)-1,max(velocidad)+1),
        "grid":True,
        "Datos":velocidad
    },

    "Altura.mp4":{
        "xlabel":"Tiempo (segundos)",
        "ylabel":"Metros",
        "title":"Tiempo vs. altura",
        "xlim":(0,t[-1]),
        "ylim":(min(altura)-1,max(altura)+1),
        "grid":True,
        "Datos":altura
    },

    "Aceleracion.mp4":{
        "xlabel":"Tiempo (segundos)",
        "ylabel":"m/s\u00b2",
        "title":"Tiempo vs. aceleración",
        "xlim":(0,t[-1]),
        "ylim":(min(aceleracion)-1,max(aceleracion)+1),
        "grid":True,
        "Datos":aceleracion
    }
}

for nombre in configuracionesPlots:
    ax.clear()
    FFMpegWriter =  manimation.writers["ffmpeg"]
    metadata = dict(title=configuracionesPlots[nombre]["title"],artist="FregonsoTECs",comment="Simulacion de frenado electromagnetico")
    writer = FFMpegWriter(fps=60,metadata=metadata)
    configuraciones = configuracionesPlots[nombre]

    with writer.saving(fig,nombre,100):
        for i in range(len(t)-1):
            datos = configuraciones["Datos"]
            ax.set_xlabel(configuraciones["xlabel"])
            ax.set_ylabel(configuraciones["ylabel"])
            ax.set_title(configuraciones["title"])
            ax.grid(configuraciones["grid"])
            ax.set_xlim(configuraciones["xlim"])
            ax.set_ylim(configuraciones["ylim"])
            

            if nombre == "simulacion.mp4":
                
                ax.set_xticklabels(["0","","","","","4"])
                ax.set_yticklabels(["0","","","","","","100"])
                
                
                ax.imshow(fondo,origin="lower")
                
                #ax.add_patch(Rectangle((270,180),50,120,facecolor="yellow"))
                #ax.add_patch(Rectangle((270,80),50,100,facecolor="blue"))
                #ax.add_patch(Rectangle((270,50),50,30,facecolor="magenta"))

                ax.imshow(tubo,extent=(210,380,5,400))

                if altura[i] <= 50:
                    break

                ax.imshow(gondola,extent=(194,194+76+50+76+10,altura[i],altura[i]+50))
                
                writer.grab_frame()

                ax.clear()
                continue

            if datos[i] >= 0 and i > 0 and nombre != "Altura.mp4" and nombre != "Aceleracion.mp4":
                break

            if nombre == "Altura.mp4":
                ax.set_yticklabels(["0","","","","","100"])
                if datos[i] <= 0:
                    break

            ax.plot(t[i],datos[i],"ro",markersize=10)
            ax.plot(t[0:i+1],datos[0:i+1])

            writer.grab_frame()
                
            ax.clear()
