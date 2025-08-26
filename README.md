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
