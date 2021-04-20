from flask import Flask, redirect, request, session, render_template, url_for

from scale_monster import scale_stats

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "I'm not dumb enough to put the actual key here, c'mon son."


@app.route("/", methods=["GET", "POST"])
def main_page():
    # Initialize all necessary variables
    if "inputs" not in session:
        session["inputs"] = []
    if "outputs" not in session:
        session["outputs"] = []
    if "cr1" not in session:
        session["cr1"] = 0
    if "cr2" not in session:
        session["cr2"] = 0
    if "pb" not in session:
        session["pb"] = 0
    if "ac" not in session:
        session["ac"] = 0
    if "hp" not in session:
        session["hp"] = 0
    if "ab" not in session:
        session["ab"] = 0
    if "dpr" not in session:
        session["dpr"] = 0
    if "dc" not in session:
        session["dc"] = 0
    if "STR" not in session:
        session["STR"] = 0
    if "DEX" not in session:
        session["DEX"] = 0
    if "CON" not in session:
        session["CON"] = 0
    if "INT" not in session:
        session["INT"] = 0
    if "WIS" not in session:
        session["WIS"] = 0
    if "CHA" not in session:
        session["CHA"] = 0
    if "size" not in session:
        session["size"] = 0

    # If the request is a GET, load the page and make all variables available
    # for the HTML to see and fill in automatically
    if request.method == "GET":
        return render_template("main_page.html", outputs=session["outputs"],
                               cr1=session["cr1"], cr2=session["cr2"],
                               pb=session["pb"], ac=session["ac"],
                               hp=session["hp"], ab=session["ab"],
                               dpr=session["dpr"], dc=session["dc"],
                               STR=session["STR"], DEX=session["DEX"],
                               CON=session["CON"], INT=session["INT"],
                               WIS=session["WIS"], CHA=session["CHA"],
                               size=session["size"])

    # Add starting CR to inputs list and save as variable
    session["inputs"].append(float(request.form["cr1"]))
    session.modified = True
    session["cr1"] = request.form["cr1"]
    session.modified = True

    # Add target CR to inputs list and save as variable
    session["inputs"].append(float(request.form["cr2"]))
    session.modified = True
    session["cr2"] = request.form["cr2"]
    session.modified = True

    # Add proficiency bonus to inputs list and save as variable
    if request.form.get("pb") != "":
        if float(request.form.get("pb")) > 0:
            session["inputs"].append(float(request.form["pb"]))
            session.modified = True
            session["pb"] = request.form["pb"]
            session.modified = True
        else:
            session["inputs"].append(0)
            session.modified = True
            session["pb"] = ""
            session.modified = True
    # If pb is left empty, fill generate the correct value for the given CR
    else:
        if int(request.form.get("cr1")) < 5:
            session["inputs"].append(2)
            session.modified = True
            session["pb"] = "2"
            session.modified = True
        elif int(request.form.get("cr1")) < 9:
            session["inputs"].append(3)
            session.modified = True
            session["pb"] = "3"
            session.modified = True
        elif int(request.form.get("cr1")) < 13:
            session["inputs"].append(4)
            session.modified = True
            session["pb"] = "4"
            session.modified = True
        elif int(request.form.get("cr1")) < 17:
            session["inputs"].append(5)
            session.modified = True
            session["pb"] = "5"
            session.modified = True
        elif int(request.form.get("cr1")) < 21:
            session["inputs"].append(6)
            session.modified = True
            session["pb"] = "6"
            session.modified = True
        elif int(request.form.get("cr1")) < 25:
            session["inputs"].append(7)
            session.modified = True
            session["pb"] = "7"
            session.modified = True
        elif int(request.form.get("cr1")) < 29:
            session["inputs"].append(8)
            session.modified = True
            session["pb"] = "8"
            session.modified = True
        elif int(request.form.get("cr1")) < 31:
            session["inputs"].append(9)
            session.modified = True
            session["pb"] = "9"
            session.modified = True
        else:
            session["inputs"].append(0)
            session.modified = True
            session["pb"] = ""
            session.modified = True

    # Add armor class to inputs list and save as variable
    if request.form.get("ac") != "":
        if float(request.form.get("ac")) > 0:
            session["inputs"].append(float(request.form["ac"]))
            session.modified = True
            session["ac"] = request.form["ac"]
            session.modified = True
        else:
            session["inputs"].append(0)
            session.modified = True
            session["ac"] = ""
            session.modified = True
    else:
        session["inputs"].append(0)
        session.modified = True
        session["ac"] = ""
        session.modified = True

    # Add hit points to inputs list and save as variable
    if request.form.get("hp") != "":
        if float(request.form.get("hp")) > 0:
            session["inputs"].append(float(request.form["hp"]))
            session.modified = True
            session["hp"] = request.form["hp"]
            session.modified = True
        else:
            session["inputs"].append(0)
            session.modified = True
            session["hp"] = ""
            session.modified = True
    else:
        session["inputs"].append(0)
        session.modified = True
        session["hp"] = ""
        session.modified = True

    # Add attack bonus to inputs list and save as variable
    if request.form.get("ab") != "":
        if float(request.form.get("ab")) > 0:
            session["inputs"].append(float(request.form["ab"]))
            session.modified = True
            session["ab"] = request.form["ab"]
            session.modified = True
        else:
            session["inputs"].append(0)
            session.modified = True
            session["ab"] = ""
            session.modified = True
    else:
        session["inputs"].append(0)
        session.modified = True
        session["ab"] = ""
        session.modified = True

    # Add damage per round to inputs list and save as variable
    if request.form.get("dpr") != "":
        if float(request.form.get("dpr")) > 0:
            session["inputs"].append(float(request.form["dpr"]))
            session.modified = True
            session["dpr"] = request.form["dpr"]
            session.modified = True
        else:
            session["inputs"].append(0)
            session.modified = True
            session["dpr"] = ""
            session.modified = True
    else:
        session["inputs"].append(0)
        session.modified = True
        session["dpr"] = ""
        session.modified = True

    # Add difficulty class to inputs list and save as variable
    if request.form.get("dc") != "":
        if float(request.form.get("dc")) > 0:
            session["inputs"].append(float(request.form["dc"]))
            session.modified = True
            session["dc"] = request.form["dc"]
            session.modified = True
        else:
            session["inputs"].append(0)
            session.modified = True
            session["dc"] = ""
            session.modified = True
    else:
        session["inputs"].append(0)
        session.modified = True
        session["dc"] = ""
        session.modified = True

    # Add strength to inputs list and save as variable
    if request.form.get("STR") != "" and float(request.form.get("STR")) > 0:
        session["inputs"].append(float(request.form["STR"]))
        session.modified = True
        session["STR"] = request.form["STR"]
        session.modified = True
    else:
        session["inputs"].append(0)
        session.modified = True
        session["STR"] = ""
        session.modified = True

    # Add dexterity to inputs list and save as variable
    if request.form.get("DEX") != "" and float(request.form.get("DEX")) > 0:
        session["inputs"].append(float(request.form["DEX"]))
        session.modified = True
        session["DEX"] = request.form["DEX"]
        session.modified = True
    else:
        session["inputs"].append(0)
        session.modified = True
        session["DEX"] = ""
        session.modified = True

    # Add constitution to inputs list and save as variable
    if request.form.get("CON") != "" and float(request.form.get("CON")) > 0:
        session["inputs"].append(float(request.form["CON"]))
        session.modified = True
        session["CON"] = request.form["CON"]
        session.modified = True
    else:
        session["inputs"].append(0)
        session.modified = True
        session["CON"] = ""
        session.modified = True

    # Add intelligence to inputs list and save as variable
    if request.form.get("INT") != "" and float(request.form.get("INT")) > 0:
        session["inputs"].append(float(request.form["INT"]))
        session.modified = True
        session["INT"] = request.form["INT"]
        session.modified = True
    else:
        session["inputs"].append(0)
        session.modified = True
        session["INT"] = ""
        session.modified = True

    # Add wisdom to inputs list and save as variable
    if request.form.get("WIS") != "" and float(request.form.get("WIS")) > 0:
        session["inputs"].append(float(request.form["WIS"]))
        session.modified = True
        session["WIS"] = request.form["WIS"]
        session.modified = True
    else:
        session["inputs"].append(0)
        session.modified = True
        session["WIS"] = ""
        session.modified = True

    # Add charisma to inputs list and save as variable
    if request.form.get("CHA") != "" and float(request.form.get("CHA")) > 0:
        session["inputs"].append(float(request.form["CHA"]))
        session.modified = True
        session["CHA"] = request.form["CHA"]
        session.modified = True
    else:
        session["inputs"].append(0)
        session.modified = True
        session["CHA"] = ""
        session.modified = True

    # Add monster size to inputs list and save as variable
    # THIS HASN'T BEEN ADDED TO THE PYTHON FUNCTION YET
    session["inputs"].append(float(request.form["size"]))
    session.modified = True
    session["size"] = request.form["size"]
    session.modified = True


    # Run the scale_stats function on the inputs to generate the new values
    session["outputs"] = scale_stats(session["inputs"][0], session["inputs"][1],
                                     session["inputs"][2], session["inputs"][3],
                                     session["inputs"][4], session["inputs"][5],
                                     session["inputs"][6], session["inputs"][7],
                                     session["inputs"][8], session["inputs"][9],
                                     session["inputs"][10], session["inputs"][11],
                                     session["inputs"][12], session["inputs"][13],
                                     session["inputs"][14])
    session.modified = True
    session["inputs"].clear()
    session.modified = True
    # Make the page default back to using a GET request as seen above
    return redirect (url_for('main_page'))
