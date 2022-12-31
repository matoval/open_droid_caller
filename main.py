import tkinter
import tkinter.messagebox
import customtkinter
from widgets import modal

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Open Droid Caller")
        self.geometry(f"{1080}x{600}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        #create main content window
        self.main_content = customtkinter.CTkFrame(self)
        self.main_content.grid(row=0, column=1, padx=(20, 20), pady=(20, 0))

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Open Droid Caller", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Add droid", command=self.add_droid_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Add program", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Add mission", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Deploy mission", command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                        command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_optionemenu._text_label.configure(text="System")

        self.tabview = customtkinter.CTkTabview(master=self.main_content, width=800, height=900)
        self.tabview.pack(padx=20, pady=20)

        self.tabview.add("Overview")
        self.tabview.add("Missions")
        self.tabview.add("Droids")
        self.tabview.add("Programs")
        self.tabview.set("Overview")

        # create tabs
        self.overview_tab = self.tabview.tab("Overview")
        self.hello = customtkinter.CTkLabel(self.overview_tab, text="Hello World", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.hello.grid(row=1, column=2)

        self.droids_tab = self.tabview.tab("Droids")
        self.hello = customtkinter.CTkLabel(self.droids_tab, text="Hello Droids", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.hello.grid(row=1, column=2)

        self.programs_tab = self.tabview.tab("Programs")
        self.hello = customtkinter.CTkLabel(self.programs_tab, text="01010010111010", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.hello.grid(row=1, column=2)

        self.programs_tab = self.tabview.tab("Missions")
        self.hello = customtkinter.CTkLabel(self.programs_tab, text="Roger Roger", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.hello.grid(row=1, column=2)


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def add_droid_button_event(self):
        dialog = modal.ModalInput(modal_inputs=[{"text": "Name"}, {"text": "ip-address"}], title="Test")
        print("New Droid:", dialog.get_input())


if __name__ == "__main__":
    app = App()
    app.mainloop()