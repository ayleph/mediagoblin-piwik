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

You must provide the name of the domain to track, the location of your Piwik install, and the site ID of the domain to track.

Add the following entries to your mediagoblin_local.ini file under the recaptcha plugin::

    [[mediagoblin.plugins.piwik]]
    PIWIK_DOMAIN = 'mediagoblin.example.com'
    PIWIK_LOCATION = 'example.com/piwik'
    PIWIK_SITEID = 1

To find these values, open the Piwik web interface and go to Settings->Tracking Code. You'll see something like::

    <!-- Piwik -->
    <script type="text/javascript">
      var _paq = _paq || [];
      _paq.push(["setDocumentTitle", document.domain + "/" + document.title]);
      _paq.push(["setCookieDomain", "*.mediagoblin.example.com"]);
      _paq.push(["setDomains", ["*.mediagoblin.example.com"]]);
      _paq.push(['trackPageView']);
      _paq.push(['enableLinkTracking']);
      (function() {
        var u=(("https:" == document.location.protocol) ? "https" : "http") + "://example.com/piwik/";
        _paq.push(['setTrackerUrl', u+'piwik.php']);
        _paq.push(['setSiteId', 1]);
        var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0]; g.type='text/javascript';
        g.defer=true; g.async=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
      })();
    </script>
    <noscript><p><img src="http://example.com/piwik/piwik.php?idsite=1" style="border:0;" alt="" /></p></noscript>
    <!-- End Piwik Code -->

The domain to track (PIWIK_DOMAIN) is the domain specified in::

    _paq.push(["setCookieDomain", "*.mediagoblin.example.com"]);

and::

    _paq.push(["setDomains", ["*.mediagoblin.example.com"]]);

The location of your Piwik install (PIWIK_LOCATION) is the location specified in::

    var u=(("https:" == document.location.protocol) ? "https" : "http") + "://example.com/piwik/";

The site ID (PIWIK_SITEID) is the site ID specified in::

    _paq.push(['setSiteId', 1]);
