Overview
--------

The idea of this is simple. Often we'll download files from tickets and eventually fill up your drive and then spend hours deleting the closed tickets after checking they are solved / closed. So this script will run through the ticket status, check if they are solved or closed and then delete the local directories you have for them.

Acknowledgements
----------------

The main framework of connecting to Zendesk comes from the project below:

https://github.com/joaquincasares/zendesk_downloader

Setup
-----

**Please note: the path and pattern are still hard coded in the "check" file** you'll need to change this manually for now, until I move it into the cfg file

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

