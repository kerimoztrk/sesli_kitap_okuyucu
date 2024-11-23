import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog


def pdfMetniCikart(pdfYolu):
    metin=""
    pdfOkuyucu=PyPDF2.PdfReader(open(pdfYolu,'rb'))
    for sayfaNum in range(len(pdfOkuyucu.pages)):
        metin+= pdfOkuyucu.pages[sayfaNum].extract_text()
    return metin


#metni sesli hale getirme fonksiyonu

def metniSeseCevir(metin,ciktiDosyasi):
    sesliCevirici= gTTS(text=metin,lang='tr')
    sesliCevirici.save(ciktiDosyasi)

#dosya seçme fonksiyonu

def dosyaSec():
    dosyaYolu=filedialog.askopenfilename(filetypes=[("PDF Dosyaları", "*.pdf")])
    if dosyaYolu:
        pdfMetin=pdfMetniCikart(dosyaYolu)
        metniSeseCevir(pdfMetin,"Kaydet.mp3")
        if os.path.exists("Kaydet.mp3"): 
            sonucLabel.config(text="Dosya başarıyla oluşturuldu.")
            os.system("start Kaydet.mp3")
        else:
            sonucLabel.config(text="Dosya oluşturulamadı.")
        
        

#tkinter arayüz

app=tk.Tk()
app.title("Sesli Kitap Uygulaması")
app.geometry("250x150")

secimButonu=tk.Button(app,text="PDF Seç",command=dosyaSec,padx=20,pady=20)
secimButonu.pack(pady=20)

sonucLabel = tk.Label(app, text="")
sonucLabel.pack(pady=10)

app.mainloop()