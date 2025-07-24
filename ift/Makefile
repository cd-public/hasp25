all: build
	vvp unit -vcd

build:
	iverilog -o unit test.v design.v

clean:
	rm unit
