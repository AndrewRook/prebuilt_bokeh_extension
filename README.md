# prebuilt_bokeh_extension
demo of my issues running prebuilt custom bokeh extensions

## Installation
* `$ conda env create -f environment.yml`
* `$ conda activate bokeh_test`

## Running
* `$ python test.py`

You should see an html page pop up with nothing on it. If you look in
the inspector console you'll get an error:

```
Uncaught (in promise) Error: Model 'package.models.pick.Pick' does not exist. This could be due to a widget or a custom model not being registered before first usage.
    at ModelResolver.get (bokeh-2.3.3.js:1359)
    at Function._instantiate_object (bokeh-2.3.3.js:872)
    at Function._instantiate_references_json (bokeh-2.3.3.js:887)
    at Function.from_json (bokeh-2.3.3.js:1130)
    at _embed_items (bokeh-2.3.3.js:566)
    at Object.embed_items (bokeh-2.3.3.js:558)
```

But if you look at the sources you'll see that the javascript is at
least included in the page. 
