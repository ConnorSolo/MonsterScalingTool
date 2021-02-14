import PySimpleGUI as sg


# create a stat class that contains the CR, Prof, AC, HP, Attack Bonus, Damage/Round, and Save DC
class Stats:
    def __init__(self, cr, pb, ac, hp, ab, dpr, dc):
        self.cr = cr
        self.pb = pb
        self.ac = ac
        self.hp = hp
        self.ab = ab
        self.dpr = dpr
        self.dc = dc


def scale_monster(cr1, cr2, pb, ac, hp, ab, dpr, dc):
    # get the starting stat values for the monster
    if "/" in cr1:
        cr_orig_list = cr1.split("/")
        cr_orig = float(cr_orig_list[0]) / float(cr_orig_list[1])
    else:
        cr_orig = float(cr1)

    if pb:
        pb_orig = float(pb)
    else:
        pb_orig = 0

    if ac:
        ac_orig = float(ac)
    else:
        ac_orig = 0

    if hp:
        hp_orig = float(hp)
    else:
        hp_orig = 0

    if ab:
        ab_orig = float(ab)
    else:
        ab_orig = 0

    if dpr:
        dpr_orig = float(dpr)
    else:
        dpr_orig = 0

    if dc:
        dc_orig = float(dc)
    else:
        dc_orig = 0

    # get the desired CR for the scaled version of the monster
    if "/" in cr2:
        cr_new_list = cr2.split("/")
        cr_new = float(cr_new_list[0]) / float(cr_new_list[1])
    else:
        cr_new = float(cr2)

    # using the levels list, find the average stat values for the target CR and create variables for them
    # add exception if any of the fields are left blank
    for level in levels:
        if level.cr == cr_new:
            pb_avg = level.pb
            ac_avg = level.ac
            hp_avg = level.hp
            ab_avg = level.ab
            dpr_avg = level.dpr
            dc_avg = level.dc
        # Divide the starting stats by the average for their original CR, then store that "percentage"
        if level.cr == cr_orig:
            pb_new = pb_orig / level.pb
            ac_new = ac_orig / level.ac
            hp_new = hp_orig / level.hp
            ab_new = ab_orig / level.ab
            dpr_new = dpr_orig / level.dpr
            dc_new = dc_orig / level.dc
    # Multiply the original stat:average ratio with the target CR average, to get a scaled value that is the same ratio
    pb_new *= pb_avg
    ac_new *= ac_avg
    hp_new *= hp_avg
    ab_new *= ab_avg
    dpr_new *= dpr_avg
    dc_new *= dc_avg
    # Update the "output" text element to be the value of "input" element
    window['-FINAL_PB-'].update(int(pb_new))
    window['-FINAL_AC-'].update(int(ac_new))
    window['-FINAL_HP-'].update(int(hp_new))
    window['-FINAL_AB-'].update(int(ab_new))
    window['-FINAL_DPR-'].update(int(dpr_new))
    window['-FINAL_DC-'].update(int(dc_new))
    return


lines = [
    (0,2,13,6,3,1,13),
    (0.125,2,13,35,3,3,13),
    (0.25,2,13,49,3,5,13),
    (0.5,2,13,70,3,8,13),
    (1,2,13,85,3,14,13),
    (2,2,13,100,3,20,13),
    (3,2,13,115,4,26,13),
    (4,2,14,130,5,32,14),
    (5,3,15,145,6,38,15),
    (6,3,15,160,6,44,15),
    (7,3,15,175,6,50,15),
    (8,3,16,190,7,56,16),
    (9,4,16,205,7,62,16),
    (10,4,17,220,7,68,16),
    (11,4,17,235,8,74,17),
    (12,4,17,250,8,80,17),
    (13,5,18,265,8,86,18),
    (14,5,18,280,8,92,18),
    (15,5,18,295,8,98,18),
    (16,5,18,310,9,104,18),
    (17,6,19,325,10,110,19),
    (18,6,19,340,10,116,19),
    (19,6,19,355,10,122,19),
    (20,6,19,400,10,140,19),
    (21,7,19,445,11,158,20),
    (22,7,19,490,11,176,20),
    (23,7,19,535,11,194,20),
    (24,7,19,580,12,212,21),
    (25,8,19,625,12,230,21),
    (26,8,19,670,12,248,21),
    (27,8,19,715,13,266,22),
    (28,8,19,760,13,284,22),
    (29,9,19,805,13,302,22),
    (30,9,19,850,14,320,23),
]
levels = []

for line in lines:
    levels.append(Stats(line[0], line[1], line[2], line[3], line[4], line[5], line[6]))

