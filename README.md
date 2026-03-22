# 🛒 Análise de Vendas - Projeto Interativo

Projeto de análise de dados de vendas utilizando Python, Pandas e SQL (DuckDB), com desenvolvimento de dashboard interativo em Streamlit para exploração de métricas comerciais.

---

## 🎯 Objetivo

Analisar o desempenho de vendas, permitindo:  

- Monitoramento de faturamento por período  
- Identificação de produtos mais vendidos  
- Comparação entre regiões, lojas ou categorias  
- Análise de tendências e sazonalidade  

---

## 🛠️ Tecnologias

- Python  
- Pandas  
- DuckDB (SQL para análise eficiente em CSVs)  
- Streamlit (dashboard interativo)  
- Matplotlib / Seaborn (visualizações gráficas)  

---

## 📚 Funcionalidades

- Importação de dados a partir de arquivos CSV  
- Limpeza e transformação automática dos dados  
- Dashboard interativo com filtros por:  
  - período  
  - loja / região  
  - categoria de produto  
- Métricas principais:  
  - faturamento total  
  - quantidade vendida  
  - ticket médio  
  - produtos mais vendidos  
- Visualizações de tendências ao longo do tempo  
- Exportação de relatórios filtrados em CSV  

---

## 📈 Principais Métricas

- Faturamento total por período  
- Ticket médio por loja ou categoria  
- Produtos mais vendidos e menos vendidos  
- Comparação de vendas entre períodos ou regiões  
- Evolução de vendas ao longo do tempo  

---

## 💡 Insights Possíveis

- Identificação de sazonalidade em produtos específicos  
- Lojas ou regiões com maior desempenho  
- Produtos com baixa rotatividade que podem ser reavaliados  
- Tendências de aumento ou queda em categorias  

---

## ⚠️ Limitações dos Dados

- Depende da qualidade do CSV importado (valores nulos ou incorretos podem afetar métricas)  
- Análise limitada aos campos presentes no arquivo  
- Não há integração automática com sistemas ERP  

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/GabrielLimaUERJ/Vendas-SQL-Independente.git
cd Vendas-SQL-Independente
pip install -r requirements.txt
streamlit run app.py
