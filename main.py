import tkinter as tk
import os
import sys
import shutil
from tkinter import Label,Canvas, Frame,ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

assets_path = os.path.join(BASE_DIR,"assets")
backgrounds_path = os.path.join(BASE_DIR, "assets", "backgrounds")
fonts_path = os.path.join(BASE_DIR, "assets", "fonts")
icons_path = os.path.join(BASE_DIR, "assets", "icons")
icon_path = os.path.join(BASE_DIR, "assets", "icons", "icon.ico")
step_images_path = os.path.join(BASE_DIR, "assets", "step_images")
readme_path = os.path.join(BASE_DIR, "README.txt")

print("Assets en:", assets_path)
print("Backgrounds en:", backgrounds_path)
print("Fonts en:", fonts_path)
print("Icons en:", icons_path)
print("Icon en:", icon_path)
print("Step Images en:", step_images_path)

for path in [assets_path, backgrounds_path, fonts_path, icons_path, step_images_path]:
    if not os.path.exists(path):
        print(f"⚠️ Advertencia: La carpeta {path} no existe.")

def delete_venv():
 venv_path = ".venv"

 if os.path.exists(venv_path):
    shutil.rmtree(venv_path)
    print("Entorno virtual eliminado correctamente")
 else:
    print("No se encontró el entorno virtual")

def show_page(frame):
    frame.tkraise()

root = tk.Tk()
root.title("The RGH 3 Encyclopedia")
root.geometry("800x600")
root.resizable(0, 0)

if os.path.exists(icon_path):
    try:
        root.iconbitmap(icon_path)  
    except Exception as e:
        print(f"⚠️ Advertencia: No se pudo cargar el icono. Error: {e}")
else:
    print(f"⚠️ Advertencia: No se encontró el icono en {icon_path}")

page1 = tk.Frame(root)
page2 = tk.Frame(root)
page3 = tk.Frame(root)

for frame in (page1, page2, page3):
    frame.place(x=0, y=0, relwidth=1, relheight=1)

########## Main Menu ##########

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

background_path = resource_path("assets/backgrounds/background.png")
winbox_path    = resource_path("assets/icons/winbox.png")
background2_path = resource_path("assets/backgrounds/background2.png")
background3_path = resource_path("assets/backgrounds/background3.png")
types_path = resource_path("assets/step_images/types.png")
font_path = resource_path("assets/fonts/tahoma.ttf")
font_bold_path = resource_path("assets/fonts/tahomabd.ttf")

img_bg = Image.open(background_path).resize((800, 600))
img_winbox = Image.open(winbox_path).resize((280, 280))

