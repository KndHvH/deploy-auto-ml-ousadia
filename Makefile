local/install:
	pipenv install --dev --skip-lock

local/shell:
	pipenv shell

local/run:
	streamlit run main.py
