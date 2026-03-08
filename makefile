.PHONY: info

NAME 	   	:= Missing Number API
VERSION		:= 1.0
DEVELOPERS	:= Ariel Plasencia Díaz
COPYRIGHT  	:= Next Technologies © 2026: $(DEVELOPERS)

run: ## Run the backend
	uvicorn app.main:app --reload --port 8080

info: ## Display project description
	@echo "$(NAME) v$(VERSION)"
	@echo "$(COPYRIGHT)"

version: ## Show the project version
	@echo "$(NAME) v$(VERSION)"

install: ## Install dependencies
	python3 -m venv .venv
	source .venv/bin/activate
	pip3 install -r requirements.txt

activate_enviroment: ## Activate the enviroment
	source .venv/bin/activate

clean: ## Remove temporary files
	echo "cleaning"

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'