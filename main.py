from phew import server, access_point
import json

# --- WiFi ---
ap = access_point("raspi_ap", "123456789")
ip = ap.ifconfig()[0]
print("Ouvre dans ton tel :", ip)

# --- Simulation d’état ---
compteur = 0
SEUIL_STRESS = 1
sens = "droite"

# --- Fichiers ---
with open("index.html", "r") as f:
    indexhtml = f.read()

with open("style.css", "r") as f:
    stylecss = f.read()

# --- Routes ---
@server.route("/", methods=["GET"])
def home(request):
    return indexhtml

@server.route("/style.css", methods=["GET"])
def style(request):
    return stylecss, 200, {"Content-Type": "text/css"}

@server.route("/Coucou", methods=["GET"])
def Coucou(request):
    return json.dumps({"ok": True, "msg": "Coucou"})

@server.route("/Stress", methods=["GET"])
def Stress(request):
    global compteur
    compteur += 1  # simulation

    if compteur >= SEUIL_STRESS:
        return json.dumps({"ok": True, "msg": "⚠️ Stress élevé"})
    else:
        return json.dumps({"ok": True, "msg": ""})

@server.route("/Jeu", methods=["GET"])
def Jeu(request):

    if sens == "droite" :
        return json.dumps({"ok": True, "msg": "➡️"})
    else :
        return json.dumps({"ok": True, "msg": "⬅️"})

@server.catchall()
def catchall(request):
    return "Not found", 404

# --- Serveur ---
server.run()
