### Document Summarization on ru_government's dataset with BART and Pegasus

# Project structure

**report**
- 	report.pdf - project report file

**models** (jupyter-notebooks for fine-tunings bart and pegasus):
-	bart    - jupyter-notebook for fine-tunings bart.large,
-	pegasus - jupyter-notebook for fine-tunings pegasus_ckpt/model.ckpt;

**dataset**
-	bart    - model training files,
-	pegasus - model training files,
-	pdf_examples - some examples of pdf files from parsing http://government.ru/,
-	pdf2txt.py - lib for extracting text from pdf,
-	parser1.py - parsing pdf's from http://government.ru/,
-	parser2.py - parsing html's from http://archive.government.ru/,
-	pdf_preprocessing.py - pdf preprocessing and merging 2 parts of datasets;

**metrics**
-	bart
-	pegasus