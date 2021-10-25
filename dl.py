import json
from humanfriendly import parse_size
import requests
import argparse
import re
import os.path
from tqdm import tqdm
from time import sleep


parser = argparse.ArgumentParser()

parser.add_argument('-ak', '--api-key', type=str, help="API Key from the tracker", required=True)
parser.add_argument('-asd', '--ad-save-dir', type=str, help="Save path for auto downloaded torrents", default='./watch_dir')
parser.add_argument('-sp', '--starting-page', type=int, help="Starting Page Number", default=1)
parser.add_argument('-ep', '--ending-page', type=int, help="Ending Page Number (-1 for last)", default=-1)
parser.add_argument('-sul', '--size-upper-limit', type=str, help="The Maximum size of torrents allowed", default='50 GB')
parser.add_argument('-sll', '--size-lower-limit', type=str, help="The Minimum size of torrents allowed", default='1 GB')
parser.add_argument('-bpt', '--breathing-page-time', type=float, help="Time (in seconds) between each page", default=2)
parser.add_argument('-btt', '--breathing-torr-time', type=float, help="Time (in seconds) between each torrent download", default=0.1)
parser.add_argument('--alive', help="Only download alive torrents", action='store_true')

args = parser.parse_args()

curr_page = args.starting_page
last_page = 50

alive = 1 if args.alive else 0
pbar = tqdm(total=last_page)

while curr_page < last_page:
    data_url = f"https://aither.cc/api/torrents/filter?api_token={args.api_key}&page={curr_page}&alive={alive}"
    data_resp = requests.get(data_url)

    parsed_json = json.loads(data_resp.text)
    data = parsed_json.get('data', [])
    for release in data:
        attributes = release.get('attributes', {})

        size = attributes.get('size', 0)
        if size < parse_size(args.size_lower_limit) or size > parse_size(args.size_upper_limit):
            continue

        download_link = attributes.get('download_link', '')
        if download_link:
            resp = requests.get(download_link)
            if resp.status_code != 200:
                continue

            content_disp = resp.headers['content-disposition']
            file_name = re.findall('filename=\"(.+)\"', content_disp)[0]

            download_path = os.path.join(args.ad_save_dir, file_name)
            with open(download_path, 'wb') as fp:
                fp.write(resp.content)
            sleep(args.breathing_torr_time)

    if curr_page == args.starting_page:
        if args.ending_page == -1:
            meta = parsed_json.get('meta', {})
            last_page = meta.get('last_page', 50)
        else:
            last_page = args.ending_page
        pbar.reset(total=last_page)

    curr_page += 1
    pbar.update(1)
    sleep(args.breathing_page_time)

pbar.close()
