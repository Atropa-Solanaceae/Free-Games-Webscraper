from bs4 import BeautifulSoup as bs
import requests
#import time

#starttime = time.time()
#interval = 86400

#while True:
for i in range(1):
    url = requests.get("https://claimfreegames.com/en")
    xml = bs(url.text, "lxml")
    html = bs(url.content, "html.parser")

    count = -1
    for heading in xml.find_all(["h3"]):
        title = (heading.name.strip() + heading.text.strip())
        count += 1
        title = title.replace("h3", str(count) + ". ")
        for r in (("Instant Push Notifications", ""), ("Follow on Reddit", ""), ("Subscribe via RSS", ""), ("Subscribe via Pushbullet", ""), ("Subscribe via Email", ""), ("Get updates to Discord", ""), ("RSS & Json Filtering NEW!", ""), ("Monitored Markets & Platforms", "")):
            title = title.replace(*r)
        print(title)
    print("------------------------------------------")

    classes = html.find_all(class_ = "platform")
    classes = str(classes)

    steam = (classes.count("Steam Icon"))
    epic = (classes.count("Epic Icon"))
    itch = (classes.count("Itch Icon"))

    classes = classes.replace('<div class="platform">', "")
    classes = classes.replace('<img alt="', "")
    classes = classes.replace('" src="/icons/itch.ico"/>', "")
    classes = classes.replace('[', "")
    classes = classes.replace(']', "")
    classes = classes.replace('itch', "")
    classes = classes.replace('steam', "")
    classes = classes.replace('epic', "")
    classes = classes.replace('</div>,', "")
    classes = classes.replace('</div>', "")
    classes = classes.replace('" src="/icons/.ico"/>', "")
    classes = classes.replace('</div>', "")
    classes = classes.replace('Icon', "")
    classes = classes.lower()
    classes = classes.split()

    count = 0

    for element in classes:
        print("Game number " + str(count) + " is from " + classes[count])
        count += 1
    print("------------------------------------------")
    print("Steam sale(s): " + str(steam) + "\nEpic Games store sale(s): " + str(epic) + "\nItch sale(s): " + str(itch) + "\n")

    #time.sleep(interval - ((time.time() - starttime) % interval))
