# cushead.py
###### _Python 3_

[![Build Status](https://api.travis-ci.org/lucasvazq/cushead.py.svg?branch=master)](https://travis-ci.org/lucasvazq/cushead.py)

This simple script improves your SEO and UX. It adds lang attribute to the 
<html> element and search and replace '$head$' string with personalized head 
elements.

## MENU

[Install](#install)

[Usage with example](#usage-with-example)
- [-h](#-h)
- [1 - Find the main file](#1---find-the-main-file)
- [2 - Define personalized values](#2---define-personalized-values)
  - [3 - Execute the script](#3---execute-the-script)
- [4 - View results](#4---view-results)
- [5 - Testing](#5---testing)

[Other tools](#other-tools)
- [Icons tool generator](#icons-tool-generator)
- [Sitemap](#sitemap)
- [Another concepts](#another-concepts)

[License](#license)

## Install

`pip3 install cushead.py`

## Usage with example

### -h

`cushead.py -h`

```
usage: cushead.py -file PATH/TO/FILE [Options]. Do cushead.py -h for help

This simple script improves your SEO and UX. It adds lang attribute to the
<html> element and search and replace '$head$' string with personalized head
elements. Git repository: https://github.com/lucasvazq/cushead.py

Required:
  -file FILEPATH        Path to file that want to edit.
  -preset FILENAME     Generate example file with presets.

Options:
  --exclude-comment     Exclude 'Custom head elements' comment.
  --exclude-html        Exclude html lang attribute.
  --exclude-config      Exclude basic head config elements.
  --exclude-basic       Exclude basic SEO elements.
  --exclude-opengraph   Exclude opengraph.
  --exclude-facebook    Exclude facebook.
  --exclude-twitter     Exclude twitter.
  --exclude-opensearch  Exclude opensearch.
  --exclude-author      Exclude author.
```

### 1 - Find the main file

This is the file that wants to edit. It needs to have the <html> element for 
add the lang attribute, and a '$head$' string that be replaced for the custom 
elements. Example:

_(my_index.html)_
```html
<html> 
  <head>
    $head$
    ...
  </head>
</html>
```

If there isn't the <html> element, cant add the lang attribute. Same way, if 
there isn't the '$head$' string, cant adds the custom head elements.

### 2 - Define personalized values

Create a file with this inside:

_(cushead.txt)_
```python
values = {

    # FILE PATH
    'path':             './index.html',

    # BASIC CONFIG
    'content-type':     'text/html; charset=utf-8',
    'X-UA-Compatible':  'ie=edge',
    'robots':           'index, follow',
    'manifest':         '/manifest.json',
    'msapp-config':     '/browserconfig.xml',
    'viewport':         {'width': 'device-width', 'initial-scale': '1'},
    'locale':           'en_US',
    'color':            '#FFFFFF',

    # BASIC SEO
    # Mask icon color obtained from BASIC CONFIG.
    'title':            'Microsoft',
    'description':      'Technology Solutions',
    'icon':             '/static/favicon.png',
    'mask-icon':        '/maskicon.svg', # svg file type
    'fluid-icon':       '/fluidicon.png', # 512x512 png file type.
    'subject':          'Home Page',
    'keywords':         'Microsoft, Windows',

    # SOCIAL MEDIA

    # General
    'preview':          '/static/preview.png', # Big image preview

    # Opengraph
    # og:title, og:description, og:image, og:image:secure_url and og:locale
    # obtained from BASIC SEO and BASIC CONFIG.
    'og:url':           'www.microsoft.com',
    'og:type':          'website', # http://ogp.me/#types
    'og:image:type':    'image/png', # image/jpeg, image/gif or image/png

    # Facebook
    'fb:app_id':        '12345', # (Str) Facebook App ID

    # Twitter
    # Only support twitter:card = summary
    # twitter:title, twitter:description, twitter:image and twitter:image:alt
    # obtained from BASIC SEO and General - SOCIAL MEDIA.
    'tw:site':          '@Microsoft', # Commerce Twitter account
    'tw:creator:id':    '123456', # Page editor ID

    # OPENSEARCH
    # OpenSearch title pretend to be the same as title from BASIC SEO.
    'opensearch':       '/opensearch.xml',
    
    # AUTHOR
    'author':           'Lucas Vazquez'
    
}
```

Look, there is a python dictionary called 'values', they are used to pass key-value pair to the script. Please, don't change the dictionary 'values' name. Feel free to add comments like python inside the dictionary.
In values there is a key called 'path', this referred to the path where is the file that you want to edit. If some keys are omitted, the elements referred to them are omitted too.
You can generate full example preset file like this using:
`python3 cushead.py -preset cushead.txt`

### 3 - Execute the script

`cushead.py -file cushead.txt --exclude-twitter`

### 4 - View results

_(my_index.html)_
```html
<html lang="en_US">
  <head>
    <!-- Custom head elements -->
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <meta name="robots" content="index, follow" />
    <link rel="manifest" href="/manifest.json" />
    <meta name="msapplication-config" content="/browserconfig.xml" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="Content-Language" content="en_US" />
    <meta name="theme-color" content="#FFFFFF" />
    <meta name="msapplication-TileColor" content="#FFFFFF" />
    <title>Microsoft</title>
    <meta name="description" content="Technology Solutions" />
    <link rel="shortcut icon" href="/static/favicon.png" type="image/x-icon" />
    <link rel="mask-icon" href="/maskicon.svg" color="#FFFFFF" />
    <link rel="fluid-icon" href="/fluidicon.png" title="Microsoft" />
    <meta name="subject" content="Home Page" />
    <meta name="keywords" content="Microsoft, Windows" />
    <meta property="og:locale" content="en_US" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="www.microsoft.com" />
    <meta property="og:site_name" content="Microsoft" />
    <meta property="og:title" content="Microsoft" />
    <meta property="og:description" content="Technology Solutions" />
    <meta property="og:image" content="/static/preview.png" />
    <meta property="og:image:secure_url" content="/static/preview.png" />
    <meta property="og:image:type" content="image/png" />
    <meta name="og:image:alt" content="Microsoft - Technology Solutions" />
    <meta porperty="fb:app_id" content="12345" />
    <link rel="search" type="application/opensearchdescription+xml" title="Microsoft" href="/opensearch.xml" />
    <meta name="author" content="Lucas Vazquez" />
  </head>
</html>
```

### 5 - Testing

[Facebook Debugger](https://developers.facebook.com/tools/debug/)
[Twitter Card validator](https://cards-dev.twitter.com/validator)

## Other tools

### Icons tool generator

[https://www.favicon-generator.org/](https://www.favicon-generator.org/)

```txt
Steps:
  Add image
  Turn on:
    'Generate icons for Web, Android, Microsoft, and iOS (iPhone and iPad) Apps'
  Turn off:
    'Generate only 16x16 favicon.ico'
    'Maintain Image Dimensions (don't resize to be square)'
  Click on 'Create favicon'

After refresh, click on 'Download the generated favicon' for download zip file
that has a big amount of icons and other files.
Use the downloaded browserconfig.xml for complementing your own 
browserconfig.xml file. Same for manifest.json
Getting back to the website, copy the html text inside the box, and paste in
your head section of your website and close the opened tags adding ' /' (with 
the space) at the end, before '>'. This's an excellent complement to cushead.py
Mixing it, you will need to ignore the next lines:
    ...
14  <link rel="manifest" href="/manifest.json">
15  <meta name="msapplication-TileColor" content="#ffffff">
    ...
17  <meta name="theme-color" content="#ffffff">
```

### Sitemap

A good practice is to add sitemap.xml to your site, linking it in robots.txt
[Sitemap generator](https://www.xml-sitemaps.com/)
[Test your sitemap with google](https://search.google.com/search-console/not-verified?original_url=/search-console/sitemaps)

### Other concepts

These concepts compose a good practice to improve SEO and UX

 - Structured data: RDFa, JSON-D, Microdata, GoodRelations, vCard, hCard

 -  Use rel profile attribute for refer to author or website owner

 -  Accelerated Mobiles Pages

 -  Progressive Web Apps

 -  Server Side Rendering

 -  Javascript and css minified and purged with short variables names
 -  Responsive Design
 -  Mobile call and Whatsapp sms for mobiles websites
 -  Google my Business integration
 -  gzip and bzip2 compression
 -  Content Delivery Network
 -  HTTP caching in Client Side

## License

**cushead.py** © 2019 Lucas Vazquez. Released under the [MIT](http://mit-license.org/) License.
