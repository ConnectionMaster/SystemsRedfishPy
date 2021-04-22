# Change Log

## [2.1.4] - 2021-4-20
- Added `get logs` to retrieve controller and disk drive logs
- Added `cs` alias as a short cut to run `create session`
- Added `decode` flag for UrlAccess.process_request() to handle retrieval of log files
- The URI discovery tag `ActiveController` is now `StorageActiveController` to relate better to the URI
- Added URI discovery service for `SystemsLogServices`
- Added the display of IP Address when creating a session for easier debug

## [2.1.3] - 2021-3-19
- Added `help configuration` to show how to use dump and set config values, also sorted help command output

## [2.1.2] - 2021-3-18
- Added `show tasks`

## [2.1.1] - 2021-2-3
- Added [Troubleshooting Guide](troubleshooting.md)
- Corrections and enhancements to `show thermal`, `create volume`, `compose volume`, `create diskgroup`,`create storagegroup`,

## [2.1.0] - 2021-1-22
- Small correction to how the Disks URL is discovered under serviceversion=1. This version will be pushed to github.

## [2.0.7] - 2021-1-22
- Updated the `http push` command to work correctly for Redfish Service firmware uploads.

## [2.0.6] - 2021-1-14
- New example JSON files for volume composition under json/
- New `compose volume` command to compose a volume using the Redfish Composition Service
- New `run cli` command to execute any MC API CLI command using the Redfish interface

## [2.0.5] - 2020-11-24
- Added requirements.txt which stipulates some new requirements for new features
- Added `http push` which allows a user to send a file to the service using http and application/octet-stream, see requirements.txt
- Added `reset system` which allows the user execute a restart controller command
- Added `show discovered` and `reset discoverd` which allows the user to see all redfish service discovered URLs
- Removed the `configurationfile` setting from the configuration file
- Replaced the `version` configuration setting with a new `serviceversion` setting - this variable is used to work with the first version of the Redfish Service (serviceversion=1) or the latest Redfish Service (serviceversion=2) that supports Fabrics, Composition Service and other new features
- Added command history that works under Windows and Linux, see requirements.txt

## [2.0.4] - 2020-10-29
- Expanded UrlAcess.process_request() to traverse all items in the header to better handle the 'json' content type

## [2.0.3] - 2020-09-08
- Corrected 'purge system' to handle both linear and virtual storage systems
- Corrected JSON errors in redfishAPI.json
- Removed the need for Python version 3.6 or greater. 3.x is sufficient.
- Add 'show fabrics'

## [2.0.2] - 2020-07-22
- Updated 'create session' to display the session key
- Enhanced 'show storagegroups' to check JSON data inclusion before retrieving values.

## [2.0.1] - 2020-07-16
- Changes based on Redfish Service Phase II updates 
- Updates to 'redfish odata' and 'redfish metadata'

## [1.2.7] - 2020-07-09
- Added new config option 'httpbasicauth' True|False. When True, use HTTP Basic Auth instead of Sessions.
- Updated Redfish URI discovery to include all possible Redfish 2020.2 ServiceRoot entities.
- Updated 'redfish urls' command to print the parent URI when an error occurs. 

## [1.2.6] - 2020-06-17
- Improvements to better handle Redfish requests when a session has not been established.
- Added 'show enclosures' command 

## [1.2.5] - 2020-05-29
- Added new config variable 'usefinalslash' which adds a '/' to the end of all URIs, or doesn't

## [1.2.4] - 2020-05-28
- Added a number of new HTTP operations in order to simply testing.
-     http get <uri> 
-     http delete <uri>
-     http post <uri> [<json> | <filename>]
-     http patch <uri> [<json> | <filename>]
- Added core.ArgExtract to help with command line argument extraction
- Added new command 'save session' to update config data with session information

## [1.2.3] - 2020-04-24
- Updated a number of show commands to match updated output 
- Created a package zip file and a package tar ball for easy downloading

## [1.2.2] - 2020-04-15
- Reduced output during unit testing

## [1.2.1] - 2020-04-09
- Updates to 'show disks' command
- Updates to 'show diskgroups' command
- Correction to TestStorageGroup

## [1.2.0] - 2020-04-06
- Support for linear and virtual storage. Tested against the Seagate PODs storage system. 
- Updates to system commands and scripts for linear storage support.
- Optimizations to system URI discovery.

## [1.1.7] - 2020-03-24
- New 'set volume' command which performs PATCH operations on a Volume
- Minor bug fixes
- Option to dump http data via !dumphttpdata

## [1.1.6] - 2020-03-17
- Full sync with github and local gitlab

## [1.1.5] - 2020-03-13
- Added a new configuration variable for the interactive session. The new value is 'entertoexit'. When True,
  the user can press Enter to exit the shell. When False, the user must type exit or quit.
- Added a new 'run loop' command to run and time multiple HTTP GET URI operations. Updated urlAccess.py to
  time and store in UrlStatus a new elapsedMicroseconds value.
- Corrected the storage of the current version in the JSON config file.
- Replaced hard-coded URIs with discovered values from the Root Service and beyond.
- Corrected a typo in the prologue of most files.
- Added testStorageGroup.py
- Added new command 'purge system' and 'show system'

## [1.1.4] - 2020-01-10
- Added new command 'delete sessions $sessionid' so that a script can automatically delete the current
  session and not leave it active after the python redfishAPI exits.
- Added a new simple Label object to encode and decode internal variables, such as $sessionid.
- Added new redfishAPI command line option to pass in a user config file. The user can now call
  python redfishAPI --config myconfig.json or -c myconfig.json and not have to modify the checked in
  version. This also applies to python redfishUnittest --config myconfig.json or -c myconfig.json.
- Added logic to automatically delete the current session before redfishAPI exits.
- Modified urlAccess to handle a byte stream
- Updated the unittest tests to only create a single session, and initialize system data only once.

## [1.1.3] - 2019-12-23
- Corrected the 'show fans' command since the reported JSON data was modified
- Corrected the 'show thermal' command since the reported JSON data was modified

## [1.1.2] - 2019-12-18
- Corrected the drive in use flag for functional testing.

## [1.1.1] - 2019-12-16
- Initial Public Release
- Commands Provided:
    * **create storagegroup** - Create a storage group to map a volume making it visible to a host or hosts.
    * **create session** - Establish a session with the Redfish Service (using mcip, username, and password)
    * **create volume** - Create a volume
    * **delete diskgroups** - Delete one or more comma-separated disk groups by name or serial number
    * **delete pools** - Delete one or more comma-separated pools by name or serial number
    * **delete sessions** - Delete one or more comma-separated session ids
    * **delete storagegroups** - Delete one or more comma-separated storage groups by serial number
    * **delete volumes** - Delete one or more comma-separated volumes by name or serial number
    * **help [command]** - Display a synopsys of all commands, or details for a command
    * **map volume** - Create or update a storage group to map a volume making it visibile to a host or hosts.
    * **redfish json** - GET and display JSON data for a given URL
    * **create diskgroup** - Create a disk group and add it to a pool
    * **redfish metadata** - GET and display the metadata reported by the Redfish Service
    * **redfish odata** - GET and display the odata reported by the Redfish Service
    * **redfish services** - GET and display the JSON data reported by the Redfish Service root
    * **redfish urls** - Test all URLs reported by this REST API
    * **redfish version** - Display the current version of the Redfish Service.
    * **run script** - Run a script file
    * **show diskgroups** - Display all allocated disk groups and disk group infromation
    * **show disks** - Display all disk drives found in the system
    * **show fans** - Display all fan readings from the system.
    * **show initiators** - Display all initiators found in the system
    * **show pools** - Display all allocated virtual pools and pool information
    * **show ports** - Display all ports found in the system
    * **show sessions** - Display all active sessions, requires an active session
    * **show storagegroups** - Display all created storage groups
    * **show thermal** - Display all temperature data from the system
    * **show volumes** - Display all configured volumes