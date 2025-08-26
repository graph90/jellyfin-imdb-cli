import requests
import sys
import urllib.parse

OMDB_API_KEY = "API_KEY"  # Replace
OMDB_URL = "http://www.omdbapi.com/"

def print_help():
    print("""
Jellyfin IMDb Helper
---------------------
Quickly fetch IMDb IDs for shows and movies to fix Jellyfin metadata.

Usage:
  jellyfin-imdb-cli.py "Title" [--list] [--year YYYY]

Options:
  --list          Search mode: lists multiple matches and lets you choose
  --year YYYY     Narrow results to a specific year
  -h, --help      Show this help message

Examples:
  jellyfin-imdb-cli.py "Breaking Bad"
  jellyfin-imdb-cli.py "Batman" --list
  jellyfin-imdb-cli.py "Batman" --list --year 2005
""")

def search_imdb(title, year=None):
    params = {"s": title, "apikey": OMDB_API_KEY}
    if year:
        params["y"] = year
    query = urllib.parse.urlencode(params)
    url = f"{OMDB_URL}?{query}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "False":
        return None, data.get("Error")

    return data.get("Search"), None

def get_imdb_id(title, year=None):
    params = {"t": title, "apikey": OMDB_API_KEY}
    if year:
        params["y"] = year
    query = urllib.parse.urlencode(params)
    url = f"{OMDB_URL}?{query}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "False":
        return None, data.get("Error")

    return data.get("imdbID"), None

if __name__ == "__main__":
    if len(sys.argv) < 2 or "-h" in sys.argv or "--help" in sys.argv:
        print_help()
        sys.exit(0)

    args = sys.argv[1:]
    year = None
    interactive = False
    title_parts = []

    for i, arg in enumerate(args):
        if arg == "--list":
            interactive = True
        elif arg in ("-h", "--help"):
            print_help()
            sys.exit(0)
        elif arg == "--year":
            try:
                year = args[i+1]
            except IndexError:
                print("❌ Error: --year requires a value (e.g. --year 2008)")
                sys.exit(1)
        elif not arg.startswith("--"):
            title_parts.append(arg)

    title = " ".join(title_parts)

    if interactive:
        results, error = search_imdb(title, year)
        if results:
            print(f"🔍 Results for '{title}'" + (f" ({year})" if year else "") + ":")
            for idx, item in enumerate(results, 1):
                print(f"{idx}. {item['Title']} ({item['Year']}) — {item['imdbID']}")
            
            choice = input("Enter the number of the correct match (or press Enter to cancel): ")
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(results):
                    chosen = results[idx]
                    print(f"✅ Selected: {chosen['Title']} ({chosen['Year']}) → {chosen['imdbID']}")
                else:
                    print("❌ Invalid selection.")
            else:
                print("❌ No selection made.")
        else:
            print(f"❌ Error: {error}")
    else:
        imdb_id, error = get_imdb_id(title, year)
        if imdb_id:
            print(f"✅ IMDb ID for '{title}'" + (f" ({year})" if year else "") + f": {imdb_id}")
        else:
            print(f"❌ Error: {error}")
