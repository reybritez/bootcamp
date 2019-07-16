try: #intentar esto
    while True:
        linea = robot.sense()
        print(robot.see(), "centimetros")
        if (linea[0]) < 300 and (linea[1]) > 0:
            print(linea[0])
            print(linea[0])
            if (robot.see()) <= 20:
                print(robot.see(), "centimetros")
                robot.pixel(255,0,0)
                robot.move_left()
                robot.move_stop()
                robot.move_backward()
            else:
                print(robot.see(), "centimetros")
                robot.pixel(0,255,0)
                robot.move_forward()
        else:
            if (linea[0]) > 300 and (linea[1]) < 1000:
                robot.pixel(255,0,0)
                robot.move_left()
                robot.move_stop()
                robot.move_backward()
except KeyboardInterrupt: #excepto cuando hay una excepcion
    print("Finalizado")
    robot.move_stop() #Al apretar Ctrl + C para el robot.