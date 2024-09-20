import xmltodict

# Com esse codigo de 2 linhas você consegue um dicionário com todos os dados que quiser e como adicionar mais
with open('NFs Finais/DANFEBrota.xml', 'rb') as arquivo:
    documento = xmltodict.parse(arquivo)

# Acessar caminho da arvore de um dicionário
for item in documento:
    print(item, '-\n')

for item in documento['nfeProc']:
    print(item)

for item in documento['nfeProc']['protNFe']:
    print(item, '-\n')

for item in documento['nfeProc']['NFe']['infNFe']['emit']:
    print(item)

dic_notafiscal = documento['nfeProc']['NFe']['infNFe']
print(dic_notafiscal)

valor_total = dic_notafiscal['total']['ICMSTot']['vNF']
print(valor_total)


# CNPJ e outras variáveis para objetificar os dados  - confere com o PDF
cnjp_vendeu = dic_notafiscal['emit']['CNPJ']
nome_vendeu = dic_notafiscal['emit']['xNome']
cpf_comprou = dic_notafiscal['dest']['CPF']
empresa = dic_notafiscal['emit']['xFant']


produtos = dic_notafiscal['det']


lista_produtos = []
for produto in produtos:
    valor_produto = produto['prod']['vProd']
    nome_produto = produto['prod']['xProd']
    lista_produtos.append((nome_produto, valor_produto))
    print(valor_produto, nome_produto)




# Até chegar no arquivo que sejar
print(documento['nfeProc']['NFe']['infNFe']['ide']['cUF'])

# valor total, produtos ou serviço, cnpj_vendeu, cpf/cnpj_comprou, nome_comprou - producurar no XML

resposta = {'valor_total': valor_total,
            'cnjp_vendeu': cnjp_vendeu,
            'nome_vendeu': nome_vendeu, 
            'empresa': empresa, 
            'cpf_comprou': cpf_comprou,
            'lista_produtos': lista_produtos}
            
print(resposta)