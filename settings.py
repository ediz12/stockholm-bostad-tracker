# INTERNAL
RESOURCE_FOLDER = "resources/"
CHECKED_APARTMENTS_FILE = f"{RESOURCE_FOLDER}/checked_apartments.json"

# DISCORD
DISCORD_TOKEN = "DISCORD TOKEN HERE"
DISCORD_GUILD_ID = 1234567890
DISCORD_CHANNEL_ID = 1234567890

# URLS
BOSTAD_STOCKHOLM_BASE_URL = "https://bostad.stockholm.se"
BOSTAD_STOCKHOLM_HOUSING_LIST_URL = f"{BOSTAD_STOCKHOLM_BASE_URL}/AllaAnnonser"
BOSTAD_STOCKHOLM_DETAILS_URL = BOSTAD_STOCKHOLM_BASE_URL + "/Lista/Details?aid={a_id}"
GOOGLE_MAPS_LOCATION_URL = "https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

# FILTERS
UNWANTED_MUNICIPALITIES = ["Sigtuna", "Upplands-Bro", "Värmdö", "Haninge", "Huddinge", "Södertälje", "Håbo", "Norrtälje", "Nykvarn", "Nynäshamn"]
UNWANTED_DISTRICTS = ["Rinkeby", "Tensta", "Husby", "Norrtälje", "Nykvarn", "Nynäshamn", "Ösmo", "Barkaby"]

MINIMUM_SQM = 60
MINIMUM_ROOMS = 2
MINIMUM_FLOOR = 0
MINIMUM_RENT = 0
MAXIMUM_RENT = 22000

SHOW_YOUTH_APARTMENTS = True
SHOW_COMMON_APARTMENTS = True
SHOW_SENIOR_APARTMENTS = False
SHOW_STUDENT_APARTMENTS = False
SHOW_SHORT_TERM_APARTMENTS = True
