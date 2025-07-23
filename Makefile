all: build
	vvp unit -vcd

build:
	iverilog -o unit testbench.v design.v

