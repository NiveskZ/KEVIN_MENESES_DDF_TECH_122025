# Case Técnico: Engenharia de Dados Jr - Dadosfera

**Candidato:** Kevin Richardson dos Santos Meneses

**Projeto:** Plataforma de Dados para Varejo 

---
## Sobre o Projeto
Este projeto simula a estruturação da área de dados de um comércio local ("Adega e Conveniência") que está iniciando sua transformação digital. O objetivo foi criar uma **Plataforma de Dados Moderna**, partindo da geração de dados brutos até a entrega de dashboards analíticos, garantindo governança, qualidade e padronização.

<div align="center">
    
### 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-ETL-150458)
![SQL](https://img.shields.io/badge/PostgreSQL-Supabase-336791)
![Dadosfera](https://img.shields.io/badge/Platform-Dadosfera-orange)
![Data Quality](https://img.shields.io/badge/Data_Quality-Great_Expectations-EF476F)
![Metabase](https://img.shields.io/badge/BI-Metabase-509EE3)

</div>

---

## 🔗 Ativos e Conexões (Links Rápidos)

| Camada | Tipo de Ativo | Link de Acesso na Dadosfera |
| :--- | :--- | :--- |
| **Ingestão** | Conexão PostgreSQL (Supabase) | [Acessar Conexão](https://app.dadosfera.ai/en-US/collect/connections/1767222609772_7i01rd4w_postgresql-1.0.0) |
| **Bronze** | Pipeline de Carga (RAW) | [Visualizar Pipeline Bronze](https://app.dadosfera.ai/en-US/collect/pipelines/50c7fc54-bd81-4c51-9991-7342aae898b1) |
| **Silver** | Pipeline de Transformação (CDM) | [Visualizar Pipeline Silver](https://app.dadosfera.ai/en-US/collect/pipelines/e34fac1c-7a56-430f-a370-9a44dffac9fd) |
| **BI** | Dashboard Público (Metabase) | [Abrir Dashboard Externo](http://metabase-treinamentos.dadosfera.ai/public/dashboard/2d9f8081-d542-44c6-8f42-e59d7c056b10) |

---

## 📋 Item 0: Planejamento (Agile & PMBOK)

Este projeto visa estruturar a área de dados de um comércio local (Adega e Conveniência) que está iniciando sua transformação digital. O objetivo é centralizar dados de vendas, clientes e estoque para permitir análises descritivas e prescritivas.

O planejamento abaixo segue as fases do ciclo de vida de dados e gerenciamento de projetos, focado na entrega de valor (MVP).

### Fluxo de Trabalho (Macro)

```mermaid
flowchart LR
    A[Iniciação & Planejamento] --> B(Geração de Dados Sintéticos)
    B --> C{Ingestão de Dados}
    C --> |Dadosfera: Coleta| D[Pipeline de Dados]
    D --> |Dadosfera: Exploração| E[Qualidade & Catalogação]
    E --> F[Análise & Visualização]
    F --> G[Entrega Final & Vídeo]

    %% Estilização Profissional e Minimalista
    style C fill:#2c3e50,stroke:#2c3e50,color:#fff
    style G fill:#27ae60,stroke:#27ae60,color:#fff
```
### Backlog de Atividades
FASE 1: Concepção e Dados (Item 1)

   - [x] Definição do Cenário de Negócio (Adega/Varejo).

   - [x] Criação do Script Python para geração de dados sintéticos (+100k registros).

   - [x] Validação da consistência dos dados (Vendas, Produtos, Clientes).

FASE 2: Integração e Exploração (Items 2 e 3)

  - [x] Integração: Carga dos arquivos CSV no módulo de Coleta da Dadosfera.

  - [x] Catalogação: Criação do Dicionário de Dados e organização nas camadas (Bronze/Silver).

  - [x] Exploração: Análise inicial dos tipos de dados e volumetria.

FASE 3: Qualidade de Dados (Item 4)

  - [x] Implementação de checagem de qualidade (Great Expectations ou Soda).

  - [x] Geração de relatório de inconsistências (ex: valores nulos, duplicatas).

FASE 4: Análise e Valor (Item 7)

  - [x] Criação do Dataset de Visualização.

  - [x] Desenvolvimento do Dashboard (Metabase/Dadosfera).

  - [x] Análise de Categorias.

  - [x] Análise de Série Temporal (Sazonalidade).

  - [x] Resposta a 5 perguntas de negócio estratégicas.

FASE 5: Entrega (Item 10)

  - [ ] Gravação do vídeo de apresentação da solução.

  - [ ] Documentação final e organização do repositório.

## Item 1: Geração de Dados 
Para simular um cenário real de varejo, foi desenvolvido um script Python utilizando a biblioteca Faker e Numpy.

- Volumetria: +115.000 registros de vendas (histórico de 5 anos).

- Lógica de Negócio:

   - Sazonalidade: Picos de vendas aos finais de semana e feriados.

   - Pesos de Probabilidade: Produtos populares (Cervejas Pilsen) vendem mais que produtos de nicho (Artesanais).

   - Cohorts: Base de clientes com datas de cadastro distribuídas ao longo de 11 anos.

- Artifacts: `vendas.csv`, `clientes.csv`, `produtos.csv`
## Item 2 & 3: Integração e Catalogação

A ingestão dos dados foi realizada conectando um banco transacional PostgreSQL (Supabase) à Dadosfera.
Estratégia de Catálogo (Via API)

Como diferencial, a catalogação não foi feita apenas manualmente. Foi desenvolvido um script Python que interage com a API da Dadosfera para:

1. Autenticar via Token.
2. Atualizar descrições técnicas e de negócio.
3. Aplicar tags (landing, varejo, sintético) automaticamente.

Ativos de Coleta e Ingestão

- Conexão PostgreSQL (Supabase): [Link para Conexão](https://app.dadosfera.ai/en-US/collect/connections/1767222609772_7i01rd4w_postgresql-1.0.0)

- Pipeline Camada Bronze (Arquivos RAW): [Link para Pipeline](https://app.dadosfera.ai/en-US/collect/pipelines/50c7fc54-bd81-4c51-9991-7342aae898b1)

Assets Acessíveis pela Camada Bronze

- PUBLIC.VAREJO | DIMENSÃO CLIENTE: [Acessar Asset](https://app.dadosfera.ai/en-US/catalog/data-assets/4eef3148-79a4-473e-8f5a-060810b55883)

- PUBLIC.VAREJO | DIMENSÃO PRODUTOS: [Acessar Asset](https://app.dadosfera.ai/en-US/catalog/data-assets/9cb82842-75af-4ec1-8f5c-0a18f677a419)

- PUBLIC.VAREJO | FATO VENDAS (5 ANOS): [Acessar Asset](https://app.dadosfera.ai/en-US/catalog/data-assets/7c448aae-d76d-4ef3-a29d-a5a2e6da9be3)

## Item 4: Data Quality (Great Expectations)
Antes de disponibilizar os dados para análise, foi implementada uma camada de validação usando a biblioteca Great Expectations.

Principais Regras Validadas:

- ✅ **Unicidade**: id_cliente, id_venda e id_produto não podem ter duplicatas.

- ✅ **Completude**: Não são permitidos valores nulos em campos chaves (nome, categoria).

- ✅ **Consistência**: valor_total deve ser maior que 0.

- ✅ **Formato**: Validação de Regex para e-mails válidos.

    **Resultado**: O dataset atingiu 100% de conformidade com as regras estabelecidas na *Expectation Suite*.

## Item 6: Arquitetura e Modelagem (Silver Layer)

Adotou-se a arquitetura **Medallion (Bronze/Silver/Gold)** com separação lógica por Schemas no banco de dados para garantir organização e segurança.

Ativos de Transformação (Silver Layer)

- Pipeline Camada Silver (CDM): [Link para Pipeline Silver](https://app.dadosfera.ai/en-US/collect/pipelines/e34fac1c-7a56-430f-a370-9a44dffac9fd)

Assets Acessíveis pela Camada Silver (CDM)

- PUBLIC.VAREJO | SILVER | CONTACT (CDM): [Acessar Asset](https://app.dadosfera.ai/en-US/catalog/data-assets/fbee5296-3b46-41ff-8bbb-a2d0b290aa00)

- PUBLIC.VAREJO | SILVER | PRODUCT (CDM): [Acessar Asset](https://app.dadosfera.ai/en-US/catalog/data-assets/4e6abcaa-2d04-497d-922e-ea15b004e5b9)

- PUBLIC.VAREJO | SILVER | SALES ORDER (CDM):[Acessar Asset](https://app.dadosfera.ai/en-US/catalog/data-assets/dd63cab5-8627-410d-a3dc-c9a37a29a2bc)

### Common Data Model (CDM)
Os dados foram mapeados para o padrão CDM para garantir interoperabilidade.

<details> <summary>🔻 Clique para ver o Mapeamento CDM</summary>
    
| Tabela Local | Entidade CDM | Atributo Local | Atributo CDM | Justificativa (Alinhamento CDM) | Tipo CDM Esperado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **clientes** | **Contact** | `id_cliente` | `ContactNumber` | Identificador único de negócio do cliente no sistema de origem. | String |
| | | `nome` | `FullName` | Nome completo do contato, conforme padrão da entidade Contact. | String |
| | | `email` | `EmailAddress` | Endereço de e-mail primário para comunicação. | String |
| | | `cidade` | `AddressCity` | Município da localização do cliente. | String |
| | | `bairro` | `AddressDistrict` | Bairro ou distrito do endereço. | String |
| | | `data_cadastro` | `CreatedOn` | Data e hora de registro do cliente no sistema. | DateTime |
| **produtos** | **Product** | `id_produto` | `ProductNumber` | Código único (SKU) do produto para identificação de negócio. | String |
| | | `nome` | `ProductName` | Nome comercial ou descrição do produto. | String |
| | | `cat` | `ProductCategory` | Categoria funcional para agrupamento e análise. | String |
| | | `preco` | `DefaultPrice` | Preço de venda padrão do produto. | Decimal (Currency) |
| | | `custo` | `StandardCost` | Custo unitário padrão para formação de preço. | Decimal (Currency) |
| | | `peso` | `Weight` | Peso físico do produto para logística. | Decimal |
| **vendas** | **SalesOrder** | `id_venda` | `SalesOrderNumber` | Número único identificador da transação comercial. | String |
| | | `data_venda` + `hora_venda` | `OrderDate` | Data e hora completa da realização do pedido. | DateTime |
| | | `id_cliente` | `CustomerId` | Referência à chave primária da entidade Contact (cliente). | Guid (FK) |
| | | `id_produto` | `ProductId` | Referência à chave primária da entidade Product (produto). | Guid (FK) |
| | | `quantidade` | `Quantity` | Quantidade de unidades vendidas na linha do pedido. | Decimal |
| | | `valor_unitario` | `UnitPrice` | Preço unitário praticado na transação específica. | Decimal (Currency) |
| | | `valor_total` | `TotalAmount` | Valor total da linha (quantidade × preço unitário). | Decimal (Currency) |

</details>

### Estratégia de Materialização (View vs Table)
Inicialmente planejado com Views, optou-se por Materializar a Camada Silver (CREATE TABLE AS) em um schema dedicado (silver).

Motivos da Decisão Técnica:

 - Performance: Criação de Índices e Primary Keys físicas para otimizar consultas no Metabase.

 - Integração: Garantia de visibilidade total pelo conector de pipeline da Dadosfera (que prioriza tabelas físicas).

 - Governança: Separação clara entre dados brutos (public) e dados curados (silver)
```mermaid
graph TD
    subgraph Bronze [Supabase: Schema Public]
        B1[(vendas)]
        B2[(clientes)]
        B3[(produtos)]
    end

    subgraph Pipeline [Dadosfera Pipeline]
        P1{Ingestão & <br>Materialização}
    end

    subgraph Silver [Supabase: Schema Silver]
        S1[Table: cdm_sales_order]
        S2[Table: cdm_contact]
        S3[Table: cdm_product]
    end

    subgraph Gold [Metabase]
        G1[Dashboards Analíticos]
    end

    B1 & B2 & B3 --> P1
    P1 --> S1
    P1 --> S2
    P1 --> S3
    S1 --> G1
    S2 -.-> G1
    S3 -.-> G1
```

## Item 7: Visualização e Geração de Valor (Analytics)

A etapa final consistiu na criação de um ecossistema analítico no **Metabase (integrado à Dadosfera)**, onde os dados processados na camada Silver foram transformados em insights de negócio.

### Dashboard Interativo
O dashboard completo pode ser acessado publicamente através do link abaixo:
[Dashboard de Performance - Adega Local](http://metabase-treinamentos.dadosfera.ai/public/dashboard/2d9f8081-d542-44c6-8f42-e59d7c056b10)

![Dashboard](https://github.com/NiveskZ/KEVIN_MENESES_DDF_TECH_122025/blob/main/imgs/Dashboard.png)
---

### Questões de Negócio e Visualizações

Para atender aos requisitos do case, foram criadas **7 visualizações** utilizando diferentes tipos de gráficos para responder a perguntas estratégicas:

1. **Faturamento Total Histórico**
   - **Tipo:** Número (Big Number)
   - **Objetivo:** Visão macro do faturamento acumulado nos últimos 5 anos de operação.

2. **Perfil do Cliente VIP (Top Spender)**
   - **Tipo:** Detalhe 
   - **Pergunta:** Qual cliente possui o maior LTV (Life Time Value)?
   - **Insight:** Exibe o nome do cliente, quantidade de pedidos e total investido na loja.

3. **Performance Diária (Ticket Médio)**
   - **Tipo:** Tendência (Smart Number)
   - **Diferencial Técnico:** Utilização de SQL com a função `LAG()` para comparar o ticket médio do último dia de vendas com o dia anterior, ignorando lacunas temporais.

4. **Ranking de Faturamento por Categoria**
   - **Tipo:** Barras Horizontais
   - **Insight:** Identificação clara de que a categoria "Cerveja Comum" detém a maior fatia do faturamento bruto por volume.

5. **Evolução Mensal de Vendas (Série Temporal)**
   - **Tipo:** Gráfico de Linhas
   - **Objetivo:** Identificar sazonalidade e tendências de crescimento ao longo dos meses.

6. **Análise de Mix: Lucro vs Faturamento por Categoria**
   - **Tipo:** Gráfico Combo (Barras + Linhas)
   - **Métricas:** Lucro Total e Faturamento (Barras) e Margem Percentual (Linha).
   - **Insight:** Demonstra visualmente quais categorias possuem maior margem, apesar de faturarem menos.

7. **Share de Lucratividade: Artesanal vs Comum**
   - **Tipo:** Gráfico de Rosca (Donut)
   - **Pergunta:** Qual categoria é mais importante para a margem líquida?
   - **Conclusão:** Revela que as Cervejas Artesanais possuem uma participação no lucro muito superior à sua participação no faturamento bruto.

---

### Queries SQL e Evidências
As queries utilizadas para gerar os insights acima foram desenvolvidas em **Snowflake SQL** na própria plataforma da metabase, também estão disponíveis na pasta `/queries` deste repositório.

> Conforme as boas práticas da Dadosfera, todos os ativos foram salvos na coleção exclusiva: `Kevin Meneses - 012026`.
