

import PySimpleGUI as sg
import glob
import ast
import time
import random

from PIL import Image, ImageTk



'''
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
'''



SHOPTAGS = {
    
    'ESS':{'cost':100,
           'name':'Earth Saving Sim',
           'files':{'path':'scip','combi':'combi.txt'}
           }
    
            }



'''
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
'''



class Windows():
    def __init__(self, name=''):
        self.format = []
        self.name = ''
        self.size = (1120, 680)
        self.state = False
        self.story_name = ''
        self.image_path = ''
        self.combi_file = ''
        self.wallet = 100
        self.storylines = {}
        
        
    def __str__(self):
        return 'layout: ' + str(self.format)
    
    
    
    def set_window(self, window):
        if self.state:
            window.Maximize()
            window['Restore Down'].Update(visible = True)
            window['Maximize'].Update(visible = False)
        else:
            window['Restore Down'].Update(visible = False)
            
        delay()
        window.SetAlpha(1)
    
    
    def maximize(self, window):
        window.Maximize()
        window['Restore Down'].Update(visible = True)
        window['Maximize'].Update(visible = False)
        self.state = True
    
    
    def minimize(self, window):
        window.normal()
        window['Restore Down'].Update(visible = False)
        window['Maximize'].Update(visible = True)
        self.state = False


    def open_new_window(self, window):
        window.close()
        window = sg.Window(str(self.name), self.format, 
                           size=self.size, alpha_channel=0)
        
        return window
    
    
    def check_story(self,window):
        if self.name == 'Selection Page':
            if 'Earth Saving Sim' not in ((self.storylines).keys()):
                window['Earth Saving Sim'].Update(disabled = True)
            else:
                window['Earth Saving Sim'].Update(disabled = False)
                
        elif self.name == 'Shop':
            if 'Earth Saving Sim' in ((self.storylines).keys()):
                window['Purchase Earth Saving Sim'].Update(disabled = True)
            else:
                window['Purchase Earth Saving Sim'].Update(disabled = False)
    
    
    def bought(self,tag):
        detailsdict = SHOPTAGS[tag]
        cost = detailsdict['cost']
        name = detailsdict['name']
        files = detailsdict['files']
        combi = files['combi']
        images = files['path']
        
        if self.wallet >= cost:
            self.wallet -= 100
            sg.Popup('purchase sucessful', keep_on_top = True)
            self.storylines[name]={'path':images,
                                   'combi':combi}
                
        else:
            sg.Popup('you broke', keep_on_top = True,)
    
    
    def ranselect(self):
        storylines_avail = list((self.storylines).keys())
        if len(storylines_avail) == 0:
            sg.Popup('''You have no storylines available lol.''', 
                     keep_on_top=True)
        else:
            choice_index = random.randrange(len(storylines_avail))-1
            self.story_name = storylines_avail[choice_index]
            self.image_path = (self.storylines[self.story_name])['path']
            self.combi_file = (self.storylines[self.story_name])['combi']
                
            sg.Popup(str('''Congrats!
Your storyline is '''+self.story_name), keep_on_top=True)
        
        
        
        
##########################################################################
###############################layouts####################################
##########################################################################
    
    
    def loadhome(self):
        self.name = 'Home Page'
        self.format = [
        [
            sg.Button("Play"),
            sg.Button("Help Page"),
            sg.Button("Selection"),
            sg.Button("Shop"),
            sg.Button("Debug"),
            sg.Button("Maximize"),
            sg.Button("Restore Down"),
        ],
                        ]
    
    
    def loadhelp(self):
        self.name = 'Help Page'
        self.format = [
                [
                    sg.Button("Home"),
                    sg.Button("Maximize"),
                    sg.Button("Restore Down"),
                ],
                [
                    sg.Text("Troubleshooting Page")
                ],
                [
                    sg.Text('''if there are errors, it might be:
- the pictures shown in the GUI are wrong
    - the path to the folder for the pictures is wrong
    - the folder contains excess picures that are not part of the storyline but are also of the png or jpg format
    - the pictures are labelled wrongly, make sure they are named in the correct sequence like, 1,2,3,4,5,6...... or slide1, slide2, slide3......
    - the combinations in combi.txt are writen wrongly
    
- the code shows an error message
    - the combinations do not match the slides
    - the combinations are written in the wrong format
    - the pictures are in the wrong format
    - the path to the folder for the pictures is wrong
    - the name of the combinations file is wrong
    - the files are not in the same folder

OR:
It's just my fault and please send a bug report to this email:
evan.h@outlook.com


''')
                ],
                [
                    sg.Text("How to play")
                ],
                [
                    sg.Text('''1. Run the code.
2. Press 'Selection' and key in details unless you want to play the default game.
3. Press 'Home'. 
4. Press 'Play' 
5. Don't die of boredom''')
                ],
        
                            ]
                
        
    def loadselect(self):
        self.name = 'Selection Page'
        self.format = [
                [
                    sg.Button("Home"),
                    sg.Button("Maximize"),
                    sg.Button("Restore Down")
                ],
                [
                    sg.Text("Available storylines: "),
                    sg.Button("Earth Saving Sim")
                ],
                [
                    sg.Button("Random Select")
                ],
                [
                    sg.Text(str("Your current storyline is " + 
                                self.story_name + 
                                "\nYour current picture path is " + 
                                self.image_path + 
                                "\nYour current combinations file is " + 
                                self.combi_file))
                ],
                [
                    sg.Text('''name of new story: '''), sg.InputText(),
                ],
                [
                    sg.Text('''system path to the folders containing
the pictures for the story: '''), sg.InputText(),
                ],
                [
                    sg.Text('''name of the text file 
containing the combinations: '''), sg.InputText()
                ],
                [
                    sg.Button('Submit')
                ]
        
                            ]


    def loadshop(self):
        self.name = 'Shop'
        self.format = [
                [
                    sg.Button("Home"),
                    sg.Button("Maximize"),
                    sg.Button("Restore Down")
                ],
                [
                    sg.Text(str("Your available credits are " + str(self.wallet)))
                ],
                [
                    sg.Text("Sold storylines: "),
                    sg.Button("Purchase Earth Saving Sim")
                ],
                            ]
        
        
    def loadpurchase(self,tag):
        detailsdict = SHOPTAGS[tag]
        cost = detailsdict['cost']
        name = detailsdict['name']
        
        
        self.name = 'Checkout'
        self.format = [
                [
                    sg.Button("Home"),
                    sg.Button("Maximize"),
                    sg.Button("Restore Down")
                ],
                [
                    sg.Text(str("\nYour available credits are " + str(self.wallet) + 
                                "\n" + str(name) + " cost: " + str(cost)))
                ],
                [
                    sg.Button("Buy " + str(name)),
                    sg.Button("Shop")
                ],
                            ]


                            
