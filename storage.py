import pickle
import variablen as var

def save():
    with open('var.dat', 'wb') as sv:
        pickle.dump(var.saved_links_name, sv)
        pickle.dump(var.saved_links, sv)
        pickle.dump(var.range_in_links, sv)

def load():
    try:
        with open('var.dat', 'rb') as lv:
            var.saved_links_name = pickle.load(lv)
            var.saved_links = pickle.load(lv)
            var.range_in_links = pickle.load(lv)
    except FileNotFoundError:
        # Datei existiert noch nicht, also erstmal nichts laden
        var.saved_links_name = []
        var.saved_links = []
        var.range_in_links = 0
