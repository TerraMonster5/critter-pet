import tkinter as tk
'''
Todo:
- Add file saving
- Add away time calculation

from datetime import datetime
'''

class Critter(tk.Tk):
    __total = 0

    # Getter for number of instantiated Critters
    @staticmethod
    def getNumberCritters() -> int:
        return Critter.__total

    # Initialise each object once instantiated
    def __init__(self, name: str) -> None:
        super().__init__()

        self._name = name

        # Stats
        self._hunger = 0
        self._boredom = 0

        # Setup window
        self.title(f"{self._name} the Critter")
        self.resizable(False, False)
        self.geometry("300x300")

        # Setup status label
        self._statusLb = tk.Label(self, text="Status Unknown", font=("Ariel", 15))
        self._statusLb.pack(pady=(100, 0))

        self._unhappinessLb = tk.Label(self, text="", font=("Ariel", 10))
        self._unhappinessLb.pack()

        self.after(2000, self._update)

        # Increment number of instatiated Critters once fully initialised
        Critter.__total += 1

    # Increment stats every 10 seconds
    def _update(self) -> None:
        self._hunger += 1
        self._boredom += 1

        self._statusLb.configure(text=f"Hunger: {self._hunger} | Boredom: {self._boredom}")
        self._unhappinessLb.configure(text=f"Happiness: {self.mood}")

        self.after(2000, self._update)

    @property
    def mood(self) -> str:
        unhappiness = self._hunger + self._boredom
        if unhappiness <= 10:
            m = "happy"
        elif 10 < unhappiness <= 20:
            m = "okay"
        elif 20 < unhappiness <= 30:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def eat(self) -> None:
        self._hunger -= 8
        if self._hunger < 0: self._hunger = 0
    
    def play(self) -> None:
        self._boredom -= 8
        if self._boredom < 0: self._boredom = 0

if __name__ == "__main__":
    a = Critter("Bob")
    a.mainloop()