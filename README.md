# Simulación de Góndola con Frenado Electromagnético

Este proyecto en Python realiza una simulación de la caída y frenado de una góndola sobre una torre, generando cuatro videos en formato MP4:
- **simulación.mp4**: recorrido vertical de la góndola junto al fondo y la torre.  
- **velocidad.mp4**: curva de velocidad vs. tiempo.  
- **Altura.mp4**: curva de altura vs. tiempo.  
- **Aceleracion.mp4**: curva de aceleración vs. tiempo.

La simulación emplea el método de Runge-Kutta de orden 4 para modelar el movimiento con diferentes constantes de frenado.


## Objetivo de la actividad
1. Aplicar el método de Runge-Kutta de 4º orden para integrar ecuaciones de movimiento con y sin fuerza de frenado.  
2. Visualizar resultados físicos (altura, velocidad, aceleración) en videos.  
3. Generar animaciones MP4 usando `matplotlib.animation.FFMpegWriter`.  
4. Practicar el escalado y posicionamiento de imágenes superpuestas con `skimage` y `matplotlib`.

## Requisitos técnicos
- **Python 12**  
- Bibliotecas:
  - `numpy`  
  - `matplotlib`  
  - `scikit-image`  
- **FFmpeg** instalado y accesible en la variable de entorno `PATH` (para el writer de MP4).  
- Imágenes de entrada:
  - `parque.jpg` (fondo)  
  - `torre.png` (torre)  
  - `gondola.png` (góndola)  


## Instalación de Dependencias
  - pip install numpy matplotlib scikit-image
  - Asegúrate de tener ffmpeg instalado con: `ffmpeg -version`

## Ejecución de la Solución
  - Ejecuta el comando `python main` para iniciar la ejecución.

## Uso y Personalización
  - Parámetros de la Simulación.
    - y_i: altura inicial de la góndola (por defecto 300 m).
    - v_i: velocidad inicial (por defecto 0 m/s).
    - masa: masa de la góndola (por defecto 500 kg).
    - GRAVEDAD: aceleración gravitatoria (9.81 m/s²).
    - Constantes de frenado k: ajustables en tres fases de la simulación.
