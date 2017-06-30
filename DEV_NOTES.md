# Development Notes

## API Generation

Code and artifacts in the `api_gen` folder provide a scheme for generating library end-user api functions. 

- `fetch_html.py` downloads all the html files associated with API endpoint documentation. 
- `generate_json_api.py` parses the downloaded pages, and transforms them into a JSON-based DSL for the Twitter api. It relies on `api_pipeline.py`, which is a [vaquero](https://github.com/jbn/vaquero) pipeline.
- `generate_src.py` uses the emitted `/api_gen/data/clean/api.json` file to produce `brittle_wit`'s api source code. 

If you are in the base directory, `make` will run this ETL pipeline. 
