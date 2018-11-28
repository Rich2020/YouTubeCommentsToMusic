import requests
import time

# FOR VIDEO statistics:
# https://www.googleapis.com/youtube/v3/videos?part=statistics&id=GFphNr0FK-0&key=AIzaSyAWTcp_JeePXF6Lp661Puq2OtOL6LjNQF


def extract_comments_from_page(page):
    results = []
    for i in range(len(page['items'])):
        comment = page['items'][i]['snippet']['topLevelComment']['snippet']
        comment_text = comment['textDisplay']
        posted_date = comment['publishedAt']
        results.append((posted_date, comment_text))
    return results


class CommentRetriever:

    def __init__(self, key):
        self.KEY = key
        self.COMMENT_URL = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&maxResults=100&videoId={videoId}&key={key}'
        self.COMMENT_URL_PAGED = self.COMMENT_URL + '&pageToken={pageToken}'
        self.comments = []

    def get_next_page_for_video(self, video_id, next_page_token):

        page_info = requests.get(
            self.COMMENT_URL_PAGED.format(videoId=video_id, key=self.KEY, pageToken=next_page_token)
        )

        while page_info.status_code != 200:
            time.sleep(20)
            page_info = requests.get(
                self.COMMENT_URL_PAGED.format(videoId=video_id, key=self.KEY, pageToken=next_page_token)
            )

            print('Something went wrong. Token is: {}'.format(next_page_token))

        page_info = page_info.json()

        return page_info

    def get_comments_for_video(self, video_id):

        keep_going = True
        next_page_token = ''

        while keep_going:

            page_info = self.get_next_page_for_video(video_id, next_page_token)

            yield extract_comments_from_page(page_info)

            keep_going = 'nextPageToken' in page_info
            if keep_going:
                next_page_token = page_info['nextPageToken']





