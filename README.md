# PageRank – CS50AI Project

This project implements the PageRank algorithm to analyze the importance of web pages based on their link structure. The program parses a collection of HTML pages, builds a corpus of links, and estimates PageRank values using both sampling and iterative methods.

## 🧠 How It Works

- The program loads a set of HTML files and extracts all links between pages.
- It constructs a directed graph representing the corpus.
- PageRank values are estimated in two ways:
  - **Sampling:** Simulates random walks through the corpus to estimate the probability of landing on each page.
  - **Iteration:** Repeatedly updates PageRank values until they converge.

## 📂 Features

- Parses HTML files to build a link graph.
- Calculates PageRank using both sampling and iterative approaches.
- Configurable damping factor and sample size.
- Outputs PageRank values for each page in the corpus.

## ▶️ Usage

To run the program, use:

```bash
python pagerank.py corpus0
```
Replace `corpus0` with the path to your corpus directory.

## ⚙️ Requirements

- Python 3.7 or higher

## 💾 Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:noeEdwin/PageRank.git
   cd pagerank
   pip install -r requirements.txt
   ```
2. **(Optional)** Install additional dependencies if required.

## 📄 Files

- `pagerank.py`: Main implementation of the PageRank algorithm.
- `corpus*`: Example corpus directories containing HTML files.
- `README.md`: Project documentation.
