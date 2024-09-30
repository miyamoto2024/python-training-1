export
.PHONY: init test build deploy

init:
	pipenv install

test:
	pipenv run pytest

# コンテナを利用する場合、make build OPT=--use-container
build:
	sam build $(OPT)

deploy:
	sam deploy \
	--stack-name python-training-1 \
	$(OPT)
