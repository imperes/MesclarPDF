import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()

lista_arquivos = os.listdir("pdf_mesclar")
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"pdf_mesclar/{arquivo}")

merger.write("PDF_Final.pdf")