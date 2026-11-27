# Auditoria de licenças e atribuições — 26/11/2026

Projeto: doc-intelligence. Responsável declarado: João Victor da Silva (JustJao1).

Revisão documental dos arquivos acessíveis no GitHub. Preserva os avisos existentes e os direitos de terceiros; não concede nova licença ao código próprio nem certifica conformidade integral. Nenhuma alteração em código executável ou contrato de serviço.

- requirements.txt: pypdf>=5.9,<7 (BSD-3-Clause declarada no aviso), openpyxl>=3.1,<4 (MIT declarada); versões não travadas. Fixar versões e conferir licenças reais e dependências transitivas de cada instalação, inclusive et-xmlfile quando presente.
- public/index.html: Google Fonts Libre Caslon Text e Figtree, e CDN @huggingface/transformers@3.8.1. A licença da biblioteca não cobre automaticamente os pesos de modelos.
- Modelo referenciado: onnx-community/xlm-roberta-base-squad2-distilled-ONNX. Verificar card, licença do modelo original e arquivos ONNX antes de redistribuir ou explorar comercialmente: https://huggingface.co/onnx-community/xlm-roberta-base-squad2-distilled-ONNX .
- Pendência: não foi comprovada a licença individual do modelo nem de todas as dependências resolvidas. Preservar os avisos existentes e não redistribuir pesos sem confirmação.

A tag autoria-2026-11-26 foi consultada na API GitHub: assinatura válida (verified=true, reason=valid), apontando para a versão documentada em EVIDENCIA-2026-11-26.md. A auditoria atual é posterior à versão assinada; seu commit não foi assinado com a chave pessoal do mantenedor.