'''
--------------------------------------------------------------------------
'''



class Gamewindow(Windows):
    def __init__(self, name=''):
        Windows.__init__(self, name)
        self.images = ''
        self.location = 0
        self.x = 1080
        self.y = 580
        self.layout = [
                    [
                        sg.Button("Home"),
                        sg.Button("Debug"),
                        sg.Button("Maximize"),
                        sg.Button("Restore Down"),
                    ],
                    [sg.Image(key="image")],
                    [
                        sg.Button("Start"),
                        sg.Button("Prev"),
                        sg.Button("Next"),
                        sg.Button("Option 1"),
                        sg.Button("Option 2"),
                        sg.Button("Option 3"),
                    ],
        
                                ]
    
    
    def maximize(self, window):
        Windows.maximize(self, window)
        self.x = 1500
        self.y = 750
        load_image((self.images)[self.location], window, self.x, self.y)
    
    
    def minimize(self, window):
        Windows.minimize(self, window)
        self.x = 1080
        self.y = 580
        load_image((self.images)[self.location], window, self.x, self.y)



'''
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
'''


def load_image(path, window, x, y):
    '''
    Parameters
    ----------
    path : string
        A single-line string denoting the system file path of 
        the specific photo to be displayed. *Is not input by the user.
    window : unknown
        The GUI for the photo to be displayed in. *Is not 
        input by the user.

    Returns
    -------
    None:
        
    Function Description
    --------------------
    Displays image onto GUI

    '''
    try:
        image = Image.open(path)
        image.thumbnail((x, y))
        photo_img = ImageTk.PhotoImage(image)
        window["image"].update(data=photo_img)
    except:
        print(f"Unable to open {path}!")

'''
--------------------------------------------------------------------------
'''

def delay():
    time.sleep(.5)


'''
--------------------------------------------------------------------------
--------------------------------------------------------------------------
--------------------------------------------------------------------------
'''


general = Windows()
currentwindow = general


sg.theme('random')
    
elementshome = [        
    [
     sg.Button("Play"),
     sg.Button("Help Page"),
     sg.Button("Selection"),
     sg.Button("Shop"),
     sg.Button("Debug"),
     sg.Button("Maximize"),
     sg.Button("Restore Down"),
     ],
        
                ]
    
window = sg.Window("Home Page", elementshome, 
                   size=(1120, 680))
window.finalize()



window['Restore Down'].Update(visible = False)
window['Maximize'].Update(visible = True)

