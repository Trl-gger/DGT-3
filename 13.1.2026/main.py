from browser import document # umožní nám pracovať s našim HTML súborom
from browser.local_storage import storage # umožní nám používať localstorage
import json # umožní nám používať JSON
 


# vytvoríme si premenné, ktoré sú viazané na naše premenné z HTML, aby sme do nich mohli neskôr vpisovať 
inp = document["inp_item"]
btn_add = document["btn_add"]
btn_clear = document["btn_clear"]
btn_last = document["btn_last"]
out = document["out"]
 

 
def render(): # Ak je pole v premennej items prázdne, tak to do odrážky v html vypíše "Zoznam je prázdny."
    if len(items) == 0:
        out.html = "<em>Zoznam je prázdny.</em>"
        return
 
    html = "<ul>" # Pre každu premennú v poli items vytvorí položku v reťazci 
    for it in items:
        html += f"<li>{it}</li>"
    html += "</ul>"
    out.html = html
 
 
def save(): # Vytvorí definícu, ktorá uloží do localstorage položky z items, potom čo sú premenené z pola na text s pomocou json
    storage["todo_items"] = json.dumps(items)
 
 
 
def load(): # Načíta položky localstorage a ak je localstorage prázdny, tak vráti "[]"
    data = storage.get("todo_items")
    if data:
        return json.loads(data)
    return[]
       
 
 
 
def add_item(ev): # Ak je text prázdny, tak na stránke vypíše "Najprv napíš položku." a ak tam niečo je, tak 
    text = inp.value.strip()
    if text == "":
        out.html = "<em>Najprv napíš položku.</em>"
        return
 
    items.append(text)
    inp.value = ""
    render()
     # TODO (Checkpoint 5): zavolaj save()
    save()
 
def clear_all(ev): # Vymaže všetky elementy z pola items, ukáze to a uloží
    items.clear()
    render()
    save()
 
def remove_last(ev): # Vymaže posledný element z pola items, ukáze to a uloží
    last_item = items.pop() 
    render()
    save()
    pass
 
items = load()  # Načíta do items text z localstorage 
render() # Na stránke ukáže hodnoty itema
btn_add.bind("click", add_item) # Keď klikneme na tlačítko "add_item", tak sa spustí funkcia "btn_add" a pridá do items a vlastne aj localstorage novú položku zoznamu
btn_clear.bind("click", clear_all) # Keď klikneme na tlačítko "clear_all", tak sa spustú funkcia "btn_clear" a vymaže z items a localstorage všetky položky 
btn_last.bind("click", remove_last) # Keď klikneme na tlačítko "remove_last", tak sa spustú funkcia "btn_last" a vymaže z items a localstorage poslednú pridanú položku
 


# Do localstorage ukladáme položky, ktoré sme si pridali do zoznamu 
# Json používame, aby sme položky, ktoré sú v poli premenili na štandardný text, pretože localstorage vie uložiť iba text, nie pole (to používame v premennej items na uloženie položiek do zoznamu)