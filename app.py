from lremote.camera.Camera import RTSP
import cv2
from pyautogui import confirm,prompt

def form():
  form1 = confirm(text='Seleciona a Opção Abaixo',
                  title='Camera RTSP VIEW',
                  buttons=['Gravação Imagens', 'Apenas Visualizar'])
  if form1 =='Gravação Imagens':
    ip = prompt(text='Digite o numero IP com porta EX: 192.168.0.13:554',
                title='Configuracoes de IP' ,
                default='192.168.0.13:554')
    acessos = prompt(text='Digite o Login e senha EX: login_admin:123456',
             title='Configuracoes de camera' ,
             default='admin:123123')

    login,senha = acessos.split(":")
    return [ip,login,senha]
  if form1 =='Apenas Visualizar':
    ip = prompt(text='Digite o numero IP com porta EX: 192.168.0.13:5554',
                 title='Configuracoes de IP' ,
                 default='192.168.0.13:5554')
    return [ip]
    #form2 = confirm(text='Seleciona a Opção Abaixo', title='Camera RTSP VIEW', buttons=['Iniciar Gravação', 'Apenas Visualizar'])



def start_process(path,login=None,senha=None):
 path = path
 if login == True and senha == True:
    camera = RTSP(path,login=login,passwd=senha)
    while True:
      frame = camera.get_image()
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    camera.stop_load()
 else:
    camera = RTSP(path)
    while True:
      frame = camera.get_image()
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    camera.stop_load()




def main():
 print("[*] AGUARDANDO USUARIO ")
 formulario = form()
 if len(formulario) > 2:
    path = formulario[0]
    login = formulario[1]
    senha = formulario[2]
    print("[X] LOAD HIGH PROCESS")
    start_process(path,login,senha)
 else:
    path = formulario[0]
    print("[*] LOAD NORMAL PROCESS")
    start_process(path)

main()
cv2.destroyAllWindows()
