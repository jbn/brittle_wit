RAW_HTML=api_gen/data/raw/raw_html.jsonl
JSON_API=api_gen/data/clean/api.json

$(JSON_API): api_gen/api_pipeline.py api_gen/generate_json_api.py $(RAW_HTML)
	PYTHONPATH=api_gen ./api_gen/generate_json_api.py

$(RAW_HTML): api_gen/fetch_html.py
	./api_gen/fetch_html.py

.PHONY: clean
clean:
	rm -rf api_gen/data

.PHONY: delete_api_code
delete_api_code:
	rm -rf brittle_wit/ads_api brittle_wit/rest_api brittle_wit/streaming_api brittle_wit/webhooks_api
