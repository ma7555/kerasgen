### UPDATE: This repo is archived. The task can now be done with [TFDataSampler](https://github.com/tensorflow/similarity/blob/dc506d63d05d012d3496041c25c1c54981d39565/tensorflow_similarity/samplers/tfdata_sampler.py#L135).

kerasgen
========
[![Latest PyPI version](https://img.shields.io/pypi/v/kerasgen.svg)](https://pypi.python.org/pypi/kerasgen)
[![DOI](https://zenodo.org/badge/454812299.svg)](https://zenodo.org/badge/latestdoi/454812299)

A Keras/Tensorflow compatible image data generator for creating balanced batches.
This datagenerator is compatible with TripletLoss as it guarantees the existence of postive pairs in every batch.

Installation
------------
```bash
pip install kerasgen
```

Usage
-----
```python
from kerasgen.balanced_image_dataset import balanced_image_dataset_from_directory

train_ds = balanced_image_dataset_from_directory(
    directory, num_classes_per_batch=2,
    num_images_per_class=5, image_size=(256, 256),
    validation_split=0.2, subset='training', seed=555,
    safe_triplet=True)

val_ds = balanced_image_dataset_from_directory(
    directory, num_classes_per_batch=2,
    num_images_per_class=5, image_size=(256, 256),
    validation_split=0.2, subset='validation', seed=555,
    safe_triplet=True)
```

Generates a balanced per batch `tf.data.Dataset` from image files in a directory.

  Your directory structure should be:

  ```
  main_directory/
  ...class_a/
  ......a_image_1.jpg
  ......a_image_2.jpg
  ...class_b/
  ......b_image_1.jpg
  ......b_image_2.jpg
  ```

  Behind the scenes, this module creates a different dataset for every class and by using weighted random sampling, some random classes `(num_classes_per_batch)` are drawn and a specific number of images is selected from every choosen class `(num_images_per_class)` as long as there are enough samples from this class.

  If there is no enough samples remaining from the choosen class, it is skipped and another class is choosen (This behaviour can be disabled and we indefinitely repeat the classes datasets) 
  
  Setting `safe_triplet` to `False` (Default) makes sure that every image is seen exactly one time per epoch but it does not guarantee a fixed num_classes_per_batch or num_images_per_class in later batches.

  Setting `safe_triplet` to `True` does not guarantee that every epoch will include all different samples from the dataset. But as sampling is weighted per class, every epoch will include a very high percentage of the dataset and should approach 100% as dataset size increases. This however guarantee that both num_classes_per_batch and num_images_per_class are fixed for all batches including later ones.

  If you are to use this generator with TripletLoss, your should either:
  * Set `safe_triplet` to `True`
  * Keep `safe_triplet` default `False` value but be careful with choosing the batch_size so you do not end up with a last batch containing a single class (or a single sample)

  Batch size is calculated by multiplying num_classes_per_batch and num_images_per_class.



Requirements
------------

* Tensorflow >= 2.9
* Numpy >= 1.19

Compatible with
-------------
* `tf.data.Dataset` API
* [TripletHardLoss](https://www.tensorflow.org/addons/api_docs/python/tfa/losses/TripletHardLoss)
* [TripletSemiHardLoss](https://www.tensorflow.org/addons/api_docs/python/tfa/losses/TripletSemiHardLoss)

Versions
--------
* v0.1.3: TF>= 2.9
* v0.1.2: TF>= 2.8
* v0.1.1: TF>= 2.7

Licence
-------
MIT

Authors
-------

`KerasGen` was written by [Mahmoud Bahaa](mailto:mah.alaa@nu.edu.eg?subject=[GitHub]%20KerasGen%20Support)

If you use this software, please cite it using the metadata from this `CITATION.cff`
