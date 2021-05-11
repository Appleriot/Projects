from operator import itemgetter

import requests

# Make an api call and store the repsone
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code:{r.status_code}")

# Process infomration about each sitiation
submission_ids = r.json()
submission_dict = []
for submission in submission_dict:
    # Make a seprate api call for each submission
    url = f'https//hacker-news.firebaseio.com/v0/item/{submission}[:30].json'
    r.requests.get(url)
    print(f"id: {submission}\tstatus: {r.status_code}")
    repsonse_dict = r.json()

    # Build a dictoary for each article.
    submission_dict = {
        'title': repsonse_dict['title'],
        'hn_link': f"http://news.ycominator.com/item?id={submission}",
        'comments': repsonse_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"\nDiscussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comment']}")
