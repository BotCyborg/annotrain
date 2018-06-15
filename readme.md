# The Annotrain System

A version tracking system for training data sets and models for machine
learning systems.  
For more details see the general description below.

## The Annotrain Shell

### Prerequisites

The annotrain system requires python3.

### Running Annotrain Shell: ats

To run the annotrain shell -> open a terminal -> brows to the annotrain folder -> type command:

    python3 annotrain_shell.py

The shell should look like:

    ats>:

Press `<tb><tb>` to see the available commands.

Type `help` to view existing commands and their short description.

For example:

    ats>: help load

shows the usages of the load command.

## The Annotrain module

Tha annotrain module provides an api for building other systems using it. Keep an eye on this page to find out more when we provide them.

## General Description

### The problem

During machine learning development and research it is very common to have a data set with multiple different tag sets. For example, for example a single set of images might be tagged at different time for different things. We treat the image set and tag sets as different entities. This this gives us complete flexibility to version control and play around with data without loosing track or consistency. We illustrate this with the following example:

Let us assume that we have a set of images of roads we call the set `dA`.  
We have manually tagged each images of `dA` for cars we call this annotation set `aA-cars`.

Now we tag another set of image `dB` for bikes and call the annotation set `aB-bikes`. 

We can train a model `mA-cars` that uses the `dA` to learn to identify cars. 
and a model `mB-bikes` to identify Bikes. 

Now we might want to use the model `mB` on `dA` to identify the bikes and create an annotation set `aA-bike`  

Now we have two separate annotation sets for `dA`.

`aA-cars` : originally annotated by hand.
`aA-bikes` : annotated by the model system `mB`.

We might want to now combine `aA-cars` and `aA-bikes` and create a combined annotation set `aA-cars-bikes`. That tags both the cars and bikes of set `dA`.

Later we might train a model `mA-car-bikes`. But we also want to keep track of the fact that in the training set all the bikes are not hand tagged but tagged by another model.

One can see that for this simple example we have already created quite a few data sets and models. And things are getting difficult to keep track of which is what.

Annotrain provides a version tracking system that keeps track of all these different versions and their interrelations. 


