from tkinter import Tk,Label,Button,Canvas,filedialog,messagebox
import tkinter.messagebox
import os


# =======================================================
#           CONTENTS - QS File Template
# =======================================================
# 1   Import the required libraries
#           a.  tkinter
#           b.  os

# 2   Define Functions
#           a.  makeMyFolder
#           b.  makeMyFile
#           c.  include_index
#           d.  include_style
#           e.  include_robots
#           f.  include_manifest
#           g.  include_java
#           h.  build
#           i.  endApp

# 3   Define variables
#           a.  appTitle
#           b.  appDescription
#           c.  appInstructions
#           d.  appCopyright
#           e.  folderName
#           f.  buttBG
#           g.  buttFG
#           h.  buttFONT
#           i.  buttWIDTH
#           j.  buttPADX
#           k.  rowPADY

# 4   Make a tkinter window including:
#           -   labels
#           -   buttons
#           -   canvas with grid layout
# ==============================================================



# if the folder doesn't exist, the folder is made, 
# else tkniter display ERRORbox and execute exit() to end script so nothing gets accidently overwritten.
def makeMyFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print('OK: '+folder)
    else:        
        print('** CAUTION **            This folder already exists: ' + folder)
        print('** SCRIPT TERMINATED **  Check the path is correct')
        print('')    
        app.destroy()
        exit()        


# changes directory and makes file in opened directory. 
# Careful, the f.write will clear any existing data. 
# This is why the script exit() is included when checking if the folder exists.
def makeMyFile(folder, file):
    os.chdir(folder)
    with open(file,'w') as f:
        f.write('')
        print('OK: '+ folder +''+file)


# changes the colour of the button when clicked on
def include_index():
    if button_index["bg"] != "red":
        button_index["bg"] = "red"           
        my_canvas.delete("tag_index")
        my_canvas.create_line(192, 40, 220, 40, fill="#444", width="4",tag="tag_index")
        my_canvas.create_text(230, 40, text="index.html", fill="#444", font=("bold 20"), anchor="w", tag="tag_index") 
    else:        
        button_index["bg"] = "green" 
        my_canvas.delete("tag_index")
        my_canvas.create_line(192, 40, 220, 40, fill="green", width="4",tag="tag_index")
        my_canvas.create_text(230, 40, text="index.html", fill="green", font=("bold 20"), anchor="w", tag="tag_index")        
    

def include_style():
    if button_style["bg"] != "red":
        button_style["bg"] = "red"   
        my_canvas.delete("tag_style")
        my_canvas.create_line(192, 80, 220, 80, fill="#444", width="4", tag="tag_style")
        my_canvas.create_text(230, 80, text="style.css", fill="#444", font=("bold 20"), anchor="w", tag="tag_style")             
    else:        
        button_style["bg"] = "green"  
        my_canvas.delete("tag_style")
        my_canvas.create_line(192, 80, 220, 80, fill="green", width="4", tag="tag_style")
        my_canvas.create_text(230, 80, text="style.css", fill="green", font=("bold 20"), anchor="w", tag="tag_style")    
         

def include_robots():
    if button_robots["bg"] != "red":
        button_robots["bg"] = "red"   
        my_canvas.delete("tag_robots")
        my_canvas.create_line(192, 120, 220, 120, fill="#444", width="4", tag="tag_robots")
        my_canvas.create_text(230, 120, text="robots.txt", fill="#444", font=("bold 20"), anchor="w", tag="tag_robots")              
    else:        
        button_robots["bg"] = "green" 
        my_canvas.delete("tag_robots")
        my_canvas.create_line(192, 120, 220, 120, fill="green", width="4", tag="tag_robots")
        my_canvas.create_text(230, 120, text="robots.txt", fill="green", font=("bold 20"), anchor="w", tag="tag_robots")        
   

def include_manifest():
    if button_manifest["bg"] != "red":
        button_manifest["bg"] = "red"   
        my_canvas.delete("tag_manifest")
        my_canvas.create_line(192, 160, 220, 160, fill="#444", width="4", tag="tag_manifest")
        my_canvas.create_text(230, 160, text="manifest.json", fill="#444", font=("bold 20"), anchor="w", tag="tag_manifest")             
    else:        
        button_manifest["bg"] = "green"    
        my_canvas.delete("tag_manifest")
        my_canvas.create_line(192, 160, 220, 160, fill="green", width="4", tag="tag_manifest")
        my_canvas.create_text(230, 160, text="manifest.json", fill="green", font=("bold 20"), anchor="w", tag="tag_manifest")    
    

