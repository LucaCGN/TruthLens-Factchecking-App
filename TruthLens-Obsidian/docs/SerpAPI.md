

# SerpAPI Documentation

## Getting Started

SerpAPI can extract clean, structured data from Google in real-time.

### API Playground
With our powerful [API playground](#api-playground), you can quickly and flexibly configure requests. Just fill in some fields, and we'll generate a request for you.

#### Making Requests
Endpoint for making requests:
```
get https://api.spaceserp.com/google/search
```

You can scrape any data from Google search via this endpoint.

#### Parameters
- `apiKey*`: An account API key that is used to authorize user API requests. (*Required parameter*)
- `q*`: The keyword which you want to search. (*Required parameter*)
- `location`: Location in which the query is executed. You can get a full list of available locations [here](#location).
- `domain`: Google domain that performs the search. You can find a full list of the available domains [here](#google-domains). *Default value: google.com*.
- `gl`: Indicate the country of the Google result page. Full list of the available `gl` parameters can be found [here](#google-countries). *Default value: us*.
- `hl`: Specify the interface language for the Google search result page. Full list of the available `hl` parameters can be found [here](#google-languages). *Default value: en*.
- `resultFormat`: Results format. Possible values: `json`, `csv`, `html`. *Default value: json*.
- `device`: The device which performed search requests. Possible values: `desktop`, `mobile`, `tablet`. *Default value: desktop*.
- `mobileOs`: Mobile OS. Possible values: `ios`, `android`. *Should be used with `device=true`*.
- `pageSize`: The number of results shown per page. *Should be from 1 to 100*.
- `pageNumber`: Number of the page of results to return.

#### Responses
- `200: OK`: Structured SERP Data

## Location
The `location` parameter is used to localize your query. You can use any string, but for increased accuracy, you should choose a supported by Google value. There are several ways to do this:

### Locations Autocomplete API
Endpoint for finding related Google locations:
```
get https://api.spaceserp.com/google/locations
```

## Google Domains
You can find a full list of the available domains in CSV file or via [API Playground](#google-domains).

- [Google Domains.csv](#google-domains) (5KB Text)

## Google Countries
You can find a full list of the available Google countries in CSV file or via [API Playground](#google-countries).

- [Google Countries.csv](#google-countries) (4KB Text)

## Google Languages
You can find a full list of the available Google languages in CSV file or via [API Playground](#google-languages).

- [Google Languages.csv](#google-languages) (2KB Text)

---