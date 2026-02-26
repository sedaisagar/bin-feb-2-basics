import tkinter as tk
from tkinter import ttk
import threading


class DesktopApp(tk.Tk):
    """
    A base class for creating desktop applications using tkinter.
    When instantiated, it creates a fully functional tkinter window.
    """

    def __init__(
        self,
        title="Desktop Application",
        width=800,
        height=600,
        resizable=True,
    ):
        """
        Initialize the desktop application.

        Args:
            title (str): The title of the application window
            width (int): The width of the application window in pixels
            height (int): The height of the application window in pixels
            resizable (bool): Whether the window can be resized (default: True)
        """
        super().__init__()

        # Window configuration
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(resizable, resizable)

        # Configure style
        self._configure_styles()

        # Create main container
        self.main_frame = ttk.Frame(self, padding="10")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

    def _configure_styles(self):
        """Configure the theme and styles for the application."""
        style = ttk.Style()
        # You can set theme or create custom styles here
        # style.theme_use('clam')  # Uncomment to use clam theme

    def add_label(self, text, row=0, column=0, **kwargs):
        """
        Add a label to the main frame.

        Args:
            text (str): The text to display
            row (int): Grid row position
            column (int): Grid column position
            **kwargs: Additional ttk.Label arguments
        """
        label = ttk.Label(self.main_frame, text=text, **kwargs)
        label.grid(row=row, column=column, sticky="w", padx=5, pady=5)
        return label

    def add_button(self, text, command, row=0, column=0, **kwargs):
        """
        Add a button to the main frame.

        Args:
            text (str): The button label
            command (callable): Function to call when button is clicked
            row (int): Grid row position
            column (int): Grid column position
            **kwargs: Additional ttk.Button arguments
        """
        button = ttk.Button(
            self.main_frame, text=text, command=command, **kwargs
        )
        button.grid(row=row, column=column, sticky="w", padx=5, pady=5)
        return button

    def add_entry(self, row=0, column=0, **kwargs):
        """
        Add an entry widget to the main frame.

        Args:
            row (int): Grid row position
            column (int): Grid column position
            **kwargs: Additional ttk.Entry arguments
        """
        entry = ttk.Entry(self.main_frame, **kwargs)
        entry.grid(row=row, column=column, sticky="ew", padx=5, pady=5)
        return entry

    def add_text(self, row=0, column=0, width=40, height=10, **kwargs):
        """
        Add a text widget to the main frame.

        Args:
            row (int): Grid row position
            column (int): Grid column position
            width (int): Width of the text widget
            height (int): Height of the text widget
            **kwargs: Additional tk.Text arguments
        """
        text = tk.Text(
            self.main_frame, width=width, height=height, **kwargs
        )
        text.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
        return text

    def add_frame(self, row=0, column=0, **kwargs):
        """
        Add a frame to the main frame.

        Args:
            row (int): Grid row position
            column (int): Grid column position
            **kwargs: Additional ttk.Frame arguments
        """
        frame = ttk.Frame(self.main_frame, **kwargs)
        frame.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
        return frame

    def add_treeview(self, columns, row=0, column=0, height=10, **kwargs):
        """
        Add a table/treeview widget to the main frame.

        Args:
            columns (list): List of column names
            row (int): Grid row position
            column (int): Grid column position
            height (int): Height of the treeview
            **kwargs: Additional ttk.Treeview arguments
        """
        tree = ttk.Treeview(
            self.main_frame, columns=columns, height=height, **kwargs
        )
        tree.column("#0", width=0, stretch=tk.NO)
        tree.heading("#0", text="", anchor=tk.W)

        for col in columns:
            tree.column(col, anchor=tk.W, width=100)
            tree.heading(col, text=col, anchor=tk.W)

        tree.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
        return tree

    def run(self):
        """Start the application event loop."""
        self.mainloop()


