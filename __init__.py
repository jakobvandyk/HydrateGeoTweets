# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HydrateGeoTweets
                                 A QGIS plugin
 This plugin imports a csv of tweet IDs and creates points from their coordinates
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-10-15
        copyright            : (C) 2021 by Jakob Van Dyk
        email                : jakobvandyk@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Jakob Van Dyk'
__date__ = '2021-10-15'
__copyright__ = '(C) 2021 by Jakob Van Dyk'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load HydrateGeoTweets class from file HydrateGeoTweets.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .hydrate_geo_tweets import HydrateGeoTweetsPlugin
    return HydrateGeoTweetsPlugin()
