import rodi #importamos el codigo del bot
import time #importamos el codigo time

robot = rodi.RoDI() #se guarda tody 

# robot.move_forward() #mueve hacia adelante
# time.sleep(1)       #queda haciendo lo anterior por un segundo.
# robot.move_left()   #hace un giro a la izquierda
# time.sleep(0.5)     #queda haciendo el giro por 0.5 segundos
# robot.move_right()   #hace un giro a la derecha
# time.sleep(2)       #queda girando a la derecha por 2 segundos
# robot.move_backward()   #mueve el robot hacia atras
# robot.move_stop()   #para el robot.

# for x in range(1,5):
#     robot.move_forward()
#     time.sleep(2)
#     robot.move_left()
#     time.sleep(0.5)
#     robot.move_stop()
#     robot.pixel(255,0,255)

# try: #intentar esto
#     ver= 3
#     while int(ver) == 3:
#         print(robot.see(), "centimetros")
#         if (robot.see()) <= 20:
#             print(robot.see(), "centimetros")
#             robot.pixel(255,0,0)
#             robot.move_left()
#             robot.move_stop()
#             robot.move_backward()
#         else:
#             print(robot.see(), "centimetros")
#             robot.pixel(0,255,0)
#             robot.move_forward()
# except KeyboardInterrupt: #excepto cuando hay una excepcion
#     print("Finalizado")
#     robot.move_stop() #Al apretar Ctrl + C para el robot.

# try: #intentar esto
#     ver= 3
#     while int(ver) == 3:
#         print(robot.see(), "centimetros")
#         if (robot.see()) <= 20:
#             print(robot.see(), "centimetros")
#             robot.move_forward()
#             robot.pixel(0,100,0)
#             if (robot.see()) <= 3:
#                 robot.move_backward()
#                 robot.move_backward()
#                 robot.move_backward()
#         else:
#             print(robot.see(), "centimetros")
#             robot.move_left()
#             robot.pixel(0,0,100)
# except KeyboardInterrupt: #excepto cuando hay una excepcion
#     print("Finalizado")
#     robot.move_stop() #Al apretar Ctrl + C para el robot.

# try:
#     ver= 3
#     while ver == 3:
#         robot.pixel(100,0,0)
#         time.sleep(1)
#         robot.pixel(0,100,0)
#         time.sleep(1)
#         robot.pixel(0,0,100)
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Finalizado")
#     robot.move_stop()

# try:
#     while True:
#         print(robot.light())
#         time.sleep(0.5)
#         if (robot.light()) < 200:
#             robot.move_forward()
#             time.sleep(2)
#         else:
#             robot.move_stop()
# except KeyboardInterrupt :
# #     print("Finalizado")
# while True:
#     robot.sing(NOTE_A7,1000)
#     time.sleep(1)

try:    
    while True:
        linea = robot.sense()
        if (linea[0]) < 100 and (linea[1]) < 100:
                robot.move_backward()
                time.sleep(0.3)
                robot.move_left()
                time.sleep(0.3)
                print(linea[0])
                print(linea[1])
        else:
            robot.move_forward
            print(linea[0])
            print(linea[1])
except KeyboardInterrupt:
    print("Acabado")
