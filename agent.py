class FruitShopAgent:
    """Agente deterministico per gestire un semplice negozio di frutta."""

    def __init__(self):
        # inventario iniziale con prezzi in euro e quantita disponibili
        self.inventory = {
            "mela": {"price": 1.0, "quantity": 10},
            "banana": {"price": 0.5, "quantity": 20},
            "arancia": {"price": 0.8, "quantity": 15},
        }

    def respond(self, user_input: str) -> str:
        tokens = user_input.strip().lower().split()
        if not tokens:
            return "Comando non riconosciuto."

        if tokens[0] in {"ciao", "hello"}:
            return "Benvenuto nel negozio di frutta!"
        if tokens[0] in {"bye", "arrivederci", "goodbye"}:
            return "Alla prossima!"

        # mostra inventario
        if tokens[0] == "mostra" and len(tokens) > 1 and tokens[1] == "inventario":
            lines = [
                f"{fruit}: \u20ac{data['price']:.2f}, quantita {data['quantity']}"
                for fruit, data in self.inventory.items()
            ]
            return "\n".join(lines)

        # cambia prezzo: "prezzo set <frutto> <valore>"
        if tokens[0] == "prezzo" and len(tokens) == 4 and tokens[1] == "set":
            fruit = tokens[2]
            try:
                price = float(tokens[3])
            except ValueError:
                return "Prezzo non valido."
            if fruit in self.inventory:
                self.inventory[fruit]["price"] = price
                return f"Prezzo di {fruit} aggiornato a \u20ac{price:.2f}"
            return "Frutto non trovato."

        # acquista frutta: "compra <frutto> <quantita>"
        if tokens[0] == "compra" and len(tokens) == 3:
            fruit = tokens[1]
            try:
                qty = int(tokens[2])
            except ValueError:
                return "Quantita non valida."
            item = self.inventory.get(fruit)
            if not item:
                return "Frutto non trovato."
            if item["quantity"] < qty:
                return "Quantita non disponibile."
            cost = qty * item["price"]
            item["quantity"] -= qty
            return f"Hai comprato {qty} {fruit} per \u20ac{cost:.2f}"

        # vendi frutta: "vendi <frutto> <quantita>"
        if tokens[0] == "vendi" and len(tokens) == 3:
            fruit = tokens[1]
            try:
                qty = int(tokens[2])
            except ValueError:
                return "Quantita non valida."
            if fruit not in self.inventory:
                return "Frutto non trovato."
            self.inventory[fruit]["quantity"] += qty
            return f"Hai venduto {qty} {fruit}."

        return "Comando sconosciuto."

