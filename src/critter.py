import tkinter as tk
import datetime as dt

'''
Todo:
- Add file saving
- Add away time calculation
- Overfeeding
- Overstimulating
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

        self.alive = True

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
        self.playBt = tk.Button(self, text="Play", font=("Ariel", 10), command=self.play)
        self.eatBt = tk.Button(self, text="Feed", font=("Ariel", 10), command=self.eat)

        self.playBt.pack(side="bottom", pady=(5, 20))
        self.eatBt.pack(side="bottom", pady=(0, 5))

        # Schedule update and render events
        self.after(5000, self._update)
        self.after(1, self._render)

        # Increment number of instatiated Critters once fully initialised
        Critter.__total += 1

        # Run event loop
        self.mainloop()

    # Increment stats every 2 seconds
    def _update(self) -> None:
        self._hunger += 5
        self._boredom += 5

        self.after(2000, self._update)
    
    # Render stats every millisecond
    def _render(self) -> None:
        self._statusLb.configure(text=f"Hunger: {self._hunger} | Boredom: {self._boredom}")
        self._unhappinessLb.configure(text=f"Happiness: {self.mood}")

        self.after(1, self._render)

    def getName(self) -> str:
        return self._name
    
    def getBoredom(self) -> int:
        return self._boredom
    
    def getHunger(self) -> int:
        return self._hunger

    @property
    def mood(self) -> str:
        unhappiness = self._hunger + self._boredom
        if unhappiness <= 10:
            m = "happy"
        elif 10 < unhappiness <= 20:
            m = "okay"
        elif 20 < unhappiness <= 30:
            m = "frustrated"
        elif 30 < unhappiness <= 100:
            m = "mad"
        else:
            m = "dead"
            self.alive = False
        return m
    
    # Helper functions to decrement hunger and boredom
    def play(self) -> None:
        self.playBt.configure(state="disabled")
        self._boredom -= 10
        if self._boredom < 0: self._boredom = 0
        self.playBt.after(10000, lambda: self.playBt.configure(state="active"))
        
    def eat(self) -> None:
        self.eatBt.configure(state="disabled")
        self._hunger -= 10
        if self._hunger < 0: self._hunger = 0
        self.eatBt.after(10000, lambda: self.eatBt.configure(state="active"))

class Main(tk.Tk):
    class State:
        def __init__(self, window) -> None:
            self._window = window
            self._frame = tk.Frame(window)
            self._frame.pack()
        
        def _switchMainMenu(self) -> None:
            self._frame.destroy()
            self._window.currentState = self._window.MainMenu(self._window)

    
    class MainMenu(State):
        def __init__(self, window) -> None:
            super().__init__(window)

            tk.Button(self._frame, text="View Critters", command=self.__switchViewCritters).pack()
        
        def __switchViewCritters(self) -> None:
            self._frame.destroy()
            self._window.currentState = self._window.ViewCritters(self._window)
    
    class ViewCritters(State):
        def __init__(self, window) -> None:
            super().__init__(window)

            tk.Button(self._frame, text="Back", command=self._switchMainMenu).pack()
            tk.Button(self._frame, text="New Critter", command=self.newCritter).pack()
        
        def newCritter(self) -> None:
            self._window.critters.append(Critter("Bob"))

    def __init__(self) -> None:
        super().__init__()

        self.currentState = self.MainMenu(self)
        self.critters = []

        # Setup window
        self.title("blah")
        self.resizable(False, False)
        self.geometry("300x300")

        self.after(1, self.__death)
    
    def __death(self) -> None:
        for count, critter in enumerate(self.critters):
            if not critter.alive:
                critter.destroy()
                self.critters.pop(count)
        
        self.after(1, self.__death)

# Main program
if __name__ == "__main__":
    app = Main()
    app.mainloop()

    with open("critters.txt", "w") as file:
        for count, critter in enumerate(app.critters):
            formattedTime = dt.datetime.now().strftime("%d %m %Y %H:%M:%S")
            file.write(f"{critter.getName()}, {critter.getBoredom()}, {critter.getHunger()}, {formattedTime}")
            critter.destroy()
            app.critters.pop(count)