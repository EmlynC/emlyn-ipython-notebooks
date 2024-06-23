# Emlyn's IPython Notebooks

A collection of ipython notebooks that I've authored for demonstration
and presentation purposes. You are welcome to use the information within as you wish, although do note that some of it was lifted from
elsewhere so I ask that you respect the original cited work.

## List of presentations

### (2014) Python as an alternative to MATLAB in life sciences; transliterating your experiments and interfacing hardware.

A talk on moving experiments that you write in MATLAB to the Python scientific
stack, [here is the notebook](./matlab_to_python/matlab_to_python.ipynb)

[PyDataLondon Celebratory First Meetup](http://www.meetup.com/PyData-London-Meetup/events/179396812/)

### (2017) Analysing the ElectroCardioGram (ECG)

A talk on how to analyse the ECG with Python, [here is the notebook](./analysing_ecg/analysing_ecg.ipynb)

It was presented at PyData London 2017, [here is the YouTube video of it](https://www.youtube.com/watch?v=WyjGCEWU4zY).

### (2024)

## How to view the slides in presentation mode?

If you'd like to convert the slides into a presentation then use the
following command

```bash
ipython nbconvert --to slides --post serve <NAME OF THE NOTEBOOK>.ipynb
```

This converts ipython notebook into Reveal.js slides and the --post
arguement fires off a simple webserver so you can view it all at once.
