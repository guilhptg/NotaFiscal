# 📄 Leitor de Notas Fiscais Eletrônicas (NF-e) em XML

Este projeto oferece um script Python robusto para leitura e extração de informações essenciais de múltiplos arquivos XML de **Notas Fiscais Eletrônicas**. Ideal para automatizar processos contábeis e integrar dados fiscais a sistemas de gestão.

---

## 🚀 Funcionalidades

- Lê todos os arquivos `.xml` de uma pasta.
- Converte XML para dicionário usando `xmltodict`.
- Extrai:
  - Valor total da nota
  - CNPJ e nome do emitente
  - Nome fantasia da empresa
  - CPF do destinatário
  - Lista de produtos e valores
- Tratamento de erros durante o parsing.

---

## 🛠️ Tecnologias

- **Python 3.x**
- **xmltodict** – Biblioteca de parsing de XML.

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## 🧾 Exemplo de Saída

📄 Nota: DANFEBrota.xml
Empresa: Empresa Exemplo LTDA (12345678000199)
Cliente (CPF): 98765432100
Valor Total: R$ 150.00
Produtos:
  - Produto A: R$ 50.00
  - Produto B: R$ 100.00

---

## 📂 Estrutura de Pastas

```nginx
NFs Finais/
├── DANFEBrota.xml
├── NF001.xml
└── ...
```

---


## ✅ Como Usar
1. Coloque todos os arquivos XML na pasta NFs Finais.

2. Execute o script:

```bash
python leitor_nfe.py
```