// Not graceful.

module unit_one(out, clk);

  input            clk;
  output reg [7:0] out;
  reg              out_t;
  reg        [7:0] key;
  reg              key_t;
  reg        [7:0] one;
  reg              one_t;
  reg        [7:0] two;
  reg              two_t;
  reg        [7:0] cnt;

  initial begin
    key   = 8'hA1;
    key_t = 0;
    one_t = 1;
    two_t = 0;
    out_t = 0;
    cnt   = 0;
  end

  always @(posedge clk) begin
    cnt <= cnt + 1;
    if (cnt == 1) 
      begin
        one <= key;
        one_t <= key_t | one_t;
      end
    else if (cnt == 2)
      begin
        two <= key;
        two_t <= key_t | two_t;
      end
    else if (cnt == 3)
      begin
        out <= two;
        out_t <= two_t | out_t;
      end
  end

endmodule // unit_one


module unit_two(out, clk);

  input            clk;
  output reg [7:0] out;
  reg              out_t;
  reg        [7:0] key;
  reg              key_t;
  reg        [7:0] one;
  reg              one_t;
  reg        [7:0] two;
  reg              two_t;
  reg        [7:0] cnt;

  initial begin
    key   = 8'hA1;
    key_t = 0;
    one_t = 0;
    two_t = 1;
    out_t = 0;
    cnt   = 0;
  end

  always @(posedge clk) begin
    cnt <= cnt + 1;
    if (cnt == 1) 
      begin
        one <= key;
        one_t <= key_t | one_t;
      end
    else if (cnt == 2)
      begin
        two <= key;
        two_t <= key_t | two_t;
      end
    else if (cnt == 3)
      begin
        out <= two;
        out_t <= two_t | out_t;
      end
  end

endmodule // unit_two