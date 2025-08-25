from tkinter import Tk, filedialog, Button, Label, Canvas, PhotoImage, Entry
from wsgiref.types import InputStream

from PIL import Image, ImageTk ,ImageDraw,ImageFont


file_path=""
photo=None
watermarked=None
def Exit_loop():
    window.destroy()
def Save_img():
    global watermarked
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Image.Files","*.png;,*.jpg;,*.jpeg;")]

    )
    if save_path:
        watermarked.convert("RGB").save(save_path)
        file_label.config(text=f"Saved as: {save_path}")
def Add_Watermark():
    global file_path
    global photo
    global watermarked
    image=Image.open(file_path).convert("RGBA")
    watermark=Image.new("RGBA",image.size,(0,0,0,0))
    draw=ImageDraw.Draw(watermark)
    
    text=inp.get()
    font_size=int(min(image.size)/7)
    try:
        fnt = ImageFont.truetype("arial.ttf", font_size)
    except:
        fnt = ImageFont.load_default()
    bbox = fnt.getbbox(text)  # (x0, y0, x1, y1)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = image.width - text_width
    y = image.height - text_height-45

    draw.text((x,y),text,font=fnt,fill=(255,255,255,125))
    watermarked=Image.alpha_composite(image,watermark)
    preview = watermarked.resize((250, 250))
    photo=ImageTk.PhotoImage(preview)
    canvas.create_image(128,126,image=photo)



def Upload_image():
    global photo
    global file_path
    file_path=filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("Image.Files","*.jpg;,*.jpeg;,*.png;,*.JPG;")]
    )

    if file_path:
        file_label.config(text=f"Selected File: {file_path}")
    img=Image.open(file_path)
    img = img.resize((250, 250))
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(128, 126, image=photo)
window=Tk()
window.title("Image Watermarker")
window.config(padx=120,pady=60)
window.config(bg="yellow")

#title label

my_label=Label(text="Image Watermarking",font=("Ariel",45,"bold"))
my_label.grid(column=1,row=0)

#upload Button
upload_btn=Button(text="Upload",font=("Ariel",14,"bold"),command=Upload_image)
upload_btn.grid(column=1,row=1)
file_label = Label(window, text="No file selected", font=("Arial", 12), bg="yellow")
file_label.grid(column=1, row=2, pady=10)
#Canvas
canvas=Canvas(window,width=250,height=250)


canvas.grid(column=1,row=4,padx=11)
#ADD TEXT
inp=Entry(width=30)
inp.grid(column=1,row=5)

#Add Watermark
watermark=Button(text="Watermark",command=Add_Watermark)
watermark.grid(column=1,row=6)

#SAVE IMAGE
Save_updated=Button(text="Save in Your Files My Dear",command=Save_img)
Save_updated.grid(column=1,row=7)
#Exit
Exit=Button(text="Exit Thanks For Using us or Trusting us",command=Exit_loop)
Exit.grid(column=1,row=8)
window.mainloop()
