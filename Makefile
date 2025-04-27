.PHONY: up down seed

up:
	docker-compose up --build

down:
	docker-compose down

seed:
	python3 scripts/populate_db.py
