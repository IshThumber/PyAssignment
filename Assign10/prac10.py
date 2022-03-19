from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter 

Uni_result = PdfFileReader(str("Assign10/Res.pdf"))
print(Uni_result.getDocumentInfo())
print(Uni_result.getNumPages()) 

for page in Uni_result.pages:
    print(page.extractText())
    PdfFileWriter().addPage(page)
    
with Path("Assign10/Result1.pdf").open("wb") as output:
    PdfFileWriter().write(output)