# This set of repositories is a mixture of affiliated packages and packages
# that use astropy_helpers and opted in receiving automated PRs to update
# the helpers version. If your package requires Python 3.5+ consider adding
# it to the list in the "helpers_3.py" file to recieve updates for the
# Python 3.5+ releases of astropy-helpers.

repositories = sorted(set([
    ('astropy', 'astroquery'),
    ('ejeschke', 'ginga'),
    ('astroML', 'astroML'),
    ('weaverba137', 'pydl'),
    ('aplpy', 'aplpy'),
    ('astrofrog', 'reproject'),
    ('pyvirtobs', 'pyvo'),
    ('gammapy', 'gammapy'),
    ('sncosmo', 'sncosmo'),
    ('glue-viz', 'glue'),
    ('astropy', 'pyregion'),
    ('radio-astro-tools', 'spectral-cube'),
    ('olebole', 'python-cpl'),
    ('astropy', 'astroplan'),
    ('astropy', 'astroscrappy'),
    ('zblz', 'naima'),
    ('RiceMunk', 'omnifit'),
    ('jobovy', 'galpy'),
    ('StingraySoftware', 'HENDRICS'),
    ('StingraySoftware', 'stingray'),
    ('astropy', 'halotools'),
    ('jesford', 'cluster-lensing'),
    ('Chandra-MARX', 'marxs'),
    ('pyspeckit', 'pyspeckit'),
    ('linetools', 'linetools'),
    ('astropy', 'regions'),
    ('hamogu', 'astrospec'),
    ('hamogu', 'arcus'),
    ('hamogu', 'marxs-lynx'),
    ('hamogu', 'psfsubtraction'),
    ('astropy', 'astropy-healpix'),
    ('astropy', 'saba'),
    ('astropy', 'package-template'),
    ('chianti-atomic', 'ChiantiPy'),
    ('spacetelescope', 'astroimtools'),
    ('spacetelescope', 'synphot_refactor'),
    ('spacetelescope', 'stsynphot_refactor'),
    ('spacetelescope', 'imexam'),
    ('desihub', 'specsim'),
    ('dkirkby', 'speclite'),
    ('matteobachetti', 'srt-single-dish-tools'),
    ('mhvk', 'baseband'),
    ('BEAST-Fitting', 'beast'),
    ('PAHFIT', 'pypahfit'),
    ('karllark', 'dust_extinction'),
    ('karllark', 'dust_attenuation'),
    ('karllark', 'measure_extinction'),
    ('matiscke', 'lcps')
]))
