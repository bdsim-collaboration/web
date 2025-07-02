import os
from urllib.parse import urljoin
import datetime

base_url = "https://https://bdsim-collaboration.github.io/web/"
html_dir = "./"  # your local directory of HTML files

urls = []
for root, _, files in os.walk(html_dir):
    for file in files:
        if file.endswith(".html"):
            rel_path = os.path.relpath(os.path.join(root, file), html_dir)
            rel_url = rel_path.replace(os.path.sep, "/")
            urls.append(urljoin(base_url, rel_url))

today = datetime.date.today().isoformat()

with open("sitemap.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for url in urls:
        f.write("  <url>\n")
        f.write(f"    <loc>{url}</loc>\n")
        f.write(f"    <lastmod>{today}</lastmod>\n")
        f.write("    <changefreq>monthly</changefreq>\n")
        f.write("    <priority>0.5</priority>\n")
        f.write("  </url>\n")
    f.write('</urlset>\n')
