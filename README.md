# Unit3DMassDL
A Unit3D Mass Release Downloader. Currently supports Aither.

## Installation
* Ensure Python 3 is installed in your system.
* Run the following command to install the dependencies:
  ```python3
  python -m pip install -r requirements.txt
  ```

## Usage
* Usage Information
```python3
python .\dl.py -h
usage: dl.py [-h] -ak API_KEY [-asd AD_SAVE_DIR] [-sp STARTING_PAGE] [-ep ENDING_PAGE] [-sul SIZE_UPPER_LIMIT] [-sll SIZE_LOWER_LIMIT]
             [-bpt BREATHING_PAGE_TIME] [-btt BREATHING_TORR_TIME] [--alive]

optional arguments:
  -h, --help            show this help message and exit
  -ak API_KEY, --api-key API_KEY
                        API Key from the tracker
  -asd AD_SAVE_DIR, --ad-save-dir AD_SAVE_DIR
                        Save path for auto downloaded torrents
  -sp STARTING_PAGE, --starting-page STARTING_PAGE
                        Starting Page Number
  -ep ENDING_PAGE, --ending-page ENDING_PAGE
                        Ending Page Number (-1 for last)
  -sul SIZE_UPPER_LIMIT, --size-upper-limit SIZE_UPPER_LIMIT
                        The Maximum size of torrents allowed
  -sll SIZE_LOWER_LIMIT, --size-lower-limit SIZE_LOWER_LIMIT
                        The Minimum size of torrents allowed
  -bpt BREATHING_PAGE_TIME, --breathing-page-time BREATHING_PAGE_TIME
                        Time (in seconds) between each page
  -btt BREATHING_TORR_TIME, --breathing-torr-time BREATHING_TORR_TIME
                        Time (in seconds) between each torrent download
  --alive               Only download alive torrents
```
* Example Usage
  ```python3
  python dl.py -ak APIKEY --alive
  ```

## WARNING
This can really cause trouble for your account if not used properly. Ask for permission and set the `-bpt` and `-btt` parameters accordingly to show a little decency towards the beloved tracker :)

## API Key
You can get your API Key by going to `My Settings > Security (Tab) > API Token (sub-tab)`