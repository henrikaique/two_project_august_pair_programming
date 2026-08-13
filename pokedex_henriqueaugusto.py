import tkinter as tk
from tkinter import messagebox, ttk
import requests


def formatar_nome(nome):
    
    return nome.capitalize().replace("-", " ")


def traduzir_estatistica(stat_name):
    
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
        self.root.geometry("420x640")
        self.root.resizable(False, False)
        self.root.configure(bg="#DC0A2D")

        
        self.modo_escuro = False

        self.criar_widgets()

    def criar_widgets(self):
        
        self.lbl_titulo = tk.Label(
            self.root,
            text="POKÉDEX",
            font=("Arial", 22, "bold"),
            bg="#DC0A2D",
            fg="white",
        )
        self.lbl_titulo.pack(pady=(10, 2))

       
        self.btn_tema = tk.Button(
            self.root,
            text="🌙 Modo Escuro",
            font=("Arial", 9, "bold"),
            bg="#212121",
            fg="white",
            activebackground="#8A0000",
            activeforeground="white",
            relief="flat",
            command=self.alternar_modo_escuro,
        )
        self.btn_tema.pack(pady=(0, 10))

        
        self.frame_busca = tk.Frame(self.root, bg="#DC0A2D")
        self.frame_busca.pack(pady=5, fill="x", padx=20)

        self.entry_busca = tk.Entry(
            self.frame_busca,
            font=("Arial", 12),
            width=22,
            bd=2,
            relief="solid",
        )
        self.entry_busca.pack(side="left", padx=5, pady=5)
        self.entry_busca.bind("<Return>", lambda event: self.buscar_pokemon())

        btn_buscar = tk.Button(
            self.frame_busca,
            text="Buscar",
            font=("Arial", 10, "bold"),
            bg="#28AAFD",
            fg="white",
            activebackground="#1E80C1",
            activeforeground="white",
            relief="flat",
            command=self.buscar_pokemon,
        )
        btn_buscar.pack(side="left", padx=5)

      
        self.card = tk.Frame(
            self.root, bg="white", bd=3, relief="ridge", padx=15, pady=15
        )
        self.card.pack(pady=10, fill="both", expand=True, padx=20)

        
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
            fg="#797171",
        )
        self.lbl_tipos.pack(anchor="w", pady=2)

        self.lbl_medidas = tk.Label(
            self.card,
            text="Altura: - | Peso: -",
            font=("Arial", 11),
            bg="white",
            fg="#7A6C6C",
        )
        self.lbl_medidas.pack(anchor="w", pady=2)

        self.lbl_habilidades = tk.Label(
            self.card,
            text="Habilidades: -",
            font=("Arial", 10),
            bg="white",
            fg="#685F5F",
            wraplength=340,
            justify="left",
        )
        self.lbl_habilidades.pack(anchor="w", pady=(2, 10))

       
        ttk.Separator(self.card, orient="horizontal").pack(
            fill="x", pady=5
        )

       
        self.lbl_stats_titulo = tk.Label(
            self.card,
            text="Estatísticas Base",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#1D1D1D",
        )
        self.lbl_stats_titulo.pack(anchor="w", pady=(5, 5))

       
        self.frame_stats = tk.Frame(self.card, bg="white")
        self.frame_stats.pack(fill="both", expand=True)

    def alternar_modo_escuro(self):
     
        self.modo_escuro = not self.modo_escuro

        if self.modo_escuro:
            cor_fundo_app = "#1F1F1F"
            cor_card = "#2D2D2D"
            cor_texto = "#FFFFFF"
            cor_subtexto = "#B0B0B0"
            texto_botao = "☀️ Modo Claro"
        else:
            cor_fundo_app = "#DC0A2D"
            cor_card = "white"
            cor_texto = "#1D1D1D"
            cor_subtexto = "#8A7A7A"
            texto_botao = "🌙 Modo Escuro"

        
        self.root.configure(bg=cor_fundo_app)
        self.lbl_titulo.configure(bg=cor_fundo_app)
        self.frame_busca.configure(bg=cor_fundo_app)
        self.btn_tema.configure(text=texto_botao)

       
        self.card.configure(bg=cor_card)
        self.lbl_nome_id.configure(bg=cor_card, fg=cor_texto)
        self.lbl_tipos.configure(bg=cor_card, fg=cor_subtexto)
        self.lbl_medidas.configure(bg=cor_card, fg=cor_subtexto)
        self.lbl_habilidades.configure(bg=cor_card, fg=cor_subtexto)
        self.lbl_stats_titulo.configure(bg=cor_card, fg=cor_texto)
        self.frame_stats.configure(bg=cor_card)

        
        for row in self.frame_stats.winfo_children():
            row.configure(bg=cor_card)
            for child in row.winfo_children():
                if isinstance(child, tk.Label):
                    child.configure(bg=cor_card, fg=cor_texto)

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

        
        for widget in self.frame_stats.winfo_children():
            widget.destroy()

        
        cor_card = "#2D2D2D" if self.modo_escuro else "white"
        cor_texto = "#FFFFFF" if self.modo_escuro else "#1D1D1D"

       
        for stat in dados["stats"]:
            nome_stat = traduzir_estatistica(stat["stat"]["name"])
            valor = stat["base_stat"]

            row_frame = tk.Frame(self.frame_stats, bg=cor_card)
            row_frame.pack(fill="x", pady=2)

            lbl_stat = tk.Label(
                row_frame,
                text=f"{nome_stat}:",
                font=("Arial", 9),
                width=12,
                anchor="w",
                bg=cor_card,
                fg=cor_texto,
            )
            lbl_stat.pack(side="left")

            lbl_val = tk.Label(
                row_frame,
                text=f"{valor:>3}",
                font=("Arial", 9, "bold"),
                width=4,
                bg=cor_card,
                fg=cor_texto,
            )
            lbl_val.pack(side="left")

            progress = ttk.Progressbar(
                row_frame, orient="horizontal", length=180, mode="determinate"
            )
            progress["value"] = min(valor, 200)
            progress["maximum"] = 200
            progress.pack(side="left", padx=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = PokedexApp(root)
    root.mainloop()