# Gruvi example program: a cURL like URL downloader

import sys
import argparse
from urllib.parse import urlsplit
import gruvi

parser = argparse.ArgumentParser()
parser.add_argument('url')
args = parser.parse_args()

url = urlsplit(args.url)
if not url.scheme:
    url = urlsplit('http://{}'.format(args.url))
is_ssl = url.scheme == 'https'
port = url.port if url.port else 443 if is_ssl else 80

client = gruvi.HttpClient()
client.connect((url.hostname, port), ssl=is_ssl)
client.request('GET', url.path or '/')

response = client.getresponse()
if not 200 <= response.status <= 299:
    sys.stderr.write('Error: got status {}\n'.format(response.status))
    sys.exit(1)

while True:
    buf = response.body.read(4096)
    if not buf:
        break
    sys.stdout.buffer.write(buf)
