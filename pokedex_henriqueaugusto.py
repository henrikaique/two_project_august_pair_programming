import tkinter as tk
from tkinter import messagebox, ttk
import requests


def formatar_nome(nome):
    """Capitaliza nomes de forma limpa."""
    return nome.capitalize().replace("-", " ")


def traduzir_estatistica(stat_name):
    """Traduz os nomes das estatísticas."""
    traducoes = {
        "hp": "HP",
        "attack": "Ataque",
        "defense": "Defesa",
        "special-attack": "Ataque Esp.",
        "special-defense": "Defesa Esp.",
        "speed": "Velocidade",
    }
    return traducoes.get(stat_name, stat_name.capitalize())


class PokedexApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Pokédex Python")
        self.root.geometry("420x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#DC0A2D")  # Vermelho clássico da Pokedex

        self.criar_widgets()

    def criar_widgets(self):
        # --- Cabeçalho ---
        lbl_titulo = tk.Label(
            self.root,
            text="POKÉDEX",
            font=("Arial", 22, "bold"),
            bg="#DC0A2D",
            fg="white",
        )
        lbl_titulo.pack(pady=10)

        # --- Área de Busca ---
        frame_busca = tk.Frame(self.root, bg="#DC0A2D")
        frame_busca.pack(pady=5, fill="x", padx=20)  # CORRIGIDO: padx

        self.entry_busca = tk.Entry(
            frame_busca,
            font=("Arial", 12),
            width=22,
            bd=2,
            relief="solid",
        )
        self.entry_busca.pack(side="left", padx=5, pady=5)  # CORRIGIDO: padx
        self.entry_busca.bind("<Return>", lambda event: self.buscar_pokemon())

        btn_buscar = tk.Button(
            frame_busca,
            text="Buscar",
            font=("Arial", 10, "bold"),
            bg="#28AAFD",
            fg="white",
            activebackground="#1E80C1",
            activeforeground="white",
            relief="flat",
            command=self.buscar_pokemon,
        )
        btn_buscar.pack(side="left", padx=5)  # CORRIGIDO: padx

        # --- Cartão de Exibição (Tela da Pokédex) ---
        self.card = tk.Frame(
            self.root, bg="white", bd=3, relief="ridge", padx=15, pady=15
        )
        self.card.pack(pady=10, fill="both", expand=True, padx=20)  # CORRIGIDO: padx

        # Labels das informações principais
        self.lbl_nome_id = tk.Label(
            self.card,
            text="Digite um nome ou ID",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#1D1D1D",
        )
        self.lbl_nome_id.pack(anchor="w", pady=(0, 5))

        self.lbl_tipos = tk.Label(
            self.card,
            text="Tipo(s): -",
            font=("Arial", 11),
            bg="white",
            fg="#666666",
        )
        self.lbl_tipos.pack(anchor="w", pady=2)

        self.lbl_medidas = tk.Label(
            self.card,
            text="Altura: - | Peso: -",
            font=("Arial", 11),
            bg="white",
            fg="#666666",
        )
        self.lbl_medidas.pack(anchor="w", pady=2)

        self.lbl_habilidades = tk.Label(
            self.card,
            text="Habilidades: -",
            font=("Arial", 10),
            bg="white",
            fg="#666666",
            wraplength=340,
            justify="left",
        )
        self.lbl_habilidades.pack(anchor="w", pady=(2, 10))

        # Divisor
        ttk.Separator(self.card, orient="horizontal").pack(
            fill="x", pady=5
        )

        # Título Estatísticas
        lbl_stats_titulo = tk.Label(
            self.card,
            text="Estatísticas Base",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#1D1D1D",
        )
        lbl_stats_titulo.pack(anchor="w", pady=(5, 5))

        # Frame interno para as barras de estatísticas
        self.frame_stats = tk.Frame(self.card, bg="white")
        self.frame_stats.pack(fill="both", expand=True)

    def buscar_pokemon(self):
        termo = self.entry_busca.get().lower().strip()
        if not termo:
            messagebox.showwarning("Aviso", "Por favor, digite um nome ou ID!")
            return

        url = f"https://pokeapi.co/api/v2/pokemon/{termo}"

        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 404:
                messagebox.showerror("Erro", "Pokémon não encontrado!")
                return
            elif response.status_code != 200:
                messagebox.showerror(
                    "Erro", f"Erro de conexão ({response.status_code})"
                )
                return

            dados = response.json()
            self.atualizar_interface(dados)

        except requests.exceptions.RequestException:
            messagebox.showerror(
                "Erro de Conexão",
                "Não foi possível conectar à PokéAPI. Verifique sua internet.",
            )

    def atualizar_interface(self, dados):
        # Atualiza dados principais
        poke_id = dados["id"]
        nome = formatar_nome(dados["name"])
        altura = dados["height"] / 10
        peso = dados["weight"] / 10

        tipos = [formatar_nome(t["type"]["name"]) for t in dados["types"]]
        habilidades = [
            formatar_nome(h["ability"]["name"]) for h in dados["abilities"]
        ]

        self.lbl_nome_id.config(text=f"#{poke_id:03d} - {nome}")
        self.lbl_tipos.config(text=f"Tipo(s): {' / '.join(tipos)}")
        self.lbl_medidas.config(
            text=f"Altura: {altura:.1f} m  |  Peso: {peso:.1f} kg"
        )
        self.lbl_habilidades.config(
            text=f"Habilidades: {', '.join(habilidades)}"
        )

        # Limpa barras antigas de estatísticas
        for widget in self.frame_stats.winfo_children():
            widget.destroy()

        # Desenha as novas barras de progresso
        for stat in dados["stats"]:
            nome_stat = traduzir_estatistica(stat["stat"]["name"])
            valor = stat["base_stat"]

            row_frame = tk.Frame(self.frame_stats, bg="white")
            row_frame.pack(fill="x", pady=2)

            lbl_stat = tk.Label(
                row_frame,
                text=f"{nome_stat}:",
                font=("Arial", 9),
                width=12,
                anchor="w",
                bg="white",
            )
            lbl_stat.pack(side="left")

            lbl_val = tk.Label(
                row_frame,
                text=f"{valor:>3}",
                font=("Arial", 9, "bold"),
                width=4,
                bg="white",
            )
            lbl_val.pack(side="left")

            # Barra visual de estatística (máximo de 200 de valor base)
            progress = ttk.Progressbar(
                row_frame, orient="horizontal", length=180, mode="determinate"
            )
            progress["value"] = min(valor, 200)
            progress["maximum"] = 200
            progress.pack(side="left", padx=5)  # CORRIGIDO: padx


if __name__ == "__main__":
    root = tk.Tk()
    app = PokedexApp(root)
    root.mainloop()
    