# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:13:17 2019

@author: Uwe
"""

import pandas as pd

daten = pd.read_excel('Daten-01.xlsx')

print(daten)

daten = daten[['Ort', 'Kosten', 'Datum']]

daten['Kosten_mwst'] = daten['Kosten'] * 1.19

daten.to_clipboard(index=False)

print(len(daten))

print(list(daten))

print('\n',daten.head(2),'\n')

print(daten.iloc[:1])

print('\n\n',daten[daten['Kosten']>50])


rewe = daten[daten['Ort'] == 'Rewe']

plz = pd.read_excel('PLZ.xlsx')

ergebnis = pd.merge(left=daten, right=plz, how='outer', left_on='Ort', right_on='Ort')

print(ergebnis)