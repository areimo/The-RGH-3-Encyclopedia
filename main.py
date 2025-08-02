import tkinter as tk
import os
import sys
import customtkinter as ctk
import tkinter.font as tkfont
from tkinter import Label,Canvas, Frame,ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if hasattr(sys, "_MEIPASS"):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

assets_path = os.path.join(BASE_DIR,"assets")
backgrounds_path = os.path.join(BASE_DIR, "assets", "backgrounds")
fonts_path = os.path.join(BASE_DIR, "assets", "fonts")
icons_path = os.path.join(BASE_DIR, "assets", "icons")
icon_path = os.path.join(BASE_DIR, "assets", "icons", "icon.ico")
step_images_path = os.path.join(BASE_DIR, "assets", "step_images")

for path in [assets_path, backgrounds_path, fonts_path, icons_path, step_images_path]:
    if not os.path.exists(path):
        print(f"Advertencia: La carpeta {path} no existe.")

def show_page(frame):
    frame.tkraise()

root = tk.Tk()
root.title("The RGH 3 Encyclopedia")
root.geometry("800x600")
root.resizable(0,0)

if os.path.exists(icon_path):
    try:
        root.iconbitmap(icon_path)  
    except Exception as e:
        print(f"Advertencia: No se pudo cargar el icono. Error: {e}")
else:
    print(f"Advertencia: No se encontró el icono en {icon_path}")

page1 = tk.Frame(root)
page1.configure(bg="white")
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
icon_png_path    = resource_path("assets/icons/icon_png.png")
background2_path = resource_path("assets/backgrounds/background2.png")
background3_path = resource_path("assets/backgrounds/background3.png")
types_path = resource_path("assets/step_images/types.png")
font_path = resource_path("assets/fonts/tahoma.ttf")
font_bold_path = resource_path("assets/fonts/tahomabd.ttf")

img_bg = Image.open(background_path).resize((380, 600))
tkimage_bg = ImageTk.PhotoImage(img_bg)
img_icon = Image.open(icon_png_path).resize((290, 250))
tkimage_icon_png = ImageTk.PhotoImage(img_icon)
panel_bg = tk.Label(page1, image=tkimage_bg, bg='white')
panel_bg.place(x=400, y=0, width=420, height=600)

icon_png_label = tk.Label(page1, image=tkimage_icon_png, bg="white")
icon_png_label.place(x=45, y=68, width=290, height=250) 
text_label = tk.Label(page1, text="The RGH 3 Encyclopedia", font=("Tahoma", 22, "bold"), fg="black", bg="white")
text_label.place(x=20, y=300)

def pages_buttons(parent, text, command, x, y):
    button = ctk.CTkButton(parent, text=text, font=("assets/fonts/tahomabd.ttf",18), width=150, height=40, 
                           fg_color="#3B77BC", hover_color="#2A5C99",
                           text_color="white", border_color="#7CB9FF",border_width=3.5,corner_radius=8,command=command)
    button.place(x=x, y=y)
    return button

rgh_button = pages_buttons(page1, "RGH 3", lambda: show_page(page2), 35, 380)
type_button = pages_buttons(page1, "Board Type", lambda: show_page(page3), 215, 380)

credits = tk.Label(page1, text="2025 - @areimo on GitHub", font=("assets/fonts/tahoma.ttf", 8), foreground="grey", background="white")
credits.place(x=135, y=550)

########## About ##########

def open_window():
    secondary_window = tk.Toplevel(root)
    secondary_window.title("Acerca de The RGH 3 Encyclopedia")
    secondary_window.geometry("400x500")
    secondary_window.configure(bg="white")
    secondary_window.resizable(0,0)

    img_icon = Image.open(icon_png_path).resize((250, 200))
    tkimg_icon = ImageTk.PhotoImage(img_icon)

    label_img = tk.Label(secondary_window, image=tkimg_icon, background="white")
    label_img.image = tkimg_icon  
    label_img.pack(pady=10)
    label_text = tk.Label(secondary_window, text="The RGH 3 Encyclopedia", font=(font_bold_path, 13), foreground="black", background="white")
    label_text.pack(pady=5)
    label_text2 = tk.Label(secondary_window, text="Versión 1.3", font=(font_path, 10), foreground="black", background="white")
    label_text2.pack(pady=8)
    label_text4 = tk.Label(secondary_window, text="The RGH 3 Encyclopedia ofrece una guía para modificar tu Xbox 360, utilizando el método RGH 3", font=(font_path, 10), foreground="black", wraplength=355, justify="center", anchor="center", background="white")
    label_text4.pack(pady=11)

    close_button = ctk.CTkButton(secondary_window, text="Cerrar", font=("assets/fonts/tahoma.ttf", 12),
                             width=60, height=35, fg_color="#DE482B", hover_color="#B53A22",
                             text_color="white", border_color="#FF866E", border_width=3,
                             corner_radius=4, command=secondary_window.destroy)
    close_button.pack(pady=10)

    credits_frame = tk.Frame(secondary_window, bg="white")
    credits_frame.pack(side="bottom", fill="x", pady=20)

    credits = tk.Label(credits_frame, text="2025 - @areimo on GitHub",
                   font=(font_path, 8), foreground="grey", background="white")
    credits.pack()

    if os.path.exists(icon_path):
     try:
        secondary_window.iconbitmap(icon_path)  
     except Exception as e:
        print(f"Advertencia: No se pudo cargar el icono. Error: {e}")
     else:
      print(f"Advertencia: No se encontró el icono en {icon_path}")    

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
style.theme_use("clam")  
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

