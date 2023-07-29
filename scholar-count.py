import os, json
from serpapi import GoogleScholarSearch

params = {
  "api_key": "bbb9eabf3742ad4f07b8e5a7a0c45fa64260907b69a0a21c8ff4bf809edf6582",
  "engine": "google_scholar_author",
  "hl": "en",
  "author_id": "c-Ub9FYAAAAJ"
}

search = GoogleScholarSearch(params)
results = search.get_dict()
data = {
    'citations': results['cited_by']['table'][0]['citations']['all'],
    'h-index': results['cited_by']['table'][1]['h_index']['all'],
    'i10-index': results['cited_by']['table'][2]['i10_index']['all']
    }

# Output each variable to separate JSON files
with open('citations.json', 'w') as citations_file:
    json.dump(data['citations'], citations_file, indent=2)

with open('h-index.json', 'w') as h_index_file:
    json.dump(data['h-index'], h_index_file, indent=2)

with open('i10-index.json', 'w') as i10_index_file:
    json.dump(data['i10-index'], i10_index_file, indent=2)

