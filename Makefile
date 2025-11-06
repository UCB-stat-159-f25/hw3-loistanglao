.PHONY: env html clean

# Environment name
ENV_NAME = ligo

env:
	@if conda env list | grep -q "^$(ENV_NAME) "; then \
		echo "Environment '$(ENV_NAME)' already exists. Updating..."; \
		conda env update -n $(ENV_NAME) -f environment.yml --prune; \
	else \
		echo "Creating environment '$(ENV_NAME)'..."; \
		conda env create -f environment.yml; \
	fi

html:
	myst build --html

clean:
	rm -rf figures audio _build