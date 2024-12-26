# Install full setup
setup:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .

app:
	streamlit run src/App.py

# test functions
test:
	python tests/tests.py

pytst:
	pytest tests/tests.py

# Clear cache
clear:
	rm -rf __pycache__ .pytest_cache
	rm -rf src/__pycache__ src/package/__pycache__
