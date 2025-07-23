module unit(out, clk);
  input            clk;
  output reg [7:0] out;
  reg        [7:0] key;
  reg        [7:0] one;
  reg        [7:0] two;
  reg        [7:0] cnt;

  initial begin
    key = 8'hA1; // Secret
    cnt = 0;
  end

  always @(posedge clk) begin
    cnt <= cnt + 1;
    if (cnt == 1) 
      one <= key;
    else if (cnt == 2)
      two <= key;
    else if (cnt == 3)
      out <= two;
  end

endmodule // unit
