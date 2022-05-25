Preparation in advance:
1. Download IAPR TC-12.
2. Download pretrained models from https://github.com/microsoft/MASS.

Data preprocessing:
1. Use ``feature-extractor'' script from Multi30k dataset to extract visual encodings ``iaprtc12-res4frelu.npy'' from the images. Instructions are included in the script.
(https://github.com/multi30k/dataset/blob/master/scripts/feature-extractor)
2. Follow the instructions in the project ``OpenKE'' to extract knowledge embeddings ``ent_embedding'' from WN18RR. After training the TransE, it will be located in ``checkpoint'' folder.
(https://github.com/thunlp/OpenKE)

Training and Evaluating:
Modify tc12_training.sh before running it.

Source structure:
./: scripts for preprocessing, training, inference
./src/: trainer (training methods) and misc.
./src/data/: data loading
./src/evaluation: evaluator
./src/model: the Transformer model
./src/openke: codes to make use of TransE embeddings
