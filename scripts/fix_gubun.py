import openpyxl, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

wb = openpyxl.load_workbook('D:/soojin/wiki/nm-reference/research_metadata.xlsx')
ws = wb.worksheets[0]

updated = 0
for row in ws.iter_rows(min_row=2):
    src = row[0].value
    gubun = row[29].value  # 구분 col30
    if src in ('KCI', 'OpenAlex') and not gubun:
        row[29].value = '검증필요'
        updated += 1
        title = str(row[1].value or '')[:50]
        print(f'  행{row[0].row}: [{src}] {title}')

wb.save('D:/soojin/wiki/nm-reference/research_metadata.xlsx')
print(f'\n완료: {updated}건 업데이트')
