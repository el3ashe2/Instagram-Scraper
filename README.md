# Instagram-Scraper

This Python script scrapes public Instagram profile data using the **Instaloader** library and optionally logs into an Instagram account for scraping private profiles (if permissions are granted). The script can extract the following data:

- Username
- Full name
- Bio
- Number of posts
- Number of followers and following
- Captions, likes, comments for each post
- Downloads Instagram posts to a specified directory

## Features
- Scrape and download all posts from any Instagram profile.
- Extract details like followers, following, and bio information.
- Optionally log in for private profiles (requires Instagram credentials).

## Requirements

- Python 3.x
- Instaloader library

## Installation

1. Clone the repository:


Install the required library:
pip install instaloader
Usage
Update the USERNAME and PASSWORD fields in the script with your Instagram credentials (if scraping private profiles).
Replace 'instagram_profile_name' with the profile name you wish to scrape.
Run the script:


python instagram_scraper.py
The script will display the profile information in the console and download posts to a local directory.

Example


python instagram_scraper.py
Limitations
Instagram may limit scraping depending on the frequency of requests or number of profiles you scrape.
License
This project is licensed under the MIT License.

yaml


---

This **Instagram Scraper** script will make a great addition to your GitHub profile and demonstrate

```bash
git clone https://github.com/yourusername/instagram-scraper.git
cd instagram-scraper
