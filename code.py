from adafruit_magtag.magtag import MagTag
from secrets import secrets
import adafruit_requests as requests

#--------- Creds ---------
# base cellar url
BASE_URL = "https://www.cellartracker.com/xlquery.asp"
# get username and password from secrets file
username = secrets["cellarTrackerUsername"]
password = secrets["cellarTrackerPassword"]
# make url string
base = BASE_URL + "?User=" + username + "&Password=" + password + "&Format=csv&Table=Inventory&Location=1"
print(base)

#--------- get data ---------
magtag = MagTag(
    url=base
    )
checkResponse = magtag.fetch()
#split
splitResponse = checkResponse.split('\r\n')

#--------- loop to get count of bottles ---------
count = 0
while count < len(splitResponse):
    count +=1
#cellartracker has extra object at end
total = count-2

#--------- Graphics layer ---------   
magtag.add_text(
    text_font="fonts/Aqua-Grotesque-14-r.bdf",
     text_position=(
        (magtag.graphics.display.width // 2),
        15,
    ),
    text_anchor_point=(0.5, 0.5),
    is_data=False
)
magtag.add_text(
    text_font="fonts/Vonique-64-48-rb.bdf",
    text_position=(
    (magtag.graphics.display.width // 2) - 100, 
    (magtag.graphics.display.height // 2) - 1,
     ),
    is_data=False
)
magtag.add_text(
    text_font="fonts/Aqua-Grotesque-14-r.bdf",
        text_position=(
    (magtag.graphics.display.width // 2), 
    (magtag.graphics.display.height // 2) + 5,
     ),
    is_data=False
)
#--------- set text ---------
magtag.set_text("cellarTracker Inventory")
magtag.set_text(str(total), 1)
magtag.set_text("bottles in \nthe cellar.", 2)

#--------- Refresh rate ---------
magtag.exit_and_deep_sleep(60 * 60 * 24)



