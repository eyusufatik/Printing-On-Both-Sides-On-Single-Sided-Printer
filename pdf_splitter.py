from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_document = "fasikul.pdf"
pdf = PdfFileReader(pdf_document)
print(pdf.getNumPages())
for page in range(pdf.getNumPages()):
    print(page)
    pdf_writer = PdfFileWriter()
    current_page = pdf.getPage(page)
    pdf_writer.addPage(page = current_page)

    outputFilename = "splitted/page-{}.pdf".format(page + 1)
    with open(outputFilename, "wb") as out:
        pdf_writer.write(out)

        print("created", outputFilename)
