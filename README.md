# ChromeHistoryGenerator

Generates aged fake Google Chrome History.

Currently only works on Windows, but can easily run on Linux/Mac with a few small changes.

## Usage

Ensure Chrome is not running, then execute the below command:

```
py.exe generatehistory.py <path_to_url_list>
```

The sample URL list is copied from the "Influencer" persona on https://trackthis.link/. You can create your own persona by simply adding a list of URLs to a text file.

```
py.exe generatehistory.py influencer.txt
```
