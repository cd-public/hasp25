module test;

  reg        clk = 0;
  wire [7:0] val;

  initial begin
     $dumpfile("test.vcd");
     $dumpvars(0,test);
     #10 $finish;
  end

  always #1 clk = !clk;

  unit u (val, clk);

endmodule // test
