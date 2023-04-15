# COMP6721-Winter2023-GroupA

# Contents

1. [Introduction](#Introduction)
2. [Downloading Datasets](#Downloading-Datasets)
   - [Animal With Attributes2](#Animal-With-Attributes-2)
   - [Animal 10](#Animal-10)
   - [Animal Faces](#Animal-Faces)
3. [How to Run](#How-to-Run)
   - [Installing Requirements](#Installing-Requirements)
   - [Sample Dataset](#Sample-Dataset)
   - [Training From Scratch](#Training-From-Scratch)
   - [Using a Pretrained Model](#Using-a-Pretrained-Model)
4. [Acknowledgment](#Acknowledgment)

# Introduction

The present research project was undertaken as a component of the Applied Artificial Intelligence (COMP6721) course that was taught at Concordia University during the Winter 2023 semester. The main objective of this study is to conduct a comparative analysis of various established Convolutional Neural Network (CNN) architectures in the context of Animal Classification.

# Downloading Datasets

Note that to split the dataset we use a python script. Make sure to see [Installing Requirements](#Installing-Requirements) section prior to running the script.

## Animal With Attributes 2

An overview of the dataset used in this study is available [here](https://cvml.ista.ac.at/AwA2/). This dataset, which is the largest among all other datasets utilized, can be downloaded from [here](https://cvml.ista.ac.at/AwA2/AwA2-data.zip). The size of the compressed dataset is approximately 13GB. After downloading, the dataset can be extracted to any desired folder. Next, to split the dataset into train, test, and validation subsets, the script available [here](https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/blob/main/src/awa2/mnetv1/preprocess_raw_data.py) (with the path to the dataset updated accordingly) can be run. It should be noted that only 11 specific classes were utilized in this study, namely antelope, cow, deer, elephant, giraffe, horse, lion, rabbit, sheep, squirrel, and zebra. Therefore, prior to executing the script to split the dataset, any unnecessary class folders can be directly deleted.

## Animal 10

This dataset is available on the kaggle and can be accessed via [this](https://www.kaggle.com/datasets/alessiocorrado99/animals10) link. Similar to stated above after downloading and extracting the dataset, run [this](https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/blob/main/src/awa2/mnetv1/preprocess_raw_data.py) script to split the dataset. Again do not forget to change the path pointing to the dataset in the script. We used the following classes: Spider, Horse, Dog, Elephant, Sheep, Cow, Squirrel, and Cat. The folders for the rest of the classes can be deleted prior to running the script.

## Animal Faces

This dataset is available on the kaggle and can be accessed via [this](https://www.kaggle.com/datasets/andrewmvd/animal-faces) link. During our study, we used all of the classes available in the dataset. Again, to split the dataset run run [this](https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/blob/main/src/awa2/mnetv1/preprocess_raw_data.py) script.

# How to Run

## Installing Requirements

You can find all the requirements to run the project in [this](https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/blob/main/requirements.txt). To install the requirement run the following command:

```
pip install -r requirements.txt
```

These requirements file does not include the pytorch. To install it you can go to [this link](https://pytorch.org/get-started/locally/) and generate an appropriate command to install the pytorch.

## Sample Dataset

A sample dataset has been included in [this](https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/blob/main/sample_dataset/) folder, along with the code. The dataset is divided into three folders: awa2, animal10, and animalfaces, each containing three subfolders: train, test, and val. The dataset includes three images for each of the categories and can be used to run the project without having to download the entire dataset. Note that you may still have to change the paths pointing to the datasets wherever necessary. Usually the paths are defined in the first cell of the notebook.

## Training From Scratch

Generally we followed this training workflow:

1. Train the model from scratch. While training, save training logs and models at each epoch in a csv file. You can use these notebooks to train models from scratch:

| Dataset      | MobilenetV2                                                                                                                      | VGG11                                                                                                                              | Resnet18                                                                                                            |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Awa2         | [notebook](https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/blob/main/src/awa2/mnetv1/new/main.ipynb)                    | [notebook](https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/blob/main/src/awa2/vgg11/main.ipynb)                           | [notebook](https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/blob/main/src/awa2/resnet18/main.ipynb)         |
| Animal 10    | [notebook](https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/blob/main/src/Animal-10/Mobilenet/animal-10-mobilenet.ipynb) | [notebook](https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/blob/main/src/Animal-10/VGG/animal-10-vgg-adam.ipynb)          | [notebook](https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/blob/main/src/Animal-10/resnet/animal-10.ipynb) |
| Animal Faces | [notebook](https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/tree/main/src/animal_faces/mobilenet)                        | [notebook](<https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/blob/main/src/animal_faces/vgg/animal-faces-vgg%20(1).ipynb>) | [notebook](https://github.com/imdeep2905/COMP6721_Winter2023_GroupA/blob/main/src/animal_faces/Resnet/main.ipynb)   |

Please make sure to change the path pointing to the dataset accordingly.

2. After the training is completed, load the trained model and CSV file to create graphs, confusion matrices, and other relevant data.

## Using a Pretrained Model

We have uploaded some of the models we trained. This pretrained models can be used to observe our model's performance without having to train them from the beginning. We have also uploaded some notebooks demonstrating this in [this](to-be-added) folder. You can run any of the notebooks to see our models in action!

# Acknowledgment

We would like to thank Dr. Mahdi S. Hosseini for the highly effective course instruction, as well as to all of the Teaching Assistants who provided guidance and support throughout the project.
