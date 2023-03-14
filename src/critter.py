import tkinter as tk

'''
Todo:
- Add file saving
- Add away time calculation
- Add support for multiple Critters
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

        # Setup unhappiness label
        self._unhappinessLb = tk.Label(self, text="", font=("Ariel", 10))
        self._unhappinessLb.pack()

        # Setup care buttons
        tk.Button(self, text="Play", font=("Ariel", 10), command=self.play).pack(side="bottom", pady=(5, 20))
        tk.Button(self, text="Feed", font=("Ariel", 10), command=self.eat).pack(side="bottom", pady=(0, 5))

        # Schedule update and render events
        self.after(2000, self._update)
        self.after(1, self._render)

        # Increment number of instatiated Critters once fully initialised
        Critter.__total += 1

    # Increment stats every 10 seconds
    def _update(self) -> None:
        self._hunger += 1
        self._boredom += 1

        self.after(2000, self._update)
    
    # Render stats every millisecond
    def _render(self) -> None:
        self._statusLb.configure(text=f"Hunger: {self._hunger} | Boredom: {self._boredom}")
        self._unhappinessLb.configure(text=f"Happiness: {self.mood}")

        self.after(1, self._render)

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
    
    # Helper functions to decrement hunger and boredom
    def eat(self) -> None:
        self._hunger -= 8
        if self._hunger < 0: self._hunger = 0
    
    def play(self) -> None:
        self._boredom -= 8
        if self._boredom < 0: self._boredom = 0

# Main program
if __name__ == "__main__":
    a = Critter("Bob")
    a.mainloop()