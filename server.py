import socket
from _thread import *
import random
import sys


def get_all_values(d):
    if isinstance(d, dict):
        for v in d.values():
            yield from get_all_values(v)
    elif isinstance(d, list):
        for v in d:
            yield from get_all_values(v)
    else:
        yield d


import pickle


##setup
def init_mainlist(no_wrds, no_teams):
    nouns = ['Hollywood', 'Screen', 'Play', 'Marble', 'Dinosaur', 'Cat', 'Pitch', 'Bond', 'Greece', 'Deck', 'Spike',
             'Center', 'Vacuum', 'Unicorn', 'Undertaker', 'Sock', 'Loch Ness', 'Horse', 'Berlin', 'Platypus', 'Port',
             'Chest', 'Box', 'Compound', 'Ship', 'Watch', 'Space', 'Flute', 'Tower', 'Death', 'Well', 'Fair', 'Tooth',
             'Staff', 'Bill', 'Shot', 'King', 'Pan', 'Square', 'Buffalo', 'Scientist', 'Chick', 'Atlantis', 'Spy',
             'Mail', 'Nut', 'Log', 'Pirate', 'Face', 'Stick', 'Disease', 'Yard', 'Mount', 'Slug', 'Dice', 'Lead',
             'Hook', 'Carrot', 'Poison', 'Stock', 'Foot', 'Torch', 'Arm', 'Figure', 'Mine', 'Suit', 'Crane', 'Beijing',
             'Mass', 'Microscope', 'Engine', 'China', 'Straw', 'Pants', 'Europe', 'Boot', 'Princess', 'Link', 'Luck',
             'Olive', 'Palm', 'Teacher', 'Thumb', 'Octopus', 'Hood', 'Tie', 'Doctor', 'Wake', 'Cricket', 'Millionaire',
             'New York', 'State', 'Bermuda', 'Park', 'Turkey', 'Chocolate', 'Trip', 'Racket', 'Bat', 'Jet',
             'Shakespeare', 'Bolt', 'Switch', 'Wall', 'Soul', 'Ghost', 'Time', 'Dance', 'Amazon', 'Grace', 'Moscow',
             'Pumpkin', 'Antactica', 'Whip', 'Heart', 'Table', 'Ball', 'Fighter', 'Cold', 'Day', 'Spring', 'Match',
             'Diamond', 'Centaur', 'March', 'Roulette', 'Dog', 'Cross', 'Wave', 'Duck', 'Wind', 'Spot', 'Skyscraper',
             'Paper', 'Apple', 'Oil', 'Cook', 'Fly', 'Cast', 'Bear', 'Pin', 'Thief', 'Trunk', 'America', 'Novel',
             'Cell', 'Bow', 'Model', 'Knife', 'Knight', 'Court', 'Iron', 'Whale', 'Shadow', 'Contract', 'Mercury',
             'Conductor', 'Seal', 'Car', 'Ring', 'Kid', 'Piano', 'Laser', 'Sound', 'Pole', 'Superhero', 'Revolution',
             'Pit', 'Gas', 'Glass', 'Washington', 'Bark', 'Snow', 'Ivory', 'Pipe', 'Cover', 'Degree', 'Tokyo', 'Church',
             'Pie', 'Tube', 'Block', 'Comic', 'Fish', 'Bridge', 'Moon', 'Part', 'Aztec', 'Smuggler', 'Train', 'Embassy',
             'Pupil', 'Scuba Diver', 'Ice', 'Tap', 'Code', 'Shoe', 'Server', 'Club', 'Row', 'Pyramid', 'Bug', 'Penguin',
             'Pound', 'Himalayas', 'Czech', 'Rome', 'Eye', 'Board', 'Bed', 'Point', 'France', 'Mammoth', 'Cotton',
             'Robin', 'Net', 'Bugle', 'Maple', 'England', 'Field', 'Robot', 'Plot', 'Africa', 'Tag', 'Mouth', 'Kiwi',
             'Mole', 'School', 'Sink', 'Pistol', 'Opera', 'Mint', 'Root', 'Sub', 'Crown', 'Back', 'Plane', 'Mexico',
             'Cloak', 'Circle', 'Tablet', 'Australia', 'Green', 'Egypt', 'Line', 'Lawyer', 'Witch', 'Parachute',
             'Crash', 'Gold', 'Note', 'Lion', 'Plastic', 'Web', 'Ambulance', 'Hospital', 'Spell', 'Lock', 'Water',
             'London', 'Casino', 'Cycle', 'Bar', 'Cliff', 'Round', 'Bomb', 'Giant', 'Hand', 'Ninja', 'Rose', 'Slip',
             'Limousine', 'Pass', 'Theater', 'Plate', 'Satellite', 'Ketchup', 'Hotel', 'Tail', 'Tick', 'Ground',
             'Police', 'Dwarf', 'Fan', 'Dress', 'Saturn', 'Grass', 'Brush', 'Chair', 'Rock', 'Pilot', 'Telescope',
             'File', 'Lab', 'India', 'Ruler', 'Nail', 'Swing', 'Olympus', 'Change', 'Date', 'Stream', 'Missile',
             'Scale', 'Band', 'Angel', 'Press', 'Berry', 'Card', 'Check', 'Draft', 'Head', 'Lap', 'Orange', 'Ice Cream',
             'Film', 'Washer', 'Pool', 'Shark', 'Van', 'String', 'Calf', 'Hawk', 'Eagle', 'Needle', 'Forest', 'Dragon',
             'Key', 'Belt', 'Cap', 'Drill', 'Glove', 'Paste', 'Fall', 'Fire', 'Spider', 'Spine', 'Soldier', 'Horn',
             'Queen', 'Ham', 'Litter', 'Life', 'Temple', 'Rabbit', 'Button', 'Game', 'Star', 'Jupiter', 'Vet', 'Night',
             'Air', 'Battery', 'Genius', 'Shop', 'Bottle', 'Stadium', 'Alien', 'Light', 'Triangle', 'Lemon', 'Nurse',
             'Drop', 'Track', 'Bank', 'Germany', 'Worm', 'Ray', 'Capital', 'Strike', 'War', 'Concert', 'Honey',
             'Canada', 'Buck', 'Snowman', 'Beat', 'Jam', 'Copper', 'Beach', 'Bell', 'Leprechaun', 'Phoenix', 'Force',
             'Boom', 'Fork', 'Alps', 'Post', 'Fence', 'Kangaroo', 'Mouse', 'Mug', 'Horseshoe', 'Scorpion', 'Agent',
             'Helicopter', 'Hole', 'Organ', 'Jack', 'Charge']

    pos_orignal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    pos = []
    pos_unedit = []
    for i in range(0, no_wrds):
        pos_unedit.append(pos_orignal[i])
        pos.append(pos_orignal[i])

    teams_word = []
    filler_word = []
    bomb_word = []
    main_dict = {}
    print(pos)
    if pos[-1] == 25:

        for i in range(0, 20):
            x = random.choice(nouns)
            teams_word.append(x)
            nouns.remove(x)
        for i in range(0, 4):
            x = random.choice(nouns)
            filler_word.append(x)
            nouns.remove(x)
        x = random.choice(nouns)
        bomb_word.append(x)
        nouns.remove(x)
        for i in teams_word:
            x = random.choice(pos)
            main_dict[x] = i
            pos.remove(x)
        for i in filler_word:
            x = random.choice(pos)
            main_dict[x] = i
            pos.remove(x)
        x = random.choice(pos)
        main_dict[x] = bomb_word[0]
        pos.remove(x)
    else:
        for i in range(0, 25):
            x = random.choice(nouns)
            teams_word.append(x)
            nouns.remove(x)
        for i in range(0, 10):
            x = random.choice(nouns)
            filler_word.append(x)
            nouns.remove(x)
        x = random.choice(nouns)
        bomb_word.append(x)
        nouns.remove(x)
        for i in teams_word:
            x = random.choice(pos)
            main_dict[x] = i
            pos.remove(x)
        for i in filler_word:
            x = random.choice(pos)
            main_dict[x] = i
            pos.remove(x)
        x = random.choice(pos)
        main_dict[x] = bomb_word[0]
        pos.remove(x)


    team_violet = {}
    team_aqua = {}
    team_blue = {}
    team_green = {}
    team_yellow = {}
    team_brown = {}

    count = 1
    filler_dict = {}
    bomb_dict = {}
    print(main_dict)

    for key, val in main_dict.items():
        if pos_unedit[-1] == 25:
            # 20 team word
            if no_teams == 2:
                if count < 11:
                    team_violet[key] = val
                if count > 10 and count < 21:
                    team_aqua[key] = val
                if count > 20 and count < 25:
                    filler_dict[key] = val

                if count == 25:
                    bomb_dict[key] = val
            if no_teams == 3:

                    if count < 7:
                        team_violet[key] = val
                    if count > 6 and count < 13:
                        team_aqua[key] = val
                    if count > 12 and count < 19:
                        team_blue[key] = val
                    if count > 18 and count < 25:
                        filler_dict[key] = val

                    if count == 25:
                        bomb_dict[key] = val
            if no_teams == 4:
                    if count < 6:
                        team_violet[key] = val
                    if count > 5 and count < 11:
                        team_aqua[key] = val
                    if count > 10 and count < 16:
                        team_blue[key] = val
                    if count > 15 and count < 21:
                        team_green[key] = val

                    if count > 20 and count < 25:
                        filler_dict[key] = val

                    if count == 25:
                        bomb_dict[key] = val
        else:
                if no_teams == 5:
                    if count < 7:
                        team_violet[key] = val
                    if count > 6 and count < 13:
                        team_aqua[key] = val
                    if count > 12 and count < 19:
                        team_blue[key] = val
                    if count > 18 and count < 25:
                        team_green[key] = val
                    if count > 24 and count < 31:
                        team_yellow[key] = val
                    if count > 30 and count < 36:
                        filler_dict[key] = val

                    if count == 36:
                        bomb_dict[key] = val
                if no_teams == 6:
                    if count < 6:
                        team_violet[key] = val
                    if count > 5 and count < 11:
                        team_aqua[key] = val
                    if count > 10 and count < 16:
                        team_blue[key] = val
                    if count > 15 and count < 21:
                        team_green[key] = val
                    if count > 20 and count < 26:
                        team_yellow[key] = val
                    if count > 25 and count < 31:
                        team_brown[key] = val
                    if count > 30 and count < 36:
                        filler_dict[key] = val
                    if count == 36:
                       bomb_dict[key] = val

        count += 1

    if no_teams == 2:
        v, a, b, g, y, br = 10,10,10,10,10,10
    if no_teams == 3:
        v, a, b, g, y, br = 6, 6, 6, 6, 6, 6
    if no_teams == 4:
        v, a, b, g, y, br = 5, 5, 5, 5, 5, 5
    if no_teams == 5:
        v, a, b, g, y, br = 6, 6, 6, 6, 6, 6
    if no_teams == 6:
        v, a, b, g, y, br =  5, 5, 5, 5, 5, 5

    SCORES_DICT = {'VIOLET': v, 'AQUA': a, 'BLUE': b, 'GREEN': g, 'YELLOW': y, 'BROWN': br}
    print(pos, pos_unedit)
    main_list = [team_violet, team_aqua, team_blue, team_green, team_yellow, filler_dict, bomb_dict, team_brown, no_teams,
                 no_wrds, pos_unedit, SCORES_DICT,
                 list(get_all_values(SCORES_DICT)), main_dict]
    print(main_list)
    return main_list

