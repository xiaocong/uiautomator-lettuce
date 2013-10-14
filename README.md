Letture-uiautomator
===================

Lettuce steps definition to perform android UI testing.

---

## Installation

    pip install -r requirements

## Run

    lettuce

## How to add more steps definitions?

See [lettuce](http://lettuce.it/) and [uiautomator](https://github.com/xiaocong/uiautomator).

## Steps definitions

### Assertion

-   `Should see the text "(\.+)"`
-   `Should not see the text "(\.+)"`
-   `Should see "(\.+)"`
-   `Shoule not see "(\.+)"`
-   `Should see view\(([\w]+=[\S+][,[\s]*[\w]+=[\S+]]+)\)`
-   `Should not see view\(([\w]+=[\S+][,[\s]*[\w]+=[\S+]]+)\)`

### Press key

-   `Press ([\w ,]+) key`
-   `Press keycode (\w+)`

### Touch

-   `Touch view\(([\w]+=[\S+][,[\s]*[\w]+=[\S+]]+)\)`
-   `Long touch view\(([\w]+=[\S+][,[\s]*[\w]+=[\S+]]+)\)`
-   `Touch the text "(\.+)"`
-   `Touch text "(\.+)"`

### Swipe

-   `Swipe view\(([\w]+=[\S+][,[\s]*[\w]+=[\S+]]+)\) to (left|right|up|down)`

### Scroll

-   `Scroll view\(([\w]+=[\S+][,[\s]*[\w]+=[\S+]]+)\) (horizentically|vertically) (forward|backward)`
-   `Scroll view\(([\w]+=[\S+][,[\s]*[\w]+=[\S+]]+)\) (horizentically|vertically) to (beginning|end)`
-   `Scroll view\(([\w]+=[\S+][,[\s]*[\w]+=[\S+]]+)\) (horizentically|vertically) until view\(([\w]+=[\S+][,[\s]*[\w]+=[\S+]]+)\)`

## TODO

It's hard to define an android uiautomator DSL, so a lot of TODOs and all may change. If you have any good idea, please email xiaocong@gmail.com
