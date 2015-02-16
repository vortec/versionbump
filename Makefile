test:
	tox

unit:
	py.test --cov-report term-missing --cov versionbump tests

style:
	flake8 --show-source versionbump
	flake8 --show-source --ignore=F811,F821 tests

style-verbose:
	flake8 -v --show-source versionbump
	flake8 -v --show-source --ignore=F811,F821 tests

clean:
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.decomp' -exec rm -f {} \;
	find versionbump -name "__pycache__" -exec rm -rf {} \;
	find tests -name "__pycache__" -exec rm -rf {} \;
	rm -rf .tox
	rm -rf build
	rm -rf *.egg-info
	rm -rf dist
	rm -f coverage.xml
	rm -f junit-*.xml
