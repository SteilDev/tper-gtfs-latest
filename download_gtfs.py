import requests
from bs4 import BeautifulSoup

# Dictionary of feeds: "name": "base details URL"
feeds = {
    "gommagtfsbo": "https://solweb.tper.it/web/tools/open-data/open-data-detail.aspx?source=&filename=gommagtfsbo",
    "gommagtfsfe": "https://solweb.tper.it/web/tools/open-data/open-data-detail.aspx?source=&filename=gommagtfsfe",
    "gtfsmex": "https://solweb.tper.it/web/tools/open-data/open-data-detail.aspx?source=&filename=gtfsmex"
}

for name, details_url in feeds.items():
    print(f"Processing feed: {name}")

    # Fetch HTML
    resp = requests.get(details_url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Extract version
    version_span = soup.find("span", id="ContentPlaceHolderMain_lblVersione")
    if not version_span:
        print(f"  Could not find version for {name}, skipping.")
        continue
    version = version_span.text.strip()
    print(f"  Latest version: {version}")

    # Construct download URL
    download_url = (
        f"https://solweb.tper.it/web/tools/open-data/open-data-download.aspx?"
        f"source=solweb.tper.it&filename={name}&version={version}&format=zip"
    )
    print(f"  Download URL: {download_url}")

    # Download the GTFS zip
    out_file = f"gtfs_{name}_latest.zip"
    with requests.get(download_url, stream=True) as r:
        r.raise_for_status()
        with open(out_file, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print(f"  Saved feed to {out_file}\n")

