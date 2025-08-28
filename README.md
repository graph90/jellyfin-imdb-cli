# jellyfin-imdb-cli

A simple Python CLI tool to quickly fetch IMDb IDs for movies and shows, making it easier to fix metadata issues in [Jellyfin](https://jellyfin.org/).

## Features
- Fetch IMDb ID by exact title
- Interactive search with multiple matches (`--list`)
- Year filter (`--year YYYY`)
- Lightweight and fast (only requires Python and `requests`)

## Requirements
- Python 3
- OMDb API key (get a free key from [OMDb](https://www.omdbapi.com))
- Python dependency: [`requests`]

Install `requests` with:
pip3 install requests
## Examples:
  - python3 jellyfin-imdb-cli.py "Breaking Bad"
  
 -  python3 jellyfin-imdb-cli.py "Batman" --list
  
  - python3 jellyfin-imdb-cli.py "Batman" --list --year 2005

## 🍻 Support / Tip Jar

This project is free and will always be free — enjoy! 🙂  
If it saved you time or made Jellyfin a little better, and you’d like to buy me a beer (totally optional), you can tip using **open source money**:

- **Bitcoin (on-chain):** `bc1qxzgdwc9pgggram8jtnhsmrhdk5pvw8tx6h7qmj`
- **Bitcoin Lightning:** `cloudyhubcap91@walletofsatoshi.com`
