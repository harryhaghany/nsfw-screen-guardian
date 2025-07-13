from fastai.vision.all import *

# Path to dataset
path = Path("/Users/harryhaghani/Downloads/nsfw_dataset_v1")

dls = ImageDataLoaders.from_folder(
    path,
    train='.',    # assumes subfolders are class names
    valid_pct=0.2, # split 20% of data for validation
    item_tfms=Resize(128),
    batch_tfms=aug_transforms(mult=1.0)
)

print("Classes:", dls.vocab)

learn = cnn_learner(dls, resnet1, metrics=accuracy)

# Train the model
learn.fine_tune(5)

        
