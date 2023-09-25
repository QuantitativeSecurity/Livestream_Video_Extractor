import requests
from bs4 import BeautifulSoup
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the URL of the livestream from the form data
        livestream_url = request.form['livestream_url']

        # Make a GET request to the URL of the livestream
        response = requests.get(livestream_url)

        # Use BeautifulSoup to parse the HTML content of the response
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the source tag that contains the video data
        video_src = soup.find('source', {'type': 'video/mp4'})['src']

        # Make another GET request to retrieve the raw video data
        video_response = requests.get(video_src)

        # Return the original livestream and the extracted video side by side
        return '''
        <html>
            <head>
                <style>
                    .video-container {
                        display: flex;
                    }

                    .video {
                        width: 50%;
                    }
                </style>
            </head>
            <body>
                <div class="video-container">
                    <div class="video">
                        <iframe src="{}" width="100%" height="100%"></iframe>
                    </div>
                    <div class="video">
                        <video width="100%" height="100%" controls>
                            <source src="data:video/mp4;base64,{}" type="video/mp4">
                        </video>
                    </div>
                </div>
            </body>
        </html>
        '''.format(livestream_url, video_response.content.encode('base64').strip())

    # Show a form for the user to input the URL of the livestream
    return '''
    <html>
        <body>
            <form action="/" method="post">
                <input type="text" name="livestream_url" placeholder="Enter the URL of the livestream">
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
