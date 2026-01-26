from browser import document
from browser.local_storage import storage
import json
 
 
btn_theme = document["btn_theme"]
theme_label = document["theme_label"]
 
 
inp = document["inp_item"]
btn_add = document["btn_add"]
btn_clear = document["btn_clear"]
btn_last = document["btn_last"]
out = document["out"]
 
 
items = []
theme = "light"
 
 
 
def render():
    if len(items) == 0:
        out.html = "<em>Zoznam je prázdny.</em>"
        return
 
    html = "<ul>"
    for it in items:
        html += f"<li>{it}</li>"
    html += "</ul>"
    out.html = html
 
 
def save_items():
    storage["todo_items"] = json.dumps(items)
 
 
def load_items():
    data = storage.get("todo_items")
    if data:
        return json.loads(data)
    return []
 
 
def add_item(ev):
    text = inp.value.strip()
    if text == "":
        out.html = "<em>Najprv napíš položku.</em>"
        return
 
    items.append(text)
    inp.value = ""
    render()
    save_items()
 
 
def clear_all(ev):
    items.clear()
    render()
    save_items()
 
 
def remove_last(ev):
    if len(items) == 0:
        out.html = "<em>Nie je čo zmazať.</em>"
        return
    items.pop()
    render()
    save_items()
 
 
 
def apply_theme(fn_theme_value):
    global theme_label #overim si farbu a
    document.body.class_name = fn_theme_value #zmenim css calssname
    fn_theme_value.text = fn_theme_value #zmenim farbu na aku vybral pouzivatel
   
 
 
 
def save_theme():
    storage["theme"] = theme
 
 
 
def load_theme():
    data = storage.get("theme", "") #pytame data pod klucom theme a pozire ci tam je nieco take , vrati prazdny retazec
    if len(data) == 0: #ak text neni
        return "light"
    return data
 
 
 
 
 
def toggle_theme(ev=None):
    global theme         #premenna thema bude golabalna
    if theme =="light":
        theme = "dark"
    else:
        theme = "light"
    apply_theme(theme)    #aplikujem novu themu
    save_theme()    #ulozim do storagu


 
def on_key(ev):
    if ev.key == "T":
        toggle_theme()



document.bind("keydown", on_key)

btn_add.bind("click", add_item)
btn_clear.bind("click", clear_all)
btn_last.bind("click", remove_last)
btn_theme.bind("click", toggle_theme)

# (Pri hodnotení môže učiteľ požiadať o malú úpravu na preukázanie vedomostí)
 
items = load_items()
render()
theme = load_theme()
apply_theme(theme)