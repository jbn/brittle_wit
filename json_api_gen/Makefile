RAW_HTML=data/raw/raw_html.jsonl
JSON_API=data/clean/rest_api.json

$(JSON_API): api_pipeline.py generate_json_apis.py $(RAW_HTML)
	./generate_json_apis.py

$(RAW_HTML): fetch_html.py
	./fetch_html.py

.PHONY: clean
clean:
	rm -rf data
