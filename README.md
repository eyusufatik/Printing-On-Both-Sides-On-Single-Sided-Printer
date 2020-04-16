# Printing On Both Sides On Single Sided Printer
My brother had an homework which would be easier to do if he printed it out first, but the problem was that our printer couldn't print on both sides of the paper so if he'd print his homework it would waste lots of paper. So in order to print on both sides of the paper I came up with this solution:

* Split the PDF with PyPDF (pdf_splitter.py)
* Use UNIX command *lp* to print the pages (printer.py)
* Print odd pages
* Put the papers back in the paper tray
* Print even pages
