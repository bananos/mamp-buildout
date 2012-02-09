Test of syntax highlight
=========================


```ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

This is a normal text


```python

    @swirl.asynchronous
    def _on_registration_success(self, callback):
        """
         This is a single hander which is called each time user successfully registers on BILL node.
         Called for all types of registration:
            * Plain
            * Invited (team)
            * Gmarket

         Useful for writing different post-registration business logic
        """

        try:
            # call Hubspot
            _ = yield lambda cb: self._push_hubspot_lead(callback=cb)

            # call some other stuff
            callback()

        except Exception as ex:
            LOG.warning("UtilityHandler._on_registration_success: Error pushing data to Hubspot %s", format_exc())
            callback(ex)

```


Test of bash script


```bash

   git clone git@github.com:bananos/mamp-buildout.git
   cd mamp-buildout

   bananos@amber: ~/Projects/github/mamp-buildout (master) $ /usr/bin/python2.7 bootstrap.py
   Creating directory '/Users/bananos/Projects/github/mamp-buildout/bin'.
   Creating directory '/Users/bananos/Projects/github/mamp-buildout/parts'.
   Creating directory '/Users/bananos/Projects/github/mamp-buildout/eggs'.
   Creating directory '/Users/bananos/Projects/github/mamp-buildout/develop-eggs'.
   Generated script '/Users/bananos/Projects/github/mamp-buildout/bin/buildout'.


```



Yet another test
