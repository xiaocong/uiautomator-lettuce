#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lettuce import *


@step('Press (.+) key')
def press_key(step, key):
    for k in key.split(","):
        world.d.press(k.strip().lower())


@step('Press keycode (.+)')
def press_keycode(step, keycode):
    for k in keycode.split(","):
        k = k.strip().lower()
        world.d.press(int(k, 16) if k.find("0x") == 0 else int(k))


@step('Touch view\((.+)\)')
def click(step, target):
    step.given('Should see view(%s)' % target)
    world.d(**world.kwargs(target)).click()


@step('Touch text "(.+)"')
def click_the_text(step, text):
    step.given('Should see text "%s"' % text)
    if world.d(text=text).exists:
        world.d(text=text).click()
    elif world.d(textContains=text).exists:
        world.d(textContains=text).click()


@step('Touch point \((\d+),\s(\d+)\)')
def click_the_point(step, x, y):
    world.d.click(int(x), int(y))


@step('Long touch view\((.+)\)')
def long_click(step, target):
    step.given('Should see view(%s)' % target)
    world.d(**world.kwargs(target)).long_click()


@step('Long touch text "(.+)"')
def long_click_the_text(step, text):
    step.given('Should see text "%s"' % text)
    if world.d(text=text).exists:
        world.d(text=text).long_click()
    elif world.d(textContains=text).exists:
        world.d(textContains=text).long_click()


@step('Long touch point \((\d+),\s(\d+)\)')
def long_click_the_point(step, x, y):
    world.d.long_click(int(x), int(y))


@step('Clear text of view\((.+)\)')
def clear_text(step, target):
    step.given('Should see view(%s)' % target)
    world.d(**world.kwargs(target)).clear_text()


@step('Input text (.+) into view\((.+)\)')
def set_text(step, text, target):
    step.given('Should see view(%s)' % target)
    world.d(**world.kwargs(target)).set_text(text)


@step('Scroll view\((.*)\) (horizentically|vertically|horiz|vert) until view\((.*)\)')
def scroll_view_until(step, target, dimen, to):
    step.given('Should see view(%s)' % target)
    step.given('Scroll view(%s) %s to beginning' % (target, dimen))

    retries = 0
    while retries < 3 and not world.d(**world.kwargs(to)).exists:
        if not world.d(**world.kwargs(target)).scroll(dimen, "forward", steps=10):
            retries += 1

    if not world.d(**world.kwargs(to)).exists:
        raise Exception("View(%s) not found!" % to)


@step('Scroll view\((.*)\) (horizentically|vertically|horiz|vert) to (beginning|end)')
def scroll_view_to_beginning_or_end(step, target, dimen, to):
    step.given('Should see view(%s)' % target)

    for i in range(3):
        world.d(**world.kwargs(target)).scroll(dimen, {"beginning": "toBeginning", "end": "toEnd"}[to], steps=10)


@step('Scroll view\((.*)\) (horizentically|vertically|horiz|vert) (forward|backward)')
def scroll_view_forward_or_backward(step, target, dimen, dir):
    step.given('Should see view(%s)' % target)
    world.d(**world.kwargs(target)).scroll(dimen, dir, steps=10)


@step('Fling view\((.*)\) (horizentically|vertically|horiz|vert) to (beginning|end)')
def fling_view_to_beginning_or_end(step, target, dimen, to):
    step.given('Should see view(%s)' % target)
    for i in range(3):
        world.d(**world.kwargs(target)).fling(dimen, {"beginning": "toBeginning", "end": "toEnd"}[to])


@step('Fling view\((.*)\) (horizentically|vertically|horiz|vert) (forward|backward)')
def fling_view_forward_or_backward(step, target, dimen, dir):
    step.given('Should see view(%s)' % target)
    world.d(**world.kwargs(target)).fling(dimen, dir)


@step('Swipe view\((.*)\) (up|down|right|left)')
def swipe_view(step, target, dir):
    step.given('Should see view(%s)' % target)
    world.d(**world.kwargs(target)).swipe(dir)


@step('Pinch (in|out) view\((.*)\)')
def pinch(step, in_or_out, target):
    step.given('Should see view(%s)' % target)
    if "in" == in_or_out.lower():
        world.d(**world.kwargs(target)).pinch.In()
    else:
        world.d(**world.kwargs(target)).pinch.Out()

#
# Assertion
#


@step('Should see view\((.*)\)')
def should_see_view(step, target):
    assert world.d(**world.kwargs(target)).exists


@step('Should see text "(.+)"')
def should_see_the_text(step, text):
    assert world.d(text=text).exists or world.d(textContains=text).exists


@step('Should not see text "(.+)"')
def should_not_see_the_text(step, text):
    assert not (d(text=text).exists or world.d(textContains=text).exists)
