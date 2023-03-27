TOP_LEVEL=$(shell git rev-parse --show-toplevel)
TOOLS_DIR := $(TOP_LEVEL)/hack/tools
TOOLS_BIN_DIR := $(TOOLS_DIR)/bin
BUILD_DIR := $(TOP_LEVEL)/build

export STACKER := $(TOOLS_BIN_DIR)/stacker

STACKER_WITH_BUILD_DIR := $(STACKER) --stacker-dir $(BUILD_DIR)/.stacker --oci-dir $(BUILD_DIR)/oci --roots-dir $(BUILD_DIR)/roots

$(STACKER):
	mkdir -p $(TOOLS_BIN_DIR)
	curl -fsSL https://github.com/project-stacker/stacker/releases/latest/download/stacker -o $@
	chmod +x $@

.PHONY: clean
clean: $(STACKER)
	$(STACKER_WITH_BUILD_DIR) clean

.PHONY: tag
tag:
	@echo $(PUBLISH_TAG)
