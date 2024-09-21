generate-venv:
# we should try and keep these platform agnostic
# since i think we are all on different OS's
ifeq ($(shell uname -s),Linux)
	rm -rf venv
	python3 -m venv venv
	. ./venv/bin/activate; $(MAKE) -C src/server install-deps
endif

start-backend:
ifeq ($(shell uname -s),Linux)
	. ./venv/bin/activate; $(MAKE) -C src/server start
endif

start-frontend:
ifeq ($(shell uname -s),Linux)
	$(MAKE) -C src/client/frontend start
endif
