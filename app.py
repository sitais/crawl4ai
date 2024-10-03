from crawl4ai import WebCrawler


# Create an instance of WebCrawler
crawler = WebCrawler()

# Warm up the crawler (load necessary models)
crawler.warmup()

# Run the crawler on a URL
result = crawler.run(url="https://mer.vin/2024/06/crawl4ai-and-praisonai/")

# Print the extracted content
print(result.markdown)
