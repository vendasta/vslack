======
vSlack
======

vSlack makes it easy to notify Slack with Incoming Webhooks!

Usage
-----

vSlack is really simple to use. Just import it like you would any other Python library and fire off some messages!

You can also send messages that have "attachments" (in Slack parlance), for example:

    from vslack import VSlack

    slacker = VSlack('some_webhook_uri')

    attachments = [
      {
        'title': 'Build is failing!',
        'value': 'See <details|http://somelink> here'
      },  # You could have n more message dictionaries in this list.
    ]

    # Message is used to display in the notification that will appear when this message goes out to users.
    slacker.notify_slack_with_attachments('#ghostbusters', 'Build is failing', attachments)


You can override the icon and username of the bot message per notification, like so:

    import vslack

    slacker = vslack.VSlack('some_webhook_uri')

    slacker.notify_slack('#general', 'Something serious is happening!', icon_emoji=':no_good:', username='Serious Notifier')

Limitations
-----------

Right now vSlack can only send incoming webhooks. You can get the an incoming webhook uri by creating or editing an
already existing Incoming Webhook and grabbing its Webhook URL. Feel free to piggyback off of another Incoming Webhook
since you can override the name and icon anyway :smile: You can create one of those by [customizing your Slack org](https://slack.com/apps/manage/custom-integrations).
That link should direct you to your Organization if you're already logged in.

Changelog
---------

1.3.0

- Add title and text to attachment.

1.2.0

- Don't override icon_emoji or username with our defaults, they'll be provided when a webhook is created.

1.1.0

- Make channel an optional field, since an incoming webhook uri has a channel associated with it upon creation.
- Enable markdown in the fields of a notification sent with attachments.

1.0.0

- Initial release.

Copyright
~~~~~~~~~

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
