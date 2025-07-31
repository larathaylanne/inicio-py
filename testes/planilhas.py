from openpyxl import load_workbook, Workbook

#ler os dados da planilha

planilha_country = load_workbook('Country AUTOMACAO.xlsx')
pagina_principal = planilha_country['Cereais']

for linha in pagina_principal.iter_rows(values_only=True):
    print(linha)

#AUTOMATIZAR PLANILHA 
#inserir dados
planilha_respondida = Workbook()
cereais = planilha_country.active

with open ('precos-country.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        cereais.append(linha.split('    '))
planilha_country.save('preenchendo_planilha.xlsx')