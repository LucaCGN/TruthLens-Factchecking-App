## NewsAPI - `Everything` Endpoint Documentation

### Overview

The `Everything` endpoint allows searching through millions of articles from over 80,000 large and small news sources and blogs. It is suitable for article discovery and analysis based on various criteria such as keyword or phrase, date published, source domain name, and language.

### Authentication

To use the NewsAPI, you need to authenticate requests with an API key, which is free for development use. The API key can be provided in two ways:

- As a query string parameter named `apiKey`.
- Via the `X-Api-Key` HTTP header.

### Request Parameters

- `q` (string): Keywords or phrases to search for in the article title and body. Supports advanced search with exact match quotes, plus `+` for must-appear words, minus `-` for must-not-appear words, and logical operators `AND`, `OR`, `NOT`.
- `searchIn` (string): Fields to restrict your search to, such as `title`, `description`, and `content`. Can specify multiple fields separated by commas.
- `sources` (string): A comma-separated string of identifiers for the news sources or blogs you want headlines from. Limited to a maximum of 20 sources.
- `domains` (string): Comma-separated string of domains to restrict the search to.
- `excludeDomains` (string): Comma-separated string of domains to exclude from the results.
- `from` (date): The oldest article date allowed in ISO 8601 format.
- `to` (date): The newest article date allowed in ISO 8601 format.
- `language` (string): The 2-letter ISO-639-1 code of the language for articles.
- `sortBy` (string): The order to sort articles in, with options `relevancy`, `popularity`, `publishedAt`.
- `pageSize` (int): The number of results to return per page, with a maximum of 100.
- `page` (int): The page number for pagination.

### Response Object

The response object includes:

- `status` (string): Indicates if the request was successful (`ok`) or not (`error`).
- `totalResults` (int): The total number of results available for the request.
- `articles` (array): The results of the request with article details such as source, author, title, description, URL, image URL, and publish date.

### Usage Examples

#### Search for Articles about Bitcoin

```http
GET https://newsapi.org/v2/everything?q=bitcoin&apiKey=API_KEY
```

#### Search for Articles Mentioning Apple from Yesterday Sorted by Popularity

```http
GET https://newsapi.org/v2/everything?q=apple&from=YYYY-MM-DD&to=YYYY-MM-DD&sortBy=popularity&apiKey=API_KEY
```

#### Search for Articles Published by TechCrunch and The Next Web

```http
GET https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey=API_KEY
```

### Error Handling

If the API key is missing or incorrect, the API will return an error status with a code and message indicating the issue, such as `apiKeyMissing`.

### Limitations

When using the free development key, be aware of the following limitations:

- Limited to 100 requests per day.
- Access to articles published in the last month.
- Results are limited to the first page for each query.

### More Information

For more detailed documentation on other endpoints, authentication methods, and error codes, please refer to the official NewsAPI documentation at:

- Authentication: https://newsapi.org/docs/authentication
- Endpoints: 
  - Everything: https://newsapi.org/docs/endpoints/everything
  - Top Headlines: https://newsapi.org/docs/endpoints/top-headlines
  - Sources: https://newsapi.org/docs/endpoints/sources

### Developer Support

For issues, questions, or feedback, you can contact NewsAPI support or follow them on Twitter for updates and announcements.