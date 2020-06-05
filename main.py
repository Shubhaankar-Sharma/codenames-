from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
import sys
from network import Network
from kivy.properties import ObjectProperty
## i am making a change
just_checking = 1000
DB = []
clicked = []
win_times = []
SCORE = []
TEAMS_dict = {}
NO_TEAMS = 0
teamnames = []
## function to spit out a string for the score board
def score_label(
        TEAMS_dict,lst_teamnames
             ):
    
        #to return a string of score 
        txt = ''
        for i in lst_teamnames:
            
            txt = txt + i + ':'+ str(TEAMS_dict[i]) + " "
            
        return txt
        



## opening window 

class Main_Window(Screen):
        def Run(Screen):
            layout = GridLayout(rows=3)
            label = Label(text="codenames")
            layout.add_widget(label)
            button1 = Button(text="host a game ", on_press=hostback)
            layout.add_widget(button1)
            button2 = Button(text="join as spymaster", on_press=onclick2)
            layout.add_widget(button2)
            Screen.add_widget(layout)

## this shows the color of the words in the spymaster window
def instance(button, lst):
    VIOLET = (238 / 225.0, 130 / 225.0, 238 / 225.0, 1)
    AQUA = (0 / 255.0, 255 / 150.0, 255 / 150.0, 0.75)
    BLUE = (0, 0, 255, 1)
    GREEN = (34 / 255.0, 139 / 70.0, 34 / 255.0, 1)
    YELLOW = (255, 165, 0, 0.5)
    BROWN = (255 / 255.0, 165 / 255.0, 0, 1)
    GREY = (47 / 150.0, 79 / 150.0, 79 / 150.0, 1)
    str_btn = button.text
    for i in lst[4::]:
        contains = str_btn in i.values()
        if contains == True:
            if i['color'] == 'VIOLET':
                button.background_color = VIOLET

            if i['color'] == 'AQUA':
                button.background_color = AQUA

            if i['color'] == 'BLUE':
                button.background_color = BLUE

            if i['color'] == 'GREEN':
                button.background_color = GREEN

            if i['color'] == 'YELLOW':
                button.background_color = YELLOW

            if i['color'] == 'GREY':
                button.background_color = GREY
            if i['color'] == 'BROWN':
                button.background_color = BROWN
            if i['color'] == 'bomb':
                button.background_color = (0, 0, 0, 0)

# this functions initializes connection to the server
def init_net():
    n = Network()
    return n

# this function fetches the main list from the server by providing required credentials stored in the DB
def network(n, game_id):
    main_list = n.send(game_id)
    
    SCORE = main_list[-2]
    main_dict = main_list[-1]
    pos = main_list[-4]
    SCORE_DICT = main_list[-3]
    
    team_violet = main_list[0]
    team_aqua = main_list[1]
    team_blue = main_list[2]
    team_green = main_list[3]
    team_yellow = main_list[4]
    team_brown = main_list[7]
    no_teams = main_list[8]
    no_words = main_list[9]
    filler = main_list[5]
    bomb = main_list[6]
    words_ordered = []
    team_violet['color'] = 'VIOLET'
    team_aqua['color'] = 'AQUA'
    team_blue['color'] = 'BLUE'
    team_green['color'] = 'GREEN'
    team_yellow['color'] = 'YELLOW'
    team_brown['color'] = 'BROWN'

    filler['color'] = 'GREY'
    bomb['color'] = 'bomb'
    for i in pos:
        words_ordered.append(main_dict[i])
    # this is the main list required to start the game 
    lst = [
        words_ordered, no_teams,SCORE_DICT,SCORE, team_violet, team_aqua, team_blue, team_green, team_yellow, team_brown, filler,
           bomb
           ]
    return lst

# this is the screen which is shown when the user joins through the spymaster option
class Joinagame(Screen):

    def Run(Screen):
        
        DB.clear()
        
        layout = GridLayout(rows=4)
        
        label = Label(text="enter the game id")
        
        layout.add_widget(label)
        
        gameid = TextInput(text='',multiline = False)
                
        Screen.gameid = gameid
        
        # when button press DB.append(gameid.text)
        
        layout.add_widget(gameid)
        
        button = Button(text="join", on_press=joinclick)
        
        layout.add_widget(button)
        
        back_button = Button(text="back", on_press=back_joinagame)
        
        layout.add_widget(back_button)
        
        Screen.add_widget(layout)


    def exit(self):
        # when exiting we will store the information entered by the user in a list
        DB.append(self.gameid.text.strip())

