import os
from urllib import response
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build
import json
import re
from numpy import False_
from tqdm import tqdm
import time
import numpy as np

api_key = "AIzaSyCGQPN3S-rrJIz2WX6aHduoAe2F5NJvMAM"
channel_id = "UC_9g6budogcAeNP4XIWGaOg"
# def cal():
# 獲取憑據並創建 API 客戶端
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
client_secrets = "id.json"

flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets, scopes)
credentials = flow.run_console()

youtube = googleapiclient.discovery.build(
    "youtube",  # api_service_name
    "v3",  # api_version
    credentials=credentials
)
#youtube = build("youtube", "v3", developerKey=api_key)


def out(request):
    response = request.execute()
    print(json.dumps(response, indent=4))


class information:  # 取得資訊
    def account():  # 取得頻道的資訊
        print("\nYour channel's informations : ")
        print("contentDetails : ")
        request = youtube.channels().list(
            part='contentDetails, status',
            id=channel_id
        )
        out(request)

    def playlist():  # 取得所有播放清單的概要資訊
        print("\nYour playlists :")
        request = youtube.playlists().list(
            part='contentDetails, snippet, status ',
            channelId=channel_id,
            maxResults=50
        ).execute()
        print("'kind' :", request["kind"])
        print("'etag' :", request["etag"])
        print("'pageInfo' :", request["pageInfo"])
        count = 1
        list_title, list_id = list(), list()
        for i in request["items"]:
            print("\nPlaylist ", count)
            print("    'title':", i['snippet']['title'])
            print("    'id':", i["id"])
            print("    'publishedAt':", i['snippet']["publishedAt"])
            print("    'privacyStatus':", i["status"]["privacyStatus"])
            print("    'itemCount':", i["contentDetails"]["itemCount"])
            list_title.append(i['snippet']['title'])
            list_id.append(i["id"])
            count += 1
            time.sleep(0.01)
        return list_title, list_id

    def single(playlist_id):  # 取得單一播放清單的資訊
        print("\nVideos : ")
        request = youtube.playlistItems().list(
            part='contentDetails, snippet',
            playlistId=playlist_id,
            maxResults=50
        ).execute()
        video_title, video_item, video_id = list(), list(), list()
        count = 1
        for j in request["items"]:
            k = j["snippet"]
            print(count, ". ", k["title"], sep='')
            print("'publishedAt' :", k["publishedAt"])
            print()
            count += 1
            video_title.append(k["title"])
            video_item.append(j["id"])
            video_id.append(j["contentDetails"]["videoId"])
            time.sleep(0.01)
        return video_title, video_item, video_id


class playlist:
    def new():  # 新增播放清單
        tit = input("Input the title : ")  # 播放清單名稱
        while True:
            print("Select the privacyStatus (1. private, 2. public, 3. unlisted) : ")
            sta = int(input())  # 設定權限
            if sta == 1:
                sta = 'private'
                break
            elif sta == 2:
                sta = 'public'
                break
            elif sta == 3:
                sta = 'unlisted'
                break
            else:
                print("Input error number! Choose again.")

        request = youtube.playlists().insert(
            part='snippet,status',
            body={
                "snippet": {
                    "title": tit,
                    "channelId": channel_id
                },
                "status": {
                    "privacyStatus": sta
                }
            }
        ).execute()

    def delete(list_id):  # 刪除播放清單
        request = youtube.playlists().delete(
            id=list_id
        ).execute()

    def rename(playlist_id):  # 更改清單名稱
        nam = input("Input new title : ")
        request = youtube.playlists().update(
            part="id, snippet",
            body={
                "id": playlist_id,
                "snippet": {
                    "title": nam
                }
            }
        ).execute()

    def status(playlist_title, playlist_id):  # 更改清單權限
        while True:
            print("Select the privacyStatus (1. private, 2. public, 3. unlisted) : ")
            sta = int(input())  # 設定權限

            if sta == 1:
                sta = 'private'
                break
            elif sta == 2:
                sta = 'public'
                break
            elif sta == 3:
                sta = 'unlisted'
                break
            else:
                print("Input error number! Choose again.")

        request = youtube.playlists().update(
            part="id, status, snippet",
            body={
                "id": playlist_id,
                "snippet": {
                    "title": playlist_title
                },
                "status": {
                    "privacyStatus": sta,
                }
            }
        ).execute()


