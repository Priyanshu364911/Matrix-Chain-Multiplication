# ⚙️ Matrix Chain Multiplication Visualizer

A dynamic and interactive web application built with **Streamlit** to solve and visualize the **Matrix Chain Multiplication** problem using Dynamic Programming. This tool calculates the most efficient way to multiply a sequence of matrices and generates the optimal parenthesization.

## 🌟 Features

* **Dynamic Configuration:** Interactive sliders and inputs to set the number of matrices and their specific dimensions.
* **Optimal Solution:** Instantly calculates the minimum number of scalar multiplications required.
* **Parenthesization:** Generates the exact sequence string (e.g., `((M1(M2M3))M4)`).
* **DP Table Visualization:** Displays the computed cost matrix (DP table) to help understand the algorithm's decision-making process.
* **Custom UI:** Features a polished, custom CSS "Purple Theme" for a modern user experience.
* **Educational Sidebar:** Quick reference for time and space complexity.

## 🛠️ Installation

1. **Clone the repository** (or download the source code):
```bash
git clone https://github.com/yourusername/matrix-chain-visualizer.git
cd matrix-chain-visualizer

```


2. **Create a virtual environment (Optional but recommended):**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

```


3. **Install dependencies:**
```bash
pip install streamlit numpy

```



## 🚀 Usage

1. Save the provided Python code into a file named `app.py`.
2. Run the Streamlit application:
```bash
streamlit run app.py

```


3. The application will open automatically in your default web browser (usually at `http://localhost:8501`).

## 🧠 Algorithm Overview

**Matrix Chain Multiplication** is a classic optimization problem that can be solved using Dynamic Programming.

Given a sequence of matrices, the goal is to find the most efficient way to multiply them. The order in which we parenthesize the product affects the number of simple arithmetic operations needed to compute the product.

* **Time Complexity:** 
* **Space Complexity:** 

### How it works in this app:

1. **Input:** The user provides dimensions for a chain of matrices.
2. **Processing:** The algorithm fills a table `m[i, j]` representing the minimum cost to multiply matrices  through .
3. **Splitting:** It simultaneously tracks the split point `s[i, j]` which records where the optimal break occurred.
4. **Output:** The app reconstructs the solution from the split table to show the parenthesization.

## 📂 Project Structure

```text
matrix-chain-visualizer/
├── app.py           # Main application logic and UI
└── README.md        # Project documentation


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


---

### Would you like me to create a `requirements.txt` file content for you as well?
