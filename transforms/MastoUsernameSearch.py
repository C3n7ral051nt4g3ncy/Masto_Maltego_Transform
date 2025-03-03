#!/usr/bin/env python3
import sys
import subprocess
import re
import requests
from maltego_trx.maltego import MaltegoTransform
from maltego_trx.server import app  # Import Flask server for `runserver`

# **Check if running the server instead of a search**
if len(sys.argv) > 1 and sys.argv[1] == "runserver":
    app.run(host="0.0.0.0", port=8080)  # Start the Maltego Transform Server
    sys.exit(0)

# Extract username from Maltego input (ignore `runserver`)
username = None
for arg in sys.argv[1:]:
    if not arg.startswith("%") and not arg.startswith("properties."):
        username = arg
        break

# If no username, return an empty response
if not username:
    print("<MaltegoMessage><MaltegoTransformResponseMessage><Entities></Entities></MaltegoTransformResponseMessage></MaltegoMessage>")
    sys.exit(1)

# Initialize Maltego transform response
transform = MaltegoTransform()

# **Step 1: Run Masto CLI Command (API Search)**
try:
    result = subprocess.run(
        ["/Library/Frameworks/Python.framework/Versions/3.10/bin/masto", "-u", username],
        capture_output=True,
        text=True
    )
except Exception as e:
    transform.addUIMessage(f"Error running Masto: {str(e)}")
    sys.stdout.write(transform.returnOutput())
    sys.exit(1)

# **Step 2: Extract ALL URLs from Output**
found_urls = set()  # Use a set to avoid duplicates
url_pattern = re.compile(r"https?://\S+")

for line in result.stdout.splitlines():
    urls = url_pattern.findall(line)
    for url in urls:
        found_urls.add(url)

# **Step 3: Fediverse List Search (Correct JSON Source)**
try:
    response = requests.get("https://raw.githubusercontent.com/C3n7ral051nt4g3ncy/Masto/master/fediverse_instances.json", timeout=10)
    fediverse_sites = response.json()["sites"]

    for site in fediverse_sites:
        instance_url = site["uri_check"].format(account=username)
        expected_string = site["e_string"]
        
        try:
            res = requests.get(instance_url, timeout=5)
            if res.status_code == 200 and expected_string in res.text:
                found_urls.add(instance_url)
        except Exception:
            continue  # Skip failed sites

except Exception as e:
    transform.addUIMessage(f"Fediverse search error: {str(e)}")

# **Step 4: Add Extracted URLs to Maltego**
if not found_urls:
    transform.addUIMessage(f"No Mastodon profiles found for '{username}'")
else:
    for url in found_urls:
        entity = transform.addEntity("maltego.Website", url)
        entity.addProperty("URL", "URL", "strict", url)

# **Return ONLY Maltego XML Output**
sys.stdout.write(transform.returnOutput())
