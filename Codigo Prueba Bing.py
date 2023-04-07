import cv2
import numpy as np
import pyautogui
import time
from multiprocessing import Pool

img_senalar_path = r"C:\Users\Leonardo Quiroga\Desktop\Script\senalar_mitad_1366.jpg"
img_cargado_path = r"C:\Users\Leonardo Quiroga\Desktop\Script\full_mitad_1366.jpg" 
img_lleno_path = r"C:\Users\Leonardo Quiroga\Desktop\Script\lleno_mitad_1366.jpg"  
img_zaap_path = r"C:\Users\Leonardo Quiroga\Desktop\Script\zaap_mitad_1366.jpg"   
img_hierro_path = r"C:\Users\Leonardo Quiroga\Desktop\Script\hierro_mitad_1366.jpg"
img_calavera_path = r"C:\Users\Leonardo Quiroga\Desktop\Script\calavera_mitad_1366.jpg"
img_monton_path = r"C:\Users\Leonardo Quiroga\Desktop\Script\monton_mitad_1366.jpg"  
img_ignorar_path = r"C:\Users\Leonardo Quiroga\Desktop\Script\ignorar_mitad_1366.jpg"

img_senalar = cv2.imread(img_senalar_path, cv2.IMREAD_GRAYSCALE)
img_cargado = cv2.imread(img_cargado_path, cv2.IMREAD_GRAYSCALE)
img_lleno = cv2.imread(img_lleno_path, cv2.IMREAD_GRAYSCALE)
img_zaap = cv2.imread(img_zaap_path, cv2.IMREAD_GRAYSCALE)
img_hierro = cv2.imread(img_hierro_path, cv2.IMREAD_GRAYSCALE)
img_calavera = cv2.imread(img_calavera_path, cv2.IMREAD_GRAYSCALE)
img_monton = cv2.imread(img_monton_path, cv2.IMREAD_GRAYSCALE)
img_ignorar = cv2.imread(img_ignorar_path, cv2.IMREAD_GRAYSCALE)

#Umbral determinado
threshold = 0.8

#Especificar la región
region = (80, 100, 683, 640) 

Cambiosala_coords = [(481, 306), (519, 246), (201, 307), (128, 270), (480, 430), (552, 470), (202, 431), (128, 468)]

#Iniciar en la sala 1 "Hierro 1"
Sala_actual = 1
Turno_actual = 0
Banco = 0
Rendicion = 0
Calavera = True

def find_matches(screenshot_gray, template):
    # Busca coincidencias entre la plantilla y la captura de pantalla
    res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

    # Encuentra la ubicación de las coincidencias con un valor superior al umbral definido
    loc = np.where(res >= threshold)

    return loc

