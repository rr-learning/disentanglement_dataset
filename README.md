## MPI3D Disentanglement datasets

MPI3D datasets have been introduced to benchmark representations learning algorithms across simulated and real-world environments. The first transfer learning results of unsupervised disentangled representations are presented in our [NeurIPS 2019 paper.](https://arxiv.org/abs/1906.03292) 
This dataset is also used in the [NeurIPS Disentanglement Challenge.](http://www.disentanglement-challenge.com)
If you use this dataset in your work then kindly cite us.
```
@article{gondal2019transfer,
  title={On the Transfer of Inductive Bias from Simulation to the Real World: a New Disentanglement Dataset},
  author={Gondal, Muhammad Waleed and W{\"u}thrich, Manuel and Miladinovi{\'c}, {\DJ}or{\dj}e and Locatello, Francesco and Breidt, Martin and Volchkov, Valentin and Akpo, Joel and Bachem, Olivier and Sch{\"o}lkopf, Bernhard and Bauer, Stefan},
  journal={arXiv preprint arXiv:1906.03292},
  year={2019}
}
```

There are three different datasets:
  
1. Simplistic rendered images (mpi3d_toy).
2. Realistic rendered images (mpi3d_realistic).
3. Real world images (mpi3d_real).

Each dataset consists of 1036800 images, corresponding to all possible combinations of the following factors of variation:

|Factors|Possible Values|
|---|---|
|object_color|white=0, green=1, red=2, blue=3, brown=4, olive=5|
|object_shape|cone=0, cube=1, cylinder=2, hexagonal=3, pyramid=4, sphere=5|
|object_size|small=0, large=1|
|camera_height|top=0, center=1, bottom=2|
|background_color|purple=0, sea green=1, salmon=2|
|horizontal_axis|0,...,39|
|vertical_axis|0,...,39|

So far we only provide the datasets in 64x64 resolution. Higher resolution versions will be made available in near future.

If you use python, this means that once the data is loaded into a numpy array you can use array.reshape([6,6,2,3,3,40,40,64,64,3]) to obtain an array where first 7 dimensions corresponds to data generative factors as in table above and the last three to the image dimensions.

For loading the dataset you may make use of the python scripts in this repository. 
## Links to datasets

1. mpi3d_toy (simplistic rendered):  [link](https://storage.googleapis.com/disentanglement_dataset/Final_Dataset/mpi3d_toy.npz)

2. mpi3d_realistic (realistic rendered): [link](https://storage.googleapis.com/disentanglement_dataset/Final_Dataset/mpi3d_realistic.npz)

3. mpi3d_real (real-world images): [link](https://storage.googleapis.com/disentanglement_dataset/Final_Dataset/mpi3d_real.npz) 

## License

This work is licensed under a Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0/).
