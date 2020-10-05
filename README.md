<p align="center">
    <img src="https://github.com/framework2232/framework2232.github.io/blob/master/images/banner.png?raw=true" alt="Framework2232 Logo" width="500"/>
</p>
<h1 align=center>QS FILE TEMPLATE</h1>

__AUTHOR:__ [Framework2232][Framework2232Website]

__COPYRIGHT:__ Framework2232, © 2020

__DATE:__ 05OCT20

__VERSION:__ 1.0.1

__GITHUB:__ [__https://github.com/framework2232/QSfiletemplate__](https://github.com/framework2232/QSfiletemplate "QS File Template")

__WEBSITE:__ [__https://framework2232.github.io__][QSfiletemplateWebsite]

---

## PURPOSE
#### _Developed as a quick folder / file builder for HTML/CSS based websites._

* QS File Template is for anyone who is building a website from complete scratch using HTML and CSS.
* QS File Template will build a common folder structure and add basic files including.
   * empty ___index.html___ inside root folder
   * empty ___style.css___ inside __css__ folder
   * empty ___img___ folder
* QS File Template reduces time in the basic setup of file structure as the folders and files are ready to go.
* QS File Template is designed to be run as the first part of the process of writting the website.
* The folders and files are built in a folder named ___/webSite/___ in the root directory of your current drive. Files built by QS File Template can be selected or deselected depending on intensons. When running the script with its default settings, the result is:
   * __/webSite/css/style.css__
   * __/webSite/img/__
   * __/webSite/index.html__
   * __/webSite/main.js__
   * __/webSite/manifest.json__
   * __/webSite/robots.txt__
* The files built by QS File Template are empty, ready for you to add your own script

---

## REQUIREMENTS

QS File Template runs successfully with:
* Windows 10
* Python 3.8.5 32bit using standard libraries:
   * tkinter
   * os

---
## HOW TO RUN QS File Template:
1. __Run QS File Template__ by opening: _"RunMe"_ python script. 
2. __Click 'BUILD'__ for the default file, or deselect the files not required. Changes can be made anytime before 'BUILD' is selected.


<p align="center">
    <img src="https://github.com/framework2232/QSfiletemplate/blob/main/img/screen_GUI_Selected.PNG?raw=true" alt="Image of GUI with afor you to add your scriptll buttons selected" width="500"/>
</p>

* ___Above:__ Image shows all buttons green, therefore when 'BUILD' is selected, all files and folders will be made (default)._

---

<p align="center">
    <img src="https://github.com/framework2232/QSfiletemplate/blob/main/img/screen_GUI_Deselected.PNG?raw=true" alt="Image of GUI with some buttons selected and others deselected" width="500"/>
</p>

* ___Above:__ Image shows the red buttons have been deselected, therefore only the green files and folders will be made. On the right the diagram has selected files in green, and deselected files in grey._

---
3. After selecting 'BUILD':
  * If the folders and files __DO__ already exist, an error messagebox will be displayed and file manager window opened. This is to prevent any existing files being accidently overwritten. 
  * If the folders and files __DON'T__ already exist, QS File Template builds the selected files, opens file manager and displays the new folders and files.

<p align="center">
    <img src="https://github.com/framework2232/QSfiletemplate/blob/main/img/screen_GUI_WarningFilesExist.PNG?raw=true" alt="Image of error messagebox displayed when file already exists" width="500"/>
</p>

* ___Above:__ Image shows an error messagebox advising the folders already exist, preventing accidental overwrite._

---

<p align="center">
    <img src="https://github.com/framework2232/QSfiletemplate/blob/main/img/screen_FileManagerDisplayingFiles.PNG?raw=true" alt="Image of opened File Manager displaying the folders and files" width="500"/>
</p>

* ___Above:__ Image shows file manager box displaying the newly build files and folders._



---
## HOW QS FILE TEMPLATE WORKS

__1.__ Variables declared and functions called:
```python
folder = '/webSite/'
file = 'index.html'
makeMyFolder(folder)
makeMyFile(folder, file)
```

__2.__ If the folder _DOES NOT_ already exist, the folder is made:
```python
def makeMyFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print('Made your folder: ' + folder)
```

__3.__ If the folder _DOES_ exist, an error messagebox is displayed:
```python
def build():     
    if os.path.exists(folderName):        
        print('Warning box displayed: '+folderName+' already exists.')    
        tkinter.messagebox.showerror("Overwrite WARNING", appOverwriteWarning)
        filedialog.askopenfilename(initialdir="/", title="Move or Rename Folder: "+ folderName)
    else:                
```

__4.__ The empty file is built in the appropriate directory.
```python
def makeMyFile(folder, file):
    os.chdir(folder)
    with open(file,'w') as f:
        f.write('')
        print('Built: '+ file)
```

---

## ABOUT FRAMEWORK2232

I independently work on Framework2232 in my free time. If you'd like show your support, please follow and promote the usual social media.

[__Twitter__][Twitter]
| [__Instagram__][Instagram]
| [__YouTube__][YouTube]
| [__GitHub__][GitHub]
| [__Pinterest__][Pinterest]

__This repository is shared public in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.__

[See the GNU General Public License for more details.][GNULicense]

---

[Framework2232Website]: https://framework2232.github.io "Framework2232"
[QSfiletemplateWebsite]: https://framework2232.github.io "Framework2232"
[GNULicense]: https://github.com/framework2232/QSfiletemplate/blob/main/LICENSE "GNU General Public License"

[Twitter]: https://github.com/framework2232/Python "Twitter - Framework2232"
[Instagram]: https://github.com/framework2232/HTML "Instagram - Framework2232"
[YouTube]: https://github.com/framework2232/CSS "YouTube - Framework2232"
[GitHub]: https://github.com/framework2232/Markdown "GitHub - Framework2232"
[Pinterest]: https://github.com/framework2232/Markdown "Pinterest - Framework2232"