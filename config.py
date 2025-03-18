import os

API_ID = os.environ.get("API_ID", "22594398")

API_HASH = os.environ.get("API_HASH", "3a2408d97d6a222d87766dac2da302df")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7653711439:AAF2xks0h6DxX8Dl8C_pSVVEE-W8ilbhG9g")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5357048091))

LOG = -1002166446304,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[5357048091]
    for x in (os.environ.get("ADMINS", "7827463899").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
