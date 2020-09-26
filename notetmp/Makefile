CXX := g++
CXXFLAGS := -g -Wall -Wundef -Wswitch-enum -Wswitch-default -Wfloat-equal -Wendif-labels -Wlogical-op -Winit-self -Wredundant-decls
CLEANER := cpytmp.sh
CURRENT_DIR := notetmp/

build: ## compile a script ("nscr" has to be given in command line argument)
	$(CXX) $(CXXFLAGS) note$(nscr)tmp.cpp -o $(nscr).out
run: ## run a binary ("nscr" and "param" have to be given in command line argument)
	./$(nscr).out $(param)
clean: ## reset scripts and remove binaries
	cd .. && bash $(CLEANER) && cd $(CURRENT_DIR)
	rm -f *.out
	rm -f core
clean-simple: ## remove scripts, remove binaries and use a simpler template
	cd .. && bash $(CLEANER) 1 && cd $(CURRENT_DIR)
	rm -f *.out
	rm -f core
help: ## print this message
	@echo "Usage: make SUB_COMMAND argument_name=argument_value"
	@echo ""
	@echo "Command list:"
	@echo ""
	@printf "\033[36m%-30s\033[0m %-50s %s\n" "[Sub command]" "[Description]"
	@grep -E '^[/a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | perl -pe 's%^([/a-zA-Z_-]+):.*?(##)%$$1 $$2%' | awk -F " *?## *?" '{printf "\033[36m%-30s\033[0m %-50s %s\n", $$1, $$2, $$3}'