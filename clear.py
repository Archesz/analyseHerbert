import pandas as pd


def clear(df):
    gabarito = ["D", "D", "B", "A", "C", "C", "D", "C", "B", "D", "C", "D", "D", "A", "D", "B", "D", "B", "A", "C", "C", "B", "A", "D", "C", "A", "B", "B", "C", "A", "D", "A",
                "A", "B", "C", "B", "B", "A", "C", "B", "B", "D", "B", "A", "C", "B", "D", "B", "B", "B", "D", "C", "C", "D", "C", "A", "D", "C", "B", "D", "C", "D", "B", "C", "D", "D"]

    df.drop(index=df.index[0], axis=0, inplace=True)
    totais = []
    total_matematica = []
    total_geografia = []
    total_fisica = []
    total_quimica = []
    total_biologia = []
    total_sociologia = []
    total_filosofia = []
    total_portugues = []
    total_historia = []

    for i in range(0, len(df)):

        total = 0
        matematica = 0
        geografia = 0
        fisica = 0
        quimica = 0
        biologia = 0
        sociologia = 0
        filosofia = 0
        portugues = 0
        historia = 0

        for j in range(2, len(df.columns)):

            if df.iloc[i][j] == gabarito[j-2]:
                total += 1

                if "Matemática" in df.columns[j]:
                    matematica += 1
                elif "História" in df.columns[j]:
                    historia += 1
                elif "Sociologia" in df.columns[j]:
                    sociologia += 1
                elif "Filosofia" in df.columns[j]:
                    filosofia += 1
                elif "Geografia" in df.columns[j]:
                    geografia += 1
                elif "Biologia" in df.columns[j]:
                    biologia += 1
                elif "Fisica" in df.columns[j]:
                    fisica += 1
                elif "Linguagens" in df.columns[j]:
                    portugues += 1
                elif "Quimica" in df.columns[j]:
                    quimica += 1

        totais.append(total)
        total_matematica.append(matematica)
        total_geografia.append(geografia)
        total_fisica.append(fisica)
        total_quimica.append(quimica)
        total_biologia.append(biologia)
        total_sociologia.append(sociologia)
        total_filosofia.append(filosofia)
        total_portugues.append(portugues)
        total_historia.append(historia)

    df["NotaTotal"] = totais
    df["NotaMatematica"] = total_matematica
    df["NotaGeografia"] = total_geografia
    df["NotaFisica"] = total_fisica
    df["NotaQuimica"] = total_quimica
    df["NotaBiologia"] = total_biologia
    df["NotaSociologia"] = total_sociologia
    df["NotaFilosofia"] = total_filosofia
    df["NotaPortugues"] = total_portugues
    df["NotaHistoria"] = total_historia

    df.to_csv("simulado_clean.csv")

    return df

df = pd.read_csv("simulado.csv")
df = clear(df)

#def clear_cursos(df):
#    df = df.drop([df.columns[0]], 1)
#    return df
