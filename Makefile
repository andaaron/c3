include config.mk
include tools.mk

SUBDIRS := static base openj9 go-devel openj9-devel multitool

.DEFAULT_GOAL := all

.PHONY: all
all: $(STACKER) build

.PHONY: build
build:
	mkdir -p $(BUILD_DIR)
	for dir in $(SUBDIRS); do \
		$(MAKE) -C images/$$dir; \
	done

.PHONY: publish
publish:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C images/$$dir publish; \
	done

.PHONY: clean
clean: 
	for dir in $(SUBDIRS); do \
		$(MAKE) -C images/$$dir clean; \
	done
	rm -rf $(BUILD_DIR)
