import urlparse


parse_result = urlparse.urlparse('http://api.twitter.com:8080/search?q=cricket,football&per_page=20&pretty')
query_result = urlparse.parse_qs(parse_result.query, keep_blank_values=True)
print(parse_result)
print(query_result)

parse_result = urlparse.urlparse('mailto:johndoe@example.com?subject=This is a test mail')
query_result = urlparse.parse_qs(parse_result.query)
print(parse_result)
print(query_result)
