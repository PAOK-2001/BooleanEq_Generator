# Script for generating boolean equations from a truth table stored in a CSV
# By: Brandon Magaña & Pablo Ortega
import pandas as pd
# Read truth table
df = pd.read_csv('pacemaker.csv', index_col=None)
headers= list(df.columns)
# Define the input and output variables
df_inputs = df[["S2","S1","S0","Sa", "Za","Sv","Zv"]]
df_outputs=["N2","N1","N0","Pa","Ta","Pv","Tv"]
# Iterate the truth table for every output
for out in df_outputs:
    df_N2=df[[out]]
    N2_truth=[]
    for row in df_N2.itertuples():
        if row[1] == 0:
            N2_truth.append(False)
        else:
            N2_truth.append(True)
    # Only consider entries where out == 1
    EqN2=df_inputs[N2_truth]
    inputs =["S2","S1","S0","Sa", "Za","Sv","Zv"]
    eq =""
    # Iterate the values in each row and formulate equation
    for row in EqN2.iterrows():
        row_ = list(row[1])
        for i in range(len(row_)):
            if row_[i] == 1:
                eq += inputs[i]
            else:
                eq+= inputs[i] + "'"
        eq += " + "
    # Display equation
    print(out,"= ",eq[0:len(eq)-3],"\n")