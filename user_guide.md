# Guia do Usuário: Assistente de IA Jurídico

Bem-vindo ao Guia do Usuário do Assistente de IA Jurídico! Esta ferramenta foi desenvolvida para auxiliar profissionais do direito na análise de documentos e na geração de peças jurídicas e minutas de votos, utilizando uma base de conhecimento de códigos legais brasileiros e jurisprudências dos tribunais superiores.

## 1. Visão Geral

O Assistente de IA Jurídico é uma aplicação baseada em Python, projetada para ser executada em ambientes como o Google Colab. Ele permite que você insira um texto (como um processo ou documento), selecione o tipo de documento jurídico que deseja gerar (análise, parecer, voto, etc.) e receba uma saída preliminar com base na análise do texto e nas informações relevantes da base de conhecimento.

## 2. Requisitos do Sistema

Para utilizar o assistente, você precisará de:

*   Acesso ao Google Colab (recomendado) ou um ambiente Python com as bibliotecas necessárias instaladas.
*   Conexão com a internet (para download de bibliotecas e, futuramente, para integração com APIs de jurisprudência).

## 3. Como Começar no Google Colab

Siga os passos abaixo para configurar e executar o assistente no Google Colab:

### 3.1. Upload dos Arquivos

Faça o upload dos seguintes arquivos Python para o seu ambiente Google Colab:

*   `knowledge_base_setup.py`
*   `legal_analysis_engine.py`
*   `app.py`
*   `api_integration.py` (este módulo é para futuras integrações e não afeta a funcionalidade principal no momento)
*   `test_legal_assistant.py` (para executar os testes, opcional)

### 3.2. Configuração da Base de Conhecimento

Primeiro, você precisa configurar a base de dados que contém os códigos legais e as jurisprudências. No Google Colab, abra uma nova célula de código e execute o seguinte comando:

```python
%run knowledge_base_setup.py
```

Este comando criará um arquivo de banco de dados chamado `legal_knowledge_base.db` no seu ambiente Colab e o preencherá com alguns dados de exemplo. Você verá a mensagem `Base de conhecimento jurídica configurada e dados de exemplo inseridos.` após a execução bem-sucedida.

### 3.3. Iniciando a Interface do Assistente

Após configurar a base de conhecimento, você pode iniciar a interface do usuário do assistente. Em uma nova célula de código no Google Colab, execute:

```python
from app import run_legal_assistant
run_legal_assistant()
```

Isso exibirá a interface do assistente diretamente no seu notebook Colab.

## 4. Utilizando o Assistente

A interface do assistente é composta por:

*   **Área de Texto (`Texto:`):** Aqui você deve digitar ou colar o texto do processo, documento ou qualquer conteúdo jurídico que deseja que o assistente analise. Quanto mais detalhado o texto, melhor a análise preliminar.
*   **Dropdown (`Tipo de Documento:`):** Selecione o tipo de documento jurídico que você deseja que o assistente gere. As opções incluem: `Análise Jurídica`, `Parecer Jurídico`, `Minuta de Voto`, `Petição Inicial` e `Contestação`.
*   **Botão `Analisar`:** Clique neste botão para iniciar o processo de análise e geração do documento.
*   **Área de Saída (`Resultado:`):** O resultado da análise e o rascunho do documento gerado aparecerão nesta área.

### Exemplo de Uso:

1.  Na **Área de Texto**, digite algo como:
    "Preciso de uma análise sobre um caso de responsabilidade civil, considerando o Código Civil e jurisprudência do STJ. O réu causou danos morais à vítima por negligência."
2.  No **Dropdown `Tipo de Documento:`**, selecione `Parecer Jurídico`.
3.  Clique no botão `Analisar`.

O assistente processará o texto, buscará referências relevantes na base de conhecimento (como o Art. 186 do Código Civil e jurisprudências do STJ sobre responsabilidade civil) e gerará um rascunho de parecer jurídico na área de saída.

## 5. Solução de Problemas e Correções

*   **`RecursionError` durante testes ou inicialização:** Este erro foi corrigido na versão atual. Ele ocorria devido a um problema na forma como as conexões com o banco de dados SQLite eram gerenciadas durante os testes. A correção garante que as funções de banco de dados se conectem corretamente sem entrar em recursão infinita.
*   **Análise de Texto Incompleta:** A lógica de análise de texto no `legal_analysis_engine.py` foi aprimorada para incluir a palavra "código" na busca por referências a leis, tornando a identificação mais robusta.
*   **"Por favor, insira um texto para análise."**: Certifique-se de que a área de texto não está vazia antes de clicar em "Analisar".
*   **Erros de Conexão com o Banco de Dados**: Verifique se você executou `%run knowledge_base_setup.py` antes de iniciar a interface. O arquivo `legal_knowledge_base.db` deve existir.
*   **Resultados Inesperados**: Lembre-se que a análise atual é básica. Para resultados mais precisos, o texto de entrada deve ser claro e conter termos que o assistente possa identificar com as regras atuais.

## 6. Limitações Atuais e Próximos Passos

É importante notar que esta é uma versão inicial do assistente. As principais limitações e áreas para desenvolvimento futuro incluem:

*   **Análise de Texto:** Atualmente, a análise de texto é baseada em regras simples e busca por palavras-chave. Futuramente, serão integrados modelos de Processamento de Linguagem Natural (PLN) mais avançados para uma compreensão contextual mais profunda e extração de entidades nomeadas (NER).
*   **Geração de Documentos:** A geração de texto é um rascunho formatado. Para documentos mais sofisticados e juridicamente precisos, serão utilizados Modelos de Linguagem Grandes (LLMs) treinados especificamente para o domínio jurídico.
*   **Base de Conhecimento:** A base de dados de exemplo é limitada. A expansão para incluir todos os códigos legais e uma vasta coleção de jurisprudências é um próximo passo crucial, possivelmente com mecanismos de atualização automatizados.
*   **Integração com APIs:** A integração com APIs de jurisprudência é um recurso futuro que permitirá a atualização dinâmica da base de dados. Atualmente, não há APIs públicas diretas para este fim, e alternativas como web scraping (com devida atenção aos termos de uso) ou parcerias seriam necessárias.

Esperamos que este assistente seja uma ferramenta útil em seu trabalho! Para dúvidas ou sugestões, entre em contato com o desenvolvedor.

**Autor:** NICKEVANNS
**Data:** 8 de agosto de 2025


