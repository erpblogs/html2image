IMGKit: Python library of HTML to IMG wrapper
```python
  _____   __  __    _____   _  __  _   _
 |_   _| |  \/  |  / ____| | |/ / (_) | |
   | |   | \  / | | |  __  | ' /   _  | |_
   | |   | |\/| | | | |_ | |  <   | | | __|
  _| |_  | |  | | | |__| | | . \  | | | |_
 |_____| |_|  |_|  \_____| |_|\_\ |_|  \__|
 ```
Python 2 and 3 wrapper for wkhtmltoimage utility to convert HTML to IMG using Webkit.

## Installation
Install imgkit:
```bash
pip install imgkit
```
## Install wkhtmltopdf:
Debian/Ubuntu:

```bash
sudo apt-get install wkhtmltopdf
```

Warning! Version in debian/ubuntu repos have reduced functionality (because it compiled without the wkhtmltopdf QT patches), such as adding outlines, headers, footers, TOC etc. To use this options you should install static binary from wkhtmltopdf site or you can use this script.

Windows and other options:

Check wkhtmltopdf homepage for binary installers or wiki page.


Usage
Simple example:
```python
import imgkit

imgkit.from_url('http://google.com', 'out.jpg')
imgkit.from_file('test.html', 'out.jpg')
imgkit.from_string('Hello!', 'out.jpg')
```

Also you can pass an opened file:

```python
with open('file.html') as f:
    imgkit.from_file(f, 'out.jpg')
```

If you wish to further process generated IMG, you can read it to a variable:
```python
# Use False instead of output path to save pdf to a variable
img = imgkit.from_url('http://google.com', False)
```

You can find all wkhtmltoimage options by type wkhtmltoimage command or visit this Manual. You can drop '--' in option name. If option without value, use None, False or '' for dict value:. For repeatable options (incl. allow, cookie, custom-header, post, postfile, run-script, replace) you may use a list or a tuple. With option that need multiple values (e.g. --custom-header Authorization secret) we may use a 2-tuple (see example below).

```python
options = {
    'format': 'png',
    'crop-h': '3',
    'crop-w': '3',
    'crop-x': '3',
    'crop-y': '3',
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None
}

imgkit.from_url('http://google.com', 'out.png', options=options)
```

At some headless servers, perhaps you need to install xvfb:

```bash
# at ubuntu server, etc.
sudo apt-get install xvfb
# at centos server, etc.
yum install xorg-x11-server-Xvfb
```

Then use IMGKit with option xvfb: {"xvfb": ""}.

By default, IMGKit will show all wkhtmltoimage output. If you don't want it, you need to pass quiet option:
```python
options = {
    'quiet': ''
    }

imgkit.from_url('google.com', 'out.jpg', options=options)
```

Due to wkhtmltoimage command syntax, TOC and Cover options must be specified separately. If you need cover before TOC, use cover_first option:
```python
toc = {
    'xsl-style-sheet': 'toc.xsl'
}

cover = 'cover.html'

imgkit.from_file('file.html', options=options, toc=toc, cover=cover)
imgkit.from_file('file.html', options=options, toc=toc, cover=cover, cover_first=True)
```

You can specify external CSS files when converting files or strings using css option.
```python
# Single CSS file
css = 'example.css'
imgkit.from_file('file.html', options=options, css=css)

# Multiple CSS files
css = ['example.css', 'example2.css']
imgkit.from_file('file.html', options=options, css=css)
```

You can also pass any options through meta tags in your HTML:
```python
body = """
<html>
  <head>
    <meta name="imgkit-format" content="png"/>
    <meta name="imgkit-orientation" content="Landscape"/>
  </head>
  Hello World!
</html>
"""

imgkit.from_string(body, 'out.png')
```


## Configuration
Each API call takes an optional config paramater. This should be an instance of imgkit.config() API call. It takes the config options as initial paramaters. The available options are:

wkhtmltoimage - the location of the wkhtmltoimage binary. By default imgkit will attempt to locate this using which (on UNIX type systems) or where (on Windows).
xvfb - the location of the xvfb-run binary. By default imgkit will attempt to locate this using which (on UNIX type systems) or where (on Windows).
meta_tag_prefix - the prefix for imgkit specific meta tags - by default this is imgkit-
Example - for when wkhtmltopdf or xvfb is not in $PATH:
```python
config = imgkit.config(wkhtmltoimage='/opt/bin/wkhtmltoimage', xvfb='/opt/bin/xvfb-run')
imgkit.from_string(html_string, output_file, config=config)
```

## Troubleshooting
1. IOError: 'No wkhtmltopdf executable found':
Make sure that you have wkhtmltoimage in your $PATH or set via custom configuration (see preceding section). where wkhtmltoimage in Windows or which wkhtmltoimage on Linux should return actual path to binary.

2. IOError: 'No xvfb executable found':
Make sure that you have xvfb-run in your $PATH or set via custom configuration (see preceding section). where xvfb in Windows or which xvfb-run or which Xvfb on Linux should return actual path to binary.

3. IOError: 'Command Failed':
This error means that IMGKit was unable to process an input. You can try to directly run a command from error message and see what error caused failure (on some wkhtmltoimage versions this can be cause by segmentation faults)