Acknowledgements
----------------

The main framework of connecting to Zendesk comes from the project below:

https://github.com/joaquincasares/zendesk_downloader

Setup
-----

First install the requests package by running:

    pip install requests

Ensure your ~/.zendesk.cfg is already configured.
You can use your API token information as found at https://support.datastax.com/settings/api.
(You will need ZenDesk admin access to view this page.)
This is mine:

    [ZenDesk]
    domain = support.datastax.com
    email = you@<domain>.com/token
    pass = <password>

    [Downloader]
    download_directory = /Users/you/Issues
    run_open = True
    open_program = subl


Usage
-----

    chmod a+x ./check
    ./check 

