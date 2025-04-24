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

