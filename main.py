from phew import server, access_point
import json

# 1) Crée le Wi-Fi du Pico (hotspot)
ap = access_point("raspi_ap", "123456789")
ip = ap.ifconfig()[0]
print("Ouvre dans ton tel :", ip)

# 2) Charge la page web
with open("index.html", "r") as f:
    indexhtml = f.read()

# 3) Routes
@server.route("/", methods=["GET"])
def home(request):
    return indexhtml

@server.route("/state", methods=["GET"])
def state(request):
    return json.dumps({"ok": True, "msg": "serveur en ligne"})

@server.catchall()
def catchall(request):
    return "Not found", 404

# 4) Lance le serveur
server.run()
