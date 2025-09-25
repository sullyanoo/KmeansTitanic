# 🚢 Clusterização com K-Means - Titanic

Este projeto utiliza a técnica de **clusterização com K-Means**, um método de **aprendizado de máquina não supervisionado**, para identificar perfis de passageiros no famoso conjunto de dados do **Titanic**. A análise é feita com base nas variáveis:

- 🎟️ Classe da passagem (`Pclass`)
- 👤 Idade dos passageiros (`Age`)
- 💰 Tarifa paga (`Fare`)

---

## 📊 Objetivos

- Aplicar o algoritmo **K-Means** para segmentar os dados em grupos (clusters)
- Analisar padrões ocultos nos dados, sem usar rótulos de saída (como sobrevivência)
- Compreender como variáveis socioeconômicas influenciam nos agrupamentos

---

## 🧠 Etapas do projeto

1. **Pré-processamento dos dados**  
   - Seleção de variáveis relevantes: Classe, Idade, Tarifa  
   - Tratamento de valores ausentes com a mediana  
   - Normalização dos dados com `StandardScaler`

2. **Determinação do número ideal de clusters (k)**  
   - Aplicação do **método do cotovelo**, com base na inércia (distância interna dos grupos)

3. **Aplicação do algoritmo K-Means**  
   - Clusterização dos dados em 3 grupos (`k = 3`)

4. **Análise dos clusters**  
   - Cálculo da média de cada variável por cluster
   - Renomeação das colunas para melhor visualização (Classe Média, Idade Média, Tarifa Média)

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- Bibliotecas:
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `matplotlib`



