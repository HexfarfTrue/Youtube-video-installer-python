# pip install yt_dlp

import tkinter
from tkinter import filedialog, messagebox
from yt_dlp import YoutubeDL

def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Ошибка, введите ссылку от YouTube")
        return

    download_path = filedialog.askdirectory(title ="Выберите путь для установки видео")
    if not download_path:
        return
    try:
         ydl_opts = {
            'outtmpl' : f'{download_path}/%(title)s.%(ext)s',
            'format' : 'bv*[height>=1080]+ba/best',
            'merge_output_format' : 'mp4',
            'quiet' : True
         }

         with YoutubeDL (ydl_opts) as ydl:
            info = ydl.extract_info(url, download= True)

         title = info.get('title', 'Unknown title')
         resolution = f"{info.get('height', '?')}p"
         bitrate = info.get('abr', 'Unknown')
         filename = info.get('_filename', 'unknows.mp4')

         messagebox.showinfo(
             "Установка завершена"
             f"Название: {title}\n Качество: {resolution}\n Битрейт: {bitrate} kbps\n Сохранено как: {filename}"
        )
 
    except Exception as e:
        messagebox.showerror("Ошибка установки", f"Что-то пошло не так:\n{str(e)}")

root = tkinter.Tk()
root.title("Установщик видео с Юпупа")

tkinter.Label(root, text="Ввдите ссылку на Ютуб видео:").pack(pady=5)

url_entry = tkinter.Entry(root, width = 60)
url_entry.pack(pady=5)

download_btn = tkinter.Button(root, text="Установить в высоком качестве", command = download_video)
download_btn.pack(pady=28)

root.mainloop()