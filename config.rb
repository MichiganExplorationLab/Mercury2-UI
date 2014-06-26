## Mercury2 Compass SASS pre-processor configuration
#
# This file contains the configuration settings for the Compass CSS pre-processor. Compass is used to generate static,
# minimized CSS files based on a set of .scss files.
#
# @note Execute "compass watch" in the mercury2/compass directory when developing for Mercury2 to have Compass 
#       automatically build the CSS files as you make changes to the scss files.

static_dir = "mercury2/static/"
compass_dir = "mercury2/compass/"

# Set Compass project variables
css_dir = static_dir+"css"
sass_dir = compass_dir+"stylesheets"
images_dir = static_dir+"images"
javascripts_dir = static_dir+"javascript"
environment = :development
output_style = :compressed
relative_assets = true
