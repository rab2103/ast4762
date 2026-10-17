# Robyn Bauamnn
# AST4762 HW7
# October 10, 2026

# import necessarry libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
from hw7_rab_support_functions import box_function
from scipy.optimize import curve_fit

# Problem 2: Paper Summaries:

print('Paper 1: Map of the Day-Night Contrast of Extrasolar Planet HD189733b by H.A. Knutson et al')
print("""\tThis paper analyzed Spitzer Space Telescope data on HD189733b, an extrasolar planet that 
    orbits a K-type dwarf star. The goal of the study was to examine the day/side temperature 
    difference of the planet. It is a hot Jupiter that is close in orbit to the star, so it is 
    expected to be tidally locked. The analysis of light with a wavelength of 8 microns found 
    that the dayside temperature minimum at 973 +/- 33 K and a maximum at 1212 +/- 11 K. The data 
    also shows a time difference from the expected secondary eclipse of 120 +/- 24s, which the 
    authors believe could be due to a slightly eccentric eclipse. There was also an offset between 
    the minimum and maximum temperatures from the eclipse, suggesting strong atmospheric winds. 
    Further research is needed to investigate these variations and the non-uniform emission.\n""" )

print('Paper 2: The Broadband Infrared Emission Spectrum of the Exoplanet HD189733b by D. Charbonneau et al')
print("""\tThis paper also analyzes Spitzer Space Telescope Data on HD189733b in the wavelengths 
    3.6 microns, 4.5 microns, 5.8 microns, 8.0 microns, and 24 microns. The paper also pulls data 
    for 16 microns from another paper to analyze. The analysis found that there is an inconsistency 
    with Planck Spectrum models, and a better fit for the planet's spectrum are models that do not 
    include temperature inversion. This leads the researchers to believe hot Jupiters can be placed 
    into two categories, thermal inversion for hot Jupiters that are strongly irradiated and those 
    that do not. With.a chi-square fit of 1.00, the researchers found that HD189733b follows models 
    that did not assume redistribution of energy in the day-night atmosphere, and that the planet 
    could have an internal energy source to explain the spectra, and that the energy distribution is 
    likely wavelength dependent and depth dependent.They also found that there are spectral features 
    indicating H2O and CO in the atmosphere.\n""")

print('Paper 3: The Deep Blue Color of HD189733b: Albedo Measurements with HST/STIS at Visibly Wavelengths\n\
    by T.M. Evans et al.')
print("""\tHere researchers looked at data taken by the Space Telescope Imaging Spectrograph on the Hubble 
    Space Telescope in the 290-570 nm range to determine the geometric albedos of the extrasolar planet 
    HD189733b. They found an albedo of 0.40 +/- 0.12 in the wavelength range of 290-450 nm and an 
    albedo of less than 0.12 in the 450-570 nm range with a confidence of one standard deviation. 
    These albedos suggest an optically thick layer of clouds at an intermediate altitude on the 
    dayside of the tidally locked planet. There is likely sodium absorption in the atmosphere as 
    well, which would suppress the scattering of light beyond 450 nm. In the visibly light spectrum, 
    the planet would likely appear as a deep blue color. There is also a chance of MgSiO3 dust grains, 
    which are abundant in hot atmospheres, causing the scattering of light. While the star does have a 
    variation in light due to active sun spots, it was found that it would only contribute a fraction 
    of the difference in albedos observed, so the researchers concluded it was more likely the 
    atmosphere, clouds, and dust causing this difference in albedos across the different wavelengths.\n""")

print('Paper 4: Reteivals on NIRCam transmission & emission spectra of HD189733b with PLATON 6, a GPU code\n\
    for the JWST era by M. Zhang et al.')
print("""\tThis paper analyzes data in the 2.5-5.0 micron range from an emission and transmission spectra 
    obtained from the NIRCam system on JWST on the extrasolar planet HD189733b. The researchers then 
    developed an updated PLATON routine, which they called PLATON 6, to process the data faster, updated 
    analysis techniques, added support for emission spectroscopy, and added new models. PLATON 6 is 
    available for public use on GitHub. By using PLATON 6, researchers found that there is evidence of 
    H20, CO, CO2, and H2S in the atmosphere of HD189733b. They compared metallicity and C/O ratios to 
    determine the make-up of the planet's atmosphere. It was determined that the metallicity of the planet 
    was 2.6 to 6.8 times larger than the metallicity of its star, and that the C/O ration was about 0.42. 
    The data indicates methane depletion in the atmosphere, and supports a clear atmosphere with an opaque 
    cloud deck. Photochemistry is likely a reason for the methane depletion, and the researchers found 
    that there is evidence of a slight thermal inversion on the day-side of the planet. \n""")

# problem 3: Loading and analyzing data
print('Problem 3:')

# a: read in data and plot

