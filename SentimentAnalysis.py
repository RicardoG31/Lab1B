#Ricardo Godoy
#This program reads reddit comments and replies from any post and classifies them as neutral,
#positive, or negative comments, depending of the words used in each comment or reply.
#Last date modified: 9/17/18
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw

reddit = praw.Reddit(client_id='UdOgsdFvN5vfig',
                     client_secret='fKBTGDzr7PsDkdG5GENs--8efVU',
                     user_agent='Recursion'
                     )


nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


def get_text_negative_proba(text):
   return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
   return sid.polarity_scores(text)['neu']


def get_text_positive_proba(text):
   return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments

#This medthod recursively navigates through the list of comments generated above, and appends
#each comment into its corresponding list.
def process_comments(comment, neglist, neulist, poslist):
    
    if comment is None:
        return 0
      
    for i in range(len(comment)):
            neg = get_text_negative_proba(comment[i].body)
            neu = get_text_neutral_proba(comment[i].body)
            pos = get_text_positive_proba(comment[i].body)
            if (neg > pos and neg > neu ):
                neglist.append (comment[i])
            elif (pos > neg and pos > neu):
                poslist.append (comment[i])
            elif (neu > pos and neu > neg):
                neulist.append (comment[i])
            process_comments(comment[i].replies, neglist, neulist, poslist)
    
    return neglist, neulist, poslist
  
def main():
    comments = get_submission_comments('https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')
    negative_comments_list = []
    positive_comments_list = []
    neutral_comments_list = []
    negative, neutral, positive = process_comments(comments, negative_comments_list, neutral_comments_list, positive_comme
                                                   
main()


