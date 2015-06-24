scrapy-history-middleware
=========================

The Logentires extension send all logs to Logentries.

https://logentries.com/doc/python/

It also functions as a drop-in replacement for the builtin scrapy
httpcache middleware
(`scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware`). For
example:

```python

    EXTENSIONS = {
        'scrapylogentries.extension.LogentriesExtension'
    }

    LOGENTRIES_TOKEN = 'XXXXXX'
    
```

## Requirements

To run the extension:

  * `logentries`

Testing:

  * `nose`
  * `nose-cov`
  * `coverage`