def include_java():
    if button_java["bg"] != "red":
        button_java["bg"] = "red"  
        my_canvas.delete("tag_java")
        my_canvas.create_line(192, 200, 220, 200, fill="#444", width="4", tag="tag_java")
        my_canvas.create_text(230, 200, text="main.js", fill="#444", font=("bold 20"), anchor="w", tag="tag_java")              
    else:        
        button_java["bg"] = "green"
        my_canvas.delete("tag_java")
        my_canvas.create_line(192, 200, 220, 200, fill="green", width="4", tag="tag_java")
        my_canvas.create_text(230, 200, text="main.js", fill="green", font=("bold 20"), anchor="w", tag="tag_java")


def build():     
    if os.path.exists(folderName):        
        print('Warning box displayed: '+folderName+' already exists.')    
        tkinter.messagebox.showerror("Overwrite WARNING", appOverwriteWarning)
        filedialog.askopenfilename(initialdir="/", title="Move or Rename Folder: "+ folderName)
    else:                
        # makes folder "webSite" and makes empty file "index.html"
        if button_index["bg"] == "green":
            folder = folderName
            file = 'index.html'
            makeMyFolder(folder)
            makeMyFile(folder, file)

        # makes folder "css" inside webSite folder and makes empty file "style.css"
        if button_style["bg"] == "green":
            folder = folderName + "css/"
            file = 'style.css'
            makeMyFolder(folder)
            makeMyFile(folder, file)

        # makes folder "webSite" and makes empty file "index.html"
        if button_robots["bg"] == "green":
            folder = folderName
            file = 'robots.txt'
            makeMyFile(folder, file)

        # makes folder "webSite" and makes empty file "index.html"
        if button_manifest["bg"] == "green":
            folder = folderName
            file = 'manifest.json'
            makeMyFile(folder, file)

        # makes folder "webSite" and makes empty file "index.html"
        if button_java["bg"] == "green":
            folder = folderName
            file = 'main.js'
            makeMyFile(folder, file)

        # makes an empty folder "img" inside Website folder
        folder = folderName + "img/"
        makeMyFolder(folder)

        # opens file manager to display made folder and files
        filedialog.askopenfilename(initialdir="/", title="Your new files and folders are in: "+ folderName)
        app.destroy()
        exit()
       
def endApp():
    app.destroy()
    exit()

 
# defines variables as listed
appTitle = "QS File Template"
appDescription = "QS File Template is for anyone who is building a website from complete scratch using HTML and CSS. QS File Template reduces time in the basic setup of file structure by building a common folders and adding blank basic files.\nBy default, the files and folders include - index.html, style.css, robots.txt, mainfest.json and main.js."
appInstructions = "Click 'BUILD' for default, or deselect as required."
appCopyright = "Framework2232 © 2020 - https://framework2232.github.io"
appOverwriteWarning = "APP WARNING:\n    These folder(s) or file(s) already exist.\nSOLUTION:\n    Move or rename the existing files or folders\n    Select 'BUILD' again."


# build folder in this varialble...
folderName = '/website/'


# define common button styles
buttBG = "green"
buttFG = "white"
buttFONT = "bold 14"
buttWIDTH = "10"
buttPADX = "10"
rowPADY = "5"


# =============== MAKE A TKINTER WINDOW =============
app=Tk()
app.title(appTitle)
app.iconbitmap("img/icon.ico")
app.geometry("800x550")
app.configure(bg="#141414")


# =================== LABELS ===================
# Label = App Title - at the top of the frame
labelAppHeading=Label(app,text=appTitle)
labelAppHeading.configure(font=("bold Arial",24))
labelAppHeading.configure(bg="#141414",fg="green")
# Label = App Description - under the App Title
labelAppDescription=Label(app,text=appDescription,bg="#141414",fg="lightgrey")
labelAppDescription.config(font=("Arial",12), justify="left")
labelAppDescription.bind('<Configure>', lambda e: labelAppDescription.config(wraplength="800"))
# Label = App Instructions - under the App Description
labelAppInstructions=Label(app,text=appInstructions,bg="#141414",fg="lightgrey")
labelAppInstructions.config(font=("Arial",14))
# Label = App Copyright - bottom of the App
labelAppCopyright=Label(app,text=appCopyright,bg="#141414",fg="#444")
labelAppCopyright.config(font=("Arial",12), justify="center")


