dcl_stats_n\_plots
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

This repository is part of the **DCLwidgets** series. These repositories
are dedicated to foster the joint development of tools and resources by
the [Defense Circuits Lab](https://www.defense-circuits-lab.com/). The
intended use of each tool may vary greatly from very lab- and/or
analysis-specific problems, to tools and resources that may be of use
also for other researchers. The common goal for each repository,
however, is to provide the tool as an interactive, userfriendly, and
intuitive GUI (usually based on
[ipywidgets](https://ipywidgets.readthedocs.io/en/stable/), hence the
name), such that the user needs little to no coding expertise.

List of all repositories of the DCLwidgets series: <br>

- [dcl_stats_n\_plots](https://github.com/DSegebarth/dcl_stats_n_plots/):
  A widget to compute statistics and plot the data with several options
  to customize the plot
- [DCL_to_NWB](https://github.com/DSegebarth/DCL_to_NWB/): A widget to
  convert datasets acquired in the DCL into the NWB file format
- [BSc_MS](https://github.com/DSegebarth/BSc_MS/): A widget to annotate
  the corners of a maze within video files and save the corresponding x-
  and y-coordinates

------------------------------------------------------------------------

## About this widget

The purpose of this widget is to make everyday life in the lab a little
easier, as it helps you to compute statistical tests and to create
highly customizable plots that visualize your data. The widget also
enables you to select exactly which statistical results you would like
to annotate within the plots. This way, statistical analysis and
visualization of your data is what it should be - simple & fast!

Please get in touch if you have any feedback, questions, or feature
requests for us!

------------------------------------------------------------------------

## Installation

### Using conda:

Although the `dcl_stats_n_plots` package itself is only available on
[PiPy](https://pypi.org/project/dcl-stats-n-plots/), we yet recommend
installation via conda - especially if you would like to use the GUI.
Simply recreate the conda environment on your local machine by running
the following command in your command line or terminal (e.g. Anaconda
prompt). You can find the corresponding “environment.yml” file in the
GitHub repo
([here](https://github.com/DSegebarth/dcl_stats_n_plots/blob/master/environment.yml)).
Just make sure to place the file either in the current working directory
(usually displayed at the beginning of each line in your terminal), or
to provide the entire filepath (e.g. something like:
“C:\Users\dsege\Downloads\environment.yml”):

With the “environment.yml” file in your current working directory: <br>

> conda env create -file environment.yml

With the “environment.yml” file in a different directory: <br>

> conda env create -file PATH\TO\THE\FILE\environment.yml

This will install all dependencies that are required to use
`dcl_stats_n_plost`, including its GUI version.

<div>

> **Note**
>
> This installation was so far only tested on Linux (Ubuntu 20.04.4)
> using conda 22.9.0

</div>

<div>

> **Note**
>
> If you would like to contribute to the development of
> `dcl_stats_n_plost` you are more than welcome! On top of the regular
> user installation, you will, however, also need to install `nbdev` in
> the same environment. Simply follow all the steps above and once you
> have verified that everything was installed correcty, simply run in
> the same conda environment:
>
> > conda install -c fastai nbdev
>
> If you are new to `nbdev`, you´d probably also want to check out their
> comprehensive tutorials and walkthroughs
> [here](https://nbdev.fast.ai/tutorials/). I will also add some more
> contribution guidelines to this repository soon. In the meantime, feel
> free to get in touch! :-)

</div>

### Using pip:

Despite the `dcl_stats_n_plots` package itself is only available via
pypi.org, we still highly recommend to follow the installation
guidelines “using conda” above, especially if you´d like to use its GUI
functionalities. If you´d still want to go down this route, here´s your
install command:

> pip install dcl-stats-n-plots

## How to use

.. the documentation, including the comprehensive tutorials, is
currently being updated ..

## Next steps

There are some major reorganizations planned:

1)  This repository will be shifted / forked / re-created under the
    recently established GitHub organisations page of the Defense
    Circuits Lab, i.e. somewhere
    [here](https://github.com/orgs/Defense-Circuits-Lab/repositories)
2)  When this migration is performed, the new repository (ideally also
    the package) will be renamed to `stats_n_plots` as the prefix to
    link it to the DCL will no longer be required
3)  Once the migration was successfully completed, the documentation
    will be updated to eventually match the “refactored” version, which
    actually already includes some new statistical tests compared to the
    old version, as well as additional functions inteded to improve
    usability (like exporting & importing your current plotting
    settings)
4)  Finally, once the documentation regarding the usage of
    `dcl_stats_n_plots` was updated, I will add some information and
    guidelines for contribution to this package

Once the steps listed above are all completed, there are plenty of ideas
for how to continue developing this package further:

- integrate tests (especially with the improved CI of nbdev v2 and also
  once additional contributors join)
- add additional statistical tests & plots (e.g. Kolmogorov-Smirnov test
  for goodness of fit for cumulative probability functions, or linear &
  linear mixed effect models, ..)
- add additional customization options (optional hue column, fonts, ..)
- improve how configs are export and imported, ideally to include all
  settings (type of plot, color scheme, …)
- create DCL-default configs
- fix bugs ;-)
