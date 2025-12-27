## Tokenization with tiktoken

We can **encode (tokenize)** and **decode (de-tokenize)** text using `tiktoken`, a fast tokenizer library developed by :contentReference[oaicite:0]{index=0}. Tokenization is a fundamental concept behind how transformer-based language models process and generate text.

---

### What is tiktoken?

`tiktoken` converts human-readable text into **tokens** (integers) that language models can understand, and converts tokens back into readable text.

Language models do **not** work directly with raw text — they operate on tokens.

---

### How Text Generation Works

Transformer models generate text using **next-token prediction**:

1. Input text is converted into tokens
2. The model predicts the most likely next token
3. That token is appended to the sequence
4. The process repeats until output completion

---

### Installation

```bash
pip install tiktoken