class single:  # 管理單一播放清單
    def new(playlist_id):  # 新增影片
        print("\nIf done, press 0.")
        while True:
            link = input("Input the video's link : ")
            if link == '0':
                break
            regex = r'((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)'
            video_id = re.search(regex, link).group()
            request = youtube.playlistItems().insert(
                part="snippet",
                body={
                    'snippet': {
                        'playlistId': playlist_id,
                        'resourceId': {
                            'kind': 'youtube#video',
                            'videoId': video_id
                        }
                    }
                }
            ).execute()
            for i in tqdm(range(100)):
                time.sleep(0.01)

    def cut(video_item):  # 刪除影片
        request = youtube.playlistItems().delete(
            id=video_item,
        ).execute()

    def video(playlist_id, vid, itid, total):  # 修改影片屬性
        while True:
            print("Press 1 : Change position.")
            print("Press 2 : Move to another playlist.")
            print("Press 0 : Done")
            k = int(input())
            if k == 1:  # 更改位置
                print("\nInput the position: ( 1 ~", total, ')')
                pos = int(input()) + 1
                request = youtube.playlistItems().update(
                    part="id, snippet",
                    body={
                        "id": itid,
                        "snippet": {
                            "playlistId": playlist_id,
                            "resourceId": {
                                "kind": "youtube#video",
                                "videoId": vid
                            },
                            "position": pos
                        }
                    }
                ).execute()
                for i in tqdm(range(100)):
                    time.sleep(0.01)
            elif k == 2:  # 搬移至其他清單
                print("Which playlist do you want move to ?")
                request = youtube.playlists().list(
                    part='contentDetails, snippet, status ',
                    channelId=channel_id,
                    maxResults=50
                ).execute()
                id = list()
                count = 1
                for i in request["items"]:
                    print("Playlist", count, ":", i['snippet']['title'])
                    id.append(i["id"])
                    count += 1
                t = int(input())
                new_playlistid = id[t-1]
                request = youtube.playlistItems().insert(
                    part="snippet",
                    body={
                        'snippet': {
                            'playlistId': new_playlistid,
                            'resourceId': {
                                'kind': 'youtube#video',
                                'videoId': vid
                            }
                        }
                    }
                ).execute()
                single.cut(itid)
                for i in tqdm(range(100)):
                    time.sleep(0.01)
            elif k == 0:
                break
            else:
                print("Input error number! Try  again.")

    def view(playlist_id, video_title):  # 尋找影片
        key = input("\nInput the key words : ")
        for i in tqdm(range(100)):
            time.sleep(0.01)
        bool = False
        for i in range(len(video_title)):
            if key in video_title[i]:
                print(i+1, video_title[i])
                bool = True
        if bool == False:
            print("This video is not in this playlist.")
        time.sleep(1)

    def sort_title(playlist_id, video_title, video_item, video_id):  # 按照名稱排序
        total = len(video_title)
        new = list(np.argsort(video_title))
        new.reverse()
        for i in tqdm(range(total)):
            itid, vid = video_item[i], video_id[i]
            request = youtube.playlistItems().update(
                part="id, snippet",
                body={
                    "id": itid,
                    "snippet": {
                        "playlistId": playlist_id,
                        "resourceId": {
                            "kind": "youtube#video",
                                    "videoId": vid
                        },
                        "position": '0'
                    }
                }
            ).execute()
            time.sleep(0.01)


def manage(playlist_id):  # 管理單一播放清單
    while True:
        video_title, video_item, video_id = information.single(
            playlist_id)  # 查看播放清單資訊
        print("Press 1 : Add a new video.")  # 新增影片
        print("Press 2 : Delete a video.")  # 刪除影片
        print("Press 3 : Change video's properties.")  # 修改影片屬性
        print("Press 4 : Search video.")  # 尋找影片
        print("Press 5 : Sort the playlist. (increase)")  # 將影片排序
        print("Press 0 : Back to playlists.")
        q = int(input())
        if q == 1:
            single.new(playlist_id)
        elif q == 2:
            print("\nWhich video do you want to delete ?")
            for i in range(len(video_title)):
                print(i+1, ". ", video_title[i], sep='')
            t = int(input())
            single.cut(video_item[t-1])
            for i in tqdm(range(100)):
                time.sleep(0.01)
        elif q == 3:
            print("\nWhich video do you want to change properties ?")
            for i in range(len(video_title)):
                print(i+1, ". ", video_title[i], sep='')
            t = int(input())
            single.video(
                playlist_id, video_id[t-1], video_item[t-1], len(video_title))
        elif q == 4:
            single.view(playlist_id, video_title)
        elif q == 5:
            single.sort_title(playlist_id, video_title, video_item, video_id)

        elif q == 0:
            break
        else:
            print("Input error number! Try again.\n")


def account_playlists():  # 管理所有播放清單
    while True:
        list_title, list_id = information.playlist()  # 播放清單的大概資料
        print("\nPress 1 : Manage single playlist.")  # 管理單一播放清單
        print("Press 2 : Add a new playlist.")  # 新增播放清單
        print("Press 3 : Delete a playlist.")  # 刪除播放清單
        print("Press 4 : Change playlist's title.")  # 更改清單名稱
        print("Press 5 : Change playlist's status.")  # 更改清單權限
        print("Press 0 : Back to menu.")
        num = int(input())
        bool = True
        if num == 1:
            print("\nWhich playlist do you want to manage ?")
            for i in range(len(list_title)):
                print(i+1, ". ", list_title[i], sep='')
            t = int(input())
            manage(list_id[t-1])
            bool = False
        elif num == 2:
            playlist.new()
        elif num == 3:
            print("\nWhich playlist do you want to delete ?")
            for i in range(len(list_title)):
                print(i+1, ". ", list_title[i], sep='')
            t = int(input())
            playlist.delete(list_id[t-1])
        elif num == 4:
            print("\nWhich playlist do you want to change title ?")
            for i in range(len(list_title)):
                print(i+1, ". ", list_title[i], sep='')
            t = int(input())
            playlist.rename(list_id[t-1])
        elif num == 5:
            print("\nWhich playlist do you want to change status ?")
            for i in range(len(list_title)):
                print(i+1, ". ", list_title[i], sep='')
            t = int(input())
            playlist.status(list_title[t-1], list_id[t-1])
        elif num == 0:
            break
        else:
            print("Input error number! Try again.")
            bool = False
        if bool == True:
            for i in tqdm(range(400)):
                time.sleep(0.01)


def main():
    while True:
        print("\nMenu - What would you like to do ?")
        print("Press 1 : Check your channel's informations.")  # 查看頻道所有資訊
        print("Press 2 : Check your channel's playlists.")  # 查看所有播放清單
        print("Press 0 : Exit.")
        act = int(input())
        if act == 1:
            information.account()
        elif act == 2:
            account_playlists()
        elif act == 0:
            print("Goodbye~")
            break
        else:
            print("Input error number! Try again.")


if __name__ == "__main__":
    main()
