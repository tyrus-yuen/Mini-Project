from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

Batch_no = 2
BATCH="Processed/Batch " + str(Batch_no)

print(folder_list)
print(filename_list)
print(path_list)

for i in range(0,len(path_list)-1):
    input_pdf = PdfFileReader(str(path_list[i]))
    total_page = PdfFileReader.getNumPages(input_pdf)
    #os.rename(source + f, destination + f)
    if ((total_page > 2) & (len(filename_list[i].split("_Edited")) == 1)):
        pdf_writer = PdfFileWriter()

        for n in range(0,int(total_page/2)):
            page_odd = input_pdf.getPage(n)
            page_even = input_pdf.getPage(total_page-1-n)
            pdf_writer.addPage(page_odd)
            pdf_writer.addPage(page_even)

        with Path(directory + folder_list[i] + "/" + filename_list[i] + "_Edited.pdf" ).open(mode="wb") as output_file:
        pdf_writer.write(output_file)

    else:
        continue

os.rename(directory, directory.partition("Unprocessed")[0] + BATCH)