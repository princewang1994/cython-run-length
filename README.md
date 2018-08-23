# A Cython implement run-length

In some segmentation tasks of [Kaggle](https://www.kaggle.com/), it will use `run-length` encoding on pixel values for compressing prediction files. Both [TGS](https://www.kaggle.com/c/tgs-salt-identification-challenge) and [DSB](https://www.kaggle.com/c/data-science-bowl-2018#evaluation) use this standard.  It is a greate idea to use  python implement in some [Kaggle Kernels](https://www.kaggle.com/c/tgs-salt-identification-challenge/kernels), such as [unet-with-depth](https://www.kaggle.com/bguberfain/unet-with-depth). But as the number of testing data growing larger, these python codes will become bottleneck of your system, which slow down your submisson. Here is a cython accelerated mask-to-runlength code. Hope it will help Kagglers.

## Getting Started

Clone this repository:

```shell
$ git clone https://github.com/princewang1994/cython-run-length.git
```

### Prerequisites

For using this code, it need some python packages, run following command to install dependencies. 

```shell
$ pip install -r requirements.txt
```

### Compile

Cython code need compiled with setup.py, run `make` to build it:

```shell
$ cd rlen
$ make
```

### Convert your prediction

You can use `from rlen import make_submission` in your projects to conver your prediction to run-length format. Here is declaration:

```python
def make_submission(preds, names, fast=True, path='submission.csv')
```

### Parameters: 

- `preds`: (list of np.array), [pred1, pred2, ...] each sized [H, W]
- `names`: (list), [name1, name2, ...]
- `fast`: (bool), flag of using Cython accelerate
- `name`: (str), path of submission csv file, default = 'submission.csv'


## Running the tests

`test_rlen.py` is an example of using `make_submission`, before testing it, make sure that `tqdm` and `pandas` is install again. Then it need a `train.pkl`, you can download from https://drive.google.com/file/d/1op6WD4X91uWqf-FLI7b7X0AQNV2wGyC6/view?usp=sharing, and put it on `$RLEN_HOME`.

**Attention: for using this train.pkl, please make sure that you are using python3, or you should make your own pickle following `tgs_pickle.ipynb`** 

- run `test_rlen.py`, it will generate `slow_submission.csv` and `fast_submission.csv`, see that fast version accelerates it near 200 times.

``` shell
$ cd $RLEN_HOME
$ python test_rlen.py
100%|█████████████████████████████████████████████████| 4000/4000 [00:00<00:00, 14292.84it/s]
Exporting to fast_submission.csv.
Done.
100%|████████████████████████████████████████████████████| 4000/4000 [00:51<00:00, 77.36it/s]
Exporting to slow_submission.csv.
Done.
```

- Then test whether they have the same contents:

```shell
diff slow_submission.csv fast_submission.csv 
```

if there is no output, done.

## Author

* **Prince Wang**: http://blog.prince2015.club
* **Github**: https://github.com/princewang1994

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [unet-with-depth](https://www.kaggle.com/bguberfain/unet-with-depth)
