# deduplicator.py

import hashlib

seen_hashes = set()

def is_new(news_item):
    content = news_item["title"] + news_item["link"]
    content_hash = hashlib.md5(content.encode()).hexdigest()
    
    if content_hash in seen_hashes:
        return False
    else:
        seen_hashes.add(content_hash)
        return True