#read in csv data and turn into numpy arrays
data = pd.read_csv('hw7_synthetic_transit_lightcurve.csv')
time, flux = data.to_numpy().T

# create plot
plt.figure(figsize = (8,5))
plt.plot(time, flux, color = 'firebrick', ls = ' ', 
         marker = '.',label = 'Normalized Flux')

# tick label size
plt.yticks( np.arange(0.988, 1.004, 0.002), fontsize = 12 )
plt.xticks( np.arange(-0.05, 0.06, 0.01),   fontsize = 12 )

# add labels and title
plt.title ('Normalized Flux of HD189733b', fontsize = 16)
plt.xlabel('Time [Days]',                  fontsize = 12)
plt.ylabel('Normalized Flux',              fontsize = 12)

#change the tick parameters for this plot:
plt.tick_params(axis='both', which='major',length=6, width=1.5,direction='in')

#add a legend
dm = plt.legend( fontsize = 12, loc = 'upper left')

# create minor ticks:
plt.minorticks_on()
plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(0.002))
plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(0.0005))
plt.tick_params(axis='both', which='minor',length=4, width=1,direction='in')

# save plot? It doesnt ask us to, but I'm a lil concerned that we might need to lol
plt.savefig('hw7__rab_problem3_graph1.png')
plt.show()

# part b: started support functions file, imported above with rest of imports

# let's find guess from the data to give curve_fit:
transit = time[flux < 0.996]
width   = np.max(transit) - np.min(transit)
center  = np.mean(transit)
height  = np.mean(flux[flux < 0.996])
guess   = [center, width, height, 1]

# pass to curve fit to see what we get
vals , covar = curve_fit(box_function, time, flux, guess)

# print curve_fit results:
print("Best-fit parameters without method='trf':", vals)
print("Covariance matrix without method='trf':")
print(covar)

print('\nYikes, a covariance matrix with inifinities. ChatGPT said to try new method.\n')

# we get a warning too! ChatGPT suggested this:
# pass to curve fit to see what we get
vals , covar = curve_fit(box_function, time, flux, guess, method='trf')
print("Best-fit parameters:", vals)
print("Covariance matrix:")
print(covar)
print('\n This is better, but it is hard to trust curve_fit, especially with\n\
    this non-smooth funciton. It is better to visually inspect the graph.\n')

# part iii: What are the best-fit window-function properties
# print my guesses for values
print('Best-fit Window-Function Properties:')
print('Estimated Height: {}'.format(height))
print('Estimated Width: {}'.format(width))
print('Estimated Center: {}'.format(center))

# print Curve_fit Estimates:
print('\n')
print('Curve_fit Estimated Height: {}'.format(vals[2]))
print('Curve_fit Estimated Width: {}'.format(vals[1]-vals[0]))
print('Curve_fit Estimated Center: {}'.format((vals[0]-vals[1])/2))

# part iii: What is the exoplanet radius, R, if you know that the stellar radius is 1.14 R
fd     = (1-vals[2])/1       #fractional depth
r_star = 1.14
r_planet = r_star * np.sqrt(fd)
print(f'\nThe planet\'s radius is {r_planet:.3f} R_sun.')

# part iv: new plot

# get fit data:
fit = box_function(time, center, width, height)

# create plot
plt.figure(figsize = (8,5))
plt.plot(time, flux, color = 'firebrick', ls = ' ', 
         marker = '.',label = 'Normalized Flux')
plt.plot(time, fit, color = 'blue', label='Box Fit')

# tick label size
plt.yticks( np.arange(0.988, 1.006, 0.002), fontsize = 12 )
plt.xticks( np.arange(-0.05, 0.06, 0.01),   fontsize = 12 )

# add labels and title
plt.title ('Normalized Flux of HD189733b', fontsize = 16)
plt.xlabel('Time [Days]',                  fontsize = 12)
plt.ylabel('Normalized Flux',              fontsize = 12)

#change the tick parameters for this plot:
plt.tick_params(axis='both', which='major',length=6, width=1.5,direction='in')

#add a legend
dm = plt.legend( fontsize = 12, loc = 'upper left')

# create minor ticks:
plt.minorticks_on()
plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(0.002))
plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(0.0005))
plt.tick_params(axis='both', which='minor',length=4, width=1,direction='in')

# save plot? It doesnt ask us to, but I'm a lil concerned that we might need to lol
plt.savefig('hw7__rab_problem3_graph2.png')
plt.show()

# part c: calculate error

# uncertainties in variables and first derivatives
unc_rs = 0.01
unc_fd = 0.002
df_drs = np.sqrt(fd)
df_dfd = 0.5 * r_star * (fd)**(-1/2)

# uncertainty is radius of planer
unc_rp = np.sqrt( (df_drs * unc_rs)**2 + (df_dfd * unc_fd)**2 )
print(f'\nThe planet\'s radius is {r_planet:.4f} +/- {unc_rp:.4f} R_sun.')
