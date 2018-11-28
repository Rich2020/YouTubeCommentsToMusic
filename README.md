# YouTubeCommentsToMusic

    Thank you to https://github.com/daviddeborin/88-Key-Virtual-Piano for his collection of piano notes.

Written over a couple of days, this program was made for entertainment and education.
Presently, it has the following features:

- See what people are talking about most for a given YouTube video by plotting word frequency distribution
- See how positive or negative a video on YouTube is using simple sentiment analysis (Positive, Negative, Neutral)
- *Listen* to YouTube comments based on their sentiment score. 

**Usage**

No command-line argment parsing has been implemented, so you will have to open main.py, modify accordingly and then run it with `python3 main.py`
You can change things like the `video_id`, the top `n` most frequent words to visualize, and the delay between each note being played.
Lower pitch notes represent negative comments while higher pitch notes represent more positive notes.
There are 88 piano keys and sentiment score can range from -1 to 1, "bins" have been created where their interval is `1/(88/2)`.

**Make sure to add your YouTube/Google Developer key**
