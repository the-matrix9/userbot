from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, STRING_SESSION9, STRING_SESSION10
from datetime import datetime
import time

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)

if API_ID:
   API_ID = API_ID
else:
   print("WARNING: API ID NOT FOUND USING UTTAM API ⚡")
   API_ID = "27079591"

if API_HASH:
   API_HASH = API_HASH
else:
   print("WARNING: API HASH NOT FOUND USING UTTAM API ⚡")   
   API_HASH = "c81ae4c3dc026ea4bf49842a8ce4a5f9"

if not BOT_TOKEN:
   print("WARNING: BOT TOKEN NOT FOUND PLZ ADD ⚡")   

# Main bot client with plugins folder
app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="UTTAM/plugins"),  # Plugins directory ka root
    in_memory=True,
)

# Additional clients using session strings, all loading plugins from the same folder
if STRING_SESSION1:
   print("Client1: Found.. Starting..📳")
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1, plugins=dict(root="UTTAM/plugins"))
   clients.append(client1)

if STRING_SESSION2:
   print("Client2: Found.. Starting.. 📳")
   client2 = Client(name="two", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION2, plugins=dict(root="UTTAM/plugins"))
   clients.append(client2)

if STRING_SESSION3:
   print("Client3: Found.. Starting.. 📳")
   client3 = Client(name="three", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION3, plugins=dict(root="UTTAM/plugins"))
   clients.append(client3)

if STRING_SESSION4:
   print("Client4: Found.. Starting.. 📳")
   client4 = Client(name="four", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION4, plugins=dict(root="UTTAM/plugins"))
   clients.append(client4)

if STRING_SESSION5:
   print("Client5: Found.. Starting.. 📳")
   client5 = Client(name="five", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION5, plugins=dict(root="UTTAM/plugins"))
   clients.append(client5)

if STRING_SESSION6:
   print("Client6: Found.. Starting.. 📳")
   client6 = Client(name="six", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION6, plugins=dict(root="UTTAM/plugins"))
   clients.append(client6)

if STRING_SESSION7:
   print("Client7: Found.. Starting.. 📳")
   client7 = Client(name="seven", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION7, plugins=dict(root="UTTAM/plugins"))
   clients.append(client7)

if STRING_SESSION8:
   print("Client8: Found.. Starting.. 📳")
   client8 = Client(name="eight", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION8, plugins=dict(root="UTTAM/plugins"))
   clients.append(client8)

if STRING_SESSION9:
   print("Client9: Found.. Starting.. 📳")
   client9 = Client(name="nine", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION9, plugins=dict(root="UTTAM/plugins"))
   clients.append(client9)

if STRING_SESSION10:
   print("Client10: Found.. Starting.. 📳")
   client10 = Client(name="ten", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION10, plugins=dict(root="UTTAM/plugins"))
   clients.append(client10)
