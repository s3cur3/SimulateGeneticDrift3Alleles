Instructions for using the Drift Simulator
==========================================
By Young, Gibson, Jennings, and Smith


To run the drift simulator, first make sure you're in a *nix
environment (Linux or Mac OS). Then, do the following:

1. Unzip the zip.
2. Modify the `team_2_settings.py` file as appropriate (to fit the
species you're simulating). Note that we use this settings file
instead of taking input from the keyboard at runtime, since the input
can get quite complicated.
3. Open a command prompt (a.k.a. a Terminal window)
4. Type the following (where the `$` indicates the command line
waiting for input):
	- `$ cd <whatever directory you unzipped the file to>`
	- `$ python3 team_2_main.py`
5. The program will churn for a bit (potentially a long time if you
set either a large population size or a large number of
generations). Eventually, it will output some data on the frequency of
events across all your simulations. This statistical data, along with
the individual charts of allele frequencies over time that it was
derived from, are saved to the `output` directory.
6. To plot your data, you can start with the sample Gnuplot
scripts. To run the one that plots only 1 allele from each of 10
simulations, type the following in to the same command prompt from
above:
	- `$ gnuplot plot_100_gens_1_allele_only.gp`
7. Modify those `.gp` scripts as you see fit to get a different
picture of the data.