class ScraperUI(DesktopApp):
    """
    A desktop application for scraping news from sidhakura.com
    and displaying it in a user-friendly table format.
    """

    def __init__(self):
        super().__init__(
            title="Web Scraper - Sidhakura News", width=1000, height=700
        )

        # Add title label
        self.add_label(
            "Web Scraper - Sidhakura News",
            row=0,
            column=0,
            font=("Arial", 16, "bold"),
        )

        # Add control frame
        control_frame = self.add_frame(row=1, column=0)
        control_frame.columnconfigure(0, weight=1)

        # Page number input
        ttk.Label(control_frame, text="Pages to scrape:").grid(
            row=0, column=0, padx=5, pady=5
        )
        self.pages_entry = ttk.Entry(control_frame, width=10)
        self.pages_entry.insert(0, "5")
        self.pages_entry.grid(row=0, column=1, padx=5, pady=5)

        # Start button
        self.start_button = ttk.Button(
            control_frame,
            text="Start Scraping",
            command=self.start_scraping_job,
        )
        self.start_button.grid(row=0, column=2, padx=5, pady=5)

        # Output text area
        ttk.Label(
            self.main_frame, text="Scraping Output:", font=("Arial", 10, "bold")
        ).grid(row=2, column=0, sticky="w", padx=5, pady=(10, 5))

        self.output_text = self.add_text(row=3, column=0, height=8)
        self.output_text.config(state="disabled")

        # Results table
        ttk.Label(
            self.main_frame,
            text="Scraped News:",
            font=("Arial", 10, "bold"),
        ).grid(row=4, column=0, sticky="w", padx=5, pady=(10, 5))

        self.results_tree = self.add_treeview(
            columns=("Title", "Image URL", "Published Date"),
            row=5,
            column=0,
            height=12,
        )

        # Configure grid weights
        self.main_frame.rowconfigure(3, weight=1)
        self.main_frame.rowconfigure(5, weight=2)
        self.main_frame.columnconfigure(0, weight=1)

        # Scraper instance
        from package_sql.scrapper import BsScraper

        self.scraper = BsScraper()
        self.scraping = False

    def log_output(self, message):
        """Write message to output text widget."""
        self.output_text.config(state="normal")
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END)
        self.output_text.config(state="disabled")
        self.update()

    def populate_table(self):
        """Populate the treeview with scraped data."""
        # Clear existing rows
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)

        # Insert new rows
        for idx, news in enumerate(self.scraper.news_list):
            self.results_tree.insert(
                "",
                "end",
                iid=idx,
                text="",
                values=(
                    news["title"][:60] + "..."
                    if len(news["title"]) > 60
                    else news["title"],
                    news["image"][:50] + "..."
                    if len(news["image"]) > 50
                    else news["image"],
                    news["publish_date"],
                ),
            )

    def scrape_worker(self, pages):
        """Worker thread function to scrape pages."""
        try:
            self.log_output(f"Starting scraping job for {pages} pages...\n")

            for page in range(1, pages + 1):
                if not self.scraping:
                    self.log_output("Scraping cancelled.")
                    break

                self.log_output(f"Scraping page {page}...")
                self.scraper.scrap_page(page)
                self.log_output(f"✓ Page {page} completed\n")

                # Update table after each page
                self.populate_table()

            if self.scraping:
                self.log_output(
                    f"\n✓ Scraping completed! Total news items: {len(self.scraper.news_list)}"
                )

        except Exception as e:
            self.log_output(f"✗ Error during scraping: {str(e)}")

        finally:
            self.scraping = False
            self.start_button.config(state="normal")
            self.pages_entry.config(state="normal")

    def start_scraping_job(self):
        """Start the scraping job in a background thread."""
        if self.scraping:
            return

        try:
            pages = int(self.pages_entry.get())
            if pages < 1:
                self.log_output("✗ Please enter a number greater than 0")
                return
        except ValueError:
            self.log_output("✗ Please enter a valid number for pages")
            return

        # Clear previous data
        self.scraper.news_list = []
        self.output_text.config(state="normal")
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state="disabled")
        self.populate_table()

        # Disable controls
        self.scraping = True
        self.start_button.config(state="disabled")
        self.pages_entry.config(state="disabled")

        # Start scraping in background thread
        scraper_thread = threading.Thread(
            target=self.scrape_worker, args=(pages,)
        )
        scraper_thread.daemon = True
        scraper_thread.start()

if __name__ == "package_sql.ui":
    app = ScraperUI()
    app.run()