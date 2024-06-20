# Pasta DataScience

Essa pasta visa analisar dados de influenciadores coletados de diferentes plataformas, como Instagram, YouTube e TikTok. Ele é composto por três principais pastas:

## Estrutura do Projeto

- **DataScrap**: Nesta etapa, os dados brutos são extraídos dos seguintes sites:
  - [Top Instagram](https://hypeauditor.com/pt/top-instagram/)
  - [Top YouTube](https://hypeauditor.com/pt/top-youtube/)
  - [Top TikTok](https://hypeauditor.com/pt/top-tiktok/)
  
  Os arquivos JSON contêm informações sobre os 1000 principais influenciadores de cada nicho em 2023. Esses dados brutos são processados para extrair apenas as informações relevantes.

- **DataAnalytics**: Aqui, os dados processados são analisados e visualizados. Alguns passos importantes incluem:
  - Mapeamento dos IDs dos influenciadores para seus respectivos nichos.
  - Criação de gráficos para entender o engajamento e outras métricas.
  - Aplicação de métodos de clusterização, como o gráfico Cotolev e a silhueta, para extrair informações sobre nichos.

- **DataPopulateScripts**: Nesta etapa, scripts são criados para popular o banco de dados. Problemas de CRUD são resolvidos, e os dados são enviados para o banco de dados por meio de uma API, sem a necessidade de scripts SQL.

## Instalação

Para executar este projeto, siga estas etapas:

1. **Python 3.10**: Certifique-se de ter o Python 3.10 instalado. Você pode baixá-lo em [python.org](https://www.python.org/).

2. **Ambiente Virtual (venv)**: Crie um ambiente virtual para isolar as dependências do projeto:
   python -m venv myenv
3. **Ative o Ambiente Virtual**:
- No Windows:
  ```
  myenv\Scripts\activate
  ```
- No macOS e Linux:
  ```
  source myenv/bin/activate
  ```

4. **Instale as Dependências**:
pip install pandas matplotlib scikit-learn
## Executando o Projeto

- Execute os scripts de coleta de dados no diretório `DataScrap`.
- Analise os dados no diretório `DataAnalytics`.
- Popule o banco de dados usando os scripts no diretório `DataPopulateScripts`.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos.

