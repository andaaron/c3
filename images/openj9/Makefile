include ../../config.mk
include ../../config_java.mk
include ../../config_busybox.mk
include ../../tools.mk

ifeq ($(strip $(PUBLISH_TAG)),)
override PUBLISH_TAG := $(shell echo $(OPENJDK) | awk -F "." '/1/ {print $$1}')
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
		--substitute DISTRO_REL=$(DISTRO_REL) \
		--substitute OPENJDK=$(OPENJDK) \
		--substitute OPENJ9=$(OPENJ9) \
		--substitute OPENJ9_JDK_HASH=$(OPENJ9_JDK_HASH) \
		--substitute OPENJ9_JRE_HASH=$(OPENJ9_JRE_HASH) \
		--substitute BUSYBOX=$(BUSYBOX)

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
		--substitute OPENJDK=$(OPENJDK) \
		--substitute OPENJ9=$(OPENJ9) \
		--substitute OPENJ9_JDK_HASH=$(OPENJ9_JDK_HASH) \
		--substitute OPENJ9_JRE_HASH=$(OPENJ9_JRE_HASH) \
		--substitute BUSYBOX=$(BUSYBOX) \
		--url $(PUBLISH_URL)/$(DISTRO) \
		--tag $(PUBLISH_TAG) \
		$(PUBLISH_EXTRA_ARGS)

.PHONY: test
test:
