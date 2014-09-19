=====================
mediagoblin-piwik
=====================

This plugin enables support for Piwik open source analytics in Gnu MediaGoblin. To make use of the Piwik plugin, you must have access Piwik installed or have access to a live Piwik instance.

Install Piwiki
==========================

Go to http://piwik.org and click ``Download Piwik Now``. Follow the Piwik installation guide at http://piwik.org/docs/installation-maintenance .

Alternatively, if your distribution packages Piwik, download and install Piwik from your distribution's repository and follow any instructions given.

Complete the Piwik install and configuration before installing the Piwik plugin for Gnu MediaGoblin.

Set up the piwik plugin
===========================

1. Clone the Piwik plugin repository from GitHub::

    git clone https://github.com/ayleph/mediagoblin-piwik.git

2. Copy the piwik folder to your MediaGoblin install::

   cp -r piwik /path/to/mediagoblin/mediagoblin/plugins/
    
3. Add the following to your mediagoblin_local.ini file in the ``[plugins]`` section::

    [[mediagoblin.plugins.piwik]]

Configure the Piwik plugin
==============================

You must provide the naem of the domain to track, the location of your Piwik install, and the site ID of the domain to track. Add the following entries to your mediagoblin_local.ini file under the recaptcha plugin::

    [[mediagoblin.plugins.piwik]]
    PIWIK_DOMAIN = 'mediagoblin.example.org'
    PIWIK_LOCATION = 'example.org/piwik'
    PIWIK_SITEID = 1
