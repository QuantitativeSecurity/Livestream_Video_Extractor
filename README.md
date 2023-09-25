Livestream Video Extractor

This web application allows users to extract and display the video from a given livestream URL. Built using Flask, the application uses the BeautifulSoup library to scrape video content from web pages and then serves the video alongside the original livestream.
Features:

    URL Submission: Users can submit a livestream URL through a simple form.
    Video Extraction: The application scrapes the provided URL, looking for video content of type 'video/mp4'.
    Side-by-Side Display: Once the video is extracted, it is displayed side-by-side with the original livestream.

Usage:

    Ensure you have the required libraries installed. You can install them via pip:

    pip install Flask requests beautifulsoup4

    Run the script. This starts the Flask development server.
    Open a web browser and go to http://127.0.0.1:5000/.
    Enter the URL of a livestream in the provided form and submit.
    The application will display the original livestream and the extracted video side-by-side.

Code Structure:

    index() function: The main function that handles both GET and POST requests.
        On a GET request, it displays a form for the user to submit a livestream URL.
        On a POST request, it processes the submitted URL, extracts the video, and displays the result.
    BeautifulSoup: Used to parse the HTML response from the livestream URL and find the video source.
    requests: Used to make HTTP requests to the livestream URL and retrieve video data.
    Flask app: The Flask application that serves the web interface.

Important Notes:

    The application currently assumes that the video source is of type 'video/mp4'. It might not work for livestreams that use different video formats.
    The application directly embeds the video data in the HTML using a base64 encoded data URL. This approach may not be efficient for large videos. Consider serving the video separately or using streaming methods for better performance.
    The Flask server runs in debug mode. This mode is not suitable for production use. Ensure you set debug=False when deploying the application in a production environment.
    Web scraping may be against the terms of service for some websites. Always ensure you have the right to scrape content and be respectful of the website's robots.txt file.
