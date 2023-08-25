# Spotify Playlist Generator for Billboard Top 100 Songs

## Introduction

Welcome to the documentation of my Spotify Playlist Generator project! This Python script connects with the Spotify API and creates personalized playlists featuring the top 100 songs from the Billboard charts of a specified year and week.

## Features

- Accesses the Spotipy API to create playlists.
- Scrapes the Billboard Top 100 songs of a chosen year and week.
- Creates a new playlist on your Spotify account.

## Technologies Used

- Python
- Spotipy
- Beautiful Soup (for web scraping)

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Install dependencies (if any)
4. Set up your Spotify API credentials and Billboard URL as ENVIRONMENT VARIABLES (for security)
5. Run the script: `python main.py`

## Usage

1. Follow the installation steps above.
2. Run the script to generate your playlist.
3. The script will ask a date (YYYY-MM-DD).
4. The script will authenticate with Spotify, fetch Billboard data, and create the playlist.
