"""
Copyright 2017 Vendasta Technologies Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



Core vSlack functionality
"""
import json
import urllib2


__all__ = ['VSlack']


class VSlack(object):
    """
    vSlack object that can notify Slack orgs via Incoming Webhooks
    """

    def __init__(self, incoming_webhook_uri, icon_emoji=None, username=None):
        """
        Create a new vSlack object
        """
        self.incoming_webhook_uri = incoming_webhook_uri
        self.icon_emoji = icon_emoji
        self.username = username

    def notify_slack(self, message, channel=None, icon_emoji=None, username=None):
        """
        Send a message to a slack channel
        :param channel: Channel that should be notified.
            Must be prefixed with # to message channels, and @ to message people. Ex: #general, @jsmith
        :param message: The message text. Can contain links in the form <
        Optional:
        :param icon_emoji: Emoji that should be displayed as the user icon for this message. Overrides what is in
            appengine_config.py. Follows usual Slack protocol, like :see_no_evil:
        :param username: The name of the bot that will be making this message. Overrides what is in appengine_config.py
        """
        message = {
            u"channel": channel or u"",
            u"text": message,
            u"icon_emoji": icon_emoji or self.icon_emoji,
            u"username": username or self.username,
        }

        urllib2.urlopen(self.incoming_webhook_uri, data=json.dumps(message))

    def notify_slack_with_attachments(self, message, fields, channel=None, icon_emoji=None, username=None, color=None,
                                      title=None, attachment_text=None):
        """
        Send a message to a slack channel
        :param channel: Channel that should be notified.
            Must be prefixed with # to message channels, and @ to message people. Ex: #general, @jsmith
        :param message: The message text; used for a fallback for the attachments (fields param).
        :param fields: A list of dictionaries of the following specification: [
            {
                "title": "Title for a message to be displayed; will be bolded",
                "value": "Message to be displayed underneath the title. Can contain <p>HTML</p>"
            }, # ... n more dicts
        ]
        Optional:
        :param icon_emoji: Emoji that should be displayed as the user icon for this message
            Follows usual Slack protocol, like :see_no_evil:
        :param username: The name of the bot that will be making this message
        :param color: Color that should be shown next to the message
        :param title: Title of the attachment
        :param attachment_text: Text in attachment
        """
        message = {
            u"channel": channel or u"",
            u"icon_emoji": icon_emoji or self.icon_emoji,
            u"username": username or self.username,
            u"attachments": [{
                u"title": title,
                u"text": attachment_text,
                u"mrkdwn_in": [u"fields", u"text"],
                u"fallback": message,
                u"color": color if color else '',
                u"fields": fields
            }
            ],
        }

        urllib2.urlopen(self.incoming_webhook_uri, data=json.dumps(message))