# ================== BUTTONS ====================
# button index.html
button_index = Button(app,text="index.html",command=include_index)
button_index.configure(bg=buttBG,fg=buttFG,font=buttFONT,width=buttWIDTH,padx=buttPADX)
# button style.css
button_style = Button(app,text="style.css",command=include_style)
button_style.configure(bg=buttBG,fg=buttFG,font=buttFONT,width=buttWIDTH,padx=buttPADX)
# button robots.txt
button_robots = Button(app,text="robots.txt",command=include_robots)
button_robots.configure(bg=buttBG,fg=buttFG,font=buttFONT,width=buttWIDTH,padx=buttPADX)
# button mainfest.json
button_manifest = Button(app, text = "manifest.json", command = include_manifest)
button_manifest.configure(bg = buttBG, fg = buttFG, font=buttFONT, width = buttWIDTH, padx = buttPADX)
# button main.js
button_java = Button(app,text="main.js",command=include_java)
button_java.configure(bg=buttBG,fg=buttFG,font=buttFONT,width=buttWIDTH,padx=buttPADX)
# button exit
button_exit = Button(app, text = "Exit", command = endApp)
button_exit.configure(bg = "grey", fg = buttFG, font=buttFONT, width = buttWIDTH, padx = buttPADX)
# button build
button_build = Button(app, text = "Build", command = build)
button_build.configure(bg = buttBG, fg = buttFG, font=buttFONT, width = buttWIDTH, padx = buttPADX) 


# =============== BUILD CANVAS (diagram)===================
my_canvas = Canvas(app, width=400, height="220", bg="#141414", highlightthickness=0)
my_canvas.create_text(140, 20, text="/website/", fill="green", font=("bold 20"), anchor="e")
my_canvas.create_line(150, 20, 192, 20, fill="green", width="4")
# line = vertical
my_canvas.create_line(190, 20, 190, 202, fill="green", width="4")

my_canvas.delete("tag_index")
my_canvas.create_line(192, 40, 220, 40, fill="green", width="4",tag="tag_index")
my_canvas.create_text(230, 40, text="index.html", fill="green", font=("bold 20"), anchor="w", tag="tag_index") 

my_canvas.delete("tag_style")
my_canvas.create_line(192, 80, 220, 80, fill="green", width="4", tag="tag_style")
my_canvas.create_text(230, 80, text="style.css", fill="green", font=("bold 20"), anchor="w", tag="tag_style")

my_canvas.delete("tag_robots")
my_canvas.create_line(192, 120, 220, 120, fill="green", width="4", tag="tag_robots")
my_canvas.create_text(230, 120, text="robots.txt", fill="green", font=("bold 20"), anchor="w", tag="tag_robots")

my_canvas.delete("tag_manifest")
my_canvas.create_line(192, 160, 220, 160, fill="green", width="4", tag="tag_manifest")
my_canvas.create_text(230, 160, text="manifest.json", fill="green", font=("bold 20"), anchor="w", tag="tag_manifest")

my_canvas.delete("tag_java")
my_canvas.create_line(192, 200, 220, 200, fill="green", width="4", tag="tag_java")
my_canvas.create_text(230, 200, text="main.js", fill="green", font=("bold 20"), anchor="w", tag="tag_java")


# option to alter the weight of each column if needed
app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)
app.grid_columnconfigure(2,weight=1)


# control the layout using grid
labelAppHeading.grid(row=1, column=0, columnspan=3)
labelAppDescription.grid(row=2, column=0, columnspan=3)
labelAppInstructions.grid(row=3, column=0, columnspan=3, pady="20")
button_index.grid(row=4, column=0, pady = rowPADY)
button_style.grid(row=5, column=0, pady = rowPADY)
button_robots.grid(row=6, column=0, pady = rowPADY)
button_manifest.grid(row=7, column=0, pady = rowPADY)
button_java.grid(row=8, column=0, pady = rowPADY)
button_exit.grid(row=9, column=1, pady = rowPADY)
button_build.grid(row=9, column=2, pady = rowPADY)
my_canvas.grid(row=4, column=1, columnspan=2, rowspan=4)
labelAppCopyright.grid(row=10,column=0,columnspan=3,pady="10")


app.mainloop()