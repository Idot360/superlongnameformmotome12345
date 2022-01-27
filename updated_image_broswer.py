'''
file name: 'updated_image_browser.py'
@author: evanh
._.

This is the updated code for the no idea what this is anymore
was originally the mm otome game my group made


DROWNING IN INEFICIENCY WTH

Not being able to reuse layouts is stupid 


Requirements:
    -Python 3 installed
    -PySimpleGUI installed:
        'python -m pip install pysimplegui'
        or if user operates with anaconda:
        'conda install -c conda-forge pysimplegui'
    -folder containing pictures for the story (png/jpeg) make sure there 
     are no other files with '.png'/'.jpeg' extentions in the folder
    -fully written combinations file

Instructions for designers:
    -Design a combinations file with the format in combi.txt
    -Move the text file with the combinations to the same folder as 
     this file with code
    -Run the code
    -Go to selection
    -Key in the system path to the folder with the story pictures
    -Key in the name for your story
    -Key in the file name of the combinations file
    -Click 'Submit'
    -Go back to Home

Instructions for players:
    -Run this code
    -Go to selection
    -Check that all the information is correct
    -Press 'Play' to load current story
    -Press 'Start' to begin
    -Press 'next' to continue to the next slide
    -Press 'prev' to go back to the previous slide
    -At intersections where you are given different choices, 
     pick option 1, 2 or 3 to denote your choice
    -If you wish to restart, press start again
'''



import glob
import PySimpleGUI as sg
import ast
import time
import random

'''
=======
'''

from PIL import Image, ImageTk




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




def delay():
    time.sleep(.3)