canvas = Canvas(page2, bg="white", highlightthickness=0, width=720)  
scroll_frame = Frame(canvas, bg="white", width=700)  

scrollbar = ttk.Scrollbar(page2, orient="vertical", style="CustomScrollbar.Vertical.TScrollbar", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=False, padx=70)  
canvas.create_window((0, 0), window=scroll_frame, anchor="nw", width=700)  

scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def _on_arrow_key(event):
    if event.keysym == "Down":
        canvas.yview_scroll(1, "units")
    elif event.keysym == "Up":
        canvas.yview_scroll(-1, "units")

canvas.bind("<MouseWheel>", _on_mousewheel)
canvas.bind("<Up>", _on_arrow_key)
canvas.bind("<Down>", _on_arrow_key)

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

def show_zoom_navigable(img_path):
    top = tk.Toplevel()
    top.title("Visor de imagen")
    top.geometry("900x700")
    top.configure(bg="black")

    img_icon2 = Image.open(icon_png_path).resize((250, 200))
    tkimg_icon2 = ImageTk.PhotoImage(img_icon2) 
    top.iconphoto(False, tkimg_icon2)
   
    canvas = tk.Canvas(top, bg="black", highlightthickness=0)
    hbar = tk.Scrollbar(top, orient="horizontal", command=canvas.xview)
    vbar = tk.Scrollbar(top, orient="vertical", command=canvas.yview)
    canvas.configure(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    hbar.pack(side="bottom", fill="x")
    vbar.pack(side="right", fill="y")
    canvas.pack(fill="both", expand=True)

    original_image = Image.open(img_path)
    zoom_factor = 1.0
    img = ImageTk.PhotoImage(original_image)
    img_id = canvas.create_image(0, 0, image=img, anchor="nw")
    canvas.image = img
    canvas.config(scrollregion=(0, 0, img.width(), img.height()))

    def update_image():
        nonlocal img
        new_w = int(original_image.width * zoom_factor)
        new_h = int(original_image.height * zoom_factor)
        resized = original_image.resize((new_w, new_h), Image.LANCZOS)
        img = ImageTk.PhotoImage(resized)
        canvas.itemconfig(img_id, image=img)
        canvas.image = img
        canvas.config(scrollregion=(0, 0, new_w, new_h))

    def start_drag(event):
        canvas.scan_mark(event.x, event.y)
    def drag(event):
        canvas.scan_dragto(event.x, event.y, gain=1)

    canvas.bind("<ButtonPress-1>", start_drag)
    canvas.bind("<B1-Motion>", drag)

    def zoom_mouse(event):
        nonlocal zoom_factor
        if event.delta > 0 or event.num == 4:
            zoom_factor *= 1.1
        else:
            zoom_factor /= 1.1
        zoom_factor = max(0.2, min(zoom_factor, 5))
        update_image()

    canvas.bind("<MouseWheel>", zoom_mouse) 
    def zoom_in_key(event):
        nonlocal zoom_factor
        zoom_factor *= 1.1
        zoom_factor = min(zoom_factor, 5)
        update_image()

    def zoom_out_key(event):
        nonlocal zoom_factor
        zoom_factor /= 1.1
        zoom_factor = max(zoom_factor, 0.2)
        update_image()

    top.bind("<plus>", zoom_in_key)            
    top.bind("<KP_Add>", zoom_in_key)          
    top.bind("<minus>", zoom_out_key)          
    top.bind("<KP_Subtract>", zoom_out_key)    
    top.bind("<Control-equal>", zoom_in_key)   
    top.bind("<Control-minus>", zoom_out_key)  


for text, size, img_name in info:

    font_path = "assets/fonts/tahomabd.ttf" if size > 15 else "assets/fonts/tahoma.ttf"

    font_style = tkfont.Font(family="Tahoma", size=size)
    if size > 15:
        font_style.configure(weight="bold", underline=1)

    if size == 8:
        text_color = "red"
    elif size > 15:
        text_color = "#8DAAE7"
    else:
        text_color = "black"

    if img_name and size == 12 and text.startswith(("PicoFlasher", "JR-P", "Sólo para", "Consolas")):
        container = Frame(scroll_frame, bg="white")
        container.pack(fill="both", pady=10)

        def toggle_image(lbl, btn):
            if lbl.winfo_viewable():
                lbl.pack_forget()
                btn.config(text=btn.cget("text").replace("▼", "►"))
            else:
                lbl.pack(pady=5)
                btn.config(text=btn.cget("text").replace("►", "▼"))

        img_path = os.path.join(stepimages_path, img_name)
        if os.path.exists(img_path):
            try:
                img = Image.open(img_path).resize((500, 300))
                img = ImageTk.PhotoImage(img)
                img_label = Label(container, image=img, bg="white")
                img_label.image = img
                img_label.pack_forget()

                btn = tk.Button(
                    container, text=f"► {text}", font=font_style,
                    fg=text_color, bg="white", bd=0, anchor="w", justify="left",
                    command=lambda l=img_label, b=None: toggle_image(l, b)
                )
                btn.pack(fill="x", anchor="w")
                btn.configure(command=lambda l=img_label, b=btn: toggle_image(l, b))
            except Exception as e:
                print(f"Error al cargar imagen {img_path}: {e}")
        else:
            print(f"Imagen no encontrada: {img_path}")

    else:
        Label(
            scroll_frame, text=text, font=font_style, foreground=text_color,
            bg="white", wraplength=625, justify="left", anchor="w"
        ).pack(fill="both", anchor="w", pady=10)

        if text in [
            "RGH 3 es un nuevo método para liberar tu consola Xbox 360, requiere solamente dos cables y algunos resistores. Por último, este método no requiere del uso de algún chip",
            "*RGH 3 puede no funcionar en algunos modelos Fat. Si tienes problemas durante el arranque u otros comportamientos extraños, es posible que tu consola no sea compatible",
            "• Si quieres usar una Raspberry Pi Pico, asegúrate de utilizar la última versión de Octal450’s J-Runner with Extras",
            "• Inicia J-Runner, verás como PicoFlasher se mostrará como un dispositivo conectado. Una vez visto ésto, sigue los pasos a continuación",
            "Paso 3: Ya conectados los cables lectores a la NAND, conecta sus cables RGH 3. Las instrucciones estarán a continuación",
            "Paso 4: Una vez terminado los puntos, es momento de glitchear la consola. Dale a tu placa energía standby y conecta el programador, finalmente sigue los pasos a continuación"
        ] or size > 20:
            separator_container = Frame(scroll_frame, bg="white")
            separator_container.pack(fill="x")
            separator = Frame(separator_container, height=1, bg="#CDCCCD")
            separator.pack(fill="x", pady=(5, 5))

        if img_name:
            img_path = os.path.join(stepimages_path, img_name)
            if os.path.exists(img_path):
              try:
                 img_pil = Image.open(img_path).resize((500, 300))
                 img = ImageTk.PhotoImage(img_pil)
                 img_label = Label(scroll_frame, image=img, bg="white", cursor="hand2")
                 img_label.image = img
                 img_label.pack(anchor="center", pady=10, expand=True)
                 img_label.bind("<Button-1>", lambda e, p=img_path: show_zoom_navigable(p))
              except Exception as e:
                 print(f"Error al cargar la imagen {img_path}: {e}")

def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scroll_frame.bind("<Configure>", update_scroll_region)

canvas.focus_set()

def close_button(parent, text, command, x, y):
    button = ctk.CTkButton(parent, text=text, font=("assets/fonts/tahomabd.ttf",18), width=35, height=35, 
                           fg_color="#DE482B", hover_color="#B53A22",
                           text_color="white", border_color="#FF866E",border_width=3,corner_radius=4,command=command)
    button.place(x=x, y=y)
    return button

x_button = close_button(page2, "X", lambda: show_page(page1), 740, 10)

########## Page 3 ##########

page3 = tk.Frame(root)
page3.place(x=0, y=0, relwidth=1, relheight=1)

img_bg_page3 = Image.open(background3_path).resize((800, 600))
tkimage_page3 = ImageTk.PhotoImage(img_bg_page3)
types_path = resource_path("assets/step_images/types.png")
types_path2 = resource_path("assets/step_images/typesb.png")

panel3 = Label(page3, image=tkimage_page3)
panel3.place(x=0, y=0, relwidth=1, relheight=1)

scrollbar = ttk.Scrollbar(page3, orient="vertical",
                          style="CustomScrollbar.Vertical.TScrollbar")
scrollbar.pack(side="right", fill="y")

canvas2 = tk.Canvas(page3, bg="white", highlightthickness=0, yscrollcommand=scrollbar.set)
canvas2.pack(side="left", fill="both", expand=True, padx=70)

scrollbar.config(command=canvas2.yview)  

scroll_frame = tk.Frame(canvas2, bg="white", width=700, height=640)
canvas2.create_window((0, 0), window=scroll_frame, anchor="nw", width=700, height=640)

style = ttk.Style()
style.theme_use("clam")
style.configure("CustomScrollbar.Vertical.TScrollbar",
                gripcount=0,
                background="#BCC9FF",
                troughcolor="#E0E6FF",
                bordercolor="#A3B2FF",
                lightcolor="#D8DEFF",
                darkcolor="#96A4E8",
                arrowcolor="black",
                borderwidth=2)
style.map("CustomScrollbar.Vertical.TScrollbar",
          background=[("active", "#AAB8FF")],
          arrowcolor=[("active", "black")])

scroll_frame.bind("<Configure>", lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")))

def _on_mousewheel(event):
    canvas2.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas2.bind_all("<MouseWheel>", _on_mousewheel)

def _on_arrow_key(event):
    if event.keysym == "Down":
        canvas2.yview_scroll(1, "units")
    elif event.keysym == "Up":
        canvas2.yview_scroll(-1, "units")

canvas2.bind_all("<Down>", _on_arrow_key)
canvas2.bind_all("<Up>", _on_arrow_key)

bold_underline_font = tkfont.Font(family="Tahoma", size=16, weight="bold", underline=1)

info2 = [
    ("Identificar Tipo de Placa", 16, None),
    ("• El método RGH 3 es compatible con las placas Fat (Jasper y Falcon), y Slim (Trinity y Corona). A continuación, una imagen guía para identificar el tipo de placa que tengas", 12, ""),
]

y_position = 10
separator_width = 600  

for text, size, img_name in info2:
    if size == 16:
        font_style = bold_underline_font
        text_color = "#8DAAE7"
        height_estimate = 30
    else:
        font_style = ("Tahoma", size)
        text_color = "black"
        height_estimate = 50

    label = tk.Label(
        scroll_frame, text=text, font=font_style, foreground=text_color,
        bg="white", wraplength=625, justify="left", anchor="w"
    )
    label.place(x=10, y=y_position, width=625)
    y_position += height_estimate + 10
    
    if text.startswith("• El método RGH 3") or size == 12:
        separator = Frame(scroll_frame, height=1, bg="#CDCCCD")
        separator.place(x=10, y=y_position, width=700)
        y_position += 10  
if not (os.path.exists(types_path) and os.path.exists(types_path2)):
    print(f"Imagen no encontrada: {types_path}, {types_path2}")
else:
    try:
      
      img1 = Image.open(types_path).resize((450, 300))
      tk_img1 = ImageTk.PhotoImage(img1)

      img_label1 = Label(scroll_frame, image=tk_img1, bg="white", cursor="hand2")
      img_label1.image = tk_img1  # mantener referencia
      img_label1.place(x=100, y=y_position, width=450, height=300)
      img_label1.bind("<Button-1>", lambda e, path=types_path: show_zoom_navigable(path))
      y_position += 300 + 10

      img2 = Image.open(types_path2).resize((450, 200))
      tk_img2 = ImageTk.PhotoImage(img2)

      img_label2 = Label(scroll_frame, image=tk_img2, bg="white", cursor="hand2")
      img_label2.image = tk_img2  # mantener referencia
      img_label2.place(x=100, y=y_position, width=450, height=200)
      img_label2.bind("<Button-1>", lambda e, path=types_path2: show_zoom_navigable(path))
      y_position += 200 + 10

    except Exception as e:
        print(f"Error al cargar la imagen {types_path}, {types_path2}: {e}")

x_button = close_button(page3, "X", lambda: show_page(page1), 740, 10)

show_page(page1)
root.mainloop()