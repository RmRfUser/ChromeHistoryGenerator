# ChromeHistoryGenerator

Generates aged fake Google Chrome History. Intended for "Scambaiters" who need believable history to help prevent scammers picking up on the fact they are connected to a Virtual Machine. 

While this is intended for Scambaiters, this is just a history generator and can be used for anything.

Currently only works on Windows, but can easily run on Linux/Mac with a few small changes.

## Usage

```
py.exe generatehistory.py <path_to_url_list>
```

The sample URL list is copied from the "Influencer" persona on https://trackthis.link/. You can create your own persona by simply adding a list of URLs to a text file.

```
py.exe generatehistory.py influencer.txt
```
