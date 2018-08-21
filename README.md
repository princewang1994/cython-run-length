# A Cython implement run-length

In some segmentation tasks in [Kaggle](), it will use `run length` endoding on pixel values for compressing prediction files. Both TGS and [DSB]() use this standard.  It is a greate idea to use  python implement in some {Kaggle Kernels](), such as https://www.kaggle.com/bguberfain/unet-with-depth. But as the number of testing data growing larger, these python codes will become bottleneck of your system, which slow down your submisson. Here is a cython accelerated mask-to-runlength code. Hope it will help Kagglers.

## Getting Started



### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds


## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
