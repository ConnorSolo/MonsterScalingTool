from bisect import bisect_left

# Create a stat class that contains the CR, Prof, AC, HP, Attack Bonus,
# Damage/Round, and Save DC
class Stats:
    def __init__(self, cr, pb, ac, hp, ab, dpr, dc, con):
        self.cr = cr
        self.pb = pb
        self.ac = ac
        self.hp = hp
        self.ab = ab
        self.dpr = dpr
        self.dc = dc
        self.con = con


def get_mod(score):
    return (score - 10) // 2;


def get_score(mod):
    if mod == -5:
        return 1
    return mod*2 + 10


def get_closest(myList, myNumber):
    # Assumes myList is sorted. Returns the index of closest value to myNumber.
    # If two numbers are equally close, return index of the smallest number.
    pos = bisect_left(myList, myNumber)
    if pos == 0 or pos == len(myList):
        return pos
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
       return pos
    else:
       return pos - 1


def scale_stats(cr1, cr2, pb, ac, hp, ab, dpr, dc, STR, DEX, CON, INT, WIS, CHA, size):

    # Table from DMG using max number in each range
    # Added an 8th field to each entry for the average CON of each CR
    lines = [
            (0,2,13,6,3,1,13,10),
            (0.125,2,13,35,3,3,13,11),
            (0.25,2,13,49,3,5,13,12),
            (0.5,2,13,70,3,8,13,12),
            (1,2,13,85,3,14,13,13),
            (2,2,13,100,3,20,13,14),
            (3,2,13,115,4,26,13,15),
            (4,2,14,130,5,32,14,15),
            (5,3,15,145,6,38,15,16),
            (6,3,15,160,6,44,15,16),
            (7,3,15,175,6,50,15,17),
            (8,3,16,190,7,56,16,17),
            (9,4,16,205,7,62,16,17),
            (10,4,17,220,7,68,16,18),
            (11,4,17,235,8,74,17,18),
            (12,4,17,250,8,80,17,18),
            (13,5,18,265,8,86,18,19),
            (14,5,18,280,8,92,18,19),
            (15,5,18,295,8,98,18,20),
            (16,5,18,310,9,104,18,20),
            (17,6,19,325,10,110,19,21),
            (18,6,19,340,10,116,19,21),
            (19,6,19,355,10,122,19,22),
            (20,6,19,400,10,140,19,23),
            (21,7,19,445,11,158,20,24),
            (22,7,19,490,11,176,20,25),
            (23,7,19,535,11,194,20,25),
            (24,7,19,580,12,212,21,25),
            (25,8,19,625,12,230,21,26),
            (26,8,19,670,12,248,21,26),
            (27,8,19,715,13,266,22,27),
            (28,8,19,760,13,284,22,28),
            (29,9,19,805,13,302,22,29),
            (30,9,19,850,14,320,23,30),
            ]
    # Create some empty lists to use later on
    levels = []
    stats_new = []
    abil_scores_old = []
    abil_scores_new = []
    mods_new = []

    # Add all of the info from the table above into a list of Stats objects
    for line in lines:
        levels.append(Stats(line[0], line[1], line[2], line[3],
                            line[4], line[5], line[6], line[7]))

    # Get the starting stat values and the target CR
    cr_old = float(cr1)
    cr_new = float(cr2)
    pb_old = float(pb) if pb else 0
    ac_old = float(ac) if ac else 0
    hp_old = float(hp) if hp else 0
    ab_old = float(ab) if ab else 0
    dpr_old = float(dpr) if dpr else 0
    dc_old = float(dc) if dc else 0
    # Get the starting ability scores
    str_old = float(STR) if STR else 0
    dex_old = float(DEX) if DEX else 0
    con_old = float(CON) if CON else 0
    int_old = float(INT) if INT else 0
    wis_old = float(WIS) if WIS else 0
    cha_old = float(CHA) if CHA else 0
    # Create integer copies of the scores to eventually output
    str_new = int(str_old)
    dex_new = int(dex_old)
    int_new = int(int_old)
    wis_new = int(wis_old)
    cha_new = int(cha_old)
    # Make lists of both old and new scores, plus an index variable that we will
    # use later
    abil_scores_old = [str_old, dex_old, int_old, wis_old, cha_old]
    abil_scores_new = [str_new, dex_new, int_new, wis_new, cha_new]
    index = 0

    # Using the levels list, find the average stat values for the target CR and
    # save them as variables
    for level in levels:
        if level.cr == cr_new:
            pb_avg = level.pb
            ac_avg = level.ac
            hp_avg = level.hp
            ab_avg = level.ab
            dpr_avg = level.dpr
            dc_avg = level.dc
            con_avg = level.con
        # Divide the starting stats by the average for their original CR, then
        # save that ratio in decimal form as a variable
        if level.cr == cr_old:
            pb_new = pb_old / level.pb
            ac_new = ac_old / level.ac
            hp_new = hp_old / level.hp
            ab_new = ab_old / level.ab
            dpr_new = dpr_old / level.dpr
            dc_new = dc_old / level.dc
            con_new = con_old / level.con
    # Multiply the original stat:average ratio with the target CR average, to
    # get a proportionately scaled value
    pb_new *= pb_avg
    ac_new *= ac_avg
    hp_new *= hp_avg
    ab_new *= ab_avg
    dpr_new *= dpr_avg
    dc_new *= dc_avg
    con_new *= con_avg
    # Round each stat to the nearest integer and save
    pb_new = int(round(pb_new))
    ac_new = int(round(ac_new))
    hp_new = int(round(hp_new))
    ab_new = int(round(ab_new))
    dpr_new = int(round(dpr_new))
    dc_new = int(round(dc_new))
    con_new = int(round(con_new))

    # Iterate through scores to find which one is used for the monster's attacks
    # then scale that score to fit with the scaled stats and update the new list
    for score in abil_scores_old:
        if get_mod(score) + pb == ab:
            if (ab_new - pb_new) != get_mod(score):
                abil_scores_new[index] = get_score(ab_new - pb_new)
        index += 1

    # Iterate through the new scores and add the correct modifier to a list
    for score in abil_scores_new:
        mod = get_mod(score)
        if mod >= 0:
            mods_new.append('+' + str(mod))
        else:
            mods_new.append(str(mod))

    # Add the rounded values of the new stats, ability scores, and modifiers
    # to the stats_new list
    stats_new.extend([pb_new, ac_new, hp_new, ab_new, dpr_new, dc_new])
    stats_new.extend(abil_scores_new)
    stats_new.insert(8, con_new)
    stats_new.extend(mods_new)
    if get_mod(con_new) >= 0:
        stats_new.insert(14, "+" + str(get_mod(con_new)))
    else:
        stats_new.insert(14, "-" + str(abs(get_mod(con_new))))

    # Iterate through possible HP die expressions until we find one that is
    # as close as possible to new value, given their size and CON scores.
    count = 1
    exit = False
    while exit is False:
        next_up = count + 1

        mod_sum = count*get_mod(con_new)

        mod_sum_next = next_up*get_mod(con_new)

        form_sum = round((count*size) + mod_sum)
        form_sum_next = round((next_up*size) + mod_sum_next)
        if abs(hp_new - form_sum) <= abs(hp_new - form_sum_next):
            hit_die = str(count) + "d" + str(int((size*2)-1))
            if get_mod(con_new) > 0:
                hit_die = hit_die + " + "
            elif get_mod(con_new) < 0:
                hit_die = hit_die + " - "
                mod_sum = abs(mod_sum)
            else:
                mod_sum = ""
            formula = [hit_die, mod_sum]
            exit = True
        else:
           count += 1

    try:
        stats_new.append(form_sum)
        stats_new.extend(formula)
    except:
        stats_new.append("")

    return stats_new
