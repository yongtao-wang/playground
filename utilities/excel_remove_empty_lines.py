import openpyxl


def remove_empty_lines(workbook_path):
    workbook = openpyxl.load_workbook(workbook_path)

    sheet = workbook.active
    output = workbook.create_sheet('remove_empty')

    for row in sheet.rows:
        if row[0].value:
            output.append([c.value for c in row])

    workbook.save(workbook_path)