while True:
    event, values = window.read()
        
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Maximize':
        currentwindow.maximize(window)
    
    if event == 'Restore Down':
        currentwindow.minimize(window)
    
    if event == 'Home':
        currentwindow.loadhome()
        window = currentwindow.open_new_window(window)
        window.Finalize()
        currentwindow.set_window(window)
    
    if event == 'Help Page':
        currentwindow.loadhelp()
        window = currentwindow.open_new_window(window)
        window.Finalize()
        currentwindow.set_window(window)
    
    
    if event == 'Selection':
        currentwindow.loadselect()
        window = currentwindow.open_new_window(window)
        window.Finalize()
        currentwindow.set_window(window)
        currentwindow.check_story(window)
    
    
    if event == 'Shop':
        currentwindow.loadshop()
        window = currentwindow.open_new_window(window)
        window.Finalize()
        currentwindow.set_window(window)
        currentwindow.check_story(window)
    
    
    if event == 'Purchase Earth Saving Sim':
        currentwindow.loadpurchase('ESS')
        window = currentwindow.open_new_window(window)
        window.Finalize()
        currentwindow.set_window(window)
    
    
    if event == 'Buy Earth Saving Sim':
        currentwindow.bought('ESS')
        currentwindow.loadshop()
        window = currentwindow.open_new_window(window)
        window.Finalize()
        currentwindow.set_window(window)
        currentwindow.check_story(window)
    
    
    if event == 'Random Select':
        currentwindow.ranselect()
        currentwindow.loadhome()
        window = currentwindow.open_new_window(window)
        window.Finalize()
        currentwindow.set_window(window)
    
    
    if event == 'Earth Saving Sim':
        currentwindow.story_name = "Earth Saving Sim"
        currentwindow.image_path = (currentwindow.storylines[currentwindow.story_name])['path']
        currentwindow.combi_file = (currentwindow.storylines[currentwindow.story_name])['combi']
        currentwindow.loadhome()
        window = currentwindow.open_new_window(window)
        window.Finalize()
        currentwindow.set_window(window)
    
    
    if event == 'Submit':
        currentwindow.story_name = values[0]
        currentwindow.image_path = values[1]
        currentwindow.combi_file = values[2]
        currentwindow.loadhome()
        window = currentwindow.open_new_window(window)
        window.Finalize()
        currentwindow.set_window(window)
    
    
#    if event == 'Play':
#        if combi_file == '':
#            sg.Popup('''You have not chosen a storyline!''', 
#                     keep_on_top=True)
#                   
#                   #########
#                   
#        else:
#            elementsgame = [
#                [
#                    sg.Button("Home"),
#                    sg.Button("Debug"),
#                    sg.Button("Maximize"),
#                    sg.Button("Restore Down"),
#                ],
#                [sg.Image(key="image")],
#                [
#                    sg.Button("Start"),
#                    sg.Button("Prev"),
#                    sg.Button("Next"),
#                    sg.Button("Option 1"),
#                    sg.Button("Option 2"),
#                    sg.Button("Option 3"),
#                ],
#        
#                            ]
#            window.close()
#            window = sg.Window(name, elementsgame, 
#                               size=(1120, 680), alpha_channel=0)
#            images = sorted( glob.glob(f'{system_path}/*.jpg')\
#                            +glob.glob(f'{system_path}/*.png') )
#            location = 0
#            window.finalize()
#        
#            window['Prev'].Update(disabled = True)
#            window['Next'].Update(disabled = True)
#            window['Option 1'].Update(disabled = True)
#            window['Option 2'].Update(disabled = True)
#            window['Option 3'].Update(disabled = True)
#            if state == 'max':
#                window.Maximize()
#                window['Restore Down'].Update(visible = True)
#                window['Maximize'].Update(visible = False)
#            elif state =='min':
#                window['Restore Down'].Update(visible = False)
#            
#            delay()
#            window.SetAlpha(1)
#
#            
#            with open(combi_file) as f:
#                lines = f.readlines()
#            indexbranches = lines.index('Branching:\n')
#            branchesbasic = (lines[indexbranches + 1])
#            story_choices = ast.literal_eval(branchesbasic)
#            
#            indexends = lines.index('Ending Points:\n')
#            endbasic = (lines[indexends + 1])
#            ends = ast.literal_eval(endbasic)
#            
#            irregularindex = lines.index('Exceptions:\n')
#            irregularity = (lines[irregularindex + 1])
#            irregularities = ast.literal_eval(irregularity)
#            
#            goodendindex = lines.index('Good Endings:\n')
#            goodend = (lines[goodendindex + 1])
#            good_ends = ast.literal_eval(goodend)
#            
#            bad_ends = []
#            for ending in ends:
#                if ending not in good_ends:
#                    bad_ends.append(ending)
#




#                        I'LL ONLY HAVE THE ENTIRE CODE FOR GAMEPLAY LEFT! YAYYYYY



