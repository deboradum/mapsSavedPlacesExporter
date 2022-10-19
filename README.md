This program allows you to migrate downloaded CSV- or JSON files to another
Google account. Simply call the program and give the filepath as an argument.
When a location can not be added for some reason, it is printed to stdout so it
can be manually added. The error rate is about 2%.

This program uses Chromedriver to open and control the browser. Please install
Chromedriver to use the program. Change the CHROMEDRIVER_PATH variable to the
install location to start migrating. To save the locations to a different folder,
change the FOLDER_NAME variable.

When migrating Google accounts I did not want to manually migrate my hundreds of
starred- and saved places. I wrote this program to transfer the places for me. If
the program does not work, please check to see if your CHROMEDRIVER_PATH variable
is correct. If this is the case and the program still does not work, the XPATHS
might have changed and would need to be updated in the program to the correct ones.

Information about how Google Maps saved places are downloaded can be found [here](https://www.knowyourmobile.com/user-guides/how-to-download-and-export-your-starred-google-maps-locations/)