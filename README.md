# ApplicationProgrammingInterfaces

Small Python demos that call public APIs: Art Institute of Chicago artworks, NewsAPI headlines, happiness quotes, and book recommendations.

## Projects

### HeartHistory (Art Institute of Chicago)

- `hearthistory.py` — CLI that searches AIC artworks by query and opens a random result image
- `hearthistory_streamlit.py` — Streamlit UI for the same search

```bash
pip install requests pillow streamlit
python hearthistory.py "monet"
streamlit run hearthistory_streamlit.py
```

Live demo (if deployed): [hearthistory.streamlit.app](https://hearthistory.streamlit.app)

AIC public search does not require an API key.

### NewsAPI (`news_api.py`)

Terminal ticker that clears the screen and prints US top headlines plus Health, Science, and Technology categories, refreshing every 5 minutes.

```bash
pip install requests pytz
export NEWS_API_KEY=your_newsapi_key
python news_api.py
```

Requires `NEWS_API_KEY`.

### QuoteAPI (`quote_api.py`)

Fetches a happiness-category quote from API Ninjas and reprints it every 10 minutes.

```bash
pip install requests
export API_NINJAS_KEY=your_api_ninjas_key
python quote_api.py
```

Requires `API_NINJAS_KEY`.

### WhatShouldIReadNext (`whatshouldireadnext.py`)

CLI that searches Big Book API by title/author and prints similar books.

```bash
pip install requests
export BIGBOOK_API_KEY=your_bigbook_api_key
python whatshouldireadnext.py "Pride and Prejudice"
```

Requires `BIGBOOK_API_KEY`.

## Requirements

Typical deps across scripts: `requests`, `pillow`, `streamlit`, `pytz`. No shared `requirements.txt` is checked in.

## Environment variables

`news_api.py`, `quote_api.py`, and `whatshouldireadnext.py` load API keys from the environment. Copy `.env.example` to `.env`, fill in your own keys, and export them before running a script. `.env` is gitignored. Each script exits with an error that names the missing variable and does not print key values.

| Variable | Script | Provider |
| --- | --- | --- |
| `NEWS_API_KEY` | `news_api.py` | NewsAPI |
| `API_NINJAS_KEY` | `quote_api.py` | API Ninjas |
| `BIGBOOK_API_KEY` | `whatshouldireadnext.py` | Big Book API |

HeartHistory uses the Art Institute of Chicago public API and does not need a key.

Keys that were previously committed in this repository should be rotated with each provider.
