import openpyxl

#carregando o arquivo
book = openpyxl.load_workbook('testão.xlsx')

#selecionando uma página
teste_page = book['teste']

#imprimindo os dados de cada linha
for rows in teste_page.iter_rows(min_row=2, max_row=4):
#    print(f'{rows[0].value},{rows[1].value},{rows[2].value}')
    for cell in rows:
    #    print(cell.value)
        if cell.value == 'um':
            cell.value = 'não é mais um'

#salvar as alterações
book.save('testão v2.xlsx')