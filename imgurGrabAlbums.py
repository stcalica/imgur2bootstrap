#!/bin/py
import requests
import sys
import json

acctEndpoint = "https://api.imgur.com/3/account/"

app_name = "ChokeOutCancerFormatter"
client_id = "61cc49026d549a8"

def album_extract(username):
    resp = requests.get(acctEndpoint+username+"/albums",  headers={'Authorization': 'Client-ID 61cc49026d549a8'})
    resp =  resp.json()
    albums = resp["data"]
    # title =  album["title"]
    # images =  album["images"]
    # link = album["link"]
    return albums

def main():
    username = sys.argv[1]
    albums = album_extract(username)
    with open(username+".txt", "w") as out:
        for album in albums:
            out.write(album["id"])
            out.write("\n")


if __name__ == "__main__":
    main()
