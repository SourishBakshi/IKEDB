import dump
import openpyxl
def get_prediction_content():
    dump.dump()
    l=list()

    wb = openpyxl.load_workbook("c:\\Python27\\myproject\\myapp\\MASTER.xlsx")
    first_sheet = wb.get_sheet_names()[0]
    worksheet = wb.get_sheet_by_name(first_sheet)
    for row in range(1, worksheet.max_row + 1):
        for column in "A":
            cell_name = "{}{}".format(column, row)
            text2 = worksheet[cell_name].value
            if text2 is None:
                break
            else:
                l.append(text2)
    return l
