This Python project aims to create a personalized Spotify playlist based on Billboard Hot 100 charts from a specified date. It utilizes web scraping techniques to extract song titles from the Billboard website and then searches for these songs on Spotify to gather their unique track identifiers (URIs). Finally, it constructs a playlist on the user's Spotify account with the identified songs.

Key Components:

Web Scraping Billboard Charts:
The project begins by fetching the Billboard Hot 100 chart from a given date using the BeautifulSoup library. It extracts the song names from the HTML elements of the webpage.

Spotify Authentication:
To interact with the Spotify API, the project utilizes Spotify's authentication system. It requires a client ID and a client secret for authorization. Additionally, it specifies the necessary scope for playlist modification and sets a redirect URI.

Search and Playlist Creation:
After authenticating with Spotify, the project searches for each extracted song on the platform, filtering results by the specified year. If a song is found, its URI is collected for playlist creation. If not found, it logs a message indicating that the song doesn't exist on Spotify.

User Interaction:
The project prompts the user to input the desired year for creating the playlist.

Usage:
Users can run the script, provide the desired date, and observe the script's progress as it searches for each song on Spotify. Upon completion, a playlist with the identified songs is created in the user's Spotify account.

Technologies Used:

Python
0auth
Requests library for HTTP requests
BeautifulSoup library for web scraping
Spotipy library for interacting with the Spotify API