if __name__ == '__main__':
    # Crea un grupo de procesos con tantos procesos como núcleos de CPU disponibles
    pool = Pool()

    while True:
        start_time = time.time()
        # Toma una captura de pantalla de la región definida y la convierte a escala de grises
        screenshot = np.array(pyautogui.screenshot(region=region))
        screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

        # Utiliza múltiples procesos para buscar coincidencias en paralelo
        loc_senalar = pool.apply_async(find_matches, [screenshot_gray, img_senalar])
        loc_cargado = pool.apply_async(find_matches, [screenshot_gray, img_cargado])
        loc_lleno = pool.apply_async(find_matches, [screenshot_gray, img_lleno])
        loc_zaap = pool.apply_async(find_matches, [screenshot_gray, img_zaap])
        loc_hierro = pool.apply_async(find_matches, [screenshot_gray, img_hierro])
        loc_calavera = pool.apply_async(find_matches, [screenshot_gray, img_calavera])
        loc_monton = pool.apply_async(find_matches, [screenshot_gray, img_monton])
        loc_ignorar = pool.apply_async(find_matches, [screenshot_gray, img_ignorar])
        
        # Obtiene los resultados de las búsquedas en paralelo
        loc_senalar = loc_senalar.get()
        loc_cargado= loc_cargado.get()
        loc_lleno = loc_lleno.get()
        loc_zaap = loc_zaap.get()
        loc_hierro = loc_hierro.get()
        loc_calavera = loc_calavera.get()
        loc_monton = loc_monton.get()
        loc_ignorar = loc_ignorar.get()
            
        # Si se encuentra la imagen "img_senalar"
        if len(loc_senalar[0]) > 0:
            # Click en Listo
            pyautogui.click(608, 493)

            # Tiempo de espera para turno crujibola
            time.sleep(12.0)

            # Acosante 1
            pyautogui.moveTo(537, 581) 
            time.sleep(0.8)    
            pyautogui.click()     
            time.sleep(0.1) 
            # Enemigo
            pyautogui.moveTo(645, 500) 
            time.sleep(0.8)  
            pyautogui.click()         
            time.sleep(0.1)  
            # Acosante 1
            pyautogui.moveTo(537, 581) 
            time.sleep(0.8)    
            pyautogui.click()     
            time.sleep(0.1) 
            # Enemigo
            pyautogui.moveTo(615, 500) 
            time.sleep(0.8)  
            pyautogui.click()         
            time.sleep(0.1)  
            # Acosante 1
            pyautogui.moveTo(488, 581) 
            time.sleep(0.8)    
            pyautogui.click()     
            time.sleep(0.1) 
            # Enemigo
            pyautogui.moveTo(615, 500) 
            time.sleep(0.8)  
            pyautogui.click()         
            time.sleep(0.1)  
            # Acosante 2
            pyautogui.moveTo(488, 581) 
            time.sleep(0.8)    
            pyautogui.click()     
            time.sleep(0.1) 
            # Enemigo
            pyautogui.moveTo(615, 500) 
            time.sleep(0.8)  
            pyautogui.click()         
            time.sleep(0.1)   


            # Acosante 1
            pyautogui.moveTo(488, 581) 
            time.sleep(0.8)    
            pyautogui.click()     
            time.sleep(0.1) 
            # Enemigo
            pyautogui.moveTo(645, 500) 
            time.sleep(0.8)  
            pyautogui.click()         
            time.sleep(0.1)  
            # Acosante 2
            pyautogui.moveTo(488, 581) 
            time.sleep(0.8)    
            pyautogui.click()     
            time.sleep(0.1) 
            # Enemigo
            pyautogui.moveTo(645, 500) 
            time.sleep(0.8)  
            pyautogui.click()         
            time.sleep(0.1)   

            # Pasar de turno
            time.sleep(0.5) 
            pyautogui.click(450, 610)
            time.sleep(0.5) 
            pyautogui.click(450, 610)

            # Cerrar
            time.sleep(5) 
            pyautogui.click(558, 460)

            Turno_actual += 1
            if Turno_actual % 20 == 0:
                time.sleep(2) 
                pyautogui.click(384, 604)
                time.sleep(2) 
                pyautogui.click(275, 350)
                time.sleep(8) 
                pyautogui.doubleClick(488, 607)
                time.sleep(1.5) 
                pyautogui.doubleClick(488, 607)
                time.sleep(1.5) 
                pyautogui.doubleClick(488, 607)
                time.sleep(1.5) 
                pyautogui.doubleClick(488, 607)
                time.sleep(1.5) 
                pyautogui.doubleClick(488, 607)
                time.sleep(1.5) 
                pyautogui.doubleClick(488, 607)
                # Cerrar
                time.sleep(4) 
                pyautogui.click(557, 448)
                Turno_actual = 0
                Rendicion += 1
                print("Rendiciones:", Rendicion)

            continue
        
        #Buscar Inventario Cargado
        if len(loc_cargado[0]) > 0:
            # Abrir inventario -> Recursos -> Destruir
            time.sleep(1.5) 
            pyautogui.click(501, 538)
            time.sleep(1.5) 
            pyautogui.click(605, 200)
            time.sleep(1.5) 
            pyautogui.click(577, 270)
            time.sleep(1.5) 
            pyautogui.click(302, 452)
            time.sleep(1.5) 
            pyautogui.click(338, 507)
            time.sleep(1.5)
            pyautogui.typewrite('60')
            time.sleep(1.5)
            pyautogui.typewrite('60\n') 
            pyautogui.click(660, 150)
            time.sleep(1)
            pyautogui.click(80, 625)
            pyautogui.typewrite('d\n')
            pyautogui.click(80, 625)
            pyautogui.typewrite('d\n')
            pyautogui.click(80, 625)
            pyautogui.typewrite('d\n')
            pyautogui.click(80, 625)
            pyautogui.typewrite('d\n')
            pyautogui.click(80, 625)
            pyautogui.typewrite('d\n')
            pyautogui.click(80, 625)
            pyautogui.typewrite('d\n')
            pyautogui.click(80, 625)
            pyautogui.typewrite('d\n')
            Sala_actual -= 1
            continue

        # Si se encuentra la imagen "img_lleno"
        if len(loc_lleno[0]) > 0:
            #click en poti brack
            time.sleep(1) 
            pyautogui.doubleClick(615, 610)

            #Click Zappi -> Transporte -> Varios -> Banco
            time.sleep(3) 
            pyautogui.click(515, 195)
            time.sleep(1) 
            pyautogui.click(570, 225)
            time.sleep(3) 
            pyautogui.click(290, 195)
            time.sleep(1) 
            pyautogui.click(290, 255)

            #Click entrada banco brack -> Bolsas minerales
            time.sleep(3) 
            pyautogui.click(524, 281)
            time.sleep(8) 
            pyautogui.doubleClick(15, 490)
            time.sleep(1.2) 
            pyautogui.doubleClick(15, 490)
            time.sleep(1.2) 
            pyautogui.doubleClick(20, 465)
            time.sleep(1.2) 
            pyautogui.doubleClick(20, 465)
            time.sleep(1.2) 
            pyautogui.doubleClick(20, 440)
            time.sleep(1.2)  
            pyautogui.doubleClick(20, 440)
            time.sleep(1.2) 
            pyautogui.doubleClick(20, 410)
            time.sleep(1.2)  
            pyautogui.doubleClick(20, 410)
            time.sleep(1.2) 
            pyautogui.doubleClick(20, 385)
            time.sleep(1.2)  
            pyautogui.doubleClick(20, 385)

            #Click NPC Banco -> Hablar -> Consultar
            time.sleep(1) 
            pyautogui.click(441, 280)
            time.sleep(1) 
            pyautogui.click(460, 290)
            time.sleep(1) 
            pyautogui.click(150, 350)

            #Click Recursos -> Materiales -> X
            time.sleep(1)
            pyautogui.click(554, 232)
            time.sleep(1)
            pyautogui.moveTo(520, 280)
            pyautogui.keyDown('ctrl')
            pyautogui.click(clicks=2)
            pyautogui.keyUp('ctrl')
            time.sleep(1)   
            pyautogui.moveTo(520, 280)
            pyautogui.keyDown('ctrl')
            pyautogui.click(clicks=2)
            pyautogui.keyUp('ctrl')
            time.sleep(1) 
            pyautogui.moveTo(520, 280)
            pyautogui.keyDown('ctrl')
            pyautogui.click(clicks=2)
            pyautogui.keyUp('ctrl')
            time.sleep(1)   
            pyautogui.moveTo(520, 280)
            pyautogui.keyDown('ctrl')
            pyautogui.click(clicks=2)
            pyautogui.keyUp('ctrl')
            time.sleep(1) 
            pyautogui.moveTo(520, 280)
            pyautogui.keyDown('ctrl')
            pyautogui.click(clicks=2)
            pyautogui.keyUp('ctrl')
            time.sleep(1)   
            pyautogui.moveTo(520, 280)
            pyautogui.keyDown('ctrl')
            pyautogui.click(clicks=2)
            pyautogui.keyUp('ctrl')
            time.sleep(1) 
            pyautogui.moveTo(520, 280)
            pyautogui.keyDown('ctrl')
            pyautogui.click(clicks=2)
            pyautogui.keyUp('ctrl')
            time.sleep(1)   
            pyautogui.moveTo(520, 280)
            pyautogui.keyDown('ctrl')
            pyautogui.click(clicks=2)
            pyautogui.keyUp('ctrl')
            time.sleep(1)               
            pyautogui.click(660, 208)

            #Borrar Inventario lleno del chat
            time.sleep(1)
            pyautogui.click(80, 625)
            pyautogui.typewrite('d\n')
            pyautogui.click(80, 625)
            pyautogui.typewrite('d\n')
            pyautogui.click(80, 625)
            pyautogui.typewrite('d\n')
            pyautogui.click(80, 625)
            pyautogui.typewrite('d\n')
            pyautogui.click(80, 625)
            pyautogui.typewrite('d\n')
            
            #Click Recuerdo
            time.sleep(1)
            pyautogui.doubleClick(590, 606)
            time.sleep(5)

            Banco += 1
            print("Idas al Bannco:", Banco)
            
            continue
        # Si se encuentra la imagen "img_zaap"
        if len(loc_zaap[0]) > 0:
            #Ruta hacia lamina
            time.sleep(2)
            pyautogui.click(431, 131)
            time.sleep(8)
            pyautogui.click(527, 131)
            time.sleep(8)
            pyautogui.click(677, 405)
            time.sleep(6)
            pyautogui.click(185,131)
            time.sleep(6)
            pyautogui.click(40, 256)
            time.sleep(6)
            pyautogui.click(335, 131)
            time.sleep(7)
            pyautogui.click(40, 405)
            time.sleep(8)
            pyautogui.click(40, 330)
            time.sleep(7)
            pyautogui.click(157, 259)
            time.sleep(7)
            pyautogui.click(507, 344)
            time.sleep(7)
            pyautogui.click(554, 245)
            time.sleep(7)
            continue

        # Si se encuentra la imagen "img_hierro"
        if len(loc_hierro[0]) > 0:
            # Haz clic en el centro de la imagen y luego en otra ubicación cercana
            x = loc_hierro[1][0] + img_hierro.shape[1] // 2
            y = loc_hierro[0][0] + img_hierro.shape[0] // 2
            pyautogui.click(x + region[0], y + region[1]-20)
            time.sleep(0.005)
            pyautogui.click(x + region[0]+30, y + region[1]+10)
            time.sleep(2)
            continue

        # Si se encuentra la imagen "img_calavera"
        if len(loc_calavera[0]) > 0:
            if Calavera == True:
                #Dar Click para Sala Cobre 3
                pyautogui.click(201, 307)
                time.sleep(4.9) 
                Sala_actual = 4
                Calavera = False
                continue
            if Calavera == False:
                #Dar Click para Sala Cobre 3
                pyautogui.click(202, 431)
                time.sleep(4.9) 
                Sala_actual = 8
                Calavera = True
                continue

        if len(loc_monton[0]) > 0:
            Sala_actual = 2
            pyautogui.click(481, 306)
            time.sleep(4.9) 

        # Si se encuentra la imagen "img_ignorar"
        if len(loc_ignorar[0]) > 0:
            # Realiza un clic aleatorio en una de dos ubicaciones posibles
            if np.random.rand() < 0.5:
                time.sleep(1.8)
                pyautogui.click(425, 512)
            else:
                time.sleep(1.8)
                pyautogui.click(570, 475)

        else:
            # Hacer clic en el botón de cambio de sala correspondiente a la sala actual
            pyautogui.click(Cambiosala_coords[Sala_actual - 1])
            # Aumentar el número de sala actual en 1 módulo 9 (9 salas en total)
            Sala_actual  = (Sala_actual  + 1) % 8
            time.sleep(4.9)
            
        end_time = time.time()  # Obtener el tiempo actual después de cada iteración
        elapsed_time = end_time - start_time  # Calcular el tiempo transcurrido
        print(f'Tiempo transcurrido: {elapsed_time} segundos') 
        
        