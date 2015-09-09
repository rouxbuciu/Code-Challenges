import csv

data_file = "hata.csv"


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

        # Session identifier structure:
        # s[x][y] s = service, x = counter (a-z), y = data signifier
        # y is (n)ame, (h)ours, (d)ate, (c)ost, (p)rice

        sa = '1'
        san = row[9]
        sah = row[10]
        sac = row[11]
        sap = row[12]
        sad = row[13]

        if len(row) > 14 and len(row) <= 18:
            sb = '2'
            sbn = row[14]
            sbh = row[15]
            sbc = row[16]
            sbp = row[17]
            sbd = row[18]

        if len(row) > 19 and len(row) <= 24:
            sc = '3'
            scn = row[19]
            sch = row[20]
            scc = row[21]
            scp = row[22]
            scd = row[23]

        if len(row) > 24 and len(row) <= 28:
            sd = '4'
            sdn = row[24]
            sdh = row[25]
            sdc = row[26]
            sdp = row[27]
            sdd = row[28]

        if len(row) > 29 and len(row) <= 33:
            se = '5'
            sen = row[29]
            seh = row[30]
            sec = row[31]
            sep = row[32]
            sed = row[33]

        pdf_file = number + ".pdf"
        generate_certificate(name, street, city, country, zip_code, phone,
                             date, number, total, pdf_file,
                             sa, san, sac, sah, sap, sad,
                             sb, sbn, sbc, sbh, sbp, sbd,
                             sc, scn, scc, sch, scp, scd,
                             sd, sdn, sdc, sdh, sdp, sdd,
                             se, sen, sec, seh, sep, sed)


def generate_certificate(name, street, city, country, zip_code, phone, date,
                         number, total, complete_name,
                         sa, san, sac, sah, sap, sad,
                         sb="", sbn="", sbc="", sbh="", sbp="", sbd="",
                         sc="", scn="", scc="", sch="", scp="", scd="",
                         sd="", sdn="", sdc="", sdh="", sdp="", sdd="",
                         se="", sen="", sec="", seh="", sep="", sed=""):

    # Do my ReportLAB stuff here
    # This part I've got down

import_data(data_file)
