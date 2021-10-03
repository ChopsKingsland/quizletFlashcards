from fpdf import FPDF

def genPDF():

    pdf_h = 179
    pdf_w = 297

    pdf = FPDF()
    pdf.add_page('L')

    pdf.set_font('Arial', 'B', 16)
    pdf.set_left_margin(0.01)


    # page 1

    pdf.cell(0.1, 0.1, '', 0, 1, 'L')

    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test1', 1, 0, 'C')
    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test1', 1, 0, 'C')
    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test1', 1, 1, 'C')

    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test2', 1, 0, 'C')
    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test2', 1, 0, 'C')
    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test2', 1, 1, 'C')

    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test3', 1, 0, 'C')
    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test3', 1, 0, 'C')
    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test3', 1, 1, 'C')


    # page 2

    pdf.cell(0.1, 0.1, '', 0, 1, 'L')

    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test4', 1, 0, 'C')
    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test4', 1, 0, 'C')
    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test4', 1, 1, 'C')

    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test5', 1, 0, 'C')
    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test5', 1, 0, 'C')
    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test5', 1, 1, 'C')

    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test6', 1, 0, 'C')
    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test6', 1, 0, 'C')
    pdf.cell(pdf_w/3, pdf_h/3, 'this is a test6', 1, 1, 'C')


    pdf.output('tuto1.pdf', 'F')