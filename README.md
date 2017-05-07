# Emlyn's IPython Notebooks

A collection of ipython notebooks that I've authored for demonstration
and presentation purposes.

You can view any of the presentations using the NBViewer website. You
concatenate the github URL to the NBViewer URL and it REST-magically
lets you view the presentation! Alternatively use the links below

## List of presentations

The links take you to a view of the presentation on NBViewer.com

<dl> <dt><a
  href="http://nbviewer.jupyter.org/github/EmlynC/emlyn-ipython-notebooks/blob/master/Matlab%20to%20Python/emlyn_matlab-to-python.ipynb">Python
  as an alternative to MATLAB in life sciences; transliterating your
  experiments and interfacing hardware.</a></dt> <dd><p>A talk on
  moving experiments that you write in MATLAB to the Python scientific
  stack</p>

<span style="font-weight: strong">List of appearances</span> <ul> <li><a
href="http://www.meetup.com/PyData-London-Meetup/events/179396812/">2014-06-03
PyDataLondon Celebratory First Meetup</a></li> </ul>

  </dd>
</dl>

## How to view the slides in presentation mode?

If you'd like to convert the slides into a presentation then use the
following command

```bash
ipython nbconvert --to slides --post serve <NAME OF THE NOTEBOOK>.ipynb
```

This converts ipython notebook into Reveal.js slides and the --post
arguement fires off a simple webserver so you can view it all at once.
