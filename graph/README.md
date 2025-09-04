The initial data source is the 182 VCD files in the `vcds` directory.

- [x] Use `vcd_to_df` to map the `vcd2df` package function over the vcds.
- [x] Use `df_to_sparse` to map the dataframes into _times-of-flow_ Series
- [x] Use `sparse_reduce` to produce the adjaceny matrix representation of the flow graph.
- [x] Use `paths` to construct `reduced/paths.json` from the _times-of-flow_ Series and the adjacency matrix.
- [ ] Use `flatten` to get a list of paths, rather than a tree.
