include ../../config.mk
include ../../tools.mk

ifeq ($(strip $(PUBLISH_TAG)),)
override PUBLISH_TAG := $(DISTRO_REL)
endif

.DEFAULT_GOAL := all

.PHONY: all
all: build test

.PHONY: build
build: $(STACKER)
	$(STACKER_WITH_BUILD_DIR) \
		build -f stacker.yaml \
		--layer-type tar --layer-type squashfs \
		--substitute REVISION=$(COMMIT) \
		--substitute LICENSES="$(shell cat LICENSE.md)" \
		--substitute DESCRIPTION="$(shell cat README.md)" \
		--substitute OS=$(OS) \
		--substitute ARCH=$(ARCH) \
		--substitute DISTRO=$(DISTRO) \
		--substitute DISTRO_REL=$(DISTRO_REL) 

.PHONY: publish
publish: $(STACKER)
	$(STACKER_WITH_BUILD_DIR) \
		publish -f stacker.yaml \
		--layer-type tar --layer-type squashfs \
		--substitute REVISION=$(COMMIT) \
		--substitute LICENSES="$(shell cat LICENSE.md)" \
		--substitute DESCRIPTION="$(shell cat README.md)" \
		--substitute OS=$(OS) \
		--substitute ARCH=$(ARCH) \
		--substitute DISTRO=$(DISTRO) \
		--substitute DISTRO_REL=$(DISTRO_REL) \
		--url $(PUBLISH_URL)/$(DISTRO) \
		--tag $(PUBLISH_TAG) \
		$(PUBLISH_EXTRA_ARGS)

.PHONY: test
test:
