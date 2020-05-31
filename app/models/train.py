import warnings

warnings.filterwarnings("ignore")

from fastai import *  # import the FastAI v3 lib which includes pytorch
from fastai.vision import *  # import all of the computer vision related libs from vision

import os

BATCH_SIZE = 64
IMG_SIZE = 224
WORKERS = 0
DATA_PATH_STR = "./dataset/parkinsons-drawings/spirals"

tfms = get_transforms()  # standard data augmentation ()

data = ImageDataBunch.from_folder(
    path=DATA_PATH_STR,
    train=os.path.join(DATA_PATH_STR, "training"),
    valid=os.path.join(DATA_PATH_STR, "testing"),
).normalize(imagenet_stats)


learn = cnn_learner(data, models.resnet34, metrics=accuracy, model_dir="./output/")
learn.fit_one_cycle(5, max_lr=slice(5.74e-03 / 10))

learn.save(file=Path("./output/model.pkl"))
