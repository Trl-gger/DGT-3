from browser import document, html

items = []

def render():
    lst = document["list"]
    lst.clear()
    for it in items:
        li = html.LI()
        li.attrs["data-id"] = str(it["id"])

        # doplnené
        if it["done"]:
            li.class_name = "done"

        txt = html.SPAN(it["text"])
        txt.attrs["data-role"] = "text"

        btn_done = html.BUTTON("Hotovo")
        btn_done.attrs["data-role"] = "done"

        btn_del = html.BUTTON("X")
        btn_del.attrs["data-role"] = "del"

        li <= txt + " " + btn_done + " " + btn_del
        lst <= li

     # doplnené
    total = len(items)
    done = sum(1 for x in items if x["done"])
    document["counts"].text = f"{total} spolu • {done} hotové"

 # doplnené
def add_item(text: str):
    text = text.strip()
    if not text:
        return
    new_id = len(items) + 1
    obj = {"id": new_id, "text": text, "done": False}
    items.append(obj)
    render()

 # doplnené
def toggle_done(item_id: int):
    for it in items:
        if it["id"] == item_id:
            it["done"] = not it["done"]
            break
    render()

def on_list_click(ev):
    target = ev.target
    role = target.attrs.get("data-role")
    li = target
    while li and li.tagName != "LI":
        li = li.parent
    if not li:
        return
    item_id = int(li.attrs.get("data-id"))

     # doplnené
    if role == "done":
        toggle_done(item_id)

    render()

 # doplnené
def on_add_click(ev):
    add_item(document["todo_in"].value)
    document["todo_in"].value = ""

 # doplnené
def on_input_key(ev):
    if ev.key == "Enter":
        on_add_click(ev)

document["add_btn"].bind("click", on_add_click)
document["todo_in"].bind("keydown", on_input_key)
document["list"].bind("click", on_list_click)

def on_keydown(ev): pass
def save(): pass
def load(): pass

load()
render()
