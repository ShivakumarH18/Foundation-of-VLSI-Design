module uart(
input clk,
input rst,
input [7:0] data_in,
output [7:0] data_out,
output tx,
input rx
);