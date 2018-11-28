import Music
from Analysis import CommentAnalyzer
from CommentTools import CommentRetriever
from collections import Counter
import operator
from AnalysisPlotter import Plotter
import numpy as np

# TODO Move developer key to external config file and read it in (to prevent accidental upload of credentials to VCS)
DEVELOPER_KEY = "YOUR_DEVELOPER_KEY_HERE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

comment_retriever = CommentRetriever(key=DEVELOPER_KEY)

ca = CommentAnalyzer()
ca.ignore_words = ['brexit','may', 'teresa', 'deal','theresa']

all_comments = []
word_frequencies = {}

# Retrieved and process/clean comments in batches/pages
# Build up array of word frequencies as well as an array of cleaned comments
for comment_batch in comment_retriever.get_comments_for_video(video_id='BXVpAoyM5oI'):
    comments = list(map(operator.itemgetter(1), comment_batch))
    cleaned_comments = ca.clean(comments)
    word_frequencies = Counter(word_frequencies) + Counter(ca.word_frequencies(cleaned_comments))
    all_comments.extend(cleaned_comments)

# Get a dataframe of the comments with their sentiment scores and classification
sentiments_df = ca.get_sentiments(all_comments)

# Plot top n word/observation frequencies
plotter = Plotter()
most_common_observations = ca.get_top_n_observations(word_frequencies, 10)
plotter.plot_observations(most_common_observations)

# Plot the moods or 'classification' of the comments
plotter.plot_moods(sentiments_df)

# Calculate bin size. Sentiment can be from 1 to -1 and since there are 88 notes, we should have 1/44 bin sizes
bin_size = 1.0/(len(Music.Notes.available_names) / 2)
bins = np.arange(-1, 1, round(bin_size, 4))

# Build bin numbers by assigning sentiment scores to a bin
bin_numbers = np.digitize(sentiments_df['Sentiment'], bins)

# Bin numbers will start from 1, so we must shift all bins back by 1 so
# that we can use them as indicies when finding their corresponding note
bin_numbers = bin_numbers -1

# Asign the comments to bins
sentiments_df['Bin'] = bin_numbers

# convert notes available and bin numbers to numpy arrays
notes = np.array(Music.Notes.available_names)
bin_numbers = np.array(bin_numbers)

# We have 88 notes available so if  any bin number is 88, we must subtract 1 from it
# otherwise we will go OOB when matching the corresponding note to play.
bin_numbers[bin_numbers >= 88] = 87

# Grab a list of notes to play
notes_to_play = list(notes[bin_numbers])

# Play each comment as a musical note whose pitch depends on the comment sentiment.
interval_between_notes = 0.5
music_player = Music.Player()
music_player.play_notes(notes_to_play, interval_between_notes)

