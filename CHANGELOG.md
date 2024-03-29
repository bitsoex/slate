# Changelog

## Version 2.1.0
*April 22, 2022*

Add new error code 0727 for the minimum number of ubos and directors required in business accounts.

## Version 2.0.9
*April 26, 2022*

Added `1106` error code for the catalogues api.

## Version 2.0.8
*March 10, 2022*

Modifying `0201` error description to a more appropiate one

## Version 2.0.7
*January 18, 2022*

Added new error codes for trading/conversions disabled on an account

## Version 2.0.6
*January 6, 2022*

Added new validation error code 0376 for Bitso Transfer rate limit check

## Version 2.0.5
*January 7, 2021*

Added new validation errors codes:
* 1401 for non-existent objects

## Version 2.0.4
*December 7, 2021*

Added new validation error code 0375 reserved for internal use of Shift API

## Version 2.0.3
*November 24, 2021*

Documentation inconsistency between REST Api service and implementation was fixed:
* in open_orders parameters are wrong, now parameters matches with the original implementation

## Version 2.0.2

*July 27, 2021*

Documentation inconsistency between REST Api service and implementation was fixed:
* in open_orders and lookup_orders services documentation, now 'status' uses 'partially filled' instead of 'partial-fill' as an option.

## Version 2.0.1

*July 19, 2021*

Documentation inconsistency between REST Api service and implementation was fixed:
* in user_trades service documentation, now 'book' is not required.

## Version 2.0.0

*July 9, 2021*

Project dependencies were updated along with javascript, css and layout code in order to be up to date with slate's latest version.
This was necessary to deploy slate without errors or missing parts, such as table of contents.

## Version 1.3.4

*June 25, 2021*

There was an inconsistency for Diff-Orders and for Orders API. The "t" field was being described as number 0 for selling
and 1 for buying, but the implementation of this api is validating the opposite.
To make the documentation consistent with the code, the field was updated to number 0 for buying and number 1 for selling.

## Version 1.3.3

*June 24, 2021*

Fixed documentation inconsistency between REST Api service and the implementation:
* in user_trades service documentation, now 'book' is required.
* in order_trades service documentation the field 'make_side' have changed to 'maker_side'
* also in the same service the 'created_at' field format have been upgraded from 2021-06-11T09:25:05+0000 to 2021-06-11T09:25:05.000+00:00

## Version 1.3.2

*February 3, 2016*

A small bugfix for slightly incorrect background colors on code samples in some cases.

## Version 1.3.1

*January 31, 2016*

A small bugfix for incorrect whitespace in code blocks.

## Version 1.3

*January 27, 2016*

We've upgraded Middleman and a number of other dependencies, which should fix quite a few bugs.

Instead of `rake build` and `rake deploy`, you should now run `bundle exec middleman build --clean` to build your server, and `./deploy.sh` to deploy it to Github Pages.

## Version 1.2

*June 20, 2015*

**Fixes:**

- Remove crash on invalid languages
- Update Tocify to scroll to the highlighted header in the Table of Contents
- Fix variable leak and update search algorithms
- Update Python examples to be valid Python
- Update gems
- More misc. bugfixes of Javascript errors
- Add Dockerfile
- Remove unused gems
- Optimize images, fonts, and generated asset files
- Add chinese font support
- Remove RedCarpet header ID patch
- Update language tabs to not disturb existing query strings

## Version 1.1

*July 27, 2014*

**Fixes:**

- Finally, a fix for the redcarpet upgrade bug

## Version 1.0

*July 2, 2014*

[View Issues](https://github.com/tripit/slate/issues?milestone=1&state=closed)

**Features:**

- Responsive designs for phones and tablets
- Started tagging versions

**Fixes:**

- Fixed 'unrecognized expression' error
- Fixed #undefined hash bug
- Fixed bug where the current language tab would be unselected
- Fixed bug where tocify wouldn't highlight the current section while searching
- Fixed bug where ids of header tags would have special characters that caused problems
- Updated layout so that pages with disabled search wouldn't load search.js
- Cleaned up Javascript
