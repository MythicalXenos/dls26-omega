# T122 — FTG site metadata endpoint checks

Date: 2026-10-06 Asia/Dhaka. Three distinct `functions.fetch_page` retrievals; numeric HTTP statuses were not exposed by the tool.

1. `https://www.ftgames.com/sitemap.xml` — response title/body: `404 Not Found`, `NoSuchKey`, key `release/sitemap.xml`.
2. `https://www.ftgames.com/robots.txt` — response title/body: `404 Not Found`, `NoSuchKey`, key `release/robots.txt`.
3. `https://www.firsttouchgames.com/sitemap.xml` — response title/body: `404 Not Found`, `NoSuchKey`, key `release/sitemap.xml`.

These exact metadata endpoints returned no sitemap or robots content. They do not establish that other FTG website pages or DLS26 materials do not exist. No Cult Heroes route/reward or position-lock evidence was obtained.
