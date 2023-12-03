
11. **Problem: Web Scraping with BeautifulSoup and Requests**
    - Description: Use BeautifulSoup and the Requests library to scrape data from a website.
    # - Code:
    #   ```python
    #   import requests
    #   from bs4 import BeautifulSoup

    #   url = "https://example.com"
    #   response = requests.get(url)

    #   if response.status_code == 200:
    #       soup = BeautifulSoup(response.text, "html.parser")
    #       # Extract and print relevant data from the HTML
    #       print(soup.title.text)
    #   ```

12. **Problem: GUI Application with Tkinter**
    - Description: Create a simple graphical user interface (GUI) application using the Tkinter library.
    - Code:
      ```python
      import tkinter as tk

      def on_button_click():
          label.config(text="Button Clicked!")

      # Create main window
      window = tk.Tk()
      window.title("Tkinter GUI")

      # Create button and label
      button = tk.Button(window, text="Click me!", command=on_button_click)
      label = tk.Label(window, text="Welcome to Tkinter!")

      # Pack widgets
      button.pack(pady=10)
      label.pack()

      # Start main loop
      window.mainloop()
      ```

13. **Problem: Data Visualization with Matplotlib**
    - Description: Use Matplotlib to create visualizations from a dataset.
    - Code:
      ```python
      import matplotlib.pyplot as plt
      import numpy as np

      # Generate sample data
      x = np.linspace(0, 10, 100)
      y = np.sin(x)

      # Create a plot
      plt.plot(x, y, label="Sine Function")

      # Add labels and legend
      plt.xlabel("X-axis")
      plt.ylabel("Y-axis")
      plt.title("Sine Function Plot")
      plt.legend()

      # Show the plot
      plt.show()
      ```

These advanced problems cover a range of topics including web scraping, GUI application development, and data visualization. Feel free to explore these challenges to enhance your Python skills in different domains!