# DNA Translation to Proteins 
# 🧬 DNA Translation to Proteins

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Author**: Abigail Ewnetu

This project simulates the biological processes of **DNA transcription** and **mRNA translation** into proteins using Python. It models the central dogma of molecular biology:

> **DNA → mRNA → Protein**

---

## 📌 Features

- ✅ Converts a DNA sequence into an mRNA sequence (transcription)
- ✅ Splits mRNA into codons and translates them to amino acids (translation)
- ✅ Handles stop codons appropriately
- ✅ Warns when unknown codons are found

---

## 🗂 Project Structure

dna-translation-to-proteins/
├── main.py # Main script for running transcription and translation
├── helper.py # Contains utility functions and the amino acid codon table
└── README.md # Project documentation (you are here)


---

## ⚙️ How It Works

### 1. Transcription
Translates DNA bases into mRNA:
- A → U  
- T → A  
- C → G  
- G → C  

### 2. Translation
- Breaks mRNA into codons (3-letter segments)
- Maps codons to amino acids using a dictionary (`helper.amino_acids`)
- Stops translation at the first `Stop` codon

---

## 🧪 Example Output

DNA Sequence: TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT
mRNA Sequence: AUGCGUCUUUUUUUAGUCGCCCCAACAACCAGUAAUCAGACUUAA
---

## 📎 Dependencies

- Python 3.8+
- No external packages required

---



