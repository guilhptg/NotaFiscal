import os
import xmltodict

def extrair_dados_nfe(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'rb') as arquivo:
            documento = xmltodict.parse(arquivo)

        infNFe = documento['nfeProc']['NFe']['infNFe']
        emitente = infNFe['emit']
        destinatario = infNFe.get('dest', {})
        produtos = infNFe['det']

        lista_produtos = []
        for item in produtos:
            prod = item['prod']
            lista_produtos.append({
                'nome': prod['xProd'],
                'valor': prod['vProd']
            })

        return {
            'arquivo': os.path.basename(caminho_arquivo),
            'valor_total': infNFe['total']['ICMSTot']['vNF'],
            'cnpj_emitente': emitente.get('CNPJ'),
            'nome_emitente': emitente.get('xNome'),
            'empresa_fantasia': emitente.get('xFant'),
            'cpf_destinatario': destinatario.get('CPF'),
            'produtos': lista_produtos
        }

    except Exception as e:
        print(f"Erro ao processar {caminho_arquivo}: {e}")
        return None


def processar_pasta(pasta):
    resultados = []
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.xml'):
            caminho = os.path.join(pasta, arquivo)
            dados = extrair_dados_nfe(caminho)
            if dados:
                resultados.append(dados)
    return resultados


if __name__ == "__main__":
    pasta_xml = "NFs Finais"
    notas = processar_pasta(pasta_xml)
    
    for nota in notas:
        print(f"\n📄 Nota: {nota['arquivo']}")
        print(f"Empresa: {nota['nome_emitente']} ({nota['cnpj_emitente']})")
        print(f"Cliente (CPF): {nota['cpf_destinatario']}")
        print(f"Valor Total: R$ {nota['valor_total']}")
        print("Produtos:")
        for p in nota['produtos']:
            print(f"  - {p['nome']}: R$ {p['valor']}")