# this is the screen for spymaster
class SecondWindow(Screen):

    def Run(Screen):
        
        n = init_net()
        
        lst = network(n, [str(DB[-1])])

        
        if lst[1] > 1 and lst[1] < 5:
        
            layout = GridLayout(cols=5)
        
        else:
        
            layout = GridLayout(cols=6)
        
        for i in lst[0]:
        
            button = Button(text=i, size_hint=(0.2, 0.1), pos_hint={'center_x': 0.1, 'center_y': 0.5},
                            background_color=(255, 0, 255))
        
            instance(button, lst)

        
            layout.add_widget(button)
        
        button2 = Button(text="Back", size_hint=(0.2, 0.1), pos_hint={'center_x': 0.1, 'center_y': 0.5},
                         on_press=onclick)
        
        layout.add_widget(button2)
        # db = Label(text = str(DB[0]))
        # layout.add_widget(db)
        
        Screen.add_widget(layout)


class Hostagame(Screen):

    def Run(Screen):
        """
        DB = []
        clicked = []
        win_times = []
        SCORE = []
        TEAMS_dict = {}
        NO_TEAMS = 0
        """

        DB.clear()

        win_times.clear()

        clicked.clear()

        TEAMS_dict.clear()

        teamnames.clear()

        NO_TEAMS = 0

        layout = GridLayout(rows=6)

        label = Button(text="enter no of teams in no.s(2-6 teams)")

        layout.add_widget(label)

        gameid = TextInput(text='', multiline=False)

        Screen.gameid = gameid

        # when button press DB.append(gameid.text)

        layout.add_widget(gameid)

        label2 = Button(

            text="Enter a unique game id to share with spymasters")

        layout.add_widget(label2)

        uniqueid = TextInput(text='', multiline=False)

        Screen.uniqueid = uniqueid

        layout.add_widget(uniqueid)

        button = Button(text="host", on_press=hostclick)

        layout.add_widget(button)

        back_button = Button(text="back", on_press=back_joinagame)

        layout.add_widget(back_button)

        Screen.add_widget(layout)

    def exit(self):

        if len(self.gameid.text) > 0 and len(self.uniqueid.text) > 0:

            DB.append(['host', int(self.gameid.text), self.uniqueid.text.strip()])


