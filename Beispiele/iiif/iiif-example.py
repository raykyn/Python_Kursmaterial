import requests
import shutil

# example request
# https://www.e-codices.unifr.ch/loris/bbb/bbb-Mss-hh-I0016/bbb-Mss-hh-I0016_039.jp2/full/full/0/default/jpg

IIIF_SPIEZER_CHRONIK = f"https://www.e-codices.unifr.ch/loris/bbb/bbb-Mss-hh-I0016/bbb-Mss-hh-I0016"


def request_and_save_image(url: str, name: str):
    """
    Docstring for request_and_save_image
    
    :param url: Description
    :param name: Description
    """
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(f'{name}.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    else:
        print("Couldn't connect to ", url)
        raise requests.ConnectionError


def save_full_image(base_url, name):
    url = base_url + "/full/full/0/default/jpg"
    request_and_save_image(url, name)


def save_split_image(base_url, direction, name):
    """
    url: str, GET zum iiif-Server
    direction: entweder "horizontal" oder "vertical"
    """
    if direction == "horizontal":
        cut1 = "pct:0,0,100,50"
        cut2 = "pct:0,50,100,100"
    elif direction == "vertical":
        cut1 = "pct:0,0,50,100"
        cut2 = "pct:50,0,100,100"
    else:
        print("Invalid split direction was given!")
        raise NotImplementedError
    
    request_and_save_image(base_url + f"/{cut1}/full/0/default/jpg", name + "_upper")
    request_and_save_image(base_url + f"/{cut2}/full/0/default/jpg", name + "_lower")
    

if __name__ == "__main__":
    # Dieser Teil wird nur ausgeführt,
    # wenn das Skript vom Terminal ausgeführt wird

    # Eine einzelne Seite speichern im Ganzen
    page = 39
    base_url = f"{IIIF_SPIEZER_CHRONIK}_{page:03d}.jp2"
    save_full_image(base_url, "seite_39")

    # Eine einzelne Seite gesplittet
    page = 39
    base_url = f"{IIIF_SPIEZER_CHRONIK}_{page:03d}.jp2"
    save_split_image(base_url, "horizontal", "seite_39")

    # Mehrere Seiten speichern
    pages = [7, 17, 42, 73]
    #pages = range(1, 2)
    for page in pages:
        base_url = f"{IIIF_SPIEZER_CHRONIK}_{page:03d}.jp2"
        save_full_image(base_url, f"seite_{page}")

