db: db-down
	docker compose up -d db
	sleep 10
	. ../../venv/bin/activate; python init-db.py


db-down:
	docker compose down