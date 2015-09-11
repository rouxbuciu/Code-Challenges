from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import menu_main
import csv
import os

data_file = "fr_csv_data.csv"


def import_data(data_file):
    inv_data = csv.reader(open(data_file, "r"))
    for row in inv_data:
        name = row[0]
        street = row[1]
        city = row[2]
        country = row[3]
        zip_code = row[4]
        phone = row[5]
        date = row[6]
        number = row[7]
        total = row[8]
        discount = row[9]
        final_total = row[10]

        # Session identifier structure:
        # s[x][y] s = service, x = counter (a-z), y = data signifier
        # y is (n)ame, (h)ours, (d)ate, (c)ost, (p)rice

        s1 = '1'
        s2 = '2'
        s3 = '3'
        s4 = '4'
        s5 = '5'

        s1n = row[11]
        s1h = row[12]
        s1c = row[13]
        s1p = row[14]
        s1d = row[15]

        try:
            s2n = row[16]
            s2h = row[17]
            s2c = row[18]
            s2p = row[19]
            s2d = row[20]
        except IndexError:
            s2n = ''
            s2h = ''
            s2c = ''
            s2p = ''
            s2d = ''

        try:
            s3n = row[21]
            s3h = row[22]
            s3c = row[23]
            s3p = row[24]
            s3d = row[25]
        except IndexError:
            s3n = ''
            s3h = ''
            s3c = ''
            s3p = ''
            s3d = ''

        try:
            s4n = row[26]
            s4h = row[27]
            s4c = row[28]
            s4p = row[29]
            s4d = row[30]
        except IndexError:
            s4n = ''
            s4h = ''
            s4c = ''
            s4p = ''
            s4d = ''

        try:
            s5n = row[31]
            s5h = row[32]
            s5c = row[33]
            s5p = row[34]
            s5d = row[35]
        except IndexError:
            s5n = ''
            s5h = ''
            s5c = ''
            s5p = ''
            s5d = ''

        pdf_name = number + ".pdf"
        save_file = os.path.join(os.path.expanduser("~"), "Desktop/", pdf_name)
        generate_pdf(name, street, city, country, zip_code, phone, date,
                     number, total, discount, final_total, save_file, s1, s1n,
                     s1c, s1h, s1p, s1d, s2, s2n, s2c, s2h, s2p, s2d, s3, s3n,
                     s3c, s3h, s3p, s3d, s4, s4n, s4c, s4h, s4p, s4d, s5, s5n,
                     s5c, s5h, s5p, s5d)


def generate_pdf(name, street, city, country, zip_code, phone, date, number,
                 total, discount, final_total, complete_name, s1, s1n, s1c,
                 s1h, s1p, s1d, s2, s2n, s2c, s2h, s2p, s2d, s3, s3n, s3c,
                 s3h, s3p, s3d, s4, s4n, s4c, s4h, s4p, s4d, s5, s5n, s5c,
                 s5h, s5p, s5d):

    c = canvas.Canvas(complete_name, pagesize=letter)

    background_img = 'invoice_template.jpg'
    c.translate(0, 0)
    c.scale(0.234, 0.234)
    c.drawImage(background_img, 0, 100, width=2500, height=3150)

    # bill to
    c.setFont("Helvetica", 40, leading=None)
    c.drawString(150, 2300, name)
    c.drawString(150, 2250, street)
    c.drawString(150, 2200, city)
    c.drawString(150, 2150, country)
    c.drawString(150, 2100, zip_code)
    c.drawString(150, 2050, phone)

    # invoice info
    c.setFont("Helvetica", 50, leading=None)
    c.drawString(2320, 2375, number)
    c.drawString(2210, 2315, date)

    # invoicable stuf
    c.setFont("Helvetica", 40, leading=None)
    c.drawString(180, 1750, s1)
    c.drawString(350, 1750, s1n)
    c.drawString(1350, 1750, s1d)
    c.drawString(1720, 1750, s1p)
    c.drawString(1950, 1750, s1h)
    c.drawString(2250, 1750, s1c)

    if s2n != '':
        c.drawString(180, 1690, s2)
        c.drawString(350, 1690, s2n)
        c.drawString(1350, 1690, s2d)
        c.drawString(1720, 1690, s2p)
        c.drawString(1950, 1690, s2h)
        c.drawString(2250, 1690, s2c)

    if s3n != '':
        c.drawString(180, 1630, s3)
        c.drawString(350, 1630, s3n)
        c.drawString(1350, 1630, s3d)
        c.drawString(1720, 1630, s3p)
        c.drawString(1950, 1630, s3h)
        c.drawString(2250, 1630, s3c)

    if s4n != '':
        c.drawString(180, 1570, s4)
        c.drawString(350, 1570, s4n)
        c.drawString(1350, 1570, s4d)
        c.drawString(1720, 1570, s4p)
        c.drawString(1950, 1570, s4h)
        c.drawString(2250, 1570, s4c)

    if s5n != '':
        c.drawString(180, 1510, s5)
        c.drawString(350, 1510, s5n)
        c.drawString(1350, 1510, s5d)
        c.drawString(1720, 1510, s5p)
        c.drawString(1950, 1510, s5h)
        c.drawString(2250, 1510, s5c)

    # totals
    c.setFont("Helvetica", 40, leading=None)
    c.drawString(2250, 1020, total)
    c.drawString(2250, 970, discount)
    c.setFont("Helvetica", 54, leading=None)
    c.drawString(2230, 830, final_total)

    c.showPage()
    c.save()


def make_invoice(data_file="fr_csv_data.csv"):
    import_data(data_file)
    menu_main.invoice_menu()
