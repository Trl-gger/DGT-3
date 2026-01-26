from browser import document

document["status"].text = "Status: je to tam"

count = 0

def greet(ev):
    global count
    meno = document["inp_name"].value
    if meno == "":
        document["out"].text = "Zadaj meno"
    else:
        document["out"].text = "Ahoj " + meno
        document["pocet"].text = str(count)
        count += 1

document["btn_greet"].bind("click", greet)


def on_key(ev):
    if ev.key == "Enter":
        greet(ev)

document["inp_name"].bind("keydown", on_key)
