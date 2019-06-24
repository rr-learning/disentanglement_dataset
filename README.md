# Disentanglement datasets

There are three different datasets: 
1. The first one consists of simplistic rendered images, 
2. the second consists of realistic rendered images and 
3. the third one consists of real images.

Each dataset consists of 460800 images corresponding to all possible combinations of the following factors of variation:

|Factors|Possible Values|
|---|---|
|object_color|green=0, red=1, blue=2, brown=3|
|object_shape|cone=0, cube=1, hexagonal prism=2, sphere=3|
|object_size|small=0, large=1|
|camera_height|top=0, center=1, bottom=2|
|background_color|purple=0, sea green=1, salmon=2|
|horizontal_axis|0,...,39|
|vertical_axis|0,...,39|

Each image has as filename padded_index.png where  
index = object_color * 115200 + object_shape * 28800 + object_size * 14400 + camera_height * 4800 + background_color * 1600 + horizontal_axis * 40 + vertical_axis  
padded_index = index padded with zeros such that it has 6 digits.

If you use python, this means that once the data is loaded into a numpy array you can use array.reshape([4,4,2,3,3,40,40]) to obtain an array where each dimension corresponds to a factor.

For more details on the dataset please consult https://arxiv.org/abs/1906.03292. For loading the dataset you may make use of the python scripts in this repository. If you use this dataset then kindly cite us.
```
@article{gondal2019transfer,
  title={On the Transfer of Inductive Bias from Simulation to the Real World: a New Disentanglement Dataset},
  author={Gondal, Muhammad Waleed and W{\"u}thrich, Manuel and Miladinovi{\'c}, {\DJ}or{\dj}e and Locatello, Francesco and Breidt, Martin and Volchkov, Valentin and Akpo, Joel and Bachem, Olivier and Sch{\"o}lkopf, Bernhard and Bauer, Stefan},
  journal={arXiv preprint arXiv:1906.03292},
  year={2019}
}
```
## Links to datasets

simplistic rendered:  https://storage.cloud.google.com/disentanglement_dataset/sim_toy_ordered.tar.gz  
realistic rendered:  _not yet published_  
real images:  _not yet published_  
