def main():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        num = input()
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_y_comentario()
            elif num == 2:
                mostrar_resultados()
            elif num == 3:
                print('Finalizando')
                break
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')

def ingresar_puntuacion_y_comentario():
    while True:
        point = input('Por favor, introduzca una puntuación en una escala de 1 a 5: ')
        
        if point.isdecimal():
            point = int(point)
            if point < 1 or point > 5:
                print('Indíquelo en una escala de 1 a 5')
            else:
                comment = input('Por favor, introduzca un comentario: ')
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('Por favor, introduzca la puntuación en números')

def mostrar_resultados():
    print('Resultados hasta la fecha:')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

if __name__ == "__main__":
    main()