
from alumnos import *

if __name__=='__main__':
    
    alumnosSistema = []
    comandosSistema = ['R','C','P','S','X']
    print("\nBienvenidos al registro de notas")
    print("R - REGISTRAR")
    print("C - INGRESAR NOTA")
    print("P - OBTENER PROMEDIO")
    print("S - SUMA DE NOTAS")
    print("X - FINALIZAR\n")
    
    while True:
        comandoInformacion = input("\nIngrese un comando : ")        
        print(f"El comando ingresado es {comandoInformacion}")
        if comandoInformacion in comandosSistema:
            if comandoInformacion == 'R':
                print("Se registrara un nuevo alumno : ")
                nombre = input("Ingrese el nombre del alumno : ")
                apellido = input("Ingrese el apellido del alumno : ")
                edad = input("Ingrese la edad del alumno : ")
                nacionalidad = input("Ingrese la nacionalidad del alumno : ")                
                
                objAlumno = alumno(nombre,apellido,edad,nacionalidad)
                alumnosSistema.append(objAlumno)
            elif comandoInformacion == 'C':
                print("Ingreso de notas")                
                for alumnoInfo in alumnosSistema:                                                                
                    while True:
                        notaAlumno = input(f"Alumno {alumnoInfo.nombre} , Ingresenota: ")                        
                        if notaAlumno.isdigit():                            
                            if (int(notaAlumno)>0 and int(notaAlumno)<=20):
                                alumnoInfo.registrarNota(notaAlumno)
                                break                  
                            
            elif comandoInformacion == 'P':                            
                acumNota=0
                for alumnoInfo in alumnosSistema:
                    acumNota=acumNota + int(alumnoInfo.nota)
                print(f"El promedio de notas para {len(alumnosSistema)} alumnos es: {acumNota/len(alumnosSistema)}")                    
            
            elif comandoInformacion == 'S':      
                acumNota1=0                      
                for alumnoInfo in alumnosSistema:
                    acumNota1=acumNota1 + int(alumnoInfo.nota)
                print(f"La suma de notas para {len(alumnosSistema)} alumnos es: {acumNota1}")                    
            else:
                print("Comando de finalizacion")
                break
        else:
            print('Comando incorrecto, vuela a ingresarlo')