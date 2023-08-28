#!/usr/bin/env python3

""" testing """

def multiple_parameters(req1, req2, *unknown_params, some_more_params):
    pass

multiple_parameters(1, 'abc','etc', 'etc', '...', some_more_params='is this part of variable')