## MPI3D Disentanglement Datasets

<img src="https://github.com/rr-learning/disentanglement_dataset/blob/master/sample_gifs/platform.jpg" width="418" height="280" /> <img src="https://github.com/rr-learning/disentanglement_dataset/blob/master/sample_gifs/platform2.jpg" width="418" height="281" />

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

## Datasets Information

There are following three different datasets. The gifs are created using [disentanglement_lib](https://github.com/google-research/disentanglement_lib) visualization tool.

### 1. Real world simple shapes (mpi3d_real).

<img src="https://github.com/rr-learning/disentanglement_dataset/blob/master/sample_gifs/real1.gif"/> <img src="https://github.com/rr-learning/disentanglement_dataset/blob/master/sample_gifs/real2.gif" />

### 2. Realistic rendered images (mpi3d_realistic).

<img src="https://github.com/rr-learning/disentanglement_dataset/blob/master/sample_gifs/realistic1.gif" /> <img src="https://github.com/rr-learning/disentanglement_dataset/blob/master/sample_gifs/realistic2.gif" />

### 3. Simplistic rendered images (mpi3d_toy).

<img src="https://github.com/rr-learning/disentanglement_dataset/blob/master/sample_gifs/toy1.gif" /><img src="https://github.com/rr-learning/disentanglement_dataset/blob/master/sample_gifs/toy2.gif" />

Each dataset consists of 1,036,800 images, corresponding to all the possible combinations of the following factors of variation:

|Factors|Possible Values|
|---|---|
|object_color|white=0, green=1, red=2, blue=3, brown=4, olive=5|
|object_shape|cone=0, cube=1, cylinder=2, hexagonal=3, pyramid=4, sphere=5|
|object_size|small=0, large=1|
|camera_height|top=0, center=1, bottom=2|
|background_color|purple=0, sea green=1, salmon=2|
|horizontal_axis|0,...,39|
|vertical_axis|0,...,39|

So far we only provide the datasets in 64x64 resolution. Higher resolution versions will be made available in the near future.

## Reading the Datasets
The datasets are provided in the form of numpy arrays. Once the data is loaded, you can use array.reshape([6,6,2,3,3,40,40,64,64,3]) to obtain an array where the first 7 dimensions corresponds to data generative factors as in the table above and the last three to the image dimensions.

```
import numpy as np
data = np.load('./mpi3d_real.npz')['images']

# To visualize each factor of the data independently, you can reshape 
# the array as the following.

data = data.reshape([6,6,2,3,3,40,40,64,64,3])
```

## Downloads

Use the following links to download the datasets. 

1. mpi3d_toy (simplistic rendered):  [link](https://storage.googleapis.com/disentanglement_dataset/Final_Dataset/mpi3d_toy.npz)
2. mpi3d_realistic (realistic rendered): [link](https://storage.googleapis.com/disentanglement_dataset/Final_Dataset/mpi3d_realistic.npz)
3. mpi3d_real (real-world images): [link](https://storage.googleapis.com/disentanglement_dataset/Final_Dataset/mpi3d_real.npz)
4. mpi3d_real_complex (real-world complex shapes images) : __ not published yet __

## Feedback
Please send any feedback to waleed.gondal@tue.mpg.de

## License

This work is licensed under a Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0/).
