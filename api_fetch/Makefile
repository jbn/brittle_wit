RAW_HTML=data/raw/raw_html.jsonl

$(RAW_HTML): fetch_api.py
	./fetch_api.py

.PHONY: clean
clean:
	rm -rf data