draw = ImageDraw.Draw(img_bg)
font = ImageFont.truetype(font_bold_path, 34)
text = "The RGH 3 Encyclopedia"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_position = ((img_bg.width - text_width) // 2, 37 + 300 + 10)
draw.text(text_position, text, font=font, fill=(255, 255, 255))

img_bg.paste(img_winbox, (270, 37), img_winbox)
tkimage = ImageTk.PhotoImage(img_bg)
panel1 = tk.Label(page1, image=tkimage)
panel1.pack(fill="both", expand=True)

rgh_button = tk.Button(page1, text="RGH 3", font=("assets/fonts/tahoma.ttf", 18), cursor="hand2",
                       relief="raised", bd=3, bg="#1621C9", fg="white",
                       command=lambda: show_page(page2))
rgh_button.bind("<ButtonPress>", lambda event: event.widget.config(bg="#0F198C"), "<ButtonHover>")
rgh_button.bind("<ButtonRelease>", lambda event: event.widget.config(bg="#1621C9"))
rgh_button.bind("<Enter>", lambda event: event.widget.config(bg="#0F198C")) 
rgh_button.bind("<Leave>", lambda event: event.widget.config(bg="#1621C9"))

type_button = tk.Button(page1, text="Board Type", font=("assets/fonts/tahoma.ttf", 18),
                        cursor="hand2", relief="raised", bd=3, bg="#1621C9", fg="white",
                        command=lambda: show_page(page3))
type_button.bind("<ButtonPress>", lambda event: event.widget.config(bg="#0F198C"))
type_button.bind("<ButtonRelease>", lambda event: event.widget.config(bg="#1621C9"))
type_button.bind("<Enter>", lambda event: event.widget.config(bg="#0F198C")) 
type_button.bind("<Leave>", lambda event: event.widget.config(bg="#1621C9"))

rgh_button.place(x=495, y=448, anchor="center")
type_button.place(x=305, y=448, anchor="center")

########## About ##########

def open_window():
    secondary_window = tk.Toplevel(root)
    secondary_window.title("Acerca de The RGH 3 Encyclopedia")
    secondary_window.geometry("400x500")
    secondary_window.configure(bg="white")

    img_icon = Image.open(winbox_path).resize((200, 200))
    tkimg_icon = ImageTk.PhotoImage(img_icon)

    label_img = tk.Label(secondary_window, image=tkimg_icon, background="white")
    label_img.image = tkimg_icon  
    label_img.pack(pady=10)
    label_text = tk.Label(secondary_window, text="The RGH 3 Encyclopedia", font=(font_bold_path, 13), foreground="black", background="white")
    label_text.pack(pady=5)
    label_text2 = tk.Label(secondary_window, text="Versión 1.1", font=(font_path, 10), foreground="black", background="white")
    label_text2.pack(pady=8)
    label_text4 = tk.Label(secondary_window, text="The RGH 3 Encyclopedia ofrece una guía para modificar tu Xbox 360, utilizando el método RGH 3", font=(font_path, 10), foreground="black", wraplength=355, justify="center", anchor="center", background="white")
    label_text4.pack(pady=11)

    close_button = tk.Button(secondary_window, text="Cerrar", font=("assets/fonts/tahoma.ttf", 10), cursor="hand2",
                             relief="raised", bd=3, bg="#e74611", fg="white", command=secondary_window.destroy)
    close_button.bind("<ButtonPress>", lambda event: event.widget.config(bg="#d94b0f"))
    close_button.bind("<ButtonRelease>", lambda event: event.widget.config(bg="#e74611"))
    close_button.bind("<Enter>", lambda event: event.widget.config(bg="#d94b0f")) 
    close_button.bind("<Leave>", lambda event: event.widget.config(bg="#e74611"))
    close_button.pack(pady=40)

    label_text3 = tk.Label(secondary_window, text="2025 - @areimo on GitHub", font=(font_path, 8), foreground="grey", background="white")
    label_text3.pack(pady=10)

    if os.path.exists(icon_path):
     try:
        secondary_window.iconbitmap(icon_path)  
     except Exception as e:
        print(f"⚠️ Advertencia: No se pudo cargar el icono. Error: {e}")
     else:
      print(f"⚠️ Advertencia: No se encontró el icono en {icon_path}")    

menu_bar = tk.Menu(root)
menu_bar = tk.Menu(root, tearoff=0, bg="white", fg="black", relief="flat")
menu_bar.add_command(label="Acerca de",command=open_window)
root.config(menu=menu_bar)

########## Page 2 ##########

img_bg_page2 = Image.open(background2_path).resize((800, 600))
tkimage_page2 = ImageTk.PhotoImage(img_bg_page2)

panel2 = Label(page2, image=tkimage_page2)
panel2.place(x=0, y=0, relwidth=1, relheight=1) 

style = ttk.Style()
style.theme_use("clam")  #
style.configure("CustomScrollbar.Vertical.TScrollbar",
                gripcount=0,
                background="#BCC9FF",  
                troughcolor="#E0E6FF",  
                bordercolor="#A3B2FF",  
                lightcolor="#D8DEFF",  
                darkcolor="#96A4E8",  
                arrowcolor="black",  
                borderwidth=2)  
style.map("CustomScrollbar.Vertical.TScrollbar",background=[("active", "#AAB8FF")], arrowcolor=[("active", "black")])  

canvas = Canvas(page2, bg="white", highlightthickness=0, width=700)  
scroll_frame = Frame(canvas, bg="white", width=700)  

scrollbar = ttk.Scrollbar(page2, orient="vertical", style="CustomScrollbar.Vertical.TScrollbar", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=False, padx=70)  
canvas.create_window((0, 0), window=scroll_frame, anchor="nw", width=700)  

scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

stepimages_path = resource_path("assets/step_images")
img1_path = resource_path("assets/step_images/img1.png")
img2_path = resource_path("assets/step_images/img2.png")
img2b_path = resource_path("assets/step_images/img2b.png")
img3_path = resource_path("assets/step_images/img3.png")
img3b_path = resource_path("assets/step_images/img3b.png")
img4_path = resource_path("assets/step_images/img4.png")
img4b_path = resource_path("assets/step_images/img4b.png")
img4c_path = resource_path("assets/step_images/img4c.png")
img4d_path = resource_path("assets/step_images/img4d.png")
img4e_path = resource_path("assets/step_images/img4e.png")
img5_path = resource_path("assets/step_images/img5.png")
img5b_path = resource_path("assets/step_images/img5b.png")
img5c_path = resource_path("assets/step_images/img5c.png")
img6_path = resource_path("assets/step_images/img6.png")
img6b_path = resource_path("assets/step_images/img6b.png")
img7_path = resource_path("assets/step_images/img7.png")
img7b_path = resource_path("assets/step_images/img7b.png")
img8_path = resource_path("assets/step_images/img8.png")
img8b_path = resource_path("assets/step_images/img8b.png")
img8c_path = resource_path("assets/step_images/img8c.png")
img8d_path = resource_path("assets/step_images/img8d.png")
img8e_path = resource_path("assets/step_images/img8e.png")
img8f_path = resource_path("assets/step_images/img8f.png")
img8g_path = resource_path("assets/step_images/img8g.png")

info = [
    ("¿Qué es RGH 3?", 16, None),
    ("RGH 3 es un nuevo método para liberar tu consola Xbox 360, requiere solamente dos cables y algunos resistores. Por último, este método no requiere del uso de algún chip", 12, None),
    ("Modelos compatibles con RGH 3", 16, None),
    ("Placas Madre Fat*:", 12,None),
    ("• Jasper (16mb/256mb/512mb)\n• Falcon",12,None),
    ("Placas Madre Slim:", 12, None),
    ("• Trinity\n• Corona (v1 - v6)", 12, None),
    ("*RGH 3 puede no funcionar en algunos modelos Fat. Si tienes problemas durante el arranque u otros comportamientos extraños, es posible que tu consola no sea compatible", 8, None),
    ("Necesitarás:", 16, None),
    ("Herramientas:", 12, None),
    ("• Una computadora\n• Actualizar Xbox 360 a la versión 17559\n• Kit básico de herramientas\n• Dispositivo para leer consolas NAND\n• Cable Kynar\n• Un soldador", 12, None),
    ("*ATENCIÓN: las placas madre Corona v3/v4/v5/v6, necesitarán un adaptador Post Fix, a continuación, una imagen guía para mayor seguridad:",8,img1_path),
    ("Resistores y diodos:", 12, None),
    ("• Fat: 1x 1n4148 Diodo y 1x 22k Resistor\n• Trinity: 1x 3k-10k Resistor\n• Corona: 1x 1k Resistor", 12, None),
    ("Raspberry Pi Pico:", 12, None),
    ("• Si quieres usar una Raspberry Pi Pico, asegúrate de utilizar la última versión de Octal450’s J-Runner with Extras", 12, None),
    ("Flashear Raspberry Pi Pico", 16, None),
    ("• Mantiene presionado el botón BOOSTEL debajo de tu Raspberry Pi Pico y conéctala a tu computadora, aparecerá como un almacenamiento removible" , 12, None),
    ("• Haz click y arrastra el UF2 file hacia la Raspberry Pi Pico hacia tu explorador de archivos, el dispositivo se desmontará automáticamente una vez completado el proceso", 12, None),
    ("• Inicia J-Runner, verás como PicoFlasher se mostrará como un dispositivo conectado. Una vez visto ésto, sigue los pasos a continuación", 12, None),
    ("Pasos a seguir", 16, None),
    ("Paso 1: Desarma tu consola y extrae la placa madre", 12, None),
    ("Paso 2: Una vez desarmada, suelda tus cabeceras NAND a la placa, los diagramas se mostrarán a continuación", 12, None),
    ("Placas Madres Fat:", 16, None),
    ("JR-P / NAND-X / xFlasher 360", 12, img2_path),
    ("PicoFlasher", 12, img2b_path),
    ("Placas Madre Trinity:", 16, None),
    ("JR-P / NAND-X / xFlasher 360", 12, img3_path),
    ("PicoFlasher", 12, img3b_path),
    ("Placas Madre Corona:", 16, None),
    ("*Atención a éstos puntos en tu placa, o de otra forma no podrás leer/escribir tu NAND", 8, img4_path),
    ("Consolas Normales:", 16, None),
    ("JR-P / NAND-X / xFlasher 360", 12, img4b_path),
    ("PicoFlasher", 12, img4c_path),
    ("Sólo para consolas de 4GB:", 12, img4d_path),
    ("PicoFlasher", 12, img4e_path),
    ("Paso 3: Ya conectados los cables lectores a la NAND, conecta sus cables RGH 3. Las instrucciones estarán a continuación", 12, None),
    ("Diagramas de Instalación RGH 3", 16, None),
    ("Placas Madre Fat:", 16, None),
    ("• Coloca una resistencia de 22k en el punto PLL y suelda tu cable al otro lado de la resistencia\n• Coloca un diodo de 1n4148 con el extremo del cátodo (al extremo negro de la banda) en POST, y suelda el cable al otro lado del diodo", 12, None),
    ("Puntos de abajo", 12, img5_path),
    ("Punto PLL en la parte superior", 12, img5b_path),
    ("Punto de abajo Alt PLL", 12, img5c_path),
    ("Placas Madre Trinity:", 16, None),
    ("• Coloca una resistencia de 3k-10k en el PLL y suelda el cable al otro lado de la resistencia", 12, img6_path),
    ("",12,img6b_path),
    ("Placas Madre Corona:", 16, None),
    ("• ATENCIÓN: Si realizas esta modificación en una placa Corona v3/v4/v5/v6, necesitarás un adaptador POSTFIX\n• Coloca una resistencia de 1k en el PLL y suelda el cable al otro lado de la resistencia", 12, img7_path),
    ("", 12, img7b_path),
    ("Paso 4: Una vez terminado los puntos, es momento de glitchear la consola. Dale a tu placa energía standby y conecta el programador, finalmente sigue los pasos a continuación", 12, None),
    ("Instrucciones para J-Runner", 16, None),
    ("Paso 1: Haz click en el botón “?” dentro de J-Runner para asegurarte de que tu programador puede detectar la consola correctamente. Si muestra algún error, asegúrate de revisar los cables de tu programador antes de continuar", 12, img8_path),
    ("Paso 2: Lee la NAND de tu placa haciendo click en  el botón “Read NAND”", 12, img8b_path),
    ("Paso 3: Una vez leída la NAND, selecciona las siguientes opciones en la esquina superior derecha, debajo de XeBuild:", 12,None),
    ("• Glitch2\n • RGH3\n • 10Mhz (Si 10Mhz no funciona, intenta con 27Mhz)", 12, img8c_path),
    ("Paso 4: Luego de crear el XeLL, haz click en “Write XeLL”", 12, img8d_path),
    ("Paso 5: Después que ECC haya sido escrito en tu consola, desconecta el programador, conecta un cable ethernet y un cable HDMI/AV. Tu consola debería bootear en el XeLL Reloaded. Si no conectaste ningún cable ethernet, se sugiere tomar una foto de la “CPU Key” en tu pantalla", 12, None),
    ("• Si conectaste un cable ethernet, anota la dirección IP y escríbela en J-Runner, en la esquina inferior derecha y selecciona “Get CPU Key”. Esto tomará la clave CPU de XeLL y probará con J-Runner haciendo uso de todo lo que sea necesario; en éste punto, es seguro apagar tu consola y conectar nuevamente el programador", 12, img8e_path),
    ("Paso 6: Una vez obtenida la clave CPU, es momento de crear una imagen hackeada. Haz click en “Create XeLL Build Image”, éste creará una imagen hackeada, la cual escribirás en tu consola", 12, img8f_path),
    ("Paso 7: Ya creada la imagen XeBuild (y que J-Runner no mostrara ningún error), haz click en “Write NAND”. Es con ésto que habrás terminado de hackear tu consola, ahora desconecta el programador y enciende la consola. Si enciendes con el botón de expulsión, deberías ver XeLL", 12, img8g_path)
]

for text, size, img_name in info:
    font_style = ("assets/fonts/tahomabd.ttf", size) if size > 15 else ("assets/fonts/tahoma.ttf")

    if size == 8:
        text_color = "red"
    elif size > 15:
        text_color = "#8DAAE7"
    else:
        text_color = "black"

    Label(
        scroll_frame, text=text, font=font_style, foreground=text_color, bg="white",wraplength=625, 
        justify="left", anchor="w").pack(fill="both", anchor="w", pady=10)

    if text in [
        "RGH 3 es un nuevo método para liberar tu consola Xbox 360, requiere solamente dos cables y algunos resistores. Por último, este método no requiere del uso de algún chip",
        "*RGH 3 puede no funcionar en algunos modelos Fat. Si tienes problemas durante el arranque u otros comportamientos extraños, es posible que tu consola no sea compatible",
        "• Si quieres usar una Raspberry Pi Pico, asegúrate de utilizar la última versión de Octal450’s J-Runner with Extras",
        "• Inicia J-Runner, verás como PicoFlasher se mostrará como un dispositivo conectado. Una vez visto ésto, sigue los pasos a continuación",
        "Paso 3: Ya conectados los cables lectores a la NAND, conecta sus cables RGH 3. Las instrucciones estarán a continuación",
        "Paso 4: Una vez terminado los puntos, es momento de glitchear la consola. Dale a tu placa energía standby y conecta el programador, finalmente sigue los pasos a continuación"
    ] or size > 20:
        Frame(scroll_frame, height=1, width=500, bg="#CDCCCD").pack(pady=5,fill="both")  

    if img_name:
        img_path = os.path.join(stepimages_path, img_name)  
        
        if os.path.exists(img_path):  
            try:
                img = Image.open(img_path).resize((400, 300))  
                img = ImageTk.PhotoImage(img)
                img_label = Label(scroll_frame, image=img, bg="white")
                img_label.image = img  
                img_label.pack(anchor="center", pady=10, expand=True)
            except Exception as e:
                print(f"Error al cargar la imagen {img_path}: {e}")
        else:
            print(f"Imagen no encontrada: {img_path}")

def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scroll_frame.bind("<Configure>", update_scroll_region)
scroll_frame = Frame(canvas, bg="white") 

back_button = tk.Button(page2, text="X", font=("assets/fonts/tahomabd.ttf", 12), bg="#e74611", 
                        fg="white",relief="raised", cursor="hand2", 
                        command=lambda: show_page(page1))
back_button.bind("<ButtonPress>", lambda event: event.widget.config(bg="#d94b0f"))
back_button.bind("<ButtonRelease>", lambda event: event.widget.config(bg="#e74611"))
back_button.bind("<Enter>", lambda event: event.widget.config(bg="#d94b0f")) 
back_button.bind("<Leave>", lambda event: event.widget.config(bg="#e74611"))
back_button.place(x=748, y=10)

########## Page 3 ##########

page3 = tk.Frame(root)
page3.place(x=0, y=0, relwidth=1, relheight=1)

img_bg_page3 = Image.open(background3_path).resize((800, 600))
tkimage_page3 = ImageTk.PhotoImage(img_bg_page3)

panel3 = Label(page3, image=tkimage_page3)
panel3.place(x=0, y=0, relwidth=1, relheight=1)

canvas2 = tk.Canvas(page3, bg="white", highlightthickness=0, width=700, height=640)
canvas2.pack(side="left", fill="both", expand=True, padx=70)

scroll_frame = tk.Frame(canvas2, bg="white", width=700, height=640)
canvas2.create_window((0, 0), window=scroll_frame, anchor="nw", width=700, height=640)

info2 = [
    ("Identificar Tipo de Placa", 16, None),
    ("• El método RGH 3 es compatible con las placas Fat (Jasper y Falcon), y Slim (Trinity y Corona). A continuación, una imagen guía para identificar el tipo de placa que tengas", 12, ""),
]

img_path = types_path

for text, size, img_name in info2:
    font_style = ("assets/fonts/tahomabd.ttf",size) if size > 15 else ("assets/fonts/tahoma.ttf")
    text_color = "#8DAAE7" if size == 16 else "black"

    tk.Label(
        scroll_frame, text=text, font=font_style, foreground=text_color,
        bg="white", wraplength=625, justify="left", anchor="w"
    ).pack(fill="both", anchor="w", pady=10)

    if text.startswith("• El método RGH 3") or size == 12:
        Frame(scroll_frame, height=1, width=650, bg="#CDCCCD").pack(pady=5,fill="both")

if not os.path.exists(img_path):
    print(f"Imagen no encontrada: {img_path}")
else:
    try:
        img = Image.open(img_path).resize((500, 300))  
        img = ImageTk.PhotoImage(img)

        img_label = Label(scroll_frame, image=img, bg="white")
        img_label.image = img  
        img_label.pack(anchor="center", pady=10, expand=True)
    except Exception as e:
        print(f"Error al cargar la imagen {img_path}: {e}")

back_button = tk.Button(page3, text="X", font=("assets/fonts/tahomabd.ttf", 12), bg="#e74611", 
                        fg="white", relief="raised", cursor="hand2", 
                        command=lambda: show_page(page1))
back_button.bind("<ButtonPress>", lambda event: event.widget.config(bg="#d94b0f"))
back_button.bind("<ButtonRelease>", lambda event: event.widget.config(bg="#e74611"))
back_button.bind("<Enter>", lambda event: event.widget.config(bg="#d94b0f")) 
back_button.bind("<Leave>", lambda event: event.widget.config(bg="#e74611"))
back_button.place(x=748, y=10)

show_page(page1)
root.mainloop()