sg.theme('LightGrey1')

# ------ Column Definitions ------ #
column1 = [[sg.Text('Starting Stats', justification='right', size=(26, 1))],
           [sg.Text("Challenge Rating", size=(15, 1)), sg.Spin(values=[
               '0', '1/8', '1/4', '1/2', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
               '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
               key='-INITIAL_CR-', initial_value='0', size=(6, 1), enable_events=True)],
           [sg.Text("Proficiency Bonus", size=(15, 1)), sg.Input(size=(7, 1), key='-INITIAL_PB-', enable_events=True)],
           [sg.Text("Armor Class", size=(15, 1)), sg.Input(size=(7, 1), key='-INITIAL_AC-', enable_events=True)],
           [sg.Text("Hit Points", size=(15, 1)), sg.Input(size=(7, 1), key='-INITIAL_HP-', enable_events=True)],
           [sg.Text("Attack Bonus", size=(15, 1)), sg.Input(size=(7, 1), key='-INITIAL_AB-', enable_events=True)],
           [sg.Text("Damage/Round", size=(15, 1)), sg.Input(size=(7, 1), key='-INITIAL_DPR-', enable_events=True)],
           [sg.Text("Save DC", size=(15, 1)), sg.Input(size=(7, 1), key='-INITIAL_DC-', enable_events=True)]]

column2 = [[sg.Text('Scaled Stats', justification='left', size=(12, 1))],
           [sg.Spin(values=[
               '0', '1/8', '1/4', '1/2', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14',
               '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
               key='-FINAL_CR-', initial_value='0', size=(6, 1), enable_events=True)],
           [sg.Text(size=(6, 1), key='-FINAL_PB-', relief=sg.RELIEF_SUNKEN)],
           [sg.Text(size=(6, 1), key='-FINAL_AC-', relief=sg.RELIEF_SUNKEN)],
           [sg.Text(size=(6, 1), key='-FINAL_HP-', relief=sg.RELIEF_SUNKEN)],
           [sg.Text(size=(6, 1), key='-FINAL_AB-', relief=sg.RELIEF_SUNKEN)],
           [sg.Text(size=(6, 1), key='-FINAL_DPR-', relief=sg.RELIEF_SUNKEN)],
           [sg.Text(size=(6, 1), key='-FINAL_DC-', relief=sg.RELIEF_SUNKEN)]]

layout = [[sg.Column(column1), sg.Column(column2)],
          [sg.Button('Scale', size=(20, 2), font='Any 15')]]

window = sg.Window('D&D 5E Monster Scaling Tool', layout, element_justification='c')

while True:  # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    # Restrict the characters allowed in an input element to digits and . or -
    # Accomplished by removing last character input if not a valid character
    if event == '-INITIAL_PB-' and values['-INITIAL_PB-'] and values['-INITIAL_PB-'][-1] not in '0123456789.':
        window['-INITIAL_PB-'].update(values['-INITIAL_PB-'][:-1])
    if event == '-INITIAL_AC-' and values['-INITIAL_AC-'] and values['-INITIAL_AC-'][-1] not in '0123456789.':
        window['-INITIAL_AC-'].update(values['-INITIAL_AC-'][:-1])
    if event == '-INITIAL_HP-' and values['-INITIAL_HP-'] and values['-INITIAL_HP-'][-1] not in '0123456789.':
        window['-INITIAL_HP-'].update(values['-INITIAL_HP-'][:-1])
    if event == '-INITIAL_AB-' and values['-INITIAL_AB-'] and values['-INITIAL_AB-'][-1] not in '0123456789.':
        window['-INITIAL_AB-'].update(values['-INITIAL_AB-'][:-1])
    if event == '-INITIAL_DPR-' and values['-INITIAL_DPR-'] and values['-INITIAL_DPR-'][-1] not in '0123456789.':
        window['-INITIAL_DPR-'].update(values['-INITIAL_DPR-'][:-1])
    if event == '-INITIAL_DC-' and values['-INITIAL_DC-'] and values['-INITIAL_DC-'][-1] not in '0123456789.':
        window['-INITIAL_DC-'].update(values['-INITIAL_DC-'][:-1])

    # if the Scale button is pressed, compute the values
    if event == 'Scale' and values:
        scale_monster(values['-INITIAL_CR-'], values['-FINAL_CR-'], values['-INITIAL_PB-'], values['-INITIAL_AC-'],
                      values['-INITIAL_HP-'], values['-INITIAL_AB-'], values['-INITIAL_DPR-'], values['-INITIAL_DC-'])

window.close()
