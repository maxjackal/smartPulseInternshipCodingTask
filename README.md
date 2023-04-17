def excel_tablo(data):
    wb = openpyxl.Workbook()
    ws = wb.active

    ws['A1'] = 'Tarih'
    ws['B1'] = 'Toplam İşlem Miktarı(MWh)'
    ws['C1'] = 'Toplam İşlem Tutar(TL)'
    ws['D1'] = 'Ağırlıklı Ortalama Fiyat(TL/MWh)'

    ws.column_dimensions['A'].width = 16
    ws.column_dimensions['B'].width = 23
    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['D'].width = 27

    for i in data:
        ws.append([data[i]['date'],
                   f"{round(data[i]['Toplam İşlem Miktarı'],2):,}",
                   f"{round(data[i]['Toplam İşlem Tutar'], 2):,} ₺",
                   f"{round(data[i]['Ağırlıklı Ortalama Fiyat'],2):,}"]
                  )

    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(horizontal='right')

    wb.save('veriler.xlsx')

burada excel tablolarımı olusturdum 
df=pd.read_excel('veriler.xslx') 
ile excel tablosu olusturmaya çalıştım fakat hata aldım
