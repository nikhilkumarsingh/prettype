import glob
import os
import tkinter as tk


class HoverButton(tk.Button):
    """
    Utility class for button which changes color on hovering
    """
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self['background']
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def on_enter(self, _):
        self['background'] = self['activebackground']

    def on_leave(self, _):
        self['background'] = self.defaultBackground


class FontSelectorGUI:
    """
    Implementation of tk based GUI for selection of font type
    """
    def __init__(self, on_select=None):
        # root (top level element) config
        h, w = 250, 220
        self.root = tk.Tk()
        self.root.title("prettype")
        self.root.minsize(width=w, height=h)
        self.position_window()

        # when 'X' button is clicked
        self.root.protocol('WM_DELETE_WINDOW', self.quit)

        # canvas to hold main scrollbar
        self.canvas = tk.Canvas(self.root, height=h - 10, width=w - 20)
        self.canvas.pack(side=tk.RIGHT, expand=True)

        # scrollbar config
        scrollbar = tk.Scrollbar(self.root, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # main frame (inside root) config
        self.mainframe = tk.Frame(self.root, padx=1, pady=1)
        self.mainframe.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

        # canvas window over mainframe
        self.canvas.create_window((0, 0), window=self.mainframe, anchor='nw')
        self.mainframe.bind('<Configure>', self.on_configure)

        # button list display
        colors = ['orange', 'tomato', 'gold']
        items = [font_path.split('/')[-1].split('.')[0] for font_path in
                 glob.glob(os.path.join(os.path.dirname(__file__), 'fonts/*.json'))]

        for i, item in enumerate(sorted(items)):
            button = HoverButton(self.mainframe, text=item, command=lambda x=item: self.callback(x), width=20,
                                 bg=colors[i % 3], activebackground='light green')
            button.grid(row=i, column=0)

        # child function to execute on button click
        self.on_select = on_select

        # call mainloop of Tk object
        self.root.mainloop()
        self.root.quit()

    def callback(self, font):
        """
        Callback function for button click
        :param font: selected font type
        """
        if self.on_select:
            self.on_select(font)
        self.quit()

    def position_window(self):
        """
        function to position window to current mouse position
        """
        x, y = self.root.winfo_pointerxy()
        self.root.geometry('+{}+{}'.format(x, y))

    def on_configure(self, _):
        """
        utility function to enable scrolling over canvas window
        """
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def quit(self):
        """
        Quit the tk window
        """
        print("Closing \"Font Selector GUI\" Window")
        self.root.destroy()


if __name__ == '__main__':
    FontSelectorGUI()
