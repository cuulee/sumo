#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, match = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# go to shape mode
netedit.shapeMode()

# select POI in list of shapes
netedit.changeShape("poi")

# create first POI
netedit.leftClick(match, 100, 50)

# go to inspect mode
netedit.inspectMode()

# inspect first POI
netedit.leftClick(match, 100, 50)

# Change parameter 1 with a non valid value (dummy)
netedit.modifyAttribute(1, "dummyPosition")

# Change parameter 1 with a valid value
netedit.modifyAttribute(1, "20.40,7.50")

# Check undos and redos
netedit.undo(match, 2)
netedit.redo(match, 2)

# save shapes
netedit.saveShapes()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
