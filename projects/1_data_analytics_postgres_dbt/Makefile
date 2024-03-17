DIR=postgres_with_dbt

setup:
	docker compose up -d
	virtualenv env
	. env/bin/activate
	pip install -r requirements.txt
	python3 generate_data.py


check:
	cp profiles.yml ~/.dbt/profiles.yml
	cd $(DIR) && dbt debug


run:
	cd $(DIR) && dbt run	


serve-dbt:
	cd postgres_with_dbt && dbt docs generate && dbt docs serve --port 8001