'''
for reference
trigger_list = [1,2,3,4,5,6,7,8]
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = ''
port = 5555
server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))


except socket.error as e:
    str(e)

s.listen()
print("Waiting For a connection, Server Started")

## team_ornge was 5
games = {}
keys = []


def threaded_client(conn, player):
    player_id = pickle.loads(conn.recv(2048))
    print(player_id)
    if player_id[0] == 'host':
        no_teams = player_id[1]
        if no_teams <= 4:
            no_wrds = 25
        if no_teams > 4 and no_teams < 7:
            no_wrds = 36

        main_list = init_mainlist(no_wrds, no_teams)
        print(main_list)
        x = player_id[-1]
        games[x] = main_list
        conn.send(pickle.dumps(main_list))
        SCORES_DICT = main_list[-3]
        keys.append(x)
        print("The KEY IS:",x)
    else:
        print(games)
        print(keys)
        id_pp = player_id[0]
        print(id_pp)
        lsdt = games[id_pp]
        conn.send(pickle.dumps(lsdt))

    reply = ''
    while True:
        try:
            if player > 4:
                data = pickle.loads(conn.recv(2048))
                if data == 'VIOLET':
                    SCORES_DICT[data] -= 1
                    print(SCORES_DICT)
                if data == 'AQUA':
                    SCORES_DICT[data] -= 1
                if data == 'BLUE':
                    SCORES_DICT[data] -= 1
                if data == 'GREEN':
                    SCORES_DICT[data] -= 1
                if data == 'YELLOW':
                    SCORES_DICT[data] -= 1


                if not data:
                    print("Disconnected")
                    break

                else:
                    if data == 'score' :
                        reply = list(get_all_values(SCORES_DICT))
                    if data == 'bomb':
                        reply = SCORES_DICT
                    else:
                        reply = SCORES_DICT[data]

                print("Recieved: ", data)
                print("Sending:", reply)
                conn.sendall(pickle.dumps(reply))
        except:
            break

            print("Lost Connection")
            conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
