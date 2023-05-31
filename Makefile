generate:
	kiota generate --language=python --openapi=service-accounts.yaml --output=jsa/client --namespace-name=client --class-name=ServiceAccountClient --clean-output --clear-cache

build:
	poetry build

publish:
	poetry publish --build -u ${USERNAME} -p ${PASSWORD}

install:
	poetry install

test:
	poetry run pytest -s

clean:
	rm -rf jsa/client
	rm -rf dist