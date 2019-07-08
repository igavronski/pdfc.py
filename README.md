# pdfc.py
Get PDF annotations using Python 2/3 and Poppler.

You will need:

- Python 2 or 3
- PyPDF2 (get using `pip install pypdf2`)
- Poppler (get using `apt install poppler`)

Usage:

`python pdfc.py [pdfname] [offset]`

It gets the annotations (notes, highlights) and spits them out to the standard output.

Use offset if document pages are not the same as PDF pages (for example, the PDF file has a preamble before the actual document starts).

I have succesfully tested it in MacOS/Brew and Android/Termux.
