import warnings

warnings.filterwarnings("ignore")

from fastai import *  # import the FastAI v3 lib which includes pytorch
from fastai.vision import *  # import all of the computer vision related libs from vision

BATCH_SIZE = 64
IMG_SIZE = 224
WORKERS = 0
DATA_PATH_STR = "./dataset/"
DATA_PATH_OBJ = Path(DATA_PATH_STR)

tfms = get_transforms()  # standard data augmentation ()

data = (
    ImageList.from_folder(DATA_PATH_OBJ)  # get data from path object
    .split_by_rand_pct()  # separate 20% of data for validation set
    .label_from_folder()  # label based on directory
    .transform(tfms, size=IMG_SIZE)  # added image data augmentation
    .databunch(bs=BATCH_SIZE, num_workers=WORKERS)  # create ImageDataBunch
    .normalize(imagenet_stats)
)  # normalize RGB vals using imagenet stats


learn = cnn_learner(data, models.resnet34, metrics=accuracy, model_dir="./output/")
learn.fit_one_cycle(5, max_lr=slice(5.74e-03 / 10))

learn.save(file=Path("./output/model.pkl"))
