import cv2
import numpy as np
import os

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;0"

class RTSP(object):
    def __init__(self,path,login=None,passwd=None):
        self.path = path
        self.login = login
        self.passwd = passwd
        self.output = "folder/saida.mp4"
        self.fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        self.out = cv2.VideoWriter('output.mp4', self.fourcc, 20.0, (640,480))
        print("[*] CONFIGURANDO METRICAS DE VALIDACAO ")
        if login == None and passwd == None:
          self.monta_url = "rtsp://%s/" % self.path
          print("[*] MONTANDO RTSP URL PADRAO ","\n",self.monta_url)
          self.cap = cv2.VideoCapture(self.monta_url)

        else:
          self.monta_url = "rtsp://%s:%s@%s/" % (self.login,self.passwd ,self.path)
          print("[*] MONTANDO RTSP URL COM LOGIN E SENHA ","\n",self.monta_url)
          self.cap = cv2.VideoCapture(self.monta_url)



    def get_image(self):
        self.ret, self.frame = self.cap.read()
        return self.frame
    def save_frame(self):
        self.out.write(self.frame)

    def stop_load(self):
        self.cap.release()
