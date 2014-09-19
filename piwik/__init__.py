# GNU MediaGoblin -- federated, autonomous media hosting
# Copyright (C) 2011, 2012 MediaGoblin contributors.  See AUTHORS.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from pkg_resources import resource_filename
import os
import logging

from mediagoblin.tools import pluginapi
from mediagoblin.tools.staticdirect import PluginStatic
_log = logging.getLogger(__name__)


PLUGIN_DIR = os.path.dirname(__file__)


def setup_plugin():
    global _setup_plugin_called

    _log.info('Setting up Piwik...')
    config = pluginapi.get_config('mediagoblin.plugins.piwik')
    if config:
        if config.get('PIWIK_DOMAIN') == 'mediagoblin.example.com':
            _log.warn('Piwik domain was not specified.')
        if config.get('PIWIK_LOCATION') == 'example.com/piwik':
            _log.warn('Piwik location was not specified.')

    # Register the template path.
    pluginapi.register_template_path(os.path.join(PLUGIN_DIR, 'templates'))

    from mediagoblin import mg_globals
    plugin_section = mg_globals.global_config.get("plugins", {})
    pluginapi.register_template_hooks(
         {"head": "mediagoblin/plugins/piwik/bits/piwik_extra_head.html"})

    _log.info('Done setting up Piwik!')

hooks = {
    'setup': setup_plugin
}
