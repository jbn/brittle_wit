RAW_HTML=api_gen/data/raw/raw_html.jsonl
JSON_API=api_gen/data/clean/api.json
API_SRC=brittle_wit/rest_api/friends.py

$(API_SRC): api_gen/generate_src.py api_gen/api_code_gen.py $(JSON_API)
	PYTHON_PATH=api_gen ./api_gen/generate_src.py

$(JSON_API): api_gen/api_pipeline.py api_gen/generate_json_api.py $(RAW_HTML)
	PYTHONPATH=api_gen ./api_gen/generate_json_api.py

$(RAW_HTML): api_gen/fetch_html.py
	./api_gen/fetch_html.py

.PHONY: test
test:
	python setup.py nosetests

.PHONY: clean
clean:
	rm -rf api_gen/data

.PHONY: delete_api_code
delete_api_code:
	rm -rf brittle_wit/ads_api brittle_wit/rest_api brittle_wit/streaming_api brittle_wit/webhooks_api