class Host(Screen):

    def instancehost(Screen, button):

        n = Screen.n

        lst = Screen.lst


        VIOLET = (238 / 225.0, 130 / 225.0, 238 / 225.0, 1)

        AQUA = (0 / 255.0, 255 / 150.0, 255 / 150.0, 0.75)

        BLUE = (0, 0, 255, 1)

        GREEN = (34 / 255.0, 139 / 70.0, 34 / 255.0, 1)

        YELLOW = (255, 165, 0, 0.5)

        BROWN = (255 / 255.0, 165 / 255.0, 0, 1)

        GREY = (47 / 150.0, 79 / 150.0, 79 / 150.0, 1)

        str_btn = button.text

        if len(win_times) < 1:

            if str_btn not in clicked:


                clicked.append(str_btn)


                for i in lst[4::]:

                    contains = str_btn in i.values()

                    if contains == True:

                        if i['color'] == 'GREY' or i['color'] == 'bomb':

                            abc = 100

                        else:

                            TEAMS_dict[i['color']] = TEAMS_dict[i['color']] - 1



                        Screen.score.text = score_label(TEAMS_dict,teamnames)

                        if i['color'] == 'VIOLET':

                            button.background_color = VIOLET

                            win_check = n.send("VIOLET")

                            if win_check == 0:

                                win_times.append(1)

                                popup = Popup(title='popup',

                                              content=Label(text='TEAM VIOLET WINS'),

                                              size_hint=(None, None), size=(400, 400))

                                popup.open()

                        if i['color'] == 'AQUA':

                            button.background_color = AQUA

                            win_check = n.send("AQUA")



                            if win_check == 0:

                                win_times.append(1)

                                popup = Popup(title='popup',

                                              content=Label(text='TEAM AQUA WINS'),

                                              size_hint=(None, None), size=(400, 400))

                                popup.open()



                        if i['color'] == 'BLUE':

                            button.background_color = BLUE

                            win_check = n.send("BLUE")

                            if win_check == 0:

                                win_times.append(1)

                                popup = Popup(title='popup',

                                              content=Label(text='TEAM BLUE WINS'),

                                              size_hint=(None, None), size=(400, 400))

                                popup.open()



                        if i['color'] == 'GREEN':

                            button.background_color = GREEN

                            win_check = n.send("GREEN")

                            if win_check == 0:

                                win_times.append(1)

                                popup = Popup(title='popup',

                                              content=Label(text='TEAM GREEN WINS'),

                                              size_hint=(None, None), size=(400, 400))

                                popup.open()

                        if i['color'] == 'YELLOW':

                            button.background_color = YELLOW

                            win_check = n.send("YELLOW")

                            if win_check == 0:

                                win_times.append(1)

                                popup = Popup(title='popup',

                                              content=Label(text='TEAM YELLOW WINS'),

                                              size_hint=(None, None), size=(400, 400))

                                popup.open()



                        if i['color'] == 'BROWN':

                            button.background_color = BROWN

                            win_check = n.send("BROWN")

                            if win_check == 0:

                                win_times.append(1)

                                popup = Popup(title='popup',

                                              content=Label(text='TEAM GOLD WINS'),

                                              size_hint=(None, None), size=(400, 400))

                                popup.open()

                        if i['color'] == 'GREY':

                            button.background_color = GREY



                        if i['color'] == 'bomb':

                            win_times.append(1)

                            button.background_color = (0, 0, 0, 0)

                            win_check = n.send('bomb')

                            d = win_check

                            minval = min(d.values())

                            res = [k for k, v in d.items() if v == minval]



                            i = len(res) - 1


                            txt = ''

                            while i > -1:


                                txt = txt + 'TEAM' + ' ' + res[i] + ' ' + 'WON'

                                i -= 1

                            new_popup = Popup(title='BOMB!!!',

                                              content=Label(text=txt),

                                              size_hint=(None, None), size=(400, 400))


                            new_popup.open()

    def Run(Screen):

        n = init_net()

        Screen.n = n

        lst = network(n, DB[-1])

        Screen.lst = lst


        # store score create a function to get score as a string then define label
        """
        ref :lst = [words_ordered, no_teams,SCORE_DICT, team_violet, team_aqua, team_blue, team_green, team_yellow, team_brown, filler,
           bomb]
        """
        """
        ref:
                    DB = []
                    clicked = []
                    win_times = []
                    SCORE = []
                    TEAMS = []
                    NO_TEAMS = 0               
        """
        NO_TEAMS = lst[1]

        SCORE = lst[3]


        SCORE_DICT = lst[2]
        
        #this gives a relevant dictionary of teams

        for k, v in SCORE_DICT.items():

            if NO_TEAMS == 0:

                break

            TEAMS_dict[k] = v
            

            NO_TEAMS -=1


        for i in TEAMS_dict.keys():

            teamnames.append(i)

        # this gives a list of names of teams



        if lst[1] > 1 and lst[1] < 5:


            layout = GridLayout(cols=5)

        else:

            layout = GridLayout(cols=6)


        for i in lst[0]:


            button = Button(

                text=i, size_hint=(0.2, 0.1), pos_hint={'center_x': 0.1, 'center_y': 0.5},

                            background_color=(255, 0, 255), on_press=Screen.instancehost
            )


            layout.add_widget(button)

        button2 = Button(
            text="Back", size_hint=(0.2, 0.1), pos_hint={'center_x': 0.1, 'center_y': 0.5},
                         on_press=hostback
        )

        layout.add_widget(button2)
        
        score = Button(

            text = score_label(TEAMS_dict,teamnames),size_hint=(0.5, 0.1), pos_hint={'center_x': 0.1, 'center_y': 0.5}

        )

        Screen.score = score



        layout.add_widget(score)

        # db = Label(text = str(DB[0]))

        # layout.add_widget(db)

        Screen.add_widget(layout)


kv = Builder.load_file("my.kv")

Window_Manager = ScreenManager()


def onclick(self):
    Window_Manager.switch_to(Joinagame(name="joinagame"))


def onclick2(self):
    Window_Manager.switch_to(Joinagame(name="joinagame"))

def joinclick(self):
    Window_Manager.switch_to(SecondWindow(name="second"))


def back_joinagame(self):
    Window_Manager.switch_to(Main_Window(name="first"))


def hostclick(self):
    Window_Manager.switch_to(Host(name='host'))


def hostback(self):
    Window_Manager.switch_to(Hostagame(name='host'))


Window_Manager.add_widget(Main_Window(name="first"))


Window_Manager.add_widget(SecondWindow(name="second"))


Window_Manager.add_widget(Joinagame(name="joinagame"))


Window_Manager.add_widget(Hostagame(name="hostagame"))

Window_Manager.add_widget(Host(name='host'))


class mainApp(App):

    def build(self):

        return Window_Manager



mainApp().run()
