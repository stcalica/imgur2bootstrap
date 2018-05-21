import requests
import sys
import json

albumEndpoint = "https://api.imgur.com/3/album/"

app_name = "ChokeOutCancerFormatter"
client_id = "61cc49026d549a8"

def album_extract(album_hash):
    album_resp = requests.get(albumEndpoint+album_hash,  headers={'Authorization': 'Client-ID 61cc49026d549a8'})
    album_resp =  album_resp.json()
    album = album_resp["data"]
    title =  album["title"]
    images =  album["images"]
    link = album["link"]
    return title, images

    return album_resp

def main():
    album_id = sys.argv[1]
    title, images = album_extract(album_id)
    images = [images[i:i+3] for i in range(0,len(images), 3)]
    html = title+".html"
    with open(html, "w") as wpPost:
        #write beginning of html section, copy from WP
        wpPost.write(title+'\n\n')
        #wpPost.write('<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">\n\n')

        for i,j,k in images:
            wpPost.write('<div class="row">\n')
            wpPost.write('<div class="col-md-4"><img src="'+  i["link"][:-4]+'m'+i["link"][-4:]  +'" alt="ChokeOuT" /></div>\n')
            wpPost.write('<div class="col-md-4"><img src="'+  j["link"][:-4]+'m'+j["link"][-4:]  +'" alt="ChokeOuT" /></div>\n')
            wpPost.write('<div class="col-md-4"><img src="'+  k["link"][:-4]+'m'+k["link"][-4:]  +'" alt="ChokeOuT" /></div>\n')
            wpPost.write('</div>\n')
        wpPost.write('More images on our <a> Imgur Album</a>!\n')

if __name__ == "__main__":
    main()
