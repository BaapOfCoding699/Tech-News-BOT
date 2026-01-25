from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key = '402faf0d8cca45c18da8f649b038de36')
top_headlines  = newsapi.get_top_headlines(category='technology',language='en')
arcticles = top_headlines['articles']
print("BAAP TECH NEWS - Top 5 headlines \n")
for i,arcticles in enumerate(arcticles[:5],1):
    print(f"{i}.{arcticles['title']}")
    print(f"Read More : {arcticles['url']}\n")

