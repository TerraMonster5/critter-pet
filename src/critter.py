import tkinter as tk
from datetime import datetime

class Critter(tk.Tk):
    __total = 0

    @staticmethod
    def getNumberCritters() -> int:
        return Critter.__total

    def __init__(self, name: str) -> None:
        super().__init__()

        self._name = name

        # Stats
        self._hunger = 0
        self._boredom = 0

        self.title(f"{self._name} the Critter")
        self.resizable(0, 0)
        self.geometry("300x300")

        self._status = tk.Label(self, text="Status Unknown", font=("Ariel", 15))
        self._status.pack(expand=True)
        self._status.after(1000, self._update)

        Critter.__total += 1

    def _update(self) -> None:
        self._hunger += 1
        self._boredom += 1

        self._status.after(1000, self._update)

    @property
    def _mood(self) -> str:
        unhappiness = self._hunger + self._boredom
        if unhappiness <= 5:
            m = "happy"
        elif 5 < unhappiness <= 10:
            m = "okay"
        elif 10 < unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self) -> None:
        return self._mood

if __name__ == "__main__":
    a = Critter("Bob")
    a.mainloop()