def main():

    storylines = {}
    name = ''
    system_path = ''
    combi_file = ''
    location = 0
    ends = []
    story_choices = {}
    trigger = False
    images = sorted( glob.glob(f'{system_path}/*.jpg')\
                    +glob.glob(f'{system_path}/*.png') )
    x = 1080
    y= 580
    state = 'min'
    money = 100
    esstrigger = False
    
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

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        
        
        '''maximize'''
        if event == "Maximize":
            window.Maximize()
            window['Restore Down'].Update(visible = True)
            window['Maximize'].Update(visible = False)
            x = 1500
            y = 750
            state = 'max'
            print('trigger', trigger)
            if trigger == True:
                load_image(images[location], window, x, y)


            
        
        '''restore down'''
        if event == "Restore Down":
            window.normal()
            window['Restore Down'].Update(visible = False)
            window['Maximize'].Update(visible = True)
            x = 1080
            y= 580
            state = 'min'
            print('trigger', trigger)
            if trigger == True:
                load_image(images[location], window, x, y)

        
        
        if event == 'Home':
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
            window.close()
            window = sg.Window("Home page", elementshome, 
                               size=(1120, 680), alpha_channel=0)
            window.finalize()
            if state == 'max':
                window.Maximize()
                window['Restore Down'].Update(visible = True)
                window['Maximize'].Update(visible = False)
            elif state =='min':
                window['Restore Down'].Update(visible = False)
            trigger = False
            
            delay()
            window.SetAlpha(1)
        
        
        if event == 'Help Page':
            elementshelp = [
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
            window.close()
            window = sg.Window("Help page", elementshelp, 
                               size=(1120, 680), alpha_channel=0)
            window.finalize()
            if state == 'max':
                window.Maximize()
                window['Restore Down'].Update(visible = True)
                window['Maximize'].Update(visible = False)
            elif state =='min':
                window['Restore Down'].Update(visible = False)
            
            delay()
            window.SetAlpha(1)
            
        
        if event == 'Shop':
            elementsshop = [
                [
                    sg.Button("Home"),
                    sg.Button("Maximize"),
                    sg.Button("Restore Down")
                ],
                [
                    sg.Text(str("Your available credits are " + str(money)))
                ],
                [
                    sg.Text("Sold storylines: "),
                    sg.Button("Purchase Earth Saving Sim")
                ],
                            ]
            window.close()
            window = sg.Window("Shop", elementsshop, 
                               size=(1120, 680), alpha_channel=0)
            window.finalize()
            if state == 'max':
                window.Maximize()
                window['Restore Down'].Update(visible = True)
                window['Maximize'].Update(visible = False)
            elif state =='min':
                window['Restore Down'].Update(visible = False)
            
            if esstrigger:
                window['Purchase Earth Saving Sim'].Update(disabled = True)
            else:
                window['Purchase Earth Saving Sim'].Update(disabled = False)
            
            delay()
            window.SetAlpha(1)
        
        
        if event == 'Purchase Earth Saving Sim':
            elementsessshop = [
                [
                    sg.Button("Home"),
                    sg.Button("Maximize"),
                    sg.Button("Restore Down")
                ],
                [
                    sg.Text(''' ''')
                ],
                [
                    sg.Text(str("Your available credits are " + str(money)))
                ],
                [
                    sg.Button("Buy Ess"),
                    sg.Button("Return to shop")
                ],
                            ]
            window.close()
            window = sg.Window("Ess", elementsessshop, 
                               size=(1120, 680), alpha_channel=0)
            window.finalize()
            if state == 'max':
                window.Maximize()
                window['Restore Down'].Update(visible = True)
                window['Maximize'].Update(visible = False)
            elif state =='min':
                window['Restore Down'].Update(visible = False)
            
            delay()
            window.SetAlpha(1)
        
        
        if event == "Buy Ess":
            if money >= 100:
                money -= 100
                esstrigger = True
                sg.Popup('purchase sucessful', keep_on_top = True)
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
                window.close()
                window = sg.Window("Home page", elementshome, 
                                   size=(1120, 680), alpha_channel=0)
                window.finalize()
                if state == 'max':
                    window.Maximize()
                    window['Restore Down'].Update(visible = True)
                    window['Maximize'].Update(visible = False)
                elif state =='min':
                    window['Restore Down'].Update(visible = False)
                trigger = False
            
                delay()
                window.SetAlpha(1)
                
                storylines['Earth Saving Sim']={'path':'scip',
                                                'combi':'combi.txt'}
                
            else:
                sg.Popup('you broke', keep_on_top = True,)
                
        
        if event == 'Return to shop':
            elementsessshop = [
                [
                    sg.Button("Home"),
                    sg.Button("Maximize"),
                    sg.Button("Restore Down")
                ],
                [
                    sg.Text(''' ''')
                ],
                [
                    sg.Text(str("Your available credits are " + str(money)))
                ],
                [
                    sg.Button("Buy Ess"),
                    sg.Button("Return to shop")
                ],
                            ]
            window.close()
            window = sg.Window("Ess", elementsessshop, 
                               size=(1120, 680), alpha_channel=0)
            window.finalize()
            if state == 'max':
                window.Maximize()
                window['Restore Down'].Update(visible = True)
                window['Maximize'].Update(visible = False)
            elif state =='min':
                window['Restore Down'].Update(visible = False)
            
            delay()
            window.SetAlpha(1)
        
        
        if event == 'Selection':
            
            elementsselect = [
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
                    sg.Text(str("Your current storyline is " + name))
                ],
                [
                    sg.Text(str("Your current picture path is " + system_path))
                ],
                [
                    sg.Text(str("Your current combinations file is " + combi_file))
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
            window.close()
            window = sg.Window("Home page", elementsselect, 
                               size=(1120, 680), alpha_channel=0)
            window.finalize()
            if state == 'max':
                window.Maximize()
                window['Restore Down'].Update(visible = True)
                window['Maximize'].Update(visible = False)
            elif state =='min':
                window['Restore Down'].Update(visible = False)
            
            if esstrigger:
                window['Earth Saving Sim'].Update(disabled = False)
            else:
                window['Earth Saving Sim'].Update(disabled = True)
            
            delay()
            window.SetAlpha(1)
        
        
        if event == 'Random Select':
            storylines_avail = list(storylines.keys())
            print(storylines_avail)
            print(type(storylines_avail))
            if len(storylines_avail) == 0:
                   sg.Popup('''You have no storylines available lol.''', 
                            keep_on_top=True)
            else:
                choice_index = random.randrange(len(storylines_avail))-1
                name = storylines_avail[choice_index]
                system_path = (storylines[name])['path']  
                combi_file = (storylines[name])['combi']
                
                sg.Popup(str('''Congrats!
Your storyline is '''+name), keep_on_top=True)
                
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
            window.close()
            window = sg.Window("Home page", elementshome, 
                               size=(1120, 680), alpha_channel=0)
            window.finalize()
            if state == 'max':
                window.Maximize()
                window['Restore Down'].Update(visible = True)
                window['Maximize'].Update(visible = False)
            elif state =='min':
                window['Restore Down'].Update(visible = False)
            trigger = False
            
            delay()
            window.SetAlpha(1)
            
        
        
        if event == "Earth Saving Sim":
            name = "Earth Saving Sim"
            system_path = (storylines[name])['path']
            combi_file = (storylines[name])['combi']
            
            elementshome = [
                [
                    sg.Button("Play"),
                    sg.Button("Help Page"),
                    sg.Button("Selection"),
                    sg.Button("Debug"),
                    sg.Button("Maximize"),
                    sg.Button("Restore Down"),
                ],
        
                        ]
            window.close()
            window = sg.Window("Home page", elementshome, 
                               size=(1120, 680), alpha_channel=0)
            window.finalize()
            if state == 'max':
                window.Maximize()
                window['Restore Down'].Update(visible = True)
                window['Maximize'].Update(visible = False)
            elif state =='min':
                window['Restore Down'].Update(visible = False)
            trigger = False
            
            delay()
            window.SetAlpha(1)
        
        
        if event == "Submit":
            name = values[0]
            system_path = values[1]
            combi_file = values[2]
            
            elementshome = [
                [
                    sg.Button("Play"),
                    sg.Button("Help Page"),
                    sg.Button("Selection"),
                    sg.Button("Debug"),
                    sg.Button("Maximize"),
                    sg.Button("Restore Down"),
                ],
        
                        ]
            window.close()
            window = sg.Window("Home page", elementshome, 
                               size=(1120, 680), alpha_channel=0)
            window.finalize()
            if state == 'max':
                window.Maximize()
                window['Restore Down'].Update(visible = True)
                window['Maximize'].Update(visible = False)
            elif state =='min':
                window['Restore Down'].Update(visible = False)
            trigger = False
            
            delay()
            window.SetAlpha(1)
        

        if event == "Debug":
            pass
        
        
        if event == "Play":
            
            if combi_file == '':
                   sg.Popup('''You have not chosen a storyline!''', 
                            keep_on_top=True)
                   
                   #########
                   
            else:
                elementsgame = [
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
                window.close()
                window = sg.Window(name, elementsgame, 
                                   size=(1120, 680), alpha_channel=0)
                images = sorted( glob.glob(f'{system_path}/*.jpg')\
                                +glob.glob(f'{system_path}/*.png') )
                location = 0
                window.finalize()
            
                window['Prev'].Update(disabled = True)
                window['Next'].Update(disabled = True)
                window['Option 1'].Update(disabled = True)
                window['Option 2'].Update(disabled = True)
                window['Option 3'].Update(disabled = True)
                if state == 'max':
                    window.Maximize()
                    window['Restore Down'].Update(visible = True)
                    window['Maximize'].Update(visible = False)
                elif state =='min':
                    window['Restore Down'].Update(visible = False)
            
                delay()
                window.SetAlpha(1)

            
                with open(combi_file) as f:
                    lines = f.readlines()
                indexbranches = lines.index('Branching:\n')
                branchesbasic = (lines[indexbranches + 1])
                story_choices = ast.literal_eval(branchesbasic)
            
                indexends = lines.index('Ending Points:\n')
                endbasic = (lines[indexends + 1])
                ends = ast.literal_eval(endbasic)
            
                irregularindex = lines.index('Exceptions:\n')
                irregularity = (lines[irregularindex + 1])
                irregularities = ast.literal_eval(irregularity)
            
                goodendindex = lines.index('Good Endings:\n')
                goodend = (lines[goodendindex + 1])
                good_ends = ast.literal_eval(goodend)
            
                bad_ends = []
                for ending in ends:
                    if ending not in good_ends:
                        bad_ends.append(ending)
            
                print()
                print(story_choices)
                print()
                print(ends)
                print()
                print(irregularities)
                print()
        
        
        '''
        basic start or reset
        '''
        if event == "Start":
            load_image(images[0], window, x, y)
            location = 0
            current_route = [0] #rerecording the sequence
            
            window['Prev'].Update(disabled = True)
            window['Next'].Update(disabled = False)
            window['Option 1'].Update(disabled = True)
            window['Option 2'].Update(disabled = True)
            window['Option 3'].Update(disabled = True)
            
            trigger = True
            print('trigger', trigger)
        
        
        '''
        basic previous button: if at the start, will not trigger
        '''
        if event == "Prev" and images:
            print('route', current_route)
            if location != 0 and location not in ends:
                print('location not at start')
                index = current_route.index(location)
                current_route.remove(location)
                print('index', index)
                location = current_route[index -1]
                print('location', location)
                load_image(images[location], window, x, y)
                window['Next'].Update(disabled = False)
        
        
        if location not in ends and location not in story_choices.keys() and trigger == True:
            window['Option 1'].Update(disabled = True)
            window['Option 2'].Update(disabled = True)
            window['Option 3'].Update(disabled = True)
            
            if event == "Next":
                if location in irregularities:
                    location = irregularities[location]
                else:
                    location += 1
                if location not in current_route:
                    current_route.append(location)
                load_image(images[location], window, x, y)
                print(location)
                window['Prev'].Update(disabled = False)
        
        
        if location in story_choices.keys() and trigger == True:
            route_choice =  story_choices[location]
            window['Next'].Update(disabled = True)
            
            enabling = len(route_choice)
            for num in range(enabling):
                button_ = 'Option ' + str(num + 1)
                window[button_].Update(disabled = False)

            if event == "Option 3":
                location = route_choice[2]
                if location not in current_route:
                    current_route.append(location)
                load_image(images[location], window, x, y)
                window['Option 1'].Update(disabled = True)
                window['Option 2'].Update(disabled = True)
                window['Option 3'].Update(disabled = True)
                window['Next'].Update(disabled = False)
                
            if event == "Option 2":
                location = route_choice[1]
                if location not in current_route:
                    current_route.append(location)
                load_image(images[location], window, x, y)
                window['Option 1'].Update(disabled = True)
                window['Option 2'].Update(disabled = True)
                window['Option 3'].Update(disabled = True)
                window['Next'].Update(disabled = False)
                
            if event == "Option 1":
                location = route_choice[0]
                if location not in current_route:
                    current_route.append(location)
                load_image(images[location], window, x ,y)
                window['Option 1'].Update(disabled = True)
                window['Option 2'].Update(disabled = True)
                window['Option 3'].Update(disabled = True)
                window['Next'].Update(disabled = False)
        
        
        if location == 0 and trigger == True:
            window['Prev'].Update(disabled = True)

        
        if location in ends and trigger == True:
            window['Prev'].Update(disabled = True)
            window['Next'].Update(disabled = True)
            window['Option 1'].Update(disabled = True)
            window['Option 2'].Update(disabled = True)
            window['Option 3'].Update(disabled = True)
            
            if location in good_ends:
                money += 100
                good_ends.remove(location)
                sg.Popup(str('''congrats on reaching a good end!
credits obtained: 100.
current credits: '''+ str(money)), keep_on_top=True)
            elif location in bad_ends:
                money -= 10
                sg.Popup('''Bad End
credits -10''', keep_on_top=True)


    window.close()



if __name__ == "__main__":
    main()