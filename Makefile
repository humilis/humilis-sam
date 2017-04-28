HUMILIS := .env/bin/humilis
PIP := .env/bin/pip
PYTHON := .env/bin/python
TOX := .env/bin/tox
STAGE := DEV
HUMILIS_ENV := tests/integration/humilis-sam-swagger tests/integration/humilis-sam-classic

# create virtual environment
.env:
	virtualenv .env -p python3

# install dev dependencies, create layers directory
develop: .env
	.env/bin/pip install -r requirements-dev.txt

# run integration tests
test: .env
	$(PIP) install tox
	$(TOX)

# remove .tox and .env dirs
clean:
	rm -rf .env .tox

# configure humilis
configure:
	$(HUMILIS) configure --local

# deploy the test environment
create: develop
	for env in $(HUMILIS_ENV) ; do \
		$(HUMILIS) create \
			--stage $(STAGE) \
			--output $$env-$(STAGE).outputs.yaml \
			$$env.yaml ; \
	done

# update the test deployment
update: develop
	for env in $(HUMILIS_ENV) ; do \
		$(HUMILIS) update \
			--stage $(STAGE) \
			--output $$env-$(STAGE).outputs.yaml \
			$$env.yaml ; \
	done

# delete the test deployment
delete: develop
	for env in $(HUMILIS_ENV) ; do \
		$(HUMILIS) delete --stage $(STAGE) $$env.yaml ; \
	done

# upload to Pypi
pypi: develop
	$(PYTHON) setup.py sdist upload
