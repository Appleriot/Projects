import requests

# Make an api call and store the respone
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store the api respone in a varible
response_dict = r.json()

#Explore information about the repostitons
repo_dicts = response_dict['items']
print(f"Responites returned:{len(repo_dicts)}")

print("\nSelected information about each repostitons.")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Descprition: {repo_dict['description']}")

# Example the first repostiitory.
repo_dict = repo_dicts[0]





