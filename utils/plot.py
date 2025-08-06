import matplotlib.pyplot as plt

def plotar_grafico(x, y, titulo, xlabel, ylabel, nome_arquivo):
    plt.figure(figsize=(12, 4))
    plt.plot(x, y, marker='o', linestyle='-', color='tab:blue')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"data/{nome_arquivo}")
    plt.close()