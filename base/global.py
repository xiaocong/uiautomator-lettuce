#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lettuce import *
from uiautomator import device as d

world.d = d


@before.all
def say_hello():
    print "Lettuce will start to run tests right now..."


@after.all
def say_goodbye(total):
    print "Goodbye!"


@before.each_feature
def wakeup_device_before_feature(feature):
    world.d.wakeup()
    world.d.wait.idle()


@before.each_step
def wakeup_device_before_step(step):
    world.d.wakeup()
    world.d.wait.idle()


@before.each_scenario
def unlock_screen(scenario):
    '''unlock screen on Android 4.3'''
    if world.d.info["currentPackageName"] == "android" and world.d(resourceId="android:id/glow_pad_view").exists:
        world.d(resourceId="android:id/glow_pad_view").swipe.down()
    world.d.wait.idle()


@world.absorb
def kwargs(view_str):
    fields = {
        "text": str,  # MASK_TEXT,
        "textContains": str,  # MASK_TEXTCONTAINS,
        "textMatches": str,  # MASK_TEXTMATCHES,
        "textStartsWith": str,  # MASK_TEXTSTARTSWITH,
        "className": str,  # MASK_CLASSNAME
        "classNameMatches": str,  # MASK_CLASSNAMEMATCHES
        "description": str,  # MASK_DESCRIPTION
        "descriptionContains": str,  # MASK_DESCRIPTIONCONTAINS
        "descriptionMatches": str,  # MASK_DESCRIPTIONMATCHES
        "descriptionStartsWith": str,  # MASK_DESCRIPTIONSTARTSWITH
        "checkable": bool,  # MASK_CHECKABLE
        "checked": bool,  # MASK_CHECKED
        "clickable": bool,  # MASK_CLICKABLE
        "longClickable": bool,  # MASK_LONGCLICKABLE,
        "scrollable": bool,  # MASK_SCROLLABLE,
        "enabled": bool,  # MASK_ENABLED,
        "focusable": bool,  # MASK_FOCUSABLE,
        "focused": bool,  # MASK_FOCUSED,
        "selected": bool,  # MASK_SELECTED,
        "packageName": str,  # MASK_PACKAGENAME,
        "packageNameMatches": str,  # MASK_PACKAGENAMEMATCHES,
        "resourceId": str,  # MASK_RESOURCEID,
        "resourceIdMatches": str,  # MASK_RESOURCEIDMATCHES,
        "index": int,  # MASK_INDEX,
        "instance": int  # MASK_INSTANCE,
    }
    return dict(map(lambda i: [i[0].strip(), fields[i[0].strip()](i[1].strip())], (item.split("=") for item in view_str.split(","))))
