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
python news_api.py
```

### QuoteAPI (`quote_api.py`)

Fetches a happiness-category quote from API Ninjas and reprints it every 10 minutes.

```bash
pip install requests
python quote_api.py
```

### WhatShouldIReadNext (`whatshouldireadnext.py`)

CLI that searches BigBookAPI by title/author and prints similar books.

```bash
pip install requests
python whatshouldireadnext.py "Pride and Prejudice"
```

## Requirements

Typical deps across scripts: `requests`, `pillow`, `streamlit`, `pytz`. No shared `requirements.txt` is checked in.

## Security

Several scripts currently **hardcode third-party API keys** in source (`news_api.py`, `quote_api.py`, `whatshouldireadnext.py`). Treat those keys as compromised: **rotate them**, move values to environment variables or Streamlit secrets, and stop committing keys. This README does not include the keys.
