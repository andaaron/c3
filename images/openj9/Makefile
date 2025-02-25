include ../../config.mk
include ../../config_java.mk
include ../../config_busybox.mk
include ../../tools.mk

ifeq ($(strip $(PUBLISH_TAG)),)
override PUBLISH_TAG := $(shell echo $(OPENJDK) | awk -F "." '/1/ {print $$1}')
endif

LAYER_SUFFIX :=
ifeq ($(LAYER_TYPE),squashfs)
LAYER_SUFFIX := "-squashfs"
endif

PUBLISH_IMAGE_NAME := $(shell basename $$(pwd))-$(ARCH)

.DEFAULT_GOAL := all

.PHONY: all
all: build test

.PHONY: build
build: $(STACKER)
	$(STACKER_WITH_BUILD_DIR) \
		build -f stacker.yaml \
		--layer-type $(LAYER_TYPE) \
		--substitute LAYER_SUFFIX=$(LAYER_SUFFIX) \
		--substitute BUILD_OCI_DIR=$(BUILD_OCI_DIR) \
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
		--layer-type $(LAYER_TYPE) \
		--substitute LAYER_SUFFIX=$(LAYER_SUFFIX) \
		--substitute BUILD_OCI_DIR=$(BUILD_OCI_DIR) \
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
		$(PUBLISH_TAGS_ARGS) \
		$(PUBLISH_CREDS) \
		$(PUBLISH_EXTRA_ARGS)

.PHONY: pkgs
pkgs: $(STACKER)
	$(STACKER_WITH_BUILD_DIR) \
		build -f stacker-pkgs.yaml \
		--layer-type $(LAYER_TYPE) \
		--substitute IMG_DIR=$$(pwd) \
		--substitute OS=$(OS) \
		--substitute ARCH=$(ARCH) \
		--substitute DISTRO=$(DISTRO) \
		--substitute DISTRO_REL=$(DISTRO_REL)

.PHONY: test
test:

.PHONY: pull
pull:
	skopeo copy $(PULL_EXTRA_ARGS) $(PUBLISH_URL)/$(strip $(DISTRO))/$(strip $(PUBLISH_IMAGE_NAME)):$(PUBLISH_TAG)$(LAYER_SUFFIX) oci:$(BUILD_OCI_DIR):$(PUBLISH_IMAGE_NAME)$(LAYER_SUFFIX)
