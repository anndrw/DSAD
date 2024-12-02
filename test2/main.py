import pandas as pd
import numpy as np

# Citirea fișierelor
etnicity_data = pd.read_csv('Ethnicity.csv')
codes_data = pd.read_excel('CoduriRomania.xlsx')

# Asigurarea că denumirile coloanelor nu au spații inutile
etnicity_data.columns = etnicity_data.columns.str.strip()
codes_data.columns = codes_data.columns.str.strip()

# Unirea datelor după localitate
merged_data = pd.merge(etnicity_data, codes_data, left_on='City', right_on='City')

# Calcularea populației totale pentru fiecare localitate
etnii = [col for col in merged_data.columns if col not in ['City', 'County', 'Code_x', 'Code_y']]
merged_data['total_populatie'] = merged_data[etnii].sum(axis=1)

# Cerința 1: Calcularea populației pe etnii la nivel de județe, regiuni și macroregiuni
levels = ['County', 'County']  # Grupare după județ

for level in levels:
    grouped = merged_data.groupby(level).sum(numeric_only=True)
    grouped.to_csv(f'Populatie_pe_etnii_{level}.csv')
    print(f"Fișierul Populatie_pe_etnii_{level}.csv a fost generat cu succes.")

# Cerința 2: Calcularea indicilor de segregare etnică la nivel de județ
judet_data = merged_data.groupby('County').sum(numeric_only=True)

# Calculul indicelui de disimilaritate (D)
def calculate_dissimilarity(data, judet):
    etnii = [col for col in data.columns if col not in ['total_populatie']]
    total_pop = data.loc[judet, 'total_populatie']
    D = 0.0
    for etnie in etnii:
        Tx = data[etnie].sum()  # Totalul populației pentru etnie
        Tr = total_pop - Tx     # Totalul populației pentru restul
        xi = data.loc[judet, etnie]
        ri = data.loc[judet, 'total_populatie'] - xi
        D += abs(xi / Tx - ri / Tr)
    return 0.5 * D

# Calculul indicelui Shannon-Weaver (H)
def calculate_shannon_weaver(data, judet):
    etnii = [col for col in data.columns if col not in ['total_populatie']]
    total_pop = data.loc[judet, 'total_populatie']
    H = 0.0
    for etnie in etnii:
        pi = data.loc[judet, etnie] / total_pop
        if pi > 0:  # Evităm log(0)
            H -= pi * np.log2(pi)
    return H

# Calculăm indicii pentru fiecare județ
dissimilarity_indices = []
shannon_weaver_indices = []

for judet in judet_data.index:
    D = calculate_dissimilarity(judet_data, judet)
    H = calculate_shannon_weaver(judet_data, judet)
    dissimilarity_indices.append(D)
    shannon_weaver_indices.append(H)

# Crearea DataFrame-ului final pentru indicii de segregare
indices_df = pd.DataFrame({
    'County': judet_data.index,
    'Dissimilarity_Index': dissimilarity_indices,
    'Shannon_Weaver_Index': shannon_weaver_indices
})

# Salvare în fișier CSV
indices_df.to_csv('Indice_Segregare_Etnica.csv', index=False)
print("Fișierul Indice_Segregare_Etnica.csv a fost generat cu succes.")
